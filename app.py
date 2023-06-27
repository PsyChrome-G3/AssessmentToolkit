from flask import Flask, render_template, request
from question import QuestionBank
from question_controller import QuestionController

app = Flask(__name__, static_folder='static')

question_bank = QuestionBank()
question_bank.load_from_json("data/DFIR-QB.json")

loaded_json = "DFIR-QB.json"  # Replace with your Question Bank file name
question_controller = QuestionController(question_bank, loaded_json)


@app.route('/')
def home():
    return question_controller.home()


@app.route('/result', methods=['POST'])
def result():
    question_id = request.form.get('question_id')
    selected_answer = request.form.get('answer')

    if not question_id or not selected_answer:
        return render_template('error.html', message='Invalid input data.')

    if not question_id.isdigit():
        return render_template('error.html', message='Invalid question ID.')

    question_id = question_id.zfill(4)  # Pad the question ID with leading zeros to a length of 4

    question = question_bank.get_question_by_id(question_id)

    if question is None:
        return render_template('error.html', message='Question not found.')

    if selected_answer not in question.answers:
        return render_template('error.html', message='Invalid selected answer.')

    return question_controller.result(question_id, selected_answer)


@app.route('/new-question')
def new_question():
    return question_controller.new_question()


if __name__ == '__main__':
    app.run()
