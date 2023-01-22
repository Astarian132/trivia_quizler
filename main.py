from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface
import html

question_bank = []
for question in question_data:
    #print(question['question'])
    question_text = html.unescape(question["question"])
    question_answer = html.unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizzInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
