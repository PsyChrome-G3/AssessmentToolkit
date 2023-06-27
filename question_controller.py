from template_renderer import TemplateRenderer


class QuestionController:
    def __init__(self, question_bank, loaded_json):
        self.question_bank = question_bank
        self.loaded_json = loaded_json

    def get_random_question(self):
        return self.question_bank.get_random_question()

    def home(self):
        question = self.get_random_question()
        return TemplateRenderer.render_question('index.html', question, self.loaded_json)

    def result(self, question_id, selected_answer):
        question = self.question_bank.get_question_by_id(question_id)

        if question is None:
            return TemplateRenderer.render('error.html', message='Question not found')

        correct_answer = str(question.correct_answer)  # Convert to string
        return TemplateRenderer.render_result(correct_answer, selected_answer, self.loaded_json)

    def new_question(self):
        question = self.get_random_question()
        return TemplateRenderer.render_question('index.html', question, self.loaded_json)
