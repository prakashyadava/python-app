class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        if answer == current_question.answer:
            self.score +=1
        # else:
        #     print(f"Wrong answer.\nCorrect answer was {current_question.answer} ")
        # print(f"Score : {self.score}/{self.question_number + 1}")
        self.question_number +=1


