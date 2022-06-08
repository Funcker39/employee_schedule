import src.solution as sol

def all_lunch_pauses(solution):
    start_lunch_index = sol.hour_to_solution_index(12)
    end_lunch_index = sol.hour_to_solution_index(14)
    for day in range(len(solution)):
        for employee_ind in range(len(solution[0])):
            has_pause = False
            for i in range(start_lunch_index, end_lunch_index-1):
                if (solution[day][employee_ind][i] == 0):
                    if (solution[day][employee_ind][i+1] == 0):
                        has_pause = True
                        
            if not has_pause: 
                for i in range(start_lunch_index, end_lunch_index):
                    print (solution[day][employee_ind][i])
                return False, employee_ind+1, day+1

    return True

def fitness(solution):
    if not all_lunch_pauses(solution): 
        return -1

    score = 0

    return score