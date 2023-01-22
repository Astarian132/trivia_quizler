import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_NAME = 'Arial'
PATH = "Day_34\\quizzler-app-start\\images\\"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score_text = tkinter.Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='White', font=(FONT_NAME, 12, "bold"))
        self.score_text.grid(row=0, column=1, padx=20, pady=20 )
        self.canvas = tkinter.Canvas(width=400, height=300, bg='white')
        self.canvas.grid(row=1, column=0,columnspan=2, padx=20, pady=20)
        self.questionid = self.canvas.create_text(200, 150, text='Test Question', font=(FONT_NAME, 20, "italic"), width=370)
        true_image = tkinter.PhotoImage(file=PATH + 'true.png')
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_image = tkinter.PhotoImage(file=PATH + 'false.png')
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questionid, text=q_text)
        else:
            self.canvas.itemconfig(self.questionid, text='\tWell done!\n\nYou\'ve reached the end of this quiz')
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')
            self.window.after(5000, exit)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.update()
        self.canvas.after(1000, self.get_next_question(), self.canvas.config(bg='white'), self.score_text.config(text=f'Score: {self.quiz.score}'))

