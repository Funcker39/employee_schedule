import numpy as np
import pandas as pd

def skill_to_int(skill_string):
    skill = 0
    if (skill_string == "LPC"):
        skill = 1

    return skill

def spe_to_int(spe_string):
    spe = 0
    if spe_string == "Jardinage":
        spe = 0
    if spe_string == "Menuiserie":
        spe = 1
    if spe_string == "Mecanique":
        spe = 2
    if spe_string == "Musique":
        spe = 3
    if spe_string == "Electricite":
        spe = 4

    return spe

def translate_mission(csv_row):
    return {
        "id": csv_row[0], 
        "day": csv_row[1], 
        "start_hour": csv_row[2] / 60, 
        "end_hour": csv_row[3] / 60, 
        "skill":  skill_to_int(csv_row[4]),
        "spe": spe_to_int(csv_row[5])
        }

def translate_employee(csv_row):
    return {
        "id": csv_row[0],
        "skill":  skill_to_int(csv_row[1]),
        "spe": spe_to_int(csv_row[2]),
        "quota": csv_row[3]
        }

def print_table(table):
    for i in range(len(table)):
        print(table[i])

csv_dir = r'./csv/45-4/'
distances_csv = pd.read_csv(csv_dir + r'/Distances.csv', header=None)
missions_csv = pd.read_csv(csv_dir + r'/Missions.csv', header=None).transpose()
employees_csv = pd.read_csv(csv_dir + r'/Intervenants.csv', header=None).transpose()

def distance_btw_missions(mission1, mission2):
    return distances_csv[mission1][mission2]

missions = []
for i in range(missions_csv.shape[1]):
    missions.append(translate_mission(missions_csv[i]))

employees = []
for i in range(employees_csv.shape[1]):
    employees.append(translate_employee(employees_csv[i]))

lsf_missions = [missions[i] for i in range(len(missions)) if missions[i]["skill"] == 0]
lcp_missions = [missions[i] for i in range(len(missions)) if missions[i]["skill"] == 1]


print_table(employees)

solutions = []
for day in range(1, 6):
    lsf_day_missions = [lsf_missions[k] for k in range(len(lsf_missions)) if lsf_missions[k]["day"] == day]
    lcp_day_missions = [lcp_missions[k] for k in range(len(lcp_missions)) if lcp_missions[k]["day"] == day]

    print_table(lsf_day_missions)

