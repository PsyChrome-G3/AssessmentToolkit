from flask import Flask, render_template, request, redirect, url_for
from question import QuestionBank
from question_controller import QuestionController

app = Flask(__name__, static_folder='static')

question_bank = QuestionBank()
question_bank_file = "data/DFIR-QB.json"  # Load the question bank from a JSON file
question_bank.load_from_json(question_bank_file)

loaded_json = question_bank_file.split("/")[-1]  # Extract the file name from the path

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


@app.route('/complete')
def complete():
    return render_template('complete.html')


@app.route('/new-question')
def new_question():
    current_score = question_controller.get_total_score()  # Get the current score
    return question_controller.new_question(total_questions, current_score)


@app.route('/restart', methods=['POST'])
def restart_test():
    question_controller.reset_test()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
