from numpy import sqrt
import src.solution as sol

no_debug = True
def debug(*arg):
    if no_debug: return
    print(arg)

def traveling_time(distances, mission1, mission2, speed = 50):
    distance = distances[mission1][mission2] / 1000 # in km
    return distance / speed # in hours

def all_lunch_pauses(solution):
    start_lunch_index = sol.hour_to_solution_index(12)
    end_lunch_index = sol.hour_to_solution_index(14)
    for day in range(len(solution)):
        for employee_ind in range(len(solution[0])):
            has_pause = False
            for i in range(start_lunch_index, end_lunch_index-1):
                if solution[day][employee_ind][i] == 0:
                    if (solution[day][employee_ind][i+1] == 0):
                        has_pause = True
                        
            if not has_pause:
                debug('The employee #' + str(employee_ind + 1) + ' can\'t eat on day ' + str(day+1))
                return False

    return True

def extra_hours(solution, employee_id, employees, distances):
    day_extra_minutes = []
    week_hours = 0
    for day in range(len(solution)):
        day_hours = 0
        hours = len(solution[0][0])
        last_mission = 0
        for hour in range(1, hours):
            mission = solution[day][employee_id][hour]
            if mission != 0:
                work_time = 0.5
                
                if mission != last_mission:
                    work_time += traveling_time(distances, last_mission, mission)
                    last_mission = mission

                day_hours += work_time
                week_hours += work_time

        extra = day_hours
        if employees[employee_id]["quota"] == 35:
            extra -= 8
        else:
            extra -= 6
        
        if extra < 0: extra = 0

        day_extra_minutes.append(round(extra*60))

    return round(week_hours, 2), day_extra_minutes

def has_time(hour1, hour2, mission1, mission2, distances):
    available_time = (hour2 - hour1) * 0.5
    okay = available_time > traveling_time(distances, mission1, mission2)
    if not okay: debug("Time too short from mission #" + str(mission1) + " to #" + str(mission2))
    return okay

def always_have_time(solution, employee_ind, distances):
    for day in range(len(solution)):
        in_mission = False
        between_missions = False
        mission1 = None
        mission1_end_hour = 0
        hours = len(solution[0][0])
        for hour in range(1, hours):
            if in_mission:
                if solution[day][employee_ind][hour] == 0:
                    in_mission = False
                    between_missions = True
                    mission1_end_hour = hour
                elif solution[day][employee_ind][hour] != mission1:
                    mission1_end_hour = hour
                    if not has_time(mission1_end_hour, hour, mission1, solution[day][employee_ind][hour], distances):
                        return False
            elif solution[day][employee_ind][hour] != 0:
                mission1 = solution[day][employee_ind][hour]
                if not between_missions:
                    in_mission = True
                else:
                    in_mission = True
                    between_missions = False
                    if not has_time(mission1_end_hour, hour, mission1, solution[day][employee_ind][hour], distances):
                        return False

    return True

def standard_deviation(values, avg):
    res = 0
    for i in range(len(values)):
        res += (values[i] - avg) ** 2

    res /= len(values)
    res = sqrt(res)

    return res

def avg(values):
    sum = 0
    for i in range(len(values)):
        sum += values[i]

    sum /= len(values)
    return sum


def fitness(solution, employees, distances, zeta, kappa):

    ###
    # HARD CONSTRAINTS
    ###

    # 1. Traveling time to go to the next mission
    for employee_ind in range(len(solution[0])):
        if not always_have_time(solution, employee_ind, distances):
            debug('The employee #' + str(employee_ind + 1) + ' can\'t teleport')
            return -1

    # 2. Lunch pauses constraint (1h between 12-14h)
    if not all_lunch_pauses(solution): 
        return -1

    # 3. Extra hours constraint (10h/week & 2h/day max)
    week_extra_hours = []
    for employee_ind in range(len(solution[0])):
        employee_extra_hours = extra_hours(solution, employee_ind, employees, distances)
        debug(employee_extra_hours)
        week_extra_hours_ = employee_extra_hours[0] - employees[employee_ind]['quota']
        for i in range(len(employee_extra_hours[1])):
            if employee_extra_hours[1][i] > 120 or week_extra_hours_ > 10:
                debug('The employee #' + str(employee_ind + 1) + ' has too much extra hours')
                return -1

        week_extra_hours.append(week_extra_hours_)


    ###
    # FITNESS CRITERIAS (closer to 0 is better)
    ###

    score = 0

    # 1. Work share between employees
    wasted_hours = []
    week_distances = []
    all_employee_distances = 0
    all_employee_wasted_hours = 0
    last_mission = 0
    for employee_ind in range(len(solution[0])):
        employee_wasted_hours = 0
        week_dis = 0
        for day in range(len(solution)):
            for hour in range(len(solution[0][0])):
                mission = solution[day][employee_ind][hour]
                if mission == 0:
                    employee_wasted_hours += 0.5
                    all_employee_wasted_hours += 0.5
                elif mission != last_mission:
                    week_dis += distances[last_mission][mission]
            week_dis += distances[last_mission][0]

        all_employee_distances += week_dis
        week_distances.append(week_dis)
        wasted_hours.append(employee_wasted_hours)

    avg_wasted_hours = all_employee_wasted_hours / len(solution[0])
    sigma_wasted_hours = standard_deviation(wasted_hours, avg_wasted_hours)

    avg_employee_distances = all_employee_distances / len(employees)
    sigma_employee_distances = standard_deviation(week_distances, avg_employee_distances)

    gamma = 10
    avg_extra_hours = avg(week_extra_hours)
    sigma_extra_hours = standard_deviation(week_extra_hours, avg_extra_hours)

    debug(zeta * sigma_wasted_hours, gamma * sigma_extra_hours, kappa * sigma_employee_distances)

    f_employees = (zeta * sigma_wasted_hours + gamma * sigma_extra_hours + kappa * sigma_employee_distances) / 3
    debug(f_employees)

    score += f_employees
                

    return score