from deep_translator import GoogleTranslator
from config.global_constants import standard_terms


def question_translator(question):
    list_question = list(question.split())

    updated_question = ""

    for i, quest in enumerate(list_question):
        if quest.upper() in standard_terms:
            updated_question += quest
            list_question.pop(i)
    question = " ".join(list_question)
    translation = GoogleTranslator(source="auto", target="en").translate(question)
    return str(translation) + " " + updated_question
