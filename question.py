import json
import random


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
            question_id = question_data['question_id']
            question_text = question_data['question_text']
            screenshot_path = question_data['screenshot_path']
            answer_choices = question_data['answer_choices']
            correct_answer = question_data['correct_answer']

            question = Question(question_id, question_text, screenshot_path, answer_choices, correct_answer)
            self.questions.append(question)

    def get_question_by_id(self, question_id):
        for question in self.questions:
            if question.qid == question_id:
                return question
        return None

    def get_random_question(self):
        return random.choice(self.questions)

    def save_to_json(self, json_file):
        # Save self.questions to a JSON file
        pass
