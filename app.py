from flask import Flask, render_template, request
from question import QuestionBank
from question_controller import QuestionController

app = Flask(__name__, static_folder='static')

question_bank = QuestionBank()
question_bank.load_from_json("data/DFIR-QB.json")

loaded_json = "DFIR-QB.json"  # Replace with your Question Bank file name

total_questions = len(question_bank.questions)  # Initialize total_questions here

question_controller = QuestionController(question_bank, loaded_json, total_questions)

question_number = 0


@app.route('/')
def home():
    current_score = question_controller.get_total_score()  # Get the current score
    return question_controller.home(total_questions, current_score)


@app.route('/result', methods=['POST'])
def result():
    question_id = request.form.get('question_id')  # Get the question ID from the form
    selected_answer = request.form.get('selected_answer')  # Get the selected answer from the form

    if not question_id or not selected_answer:
        return render_template('error.html', message='Invalid input data.')

    if not question_id.isdigit():
        return render_template('error.html', message='Invalid question ID.')

    question_id = question_id.zfill(4)  # Pad the question ID with leading zeros to a length of 4

    return question_controller.result(question_id, selected_answer)


@app.route('/new-question')
def new_question():
    current_score = question_controller.get_total_score()  # Get the current score
    return question_controller.new_question(total_questions, current_score)


if __name__ == '__main__':
    app.run()
