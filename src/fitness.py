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

def extra_hours(solution, employee_id, employees):
    day_extra_hours = []
    week_hours = 0
    for day in range(len(solution)):
        day_hours = 0
        hours = len(solution[0][0])
        for hour in range(1, hours):
            if (solution[day][employee_id][hour] != 0):
                day_hours += 1
                week_hours += 1

        extra = day_hours
        if employees[employee_id]["quota"] == 35:
            extra -= 8
        else:
            extra -= 6
        
        if extra < 0: extra = 0

        day_extra_hours.append(extra)

    return week_hours, day_extra_hours


def fitness(solution, employees):
    if not all_lunch_pauses(solution): 
        return -1

    score = 1000

    for employee_id in range(len(solution[0])):
        employee_extra_hours = extra_hours(solution, employee_id, employees)
        for i in range(len(employee_extra_hours[1])):
            if employee_extra_hours[1][i] > 2:
                score -= 25 * (employee_extra_hours[1][i] - 2)
        print(employee_extra_hours)

    return score