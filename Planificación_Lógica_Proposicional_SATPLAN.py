# Ejemplo de planificación con SATPLAN
from satplan import *

problem = SatPlanProblem()
problem.declare_actions(...)
problem.set_initial_state(...)
problem.set_goal(...)

planner = SatPlan(problem)
plan = planner.plan()
print(plan)

