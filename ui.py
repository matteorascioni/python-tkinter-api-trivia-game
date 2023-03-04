from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE_COLOR = "#fff"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): 
        # General UI setup
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label
        self.score_label = Label(fg=WHITE_COLOR, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg=WHITE_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Dummy text",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #Buttons 
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, columnspan=1)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, columnspan=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """ This function deals with moving on to the next question (checking if there are still any), if not, it disables the buttons and informs the user that the game is over. """
        self.canvas.config(bg=WHITE_COLOR)
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """ This function detect if the true button got pressed """
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """ This function detect if the false button got pressed """
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """ This function gives graphical feedback to the user by changing the colour of the interface, basing the colour on the response (green if it is True, red if it is False). """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)