import constants
from main import app
from flask import render_template, request


@app.route('/olimpiads/<olim>')
def olimpiads(olim):
    html = render_template(
        'olimpiads.html',
        olim=olim,
        description=constants.olimpiads_dict[olim]
    )
    return html
