from model import Question
from model import connect_to_db, db
from server import app
import csv

def load_questions():
	"""Load questions from questions.csv"""

	print "Questions table"

	with open('questions.csv') as questions_file:
		for row in questions_file.readlines()[1:]:
			row = row.rstrip()
			strand_id, strand_name, standard_id, standard_name, question_id, difficulty = row.split(',')

			question = Question(strand_id=strand_id, strand_name=strand_name, standard_id=standard_id, standard_name=standard_name, question_id=question_id, difficulty=difficulty)
			
			db.session.add(question)
		db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    print "Connected to DB."
    # In case tables haven't been created, create them
    db.create_all()
    # Import the questions data
    load_questions()
