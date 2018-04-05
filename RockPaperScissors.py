from scipy.optimize import minimize
import numpy as np

#reward matrix for A (zero-sum game)
reward_matrix = [[0,  1, -1],
                 [-1, 0,  1],
                 [1, -1,  0]]
reward_matrix = [[0,  2, -1],
                 [-2, 0,  1],
                 [1, -1,  0]]

# We want to minimize ( maximum (R(probabilities)))

def objective(x):
    #maximum (R(probabilities)) is set to the last in array
    return x[-1]

def Rock(x):
    column = 0
    reward =  x[0] * reward_matrix[0][column] + x[1] * reward_matrix[1][column] + x[2] * reward_matrix[2][column]
    return -(reward - x[-1])
def Paper(x):
    column = 1
    reward = x[0] * reward_matrix[0][column] + x[1] * reward_matrix[1][column] + x[2] * reward_matrix[2][column]
    return -(reward - x[-1])
def Scissors(x):
    column = 2
    reward = x[0] * reward_matrix[0][column] + x[1] * reward_matrix[1][column] + x[2] * reward_matrix[2][column]
    return -(reward - x[-1])

def Probabilities(x):
    return sum(x[0:-1]) - 1

x0 = [1,1,1,1]
b = (0.0,1.0)
bnds = (b,b,b,(None,None))
rock = {'type': 'ineq','fun':Rock}
paper = {'type': 'ineq','fun':Paper}
scissors = {'type': 'ineq','fun':Scissors}
prob = {'type': 'eq','fun':Probabilities}
sol = minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=[rock,paper,scissors,prob])
print(sol)