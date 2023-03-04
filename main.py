# Before to run this program this program run this commands:
# python3 -m venv venv
# pip3 install requests
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
# Loop throught the list of json we got back from the API call.
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
# Save the new list inside the QuizBrain
quiz = QuizBrain(question_bank)
# Passing the quiz to the QuizInterface
quiz_ui = QuizInterface(quiz)