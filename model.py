from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
	"""Questions for users."""

	__tablename__ = "questions"

	question_id = db.Column(db.Integer, primary_key=True)
	strand_id = db.Column(db.Integer)
	strand_name = db.Column(db.String(64))
	standard_id = db.Column(db.Integer)
	standard_name = db.Column(db.String(64))
	difficulty = db.Column(db.Float)

	def __repr__(self):
		"""Provides helpful representation when printed of question id."""

		# return "<Question question_id={}, strand_name={}, standard_name={}, difficulty={}".format(self.question_id, self.strand_name, self.standard_name, self.difficulty)
		return '{}'.format(self.question_id)

def connect_to_db(app):
	"""Connect the database to our Flask app."""

	# Configure to use our PstgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///questions'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.app = app
	db.init_app(app)


if __name__ == "__main__":
	# As a convenience, if we run this module interactively, it will leave
	# you in a state of being able to work with the database directly.

	from server import app
	connect_to_db(app)
