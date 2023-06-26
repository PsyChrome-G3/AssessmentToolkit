from flask import Flask, render_template, request
from question import QuestionBank

app = Flask(__name__)
question_bank = QuestionBank()
question_bank.load_from_json("data/question_bank.json")


@app.route('/')
def home():
    return render_template('index.html', questions=question_bank.questions)


@app.route('/submit', methods=['POST'])
def submit():
    question_id = request.form['question_id']
    selected_answer = request.form['answer']

    question = question_bank.get_question_by_id(question_id)
    correct_answer = question.correct_answer

    if selected_answer == correct_answer:
        result = "Correct!"
    else:
        result = "Incorrect!"

    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
