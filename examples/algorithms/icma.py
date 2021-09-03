from pymoo.algorithms.moo.icma import ICMA
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.factory import get_problem, get_reference_directions, ZDT1, ZDT3, ZDT4, ZDT6, TNK, DASCMOP1, C1DTLZ1, DTLZ1, \
    C2DTLZ2, C3DTLZ1, DTLZ7
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

# problem = get_problem("dascmop1", difficulty=2)

problem = TNK()

# problem = C1DTLZ1()

# problem = DTLZ7()

# problem = get_problem("zdt6")

# create the reference directions to be used for the optimization
if problem.n_obj == 2:
    ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=99)
if problem.n_obj == 3:
    ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)

algorithm = ICMA(ref_dirs=ref_dirs)

res = minimize(problem,
               algorithm,
               ("n_gen", 400),
               seed=1,
               verbose=True)

plot = Scatter()
plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
plot.add(res.F, color="red")
plot.show()
