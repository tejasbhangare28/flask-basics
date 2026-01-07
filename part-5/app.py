"""
Personal Website with Flask - Complete Version
Includes: Home, About, Projects, Project Detail, Contact, Dynamic Skill Page
"""

from flask import Flask, render_template

app = Flask(__name__)

# -----------------------------
# PERSONAL INFO
# -----------------------------
PERSONAL_INFO = {
    'name': 'Tejas Bhangare',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask, Python, and web development.',
    'email': 'tejasbhangare5228@gmail.com',
    'github': 'https://github.com/tejasbhangare',
    'linkedin': 'https://linkedin.com/in/tejasbhangare',
}

# -----------------------------
# SKILLS
# -----------------------------
SKILLS = [
    {'name': 'Python', 'level': 85},
    {'name': 'HTML/CSS', 'level': 80},
    {'name': 'Flask', 'level': 70},
    {'name': 'JavaScript', 'level': 60},
    {'name': 'SQL', 'level': 50},
]

# -----------------------------
# PROJECTS
# -----------------------------
PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
]

# -----------------------------
# ROUTES
# -----------------------------

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)

@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS, projects=PROJECTS)

@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)

@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

# Exercise 5.4: Dynamic Skill Route
@app.route('/skill/<skill_name>')
def skill_detail(skill_name):
    filtered_projects = [p for p in PROJECTS if skill_name in p['tech']]
    return render_template('skill.html', info=PERSONAL_INFO, skill_name=skill_name, projects=filtered_projects)

if __name__ == '__main__':
    app.run(debug=True)
