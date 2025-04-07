from flask import render_template, request
from . import app
from .root_finding import *
from .integration import *
from .rref import reduced_row_echelon_form

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/usage')
def usage():
    return render_template('usage.html')

@app.route('/bisection-method', methods=['POST', 'GET'])
def bisection():
    if request.method == 'POST':
        func = request.form['function']
        interval = request.form['interval'].split(',')
        TOL = float(request.form['TOL'])
        result, eq = bisect(func, interval[0], interval[1], TOL)
        return render_template('bisection.html', data={'result': result, 'equation':eq})
    return render_template('bisection.html', data=None)

@app.route('/fixed-point', methods=['POST', 'GET'])
def fixed_point():
    if request.method == 'POST':
        func = request.form['function']
        initial = request.form['initial']
        TOL = float(request.form['TOL'])
        result, eq = fixed_point_iteration(func, initial, TOL)
        return render_template('fixed-point.html', data={'result': result, 'equation':eq})
    return render_template('fixed-point.html', data=None)

@app.route('/newton', methods=['POST', 'GET'])
def newton():
    if request.method == 'POST':
        func = request.form['function']
        derivative = request.form['derivative']
        checked = request.form.get('option')            # Check if the check-box is selected. If it is, user wants Modified Newton's Method.
        initial = request.form['initial']
        TOL = float(request.form['TOL'])
        if checked == "on":
            second_derivative = request.form['second_derivative']
            result, eq, df, ddf = modified_newton(func, derivative, second_derivative, initial, TOL)
            return render_template('newton.html', data={'modified_newton':True, 'result': result, 'equation':eq, 'derivative': df, 'ddf': ddf})
        else:
            result, eq, df = newton_raphson(func, derivative, initial, TOL)
            return render_template('newton.html', data={'result': result, 'equation':eq, 'derivative': df})
    return render_template('newton.html', data=None)

@app.route('/secant-method', methods=['POST', 'GET'])
def secant():
    if request.method == 'POST':
        func = request.form['function']
        points = request.form['initial_points'].split(',')
        TOL = float(request.form['TOL'])
        result, eq = secant_method(func, points[0], points[1], TOL)
        return render_template('secant.html', data={'result': result, 'equation':eq})
    return render_template('secant.html', data=None)

@app.route('/muellers-method', methods=['POST', 'GET'])
def muellers():
    if request.method == 'POST':
        func = request.form['function']
        points = request.form['initial_points'].split(',')
        TOL = float(request.form['TOL'])
        result, eq = muellers_method(func, points[0], points[1], points[2], TOL)
        return render_template('muellers.html', data={'result': result, 'equation':eq})
    return render_template('muellers.html', data=None)

@app.route('/aitkens-method', methods=['POST', 'GET'])
def aitkens():
    if request.method == 'POST':
        func = request.form['function']
        point = request.form['initial_point']
        iterations = int(request.form['iter'])
        result, eq = aitkens_method(func, point, iterations)
        return render_template('aitkens.html', data={'result': result, 'equation':eq})
    return render_template('aitkens.html', data=None)

@app.route('/steffensens-method', methods=['POST', 'GET'])
def steffensens():
    if request.method == 'POST':
        func = request.form['function']
        point = request.form['initial_point']
        TOL = float(request.form['TOL'])
        result, eq = steffensens_method(func, point, TOL)
        return render_template('steffensens.html', data={'result': result, 'equation':eq})
    return render_template('steffensens.html', data=None)

@app.route('/composite-trapezoidal', methods=['POST', 'GET'])
def composite_trapezoidal():
    if request.method == 'POST':
        func = request.form['function']
        llimit = request.form['llimit']
        ulimit = request.form['ulimit']
        n = request.form['n']
        result, eq = trapezoidal(func, llimit, ulimit, n)
        return render_template('trapezoidal.html', data={'result': result, 'equation':eq})
    return render_template('trapezoidal.html', data=None)

@app.route('/simpsons', methods=['POST', 'GET'])
def composite_simpsons():
    if request.method == 'POST':
        func = request.form['function']
        llimit = request.form['llimit']
        ulimit = request.form['ulimit']
        n = request.form['n']
        result, eq = simpsons(func, llimit, ulimit, n)
        return render_template('simpsons.html', data={'result': result, 'equation':eq})
    return render_template('simpsons.html', data=None)

@app.route('/rombergs', methods=['POST', 'GET'])
def romberg():
    if request.method == 'POST':
        func = request.form['function']
        llimit = request.form['llimit']
        ulimit = request.form['ulimit']
        n = request.form['n']
        result, eq = rombergs(func, llimit, ulimit, n)
        return render_template('romberg.html', data={'result': result, 'equation':eq})
    return render_template('romberg.html', data=None)


@app.route("/rref", methods=["GET", "POST"])
def rref():
    """
    Shows a form where the user can:
      - Enter # of rows/cols
      - Dynamically fill in the matrix
    On submission, runs reduced_row_echelon_form and displays the result.
    """
    if request.method == "POST":

        rows = int(request.form.get("rows", "0"))
        cols = int(request.form.get("cols", "0"))

        matrix = []
        for r in range(rows):
            row_data = []
            for c in range(cols):
                key = f"matrix-{r}-{c}"
                val_str = request.form.get(key, "0")
                val_float = int(val_str)
                row_data.append(val_float)
            matrix.append(row_data)
        import copy
        in_matrix = copy.deepcopy(matrix)
        reduced_row_echelon_form(matrix)

        data = {
            "original_matrix": in_matrix,
            "rref_matrix": matrix,
            "rows": rows,
            "cols": cols
        }
        
        return render_template("rref.html", data=data)

    return render_template("rref.html")