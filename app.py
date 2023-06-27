from flask import Flask, render_template, request
from question import QuestionBank
from markupsafe import Markup

app = Flask(__name__)

question_bank = QuestionBank()
question_bank.load_from_json("data/question_bank.json")

# Function to get a random question
def get_random_question():
    return question_bank.get_random_question()


@app.route('/')
def home():
    question = get_random_question()
    question_text = question.question
    answer_choices = question.answers
    question_id = question.qid
    return render_template('index.html', question_text=question_text, answer_choices=answer_choices, question_id=question_id)


@app.route('/result', methods=['POST'])
def result():
    question_id = request.form['question_id']
    selected_answer = request.form['answer']

    question = question_bank.get_question_by_id(question_id)

    if question is None:
        return render_template('error.html', message='Question not found')

    correct_answer = question.correct_answer

    if selected_answer == correct_answer:
        result = Markup('<div class="alert alert-success" role="alert">Congratulations! You answered correctly.</div>')
    else:
        result = Markup('<div class="alert alert-danger" role="alert">Sorry, your answer is incorrect.</div>')

    return render_template('result.html', result=result)


@app.route('/new-question')
def new_question():
    question = get_random_question()
    question_text = question.question
    answer_choices = question.answers
    question_id = question.qid
    return render_template('index.html', question=question)


if __name__ == '__main__':
    app.run()
