from flask import render_template, request
from markupsafe import Markup

class QuestionController:
    def __init__(self, question_bank):
        self.question_bank = question_bank

    def get_random_question(self):
        return self.question_bank.get_random_question()

    def render_question(self, template_name):
        question = self.get_random_question()
        question_text = question.question
        answer_choices = question.answers
        question_id = question.qid
        screenshot_path = question.screenshot_path
        return render_template(template_name, question_text=question_text, answer_choices=answer_choices,
                               question_id=question_id, screenshot_path=screenshot_path)

    def home(self):
        return self.render_question('index.html')

    def result(self):
        question_id = request.form['question_id']
        selected_answer = request.form['answer']

        question = self.question_bank.get_question_by_id(question_id)

        if question is None:
            return render_template('error.html', message='Question not found')

        correct_answer = question.correct_answer

        if selected_answer == correct_answer:
            result = Markup('<div class="alert alert-success" role="alert">Congratulations! You answered correctly.</div>')
        else:
            incorrect_alert = Markup('<div class="alert alert-danger" role="alert">Sorry, your answer is incorrect.</div>')
            correct_alert = Markup('<div class="alert alert-primary" role="alert"><strong>The correct answer is:</strong><br>'
                                   '<div class="correct-answer">' + correct_answer + '</div></div>')
            result = incorrect_alert + correct_alert

        return render_template('result.html', result=result)

    def new_question(self):
        return self.render_question('index.html')
