import json


class Question:
    def __init__(self, qid, question, screenshot, answers, correct_answer):
        self.qid = qid
        self.question = question
        self.screenshot = screenshot
        self.answers = answers
        self.correct_answer = correct_answer

    def __str__(self):
        return f"Question {self.qid}: {self.question}"


class QuestionBank:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def load_from_json(self, json_file):
        with open(json_file) as file:
            question_bank_data = json.load(file)

        for question_data in question_bank_data:
            question_id = question_data['QID']
            question_text = question_data['Question']
            screenshot_path = question_data['Screenshot relative path']
            answer_choices = []
            for i in range(1, 11):
                answer = question_data.get(f'A{i}', None)
                if answer:
                    answer_choices.append(answer)

            correct_answer = question_data['Correct Answer']

            question = Question(question_id, question_text, screenshot_path, answer_choices, correct_answer)
            self.questions.append(question)

    def save_to_json(self, json_file):
        # Save self.questions to a JSON file
        pass