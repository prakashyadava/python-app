class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]

        # else:
        #     print(f"Wrong answer.\nCorrect answer was {current_question.answer} ")
        # print(f"Score : {self.score}/{self.question_number + 1}")
        self.question_number += 1
        return current_question
