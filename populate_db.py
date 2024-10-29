import datetime
from poll.models import Question, Choice

# Questions to be added to the database
questions = [
    {"question_text": "What's your favorite programming language?", "pub_date": datetime.date(2022, 1, 1)},
    {"question_text": "What's your favorite framework?", "pub_date": datetime.date(2022, 1, 2)},
    {"question_text": "What's your favorite database?", "pub_date": datetime.date(2022, 1, 3)},
]

# Choices to be added to the database, linked to the right question
choices = {
    "What's your favorite programming language?": ["Python", "JavaScript", "Java"],
    "What's your favorite framework?": ["Django", "React"],
    "What's your favorite database?": ["MySQL", "PostgreSQL"],
}

# Add questions to the database
for q in questions:
    question = Question(question_text=q["question_text"], pub_date=q["pub_date"])
    question.save()

    # Add corresponding choices to the question
    for choice_text in choices[q["question_text"]]:
        choice = Choice(question=question, choice_text=choice_text, votes=0)
        choice.save()
