from day17_question_model import Question
from day17_question_data import question_data
from day17_quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    # question_bank.append(Question(question["text"],question["answer"]))
quiz = QuizBrain(question_bank)
for question in question_bank:

    quiz.next_question()

print("You have completed the quiz.")
print(f"Final Score : {quiz.score}/{quiz.question_number}")