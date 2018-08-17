from flask import Flask
from model import Question, connect_to_db, db
import sys
import random

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


def distribute_questions():
    """Print out num of questions based on argv"""
    try:
        if sys.argv[1]:
            num_questions = int(sys.argv[1])
            strand_1 = Question.query.filter_by(strand_id=1).all()
            strand_2 = Question.query.filter_by(strand_id=2).all()
            if num_questions % 2 == 0:
                final_questions = random.sample(strand_1, num_questions/2) + random.sample(strand_2, num_questions/2)
                print ', '.join([str(i) for i in final_questions])


                
            
    except IndexError:
        print 'Please enter a number to receive questions'


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    distribute_questions()
    #do not need to run server on localhost for this assignment
    # app.run(port=5000, host='0.0.0.0')
