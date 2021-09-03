from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.factory import get_problem
from pymoo.optimize import minimize


problem = get_problem("ackley", n_var=30)

algorithm = DE(
    pop_size=100,
    variant="DE/best/1/bin",
    CR=0.7,
    dither="vector",
    jitter=True
)

res = minimize(problem,
               algorithm,
               seed=1,
               verbose=False)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))
