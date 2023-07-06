from tkinter import *

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self):
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

        self.window.mainloop()

    def select_true(self):
        print("True!")


    def select_false(self):
        print("False!")

