from flask import Flask
app = Flask(__name__)

def is_complex(val):
    return isinstance(val, complex)

app.jinja_env.filters['is_complex'] = is_complex

import analysis.views
