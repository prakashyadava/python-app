from day_34_ui import QuizInterface
from day_34_data import question_data
from day_34_question_model import QuestionModel
from day_34_quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
