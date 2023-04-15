THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", font=("Arial", 15, "normal"), bg=THEME_COLOR)
        self.score.grid(column=1, row=0, pady=20)


        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="quote by quote", font=("Arial", 20, "italic"), width=280, fill="black")





        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, borderwidth=0, highlightcolor=THEME_COLOR, command=self.false_pressed)
        self.false.grid(column=0, row=2, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.true_img, highlightthickness=0, borderwidth=0, highlightcolor=THEME_COLOR, command=self.true_pressed)
        self.true.grid(column=1, row=2, pady=20)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.scores}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)








