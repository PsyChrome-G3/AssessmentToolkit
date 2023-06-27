from flask import Flask
from question import QuestionBank
from question_controller import QuestionController

app = Flask(__name__)

question_bank = QuestionBank()
question_bank.load_from_json("data/question_bank.json")

question_controller = QuestionController(question_bank)


@app.route('/')
def home():
    return question_controller.home()


@app.route('/result', methods=['POST'])
def result():
    return question_controller.result()


@app.route('/new-question')
def new_question():
    return question_controller.new_question()


if __name__ == '__main__':
    app.run()
