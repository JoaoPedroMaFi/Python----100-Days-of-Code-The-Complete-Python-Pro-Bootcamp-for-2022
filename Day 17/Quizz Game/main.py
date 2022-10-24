from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_item in question_data:
    # text = question_item["text"]
    # answer = question_item["answer"]
    text = question_item["question"]
    answer = question_item["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

# for question in question_bank:
#     print(question.text)
#     print(question.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
quiz.quiz_report()
