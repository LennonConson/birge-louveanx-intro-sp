import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x_1 = pyo.Var(within=pyo.NonNegativeReals)
model.x_2 = pyo.Var(within=pyo.NonNegativeReals)
model.x_3 = pyo.Var(within=pyo.NonNegativeReals)
model.x_4 = pyo.Var(within=pyo.NonNegativeReals)
model.y_1 = pyo.Var(within=pyo.NonNegativeReals)
model.y_2 = pyo.Var(within=pyo.NonNegativeReals)

model.obj = pyo.Objective(expr= -150 *model.x_1 - 180 *model.x_2 - 12*model.x_3 - 10*model.x_4
                        + (30*model.y_1 + 70*model.y_2) , sense=pyo.maximize)

model.con1 = pyo.Constraint(expr= 6*model.x_3 + 10*model.x_4 <=  60*model.x_1)
model.con2 = pyo.Constraint(expr= 8*model.x_3 +  5*model.x_4 <=  90*model.x_2)
model.con3 = pyo.Constraint(expr=   model.x_1 +  model.x_2 <= 120)
model.con4 = pyo.Constraint(expr= 73.333333333333                        ==     model.x_1)
model.con5 = pyo.Constraint(expr= 46.666666666666                         ==     model.x_2)
model.con6 = pyo.Constraint(expr=   model.y_1                <= 500)
model.con7 = pyo.Constraint(expr=   model.y_2                <= 200)
model.con8 = pyo.Constraint(expr=   model.x_3                >= model.y_1)
model.con9 = pyo.Constraint(expr=   model.x_4                >= model.y_2)


opt = pyo.SolverFactory('glpk')
results = opt.solve(model)
pyo.assert_optimal_termination(results) 

model.display()
