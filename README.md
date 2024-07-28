![image](https://github.com/user-attachments/assets/e94fd5fd-d852-4edb-b3a4-a475dc00a186)
# Production Engineering Portfolio Site
I used a Digital Ocean droplet VPS with CentOS to host this website on port 5000. This is a flask app which uses Jinja templating

![DigitalOcean](https://img.shields.io/badge/DigitalOcean-0080FF?style=flat&logo=digitalocean&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja-FFB94D?style=flat&logo=jinja&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Tmux](https://img.shields.io/badge/Tmux-1BB91F?style=flat&logo=tmux&logoColor=white)
![Vim](https://img.shields.io/badge/Vim-019833?style=flat&logo=vim&logoColor=white)


## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run --host=0.0.0.0
```