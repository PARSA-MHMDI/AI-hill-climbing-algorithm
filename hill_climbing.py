# -*- coding: utf-8 -*-
"""Hill Climbing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EhN-BaCRjStBN_W0X7w2hVi7RZUmXu2N

# Hill Climbing Algorithem

## librarires
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from copy import deepcopy
from copy import copy
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import random
import matplotlib.pyplot as plt

# %matplotlib inline

"""## Colab Setting

### Mount Drive on Colab
"""

from google.colab import drive
drive.mount('/content/drive')

"""## Pre_prosseing With DATA

### Load Data
"""

with open('/content/drive/MyDrive/Colab Notebooks/AI Class Project 1/dj38.tsp') as f:
    file = f.read().split("\n")
    #print(file)
    index=[]
    x=[]
    y = []
    for i in file:
        a , b, c = i.split()
        index.append(int(a)-1) # in here I change city numbers from 1 to m into 0 to m-1 to be same as list index
        x.append(float(b))
        y.append(float(c))
print(index)
print(x)
print(y)

"""### Display data"""

plt.style.use('seaborn-whitegrid')

plt.plot(y, x, 'o', color='black');

"""## Defind Functions

### Computing distanatce between two cities (Function):
"""

def distance(x1,y1 ,x2,y2):
  dis = np.sqrt(np.square(x1-x2) + np.square(y1-y2))
  return dis

print(f"first ({x[0]},{y[0]}) and second ({x[1]},{y[1]})")
distance(x[0],y[0], x[1],y[1])

"""### Make matrix of distance:"""

def tsp_matrix(x,y):
  tsp = []
  row = []
  for i in range(len(x)):
    row.clear()
    for j in range(len(x)):
      row.append(distance(x[i],y[i] ,x[j],y[j]))
    r = copy(row)
    tsp.append(r)
  return tsp

#test

print(tsp_matrix(x,y))

"""### Make random sluoition"""

def random_solution(tsp):
  cities = list(range(len(tsp)))
  solution = []

  for i in range(len(tsp)):
    random_city = cities[random.randint(0,len(cities)-1)]
    solution.append(random_city)
    cities.remove(random_city)

  return solution

# test of function
tsp = tsp_matrix(x,y)
print(random_solution(tsp), len(random_solution(tsp)))

"""### Find routelength of soluotion"""

def route_length(tsp, solution):
  """
  Funciton input is tsp and solution which tsp is matrix of distance between cites and solution is list of cites

  The output is length of solution from firt city to the goal (cost)
  """
  length = 0
  for i in range(len(solution)):
    length += tsp[solution[i-1]][solution[i]]
  return length

# test
tsp = tsp_matrix(x,y)
rands = random_solution(tsp)
print(route_length(tsp,rands))

"""### Find neighbors of a solution

"""

def find_neighbors(solution):
  neighbors = []
  for i in range(len(solution)): #This for loop will make new list from solution by changing element positions
    for j in range(i+1,len(solution)):
      a = solution.copy()
      a[i] = solution[j]
      a[j] = solution[i]
      neighbors.append(a)
  return neighbors

# test
solution = random_solution(tsp)
print(find_neighbors(solution))

"""### Find best neighbor"""

def find_best_neighbor(tsp , neighbors):
  best_neighbor_length = route_length(tsp, neighbors[0]) # Initial answer
  best_neighbor = neighbors[0]

  for i in neighbors:
    current_length = route_length(tsp , i)
    if current_length < best_neighbor_length :
      best_neighbor_length = current_length
      best_neighbor = i
  
  return best_neighbor, best_neighbor_length

"""### Plot Cost"""

def plot_cost(cost_value):
  iteration = []
  for i in range(1,len(cost_value)+1):
    iteration.append(i)
    
  plt.plot(iteration, cost_value, '-o', color='blue');

"""### Hill Climbing Function"""

def hill_climbing(tsp):
  
  cost_value = []

  current_solution = random_solution(tsp) # This line of code will give us a random road to all cities

  current_route_length = route_length(tsp,current_solution) # This our cost value for current route

  print(f"Current solution is {current_solution} with cost of: {current_route_length}")

  neighbors = find_neighbors(solution)

  best_neighbor , best_neighbor_length = find_best_neighbor(tsp , neighbors)

  while best_neighbor_length < current_route_length :
    current_solution = best_neighbor
    print(f"Current solution is {current_solution} with cost of: {current_route_length}")
    current_route_length = best_neighbor_length

    cost_value.append(current_route_length)

    neighbors = find_neighbors(current_solution)
    best_neighbor , best_neighbor_length = find_best_neighbor(tsp , neighbors)

  return current_solution , current_route_length, cost_value

"""## Main program"""

tsp = tsp_matrix(x,y) # This line will give us m*m matrix of distance between cites. m is total number of cities

Best_solution, best_cost , cost_value= hill_climbing(tsp) # This line of code will find best solution with hill_climbing algorithm

print("\n"+ f"Best solution is {Best_solution} and best cost is {best_cost}")

plot_cost(cost_value)
plt.xlabel("iteration")
plt.ylabel("Cost")

