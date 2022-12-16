import constants
from main import app
from flask import render_template, request


@app.route('/hello', methods=['GET'])
def hello():
    gender = ""
    program_id = 0
    subject_id = []
    subject_select = []
    olimpiads_id = []
    olimpiads_select = []

    gender = request.values.get('gender')
    name = request.values.get('username')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    olimpiads_id = request.values.getlist('olimpiads[]')
    olimpiads_select = [constants.olimpiads[int(i)] for i in olimpiads_id]
    subjects_select = [constants.subjects[int(i)] for i in subject_id]

    html = render_template(
        'hello.html',
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        subjects_select=subjects_select,
        subject_list=constants.subjects,
        olimpiads_select=olimpiads_select
    )
    return html
