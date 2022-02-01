from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 24, "normal")
PLACEHOLDER = "[score]"
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("day24_snake_score.txt") as f:
            self.high_score = int(f.read())

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.increase_score_board()

    def increase_score_board(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align = ALLIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.increase_score_board()
    def update(self):
        self.score += 1
        if self.score>=self.high_score:
            self.high_score = self.score
            with open("day24_snake_score.txt","w") as f:


                f.write(str(self.high_score))
        self.clear()
        self.increase_score_board()
    def final(self):
        self.clear()
        self.write(f"Final Score: {self.score}", align=ALLIGNMENT, font=FONT)
