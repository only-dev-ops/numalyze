from .evaluate import Evaluator

def trapezoidal(expr, a, b, n):
    f = Evaluator(expr)
    a, b, n = f.parse_arguments(a,b,n)
    h = (b-a)/n

    total = (f.evaluate(a)+f.evaluate(b))/2
    x = a + h

    for i in range(n-1):
        total += f.evaluate(x)
        x += h

    return total*h, f.get_latex()

def simpsons(expr, a, b, n):
    f = Evaluator(expr)
    a, b, n = f.parse_arguments(a,b,n)
    if n % 2 == 1:
        n += 1
    h = (b-a)/n

    total = f.evaluate(a) + f.evaluate(b)
    x = a+h

    for i in range(n-1):
        coeff = 2 if (i & 1) else 4
        total += coeff * f.evaluate(x)
        x += h

    return total*h/3, f.get_latex()

def rombergs(expr, a, b, n):
    f = Evaluator(expr)
    a, b, n = f.parse_arguments(a, b, n)
    h = (b-a)
    R = [[0]*n,[0]*n]
    R[0][0] = h/2*(f.evaluate(a)+ f.evaluate(b))
    results = []
    results.append([R[0][0]])

    for i in range(2, n+1):
        R[1][0] = 0.5*(R[0][0] + h*(sum([f.evaluate(a+(k-0.5)*h) for k in range(1, 2**(i-2)+1)])))

        for j in range(2, i+1):
            R[1][j-1] = R[1][j-2]+(R[1][j-2]-R[0][j-2])/(4**(j-1)-1)

        res = []
        for k in range(i):
            res.append(R[1][k])
        results.append(res)

        h = h/2

        for j in range(1, i+1):
            R[0][j-1] = R[1][j-1]
        
    return results, f.get_latex()
