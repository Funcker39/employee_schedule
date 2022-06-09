import numpy as np
import pandas as pd
import random
import src.solution as sol
import src.fitness as fit

week_days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']

csv_dir = r'./csv/45-4/'
distances_csv = pd.read_csv(csv_dir + r'/Distances.csv', header=None)
missions_csv = pd.read_csv(csv_dir + r'/Missions.csv', header=None).transpose()
employees_csv = pd.read_csv(csv_dir + r'/Intervenants.csv', header=None).transpose()

def distance_btw_missions(mission1, mission2):
    return distances_csv[mission1["id"]][mission2["id"]]

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

for day in range(1, 6):
    lsf_day_missions = [lsf_missions[k] for k in range(len(lsf_missions)) if lsf_missions[k]["day"] == day]
    lcp_day_missions = [lcp_missions[k] for k in range(len(lcp_missions)) if lcp_missions[k]["day"] == day]
    
    day_mission_index = 0
    while day_mission_index < len(lsf_day_missions):
        random.shuffle(lsf_employees)
        for i in range(len(lsf_employees)):
            if sol.assign_mission(lsf_day_missions[day_mission_index], lsf_employees[i], population[0][day]):
                break
        day_mission_index += 1
    
    day_mission_index = 0
    while day_mission_index < len(lcp_day_missions):
        random.shuffle(lcp_employees)
        for i in range(len(lcp_employees)):
            if sol.assign_mission(lcp_day_missions[day_mission_index], lcp_employees[i], population[0][day]):
                break
        day_mission_index += 1
    
    print('\n' + week_days[day-1])
    sol.print_day(population[0][day])

print()
print(employees)
print(fit.fitness(population[0], employees))
