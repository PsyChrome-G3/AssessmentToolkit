import pandas as pd
import json

# Place this script in the same directory as your excel file and change the name below to match.
excel_file = 'SANS FOR508 Questions.xlsx'
df = pd.read_excel(excel_file)

# Create an empty list to store the questions
questions = []

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    # Extract the relevant information from the row
    question_id = str(row['QID']).zfill(4)  # Preserve leading zeros
    question_text = row['Question']
    screenshot_path = row['Image']
    answer_choices = [answer for answer in row[['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']].tolist() if not pd.isnull(answer)]
    correct_answer = row['Correct Answer']

    # Handle empty screenshot field
    if pd.isnull(screenshot_path):
        screenshot_path = None

    # Create a dictionary for the question
    question_data = {
        'question_id': question_id,
        'question_text': question_text,
        'screenshot_path': screenshot_path,
        'answer_choices': answer_choices,
        'correct_answer': correct_answer
    }

    # Append the question to the list
    questions.append(question_data)

# Write the questions to a JSON file
output_file = 'DFIR-QB.json'
with open(output_file, 'w') as json_file:
    json.dump(questions, json_file, indent=4)

print('JSON question bank has been created successfully.')