from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: ", padx=20, pady=20, bg=THEME_COLOR, fg=WHITE, font=(FONT_NAME, 20))
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=275, text="This is what a sample question will look like. Of course "
                                                          "this is a",
            fill="black",
            font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        check_image = PhotoImage(file="./images/true.png")
        x_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=check_image,
                                  padx=20, pady=20,
                                  highlightthickness=0,
                                  command=self.select_true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=x_image,
                                   padx=20,
                                   pady=20,
                                   highlightthickness=0,
                                   command=self.select_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def select_true(self):
        self.return_feedback(self.quiz.check_answer("True"))
        #self.get_next_question()

    def select_false(self):
        self.return_feedback(self.quiz.check_answer("False"))
        #self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def return_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



