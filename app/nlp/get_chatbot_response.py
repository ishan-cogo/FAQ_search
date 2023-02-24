from nlp.helpers.processor import g
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nlp.helpers.question_transator import question_translator
import json

def get_chatbot_response(question, vectors=g["vectors"], df=g["data"]):
    question = question_translator(question)
    question_vector = g["vectorizer"].transform([question])
    similarity_scores = cosine_similarity(question_vector, vectors)
    # most_similar_index = np.argmax(similarity_scores)
    related_questions = np.argsort(similarity_scores[0])[::-1][:5]

    result = {}
    for i, index in enumerate(related_questions):
        result[str(i)]=str(g["keys"][index])
    return result
