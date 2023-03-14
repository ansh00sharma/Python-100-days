from Question_model import Question
from quiz import Quiz
from Data import question_data

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.still_has_question() :
    quiz.next_question()

print(f"You have completed the quiz. Your final score is {quiz.score}/{quiz.question_number}")