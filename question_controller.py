from template_renderer import TemplateRenderer


class QuestionController:
    def __init__(self, question_bank, loaded_json):
        self.question_bank = question_bank
        self.loaded_json = loaded_json
        self.question_number = 0  # Initialize question number
        self.score = 0  # Initialize the score attribute to 0

    def get_random_question(self):
        return self.question_bank.get_random_question()

    def home(self, total_questions):
        self.question_number += 1  # Increment question number
        question = self.get_random_question()
        return TemplateRenderer.render_question('index.html', question, self.question_number, total_questions,
                                                self.loaded_json, self.score)

    def result(self, question_id, selected_answer, total_score):
        question = self.question_bank.get_question_by_id(question_id)

        if question is None:
            return TemplateRenderer.render('error.html', message='Question not found')

        correct_answer = str(question.correct_answer)  # Convert to string

        if selected_answer == correct_answer:
            self.score += 1

        score = self.calculate_score(question_id, selected_answer)
        return TemplateRenderer.render_result(correct_answer, selected_answer, self.loaded_json, score, total_score)

    def calculate_score(self, question_id, selected_answer):
        question = self.question_bank.get_question_by_id(question_id)

        if question is None:
            return 0

        correct_answer = str(question.correct_answer)  # Convert to string

        if selected_answer == correct_answer:
            return 1
        else:
            return 0

    def get_total_score(self):
        return self.score

    def new_question(self, total_questions):
        self.question_number += 1  # Increment question number
        question = self.get_random_question()
        return TemplateRenderer.render_question('index.html', question, self.question_number, total_questions,
                                                self.loaded_json, self.score)

