import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), 
                     user=os.getenv("MYSQL_USER"), 
                     password=os.getenv("MYSQL_PASSWORD"), 
                     host=os.getenv("MYSQL_HOST"), 
                     port=3306) 

class TimelinePost(Model): 
    name = CharField() 
    email = CharField() 
    content = TextField() 
    created_at = DateTimeField(default=datetime.datetime.now) 
    class Meta: 
        database = mydb 

mydb.connect() 
mydb.create_tables([TimelinePost]) 


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


@app.route('/api/timeline_post', methods=['POST']) 
def post_time_line_post(): 
    name = request.form['name'] 
    email = request.form['email'] 
    content = request.form['content'] 
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post) 

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts' : [
            model_to_dict(p) 
            for p in 
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline():
   return render_template('timeline.html', title="Timeline")

# @app.route('/api/delete_timeline_post/<int:id>', methods=['DELETE'])
# def get_timeline_post(id):
#     try:
#         timeline_post = TimelinePost.get(TimelinePost.id == id)
#         timeline_post.delete_instance()
#         return {'message': 'Timeline post deleted successfully'}, 200
#     except TimelinePost.DoesNotExist:
#         return {'error': 'Timeline post not found'}, 404
