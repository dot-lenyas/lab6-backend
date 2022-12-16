
from flask import render_template

import constants
from main import app


@app.route('/', methods=['GET'])
def index():
     html = render_template('index.html',
                            len=len,
                            program_list=constants.programs,
                            subject_list=constants.subjects,
                            olimpiad_list=constants.olimpiads)
     return html
