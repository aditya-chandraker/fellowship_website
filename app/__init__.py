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
            'title': 'Front-End Developer',
            'company': 'Acme Inc.',
            'period': '2021 - 2023',
            'responsibilities': [
                'Developed responsive and accessible web applications using React, Next.js, and Tailwind CSS.',
                'Collaborated with designers and back-end developers to deliver high-quality features.',
                'Implemented best practices for performance optimization and code maintainability.',
                'Participated in code reviews and mentored junior developers.'
            ]
        },
        # Add more jobs here
    ]
    projects = [
        {
            'title': 'Project 1',
            'description': 'A modern and responsive website for a startup company.',
            'image': '/placeholder.svg'
        },
        # Add more projects here
    ]
    return render_template('index.html', skills=skills, jobs=jobs, projects=projects, url=os.getenv("URL"), title="MLH Fellow")