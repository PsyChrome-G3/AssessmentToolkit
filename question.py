import json
import random


class Question:
    def __init__(self, qid, question, screenshot_path, answers, correct_answer):
        self.qid = qid
        self.question = question
        self.screenshot_path = screenshot_path
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
        try:
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

        except FileNotFoundError:
            print(f"Error: JSON file '{json_file}' not found.")

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file '{json_file}'.")

    def get_question_by_id(self, question_id):
        for question in self.questions:
            if question.qid == question_id:
                return question
        return None

    def get_random_question(self):
        return random.choice(self.questions)

    def save_to_json(self, json_file):
        try:
            question_bank_data = []
            for question in self.questions:
                question_data = {
                    'question_id': question.qid,
                    'question_text': question.question,
                    'screenshot_path': question.screenshot_path,
                    'answer_choices': question.answers,
                    'correct_answer': question.correct_answer
                }
                question_bank_data.append(question_data)

            with open(json_file, 'w') as file:
                json.dump(question_bank_data, file)

        except Exception as e:
            print(f"Error: Failed to save question bank to JSON file '{json_file}'.")
            print(e)
