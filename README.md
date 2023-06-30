# AssessmentToolkit

This is a simple quiz application built with Flask. It allows users to answer multiple-choice questions and provides feedback on their answers.

## Features

- Create and manage your own exam question bank.
- Support for multiple-choice questions with customizable answer options.
- Ability to include media images to aid in the assessment process.
- Visually appealing GUI front end for an intuitive user experience.
- Immediate feedback on correct and incorrect answers during the assessment.
- Randomization of question order for enhanced challenge.
- Keeps track of the user's score.


## Usage

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/AssessmentToolkit.git
   cd AssessmentToolkit
2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
3. Place your question bank JSON file in the data directory.
4. add any screenshots to the /screenshots directory.
5. Update the **loaded_json** variable in **app.py** with the name of your question bank file.
6. Run the application:
   ```shell
   flask run
7. Open your web browser and go to **http://localhost:5000** to start the quiz.
8. Answer each question by selecting an option and clicking the "Submit" button.
9. After submitting an answer, you will receive feedback on whether your answer was correct or not.
10. Continue answering questions until you have completed the quiz.
11. At the end of the quiz, you will see your total score and the option to restart the quiz.

## Customising the Question Bank

You can customize the questions by modifying the question bank JSON file. The JSON file should follow the following format:

```json lines
[
  {
    "question_id": "001",
    "question_text": "What is the capital of France?",
    "screenshot_path": "screenshots/001.png",
    "answer_choices": ["London", "Paris", "Berlin", "Rome"],
    "correct_answer": "Paris"
  },
  {
    "question_id": "002",
    "question_text": "Which planet is closest to the Sun?",
    "screenshot_path": "screenshots/002.png",
    "answer_choices": ["Venus", "Mars", "Mercury", "Earth"],
    "correct_answer": "Mercury"
  },
  ...
]
```
- **question_id** (string): A unique identifier for the question.
- **question_text** (string): The text of the question.
- **screenshot_path** (string): The path to an optional screenshot image related to the question.
- **answer_choices** (list of strings): The available answer choices for the question.
- **correct_answer** (string): The correct answer for the question.

You can add, remove, or modify the questions in the JSON file to suit your needs.

## TO-DO

- [X] Determine the file format for storing exam questions.
- [X] Design the data structure to represent questions, answers, and media.
- [X] Implement the GUI using a suitable library (e.g., Tkinter, PyQt, etc.).
- [X] Read and parse the input file to extract question data.
- [X] Present questions to the user with answer options and media images.
- [X] Evaluate user answers and provide immediate feedback.
- [X] Implement the ability to move to the next question.
- [X] Repeat the process until the end of the exam.
- [ ] Add extra features like a timer, random question order, review mode, and progress saving.
- [ ] Implement statistics and analytics for performance tracking.
- [ ] Perform thorough testing and bug fixing.

## License

This project is licensed under the [MIT License](LICENSE).