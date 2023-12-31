from flask import render_template
from markupsafe import Markup


class TemplateRenderer:
    @staticmethod
    def render(template_name, **context):
        return render_template(template_name, **context)

    @staticmethod
    def render_question(template_name, question, question_number, total_questions, loaded_json, score, current_score):
        context = {
            'question_text': question.question,
            'answer_choices': question.answers,
            'question_id': question.qid,
            'screenshot_path': question.screenshot_path,
            'question_number': question_number,
            'total_questions': total_questions,
            'loaded_json': loaded_json,
            'score': score,
            'current_score': current_score
        }
        return TemplateRenderer.render(template_name, **context)

    @staticmethod
    def render_result(correct_answer, selected_answer, loaded_json, score, total_questions, current_score):
        correct_answer_str = str(correct_answer)

        if selected_answer == correct_answer:
            result = Markup(
                '<div class="alert alert-success" role="alert">Congratulations! You answered correctly.</div>')
        else:
            incorrect_alert = Markup(
                '<div class="alert alert-danger" role="alert">Sorry, your answer is incorrect.</div>')
            correct_alert = Markup(
                '<div class="alert alert-primary" role="alert"><strong>The correct answer is:</strong><br>'
                '<div class="correct-answer">' + correct_answer_str + '</div></div>')
            result = incorrect_alert + correct_alert

        context = {
            'result': result,
            'loaded_json': loaded_json,
            'score': score,
            'total_questions': total_questions,
            'current_score': current_score
        }

        return TemplateRenderer.render('result.html', **context)
