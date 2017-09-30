from flask import Flask, render_template
from utils import occupation

my_app = Flask(__name__)

jobs = occupation.dictCreate(occupation.read('data/occupations.csv'))

def output():
    return render_template('occupations.html', dict = jobs, job = occupation.jobGen(jobs))

@my_app.route('/')
def root():
    return "Welcome to your future!"

@my_app.route('/occupations')
def occ():
    return output()

if __name__=='__main__':
    my_app.debug = "true"
    my_app.run()
