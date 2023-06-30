import json
import random


class Question:
    def __init__(self, qid, text, question, screenshot_path, answers, correct_answer):
        self.qid = qid
        self.text = text
        self.question = question
        self.screenshot_path = screenshot_path
        self.answers = answers
        self.correct_answer = correct_answer

    def __str__(self):
        return f"Question {self.qid}: {self.question}"

    def randomize_answers(self):
        random.shuffle(self.answers)


class QuestionBank:
    def __init__(self):
        self.questions = []
        self.used_question_ids = set()

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

                question = Question(
                    question_id, question_text, question_text, screenshot_path, answer_choices, correct_answer
                )
                question.randomize_answers()  # Randomize the answer choices
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
        if len(self.used_question_ids) == len(self.questions):
            # All questions have been used
            print("All questions have been used.")
            return None

        remaining_questions = [question for question in self.questions if question.qid not in self.used_question_ids]
        if len(remaining_questions) == 1:
            # Last remaining question
            print("Last remaining question.")
            question = remaining_questions[0]
        else:
            question = random.choice(remaining_questions)

        self.used_question_ids.add(question.qid)
        return question

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
