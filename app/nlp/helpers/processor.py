from database.models.faq_questions import FaqQuestions
import transliterate
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from googletrans import Translator
import re
import time
from googletrans import Translator
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def processor():
    questions = []
    primary_keys = []
    faq_quesitons = FaqQuestions.select(FaqQuestions.id, FaqQuestions.question_abstract)
    for faq_question in faq_quesitons:
        questions.append(faq_question.question_abstract)
        primary_keys.append(faq_question.id)

    # Create the pandas DataFrame with column name is provided explicitly
    df = pd.DataFrame(questions, columns=["Questions"])
    df.fillna("", inplace=True)

    def preprocess_text(text):
        # Apply lower casing
        text = text.lower()
        # Remove punctuation
        text = re.sub(r"[^\w\s]", "", text)
        # Remove stop words
        stop_words = set(stopwords.words("english"))
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word not in stop_words]
        # Lemmatize text
        lemmatizer = WordNetLemmatizer()
        lemmatized_text = [lemmatizer.lemmatize(word) for word in filtered_text]
        # Join tokens to form string
        return " ".join(lemmatized_text)

    # Define the vectorizer
    vectorizer = TfidfVectorizer(preprocessor=preprocess_text)
    # Vectorize the questions
    start_time = time.time()
    vectors = vectorizer.fit_transform(df["Questions"])
    print("--- Vectorization took %s seconds ---" % (time.time() - start_time))

    # Compute the cosine similarity matrix
    start_time = time.time()
    cosine_sim_matrix = cosine_similarity(vectors)
    print(
        "--- Cosine similarity matrix computation took %s seconds ---"
        % (time.time() - start_time)
    )
    return {
        "data": df,
        "vectors": vectors,
        "keys": primary_keys,
        "vectorizer": vectorizer,
    }


g = processor()
