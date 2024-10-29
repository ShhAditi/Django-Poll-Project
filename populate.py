import os
import django
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djpoll.settings')
django.setup()

# Import your models
from poll.models import Question, Choice

def populate():
    # Create some sample questions
    question1 = Question.objects.create(
        question_text="What's your favorite programming language?",
        pub_date=timezone.now()
    )
    
    question2 = Question.objects.create(
        question_text="Do you prefer frontend or backend development?",
        pub_date=timezone.now()
    )
    
    # Create some sample choices for question 1
    Choice.objects.create(question=question1, choice_text="Python", votes=5)
    Choice.objects.create(question=question1, choice_text="JavaScript", votes=3)
    Choice.objects.create(question=question1, choice_text="Java", votes=2)
    
    # Create some sample choices for question 2
    Choice.objects.create(question=question2, choice_text="Frontend", votes=7)
    Choice.objects.create(question=question2, choice_text="Backend", votes=10)
    Choice.objects.create(question=question2, choice_text="Fullstack", votes=4)
    
    print("Database has been populated with sample questions and choices.")

# Execute the populate function
if __name__ == '__main__':
    populate()
