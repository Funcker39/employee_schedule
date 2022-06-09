from dis import dis
import src.solution as sol

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
                print('The employee #' + str(employee_ind + 1) + ' can\'t eat on day ' + str(day+1))
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
                    #print(last_mission, 'to', mission, '=', traveling_time(distances, last_mission, mission))
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
    if not okay: print("Time too short from mission #" + str(mission1) + " to #" + str(mission2))
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
                


def fitness(solution, employees, distances):

    ###
    # HARD CONSTRAINTS
    ###

    # 1. Traveling time to go to the next mission
    for employee_ind in range(len(solution[0])):
        if not always_have_time(solution, employee_ind, distances):
            print('The employee #' + str(employee_ind + 1) + ' can\'t teleport')
            return -1

    # 2. Lunch pauses constraint (1h between 12-14h)
    if not all_lunch_pauses(solution): 
        return -1

    # 3. Extra hours constraint (10h/week & 2h/day max)
    for employee_ind in range(len(solution[0])):
        employee_extra_hours = extra_hours(solution, employee_ind, employees, distances)
        print(employee_extra_hours)
        for i in range(len(employee_extra_hours[1])):
            if employee_extra_hours[1][i] > 120 or employee_extra_hours[0] - employees[employee_ind]['quota'] > 10:
                print('The employee #' + str(employee_ind + 1) + ' has too much extra hours')
                return -1


    ###
    # FITNESS SCORE
    ###

    score = 1000

    return score