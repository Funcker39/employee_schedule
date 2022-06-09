import numpy as np
import pandas as pd
import random
import src.solution as sol
import src.fitness as fit
import sys

week_days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']

csv_dir = r'./csv/45-4/'
if len(sys.argv) > 1:
    csv_dir = r'./csv/' + sys.argv[1] + r'/'

missions_csv = pd.read_csv(csv_dir + r'/Missions.csv', header=None).transpose()
employees_csv = pd.read_csv(csv_dir + r'/Intervenants.csv', header=None).transpose()
distances = pd.read_csv(csv_dir + r'/Distances.csv', header=None)

missions = []
for i in range(missions_csv.shape[1]):
    missions.append(sol.translate_mission(missions_csv[i]))

employees = []
for i in range(employees_csv.shape[1]):
    employees.append(sol.translate_employee(employees_csv[i]))

lsf_missions = [missions[i] for i in range(len(missions)) if missions[i]["skill"] == 0]
lcp_missions = [missions[i] for i in range(len(missions)) if missions[i]["skill"] == 1]
lsf_employees = [employees[i] for i in range(len(employees)) if employees[i]["skill"] == 0]
lcp_employees = [employees[i] for i in range(len(employees)) if employees[i]["skill"] == 1]

population = [[[]]]

population[0] = sol.init_empty_solution(len(employees))

for day in range(5):
    lsf_day_missions = [lsf_missions[k] for k in range(len(lsf_missions)) if lsf_missions[k]["day"] == day+1]
    lcp_day_missions = [lcp_missions[k] for k in range(len(lcp_missions)) if lcp_missions[k]["day"] == day+1]
    
    day_mission_index = 0
    while day_mission_index < len(lsf_day_missions):
        day_mission = lsf_day_missions[day_mission_index]
        random.shuffle(lsf_employees)

        assigned = False
        trials = 0
        while not assigned:
            trials += 1
            for i in range(len(lsf_employees)):
                if sol.assign_mission(day_mission, lsf_employees[i], population[0][day], trials < 2):
                    assigned = True
                    break

            if trials >= 2 and not assigned:
                print("Can't generate initial solution")
                quit()

        day_mission_index += 1
    
    day_mission_index = 0
    while day_mission_index < len(lcp_day_missions):
        random.shuffle(lcp_employees)
        
        assigned = False
        trials = 0
        while not assigned:
            trials += 1
            for i in range(len(lcp_employees)):
                if sol.assign_mission(lcp_day_missions[day_mission_index], lcp_employees[i], population[0][day], trials < 2):
                    assigned = True
                    break

            if trials >= 2 and not assigned:
                print("Can't generate initial solution")
                quit()
        
        day_mission_index += 1
    
    print('\n' + week_days[day])
    sol.print_day(population[0][day])

print()
print(fit.fitness(population[0], employees, distances))
