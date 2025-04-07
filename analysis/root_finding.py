from .evaluate import Evaluator

MAX_ITERATIONS = 250

def bisect(expr, a,b, TOL):

    f = Evaluator(expr)
    a,b = f.parse_arguments(a,b)

    if f.evaluate(a) * f.evaluate(b) >= 0:
        print("You have not assumed the right interval.")
        return 404
    mid = a
    iterations = 0
    results = []
    while (b-a) >= TOL and iterations < MAX_ITERATIONS:
        mid = (a+b)/2
        a_copy = a
        b_copy = b
        result = f.evaluate(mid)
        # Check if middle point is root
        if (result == 0):
            break
        # Decide the side to repeat the steps
        if (result*f.evaluate(a) < 0):
            b = mid
        else:
            a = mid
        iterations += 1
        results.append((iterations, a_copy, b_copy, mid, b-a))
    return results, f.get_latex()

def fixed_point_iteration(expr, p, TOL):
    f = Evaluator(expr)
    p = f.parse_arguments(p)
    error = TOL + 2
    iterations = 0
    log = []
    while error > TOL and iterations < MAX_ITERATIONS:
        p_new = f.evaluate(p)
        error = abs(p_new - p)
        p = p_new
        iterations += 1
        log.append((iterations, p, error))
    return log,f.get_latex()

def newton_raphson(expr, derivative, x, TOL):
    f = Evaluator(expr)
    df = Evaluator(derivative)
    x = f.parse_arguments(x)
    error = 1
    iterations = 0
    results = []
    while error > TOL and iterations < MAX_ITERATIONS:
        new_x = x - f.evaluate(x)/df.evaluate(x)
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        results.append((iterations, x, error))
    return results, f.get_latex(), df.get_latex()

def modified_newton(expr, df1, df2, x, TOL):
    f = Evaluator(expr)
    df = Evaluator(df1)
    ddf = Evaluator(df2)
    x = f.parse_arguments(x)
    error = 1
    iterations = 0
    results = []
    while error > TOL and iterations < MAX_ITERATIONS:
        f_x = f.evaluate(x)
        d_x = df.evaluate(x)
        new_x = x - (f_x*d_x)/(d_x*d_x - f_x*ddf.evaluate(x))
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        results.append((iterations, x, error))
    return results, f.get_latex(), df.get_latex(), ddf.get_latex()

def secant_method(expr, x1, x2, TOL):
    f = Evaluator(expr)
    x1, x2 = f.parse_arguments(x1, x2)
    error = 1
    iterations = 2
    result = [(0, x1, 0), (1, x2, 0)]
    while error > TOL and iterations-2 < MAX_ITERATIONS:
        x2_result = f.evaluate(x2)
        x1_result = f.evaluate(x1)
        x_new = x2 - (x2_result*(x2-x1))/(x2_result-x1_result)
        error = abs(x_new - x2)
        x1 = x2
        x2 = x_new
        result.append((iterations, x2, error))
        iterations += 1
    return result, f.get_latex()

def muellers_method(exp, p0, p1, p2, TOL):
    f = Evaluator(exp)
    p0, p1, p2 = f.parse_arguments(p0, p1, p2)
    results = [(0,p0,0),(1,p1,0),(2,p2,0)]
    iterations = 3
    error = 1
    while error > TOL and iterations-3 < MAX_ITERATIONS:

        h1 = p1-p0
        h2 = p2-p1
        print(f'h1={h1}\th2={h2}')
        p1_result = f.evaluate(p1)
        p2_result = f.evaluate(p2)
        del1 = (p1_result-f.evaluate(p0))/h1
        del2 = (p2_result-p1_result)/h2
        d = (del2-del1)/(h2+h1)
        c = p2_result

        b = del2 + h2*d
        discriminant = (b*b - 4*c*d)**0.5

        E = b+discriminant if abs(b-discriminant) < abs(b+discriminant) else b-discriminant

        proximity = -2*c/E
        p = p2+proximity

        error = abs(proximity)
        results.append((iterations, p, error))

        p0 = p1
        p1 = p2
        p2 = p
        iterations += 1
    return results, f.get_latex()

#---------------------------------------Acceleration Technique--------------------------------------------------------

def aitkens_method(expr, p, n):
    f = Evaluator(expr)
    p = f.parse_arguments(p)
    accelerate = lambda x0, x1, x2: (x0*x2 - x1*x1)/(x0 + x2 - 2*x1)
    initial_values = [0] * (n+2)
    for i in range(n+2):
        initial_values[i] = f.evaluate(p)
        p = initial_values[i]
    return [(i, initial_values[i], initial_values[i+1], initial_values[i+2], accelerate(initial_values[i], initial_values[i+1], initial_values[i+2])) for i in range(n)], f.get_latex()

def steffensens_method(expr, p, TOL):
    accelerate = lambda x0, x1, x2: (x0*x2 - x1*x1)/(x0 + x2 - 2*x1)
    f = Evaluator(expr)
    p = f.parse_arguments(p)
    error = 1
    iterations = 0
    result = []
    while error > TOL and iterations < MAX_ITERATIONS:
        p1 = f.evaluate(p)
        p2 = f.evaluate(p1)
        p_new = accelerate(p, p1, p2)
        error = abs(p_new-p)
        iterations += 1
        result.append((iterations, p, p1, p_new, error))
        p = p_new
    return result, f.get_latex()
