from pymoo.algorithms.soo.nonconvex.cmaes import CMAES
from pymoo.factory import Problem
from pymoo.core.evaluator import set_cv

from pymoo.util.termination.no_termination import NoTermination


class MyProblem(Problem):

    def __init__(self, n_var=10):
        super().__init__(n_var=n_var, n_obj=1, n_constr=0, xl=-0, xu=1)


problem = MyProblem()

algorithm = CMAES().setup(problem, termination=NoTermination(), verbose=False)

for k in range(200):

    if not algorithm.has_next():
        break

    infills = algorithm.ask()

    X = infills.get("X")

    F = (X ** 2).sum(axis=1)
    G = - (X[:, 0] + X[:, 1]) - 0.3

    infills.set("F", F[:, None], "G", G[:, None])
    set_cv(infills)

    algorithm.tell(infills=infills)

    print(k + 1, algorithm.opt[0].F[0])

print(algorithm.opt.get("F"))
