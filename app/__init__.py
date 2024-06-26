import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    skills = ['HTML', 'CSS', 'JavaScript', 'React', 'Next.js', 'Tailwind CSS']
    jobs = [
        {
            'title': 'Front Desk Worker',
            'company': 'Dr. Radhika Jasthi',
            'period': 'Summer 2024',
            'responsibilities': [
                'Greeted patients and visitors in a professional and courteous manner.',
                'Answered and managed incoming calls while recording accurate messages.',
                'Scheduled patient appointments and managed office calendar.'
            ]
        },
        # Add more jobs here
    ]
    projects = [
        {
            'title': 'LaundryConn',
            'description': 'A way to connect UConn student to the laundry machine',
            'image': '../static/img/LaundryConnLogo.jpg',
            'link': 'https://laundryconn.github.io'
        },
        # Add more projects here
    ]
    return render_template('index.html', skills=skills, jobs=jobs, projects=projects, url=os.getenv("URL"), title="MLH Fellow")


# @app.route('/contact', methods=['GET', 'POST'])
# def contact():

@app.route('/hobbies')
def hobbies():
    class Hobby:
        def __init__(self, name, image, description):
            self.name = name
            self.image = image
            self.description = description

    hobbies = [
        Hobby('Piano', '../static/img/', 'Playing the piano brings me joy and relaxation.'),
        Hobby('Chess', '../static/img/chess_image.jpeg', 'Chess is a game of strategy and critical thinking.'),
        Hobby('Art', '../static/img/potato_oil.jpeg', 'Creating art allows me to express my creativity and emotions.')
    ]
    return render_template('hobbies.html', hobbies=hobbies, title="Hobbies")