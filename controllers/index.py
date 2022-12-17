
from flask import render_template, request

import constants
from main import app


@app.route('/', methods=['GET'])
def index():
    gender = request.values.get('gender')
    name = str(request.values.get('username'))
    program_id = request.values.get('program')
    if str(program_id) == "None":
        program_id = -4
    subject_id = request.values.getlist('subject[]')
    olimpiads_id = request.values.getlist('olimpiads[]')
    olimpiads_select = [constants.olimpiads[int(i)] for i in olimpiads_id]
    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    program = ""
    if program_id == -4:
        program = ""
    else:
        program = constants.programs[int(program_id)]
    print(name)
    html = render_template('index.html',
                            len=len,
                            program_list=constants.programs,
                            subject_list=constants.subjects,
                            olimpiad_list=constants.olimpiads,
                            name=name,
                            gender=gender,
                            program=program,
                            subjects_select=subjects_select,
                            olimpiads_select=olimpiads_select
                           )
    return html
