# AI Hill Climbing Algorithm
This repository contains programs using classical Machine Learning algorithms to Artificial Intelligence implemented from scratch and Solving traveling-salesman problem (TSP) using an goal-based AI agent.

This project is about finding a solution to the traveling-salesman problem (TSP) using a so called goal-based AI agent. The goal is to find a cycle (a roundtrip) which visits every city once, while traveling the minimal possible distance.

A search algorithm called first-choice hill-climbing search has been used, which is a algorithms from the family of local search algorithms. This search evaluates and modifies one current state rather than systematically exploring paths from an initial state to a goal state, as it is done in classical search. This path to reach the goal is not of interest. Thus, no data structure representing the search space needs to be maintained. Only the current node needs to record the state and the value of the objective function, here the distance.

The current sate is a sequence of cities along with the distance. The search creates new randomly sequences and checks if the new sequences has a shorter distance compared to the current sequence. As soon as any shorter distance is found, take this as the new current state and repeat. It resets the best sequence five times in total - every time after 2000 iterations. Hence it checks overall 10,000 sequences. The best sequence within all is the solution and is printed out to the command line in the end.

### DATA:
For this project Qatar and Djibouti cites loaction have been used. Qater data is in `DATA/qa194.tsp` directory. Djibouti data is in `DATA/dj38.tsp` directory.



# How to use
 
1. **Google Colab**:
    1. Copy **Hill_Climbing.ipynb** file in your google drive
    2. Copy data in data folder in your google drive 
    3. Open **Hill_Climbing.ipynb** in your google drive
    4. change data path in the code
2. **.py file**:
    1. Open **hill_climbing.py** in your pyhton code editor
    2. Change data path in python code
    3. Run the code
    
# Properties of the task environment
- Fully observable
- Single agent
- Stochastic
- Episodic
- Static
- Discrete
- Known

# Descriptions of the files of this project:
1. **Project.pdf**
    - In this file, all details about the project have been explained.
2. **Report.pdf**
    - Report file for the project. All results of implemented Matlab codes with Plots are visible here.
3. **Hill_Climbing.ipynb**
    - Hill climbing google colab code
4. **hill_climbing.py**
    - Hill climbing python code
