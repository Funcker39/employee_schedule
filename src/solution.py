import numpy as np

def init_empty_day(employees_count):
    day = [[0 for _ in range(25)] for _ in range(employees_count)]
    
    for i in range(employees_count):
        day[i][0] = i + 1

    return day

def init_empty_solution(employees_count):
    solution = [init_empty_day(employees_count) for i in range(6)]

    return solution

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

# Ex : 8h to 0, 9.5h to 3
def hour_to_solution_index(hour):
    return (int)(hour * 2) - 16

def has_mission_between(hour1, hour2, employee, day):
    start_index = hour_to_solution_index(hour1)
    end_index = hour_to_solution_index(hour2)

    for i in range(start_index, end_index):
        if day[employee["id"] - 1][i + 1] != 0: return True

def assign_mission(mission, employee, day):
    if has_mission_between(mission["start_hour"], mission["end_hour"], employee, day): return False

    start_index = hour_to_solution_index(mission["start_hour"])
    end_index = hour_to_solution_index(mission["end_hour"])

    for i in range(start_index, end_index):
        day[employee["id"] - 1][i + 1] = mission["id"]

    return True

def print_table(table):
    for i in range(len(table)):
        print(table[i])

def print_day(day):
    header = ['id', '8h', '8h30', '9h', '9h30', '10h', '10h30', '11h', '11h30', '12h', 
                '12h30', '13h', '13h30', '14h', '14h30', '15h', '15h30', '16h', '16h30', '17h', '17h30',
                '18h', '18h30', '19h', '19h30']
    #_sol = sol
    _day = np.vstack([header, day])
    s = [[str(e) for e in row] for row in _day]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    return