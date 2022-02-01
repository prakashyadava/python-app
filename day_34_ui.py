from tkinter import *
from day_34_quiz_brain import QuizBrain

THEME_COLOR = "#375362"
display_question = ""
display_question_answer = ""


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.minsize(width=340, height=600)
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f"Score : {self.score}", font=("Arial", 10, "bold"), bg=THEME_COLOR, fg="white")
        self.count = 10
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="true.png")
        false_img = PhotoImage(file="false.png")
        self.True_btn = Button(image=true_img, highlightthickness=0, command=self.check_true)
        self.True_btn.grid(column=0, row=2)

        self.False_btn = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.False_btn.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def check_true(self):
        self.count = self.count - 1
        if display_question_answer == "True" and self.count > 0:
            self.score = self.score + 1
            self.score_label.config(text=f"Score: {self.score}")

            self.get_next_question()
        else:

            self.get_next_question()

    def check_false(self):
        self.count = self.count - 1
        if display_question_answer == "False" and self.count > 0:
            self.score = self.score + 1
            self.score_label.config(text=f"Score: {self.score}")

            self.get_next_question()
        else:

            self.get_next_question()

    def get_next_question(self):
        global display_question, display_question_answer

        if self.count > 0:
            q_text = self.quiz.next_question()
            display_question = q_text.text
            display_question_answer = q_text.answer

            self.canvas.itemconfig(self.question_text, text=f"Q{self.quiz.question_number}. {display_question}")
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_text, text=f"Final Score:{self.score}/10")
            self.True_btn.destroy()
            self.False_btn.destroy()
            exit_btn = Button(text="Exit", bg="red", command=lambda: self.window.destroy(), font=("Arial", 30, "bold"))

            exit_btn.grid(column=0, row=2, columnspan=2)
