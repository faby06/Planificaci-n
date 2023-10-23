# Ejemplo de planificación con GRAPHPLAN
from graphplan import *

problem = GraphPlanProblem()
problem.declare_actions(...)
problem.set_initial_state(...)
problem.set_goal(...)

planner = GraphPlan(problem)
plan = planner.plan()
print(plan)

