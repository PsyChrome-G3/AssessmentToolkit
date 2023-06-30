from template_renderer import TemplateRenderer
import random


class QuestionController:
    def __init__(self, question_bank, loaded_json, total_questions):
        self.question_bank = question_bank
        self.questions = question_bank.questions
        self.loaded_json = loaded_json
        self.question_number = 0
        self.score = 0
        self.total_questions = total_questions
        self.used_question_ids = set()  # Initialize as an empty set

    def get_random_question(self):
        if len(self.used_question_ids) == len(self.questions):
            # All questions have been used
            print("All questions have been used.")
            return None

        remaining_questions = [question for question in self.questions if question.qid not in self.used_question_ids]
        if len(remaining_questions) <= 1:
            # Last remaining question or no remaining questions
            print("Last remaining question or no remaining questions.")
            question = remaining_questions[0] if remaining_questions else None
        else:
            question = random.choice(remaining_questions)

        if question:
            self.used_question_ids.add(question.qid)

        print("Selected question:", question.qid)
        print('Remaining Questions: ' + str(len(remaining_questions)))

        return question

    def home(self, total_questions, current_score):
        self.question_number += 1

        if self.question_number == 1:
            question = self.get_random_question()
        else:
            remaining_questions = [question for question in self.questions if
                                   question.qid not in self.used_question_ids]
            if len(remaining_questions) == 0:
                # No more questions remaining
                return TemplateRenderer.render('complete.html', current_score=current_score,
                                               total_questions=self.total_questions)
            question = remaining_questions[0]
            self.used_question_ids.add(question.qid)

        if question is None:
            return TemplateRenderer.render('complete.html', current_score=current_score,
                                           total_questions=self.total_questions)

        return TemplateRenderer.render_question('index.html', question, self.question_number, total_questions,
                                                self.loaded_json, self.score, current_score)

    def result(self, question_id, selected_answer):
        question = self.question_bank.get_question_by_id(question_id)

        if question is None:
            return TemplateRenderer.render('error.html', message='Question not found')

        correct_answer = str(question.correct_answer)

        score = self.calculate_score(question_id, selected_answer)
        self.score += score  # Update the overall score

        current_score = self.score
        return TemplateRenderer.render_result(correct_answer, selected_answer, self.loaded_json, score,
                                              self.total_questions, current_score)

    def calculate_score(self, question_id, selected_answer):
        question = self.question_bank.get_question_by_id(question_id)

        if question is None:
            return 0

        correct_answer = str(question.correct_answer)

        if selected_answer == correct_answer:
            return 1
        else:
            return 0

    def get_total_score(self):
        return self.score

    def new_question(self, total_questions, current_score):
        if self.question_number >= self.total_questions:
            print('we are at 1')
            return TemplateRenderer.render('complete.html', current_score=current_score,
                                           total_questions=self.total_questions)
        else:
            question = self.get_random_question()

            if question is None:
                print('we are at 2')
                return TemplateRenderer.render('complete.html', current_score=current_score,
                                               total_questions=self.total_questions)

            self.question_number += 1
            print('we are at 3')
            return TemplateRenderer.render_question('index.html', question, self.question_number, total_questions,
                                                    self.loaded_json, self.score, current_score)

    def reset_test(self):
        self.question_number = 0
        self.used_question_ids = set()  # Initialize as an empty set
        self.score = 0
