from dis import dis
import numpy as np
import pandas as pd

coords = pd.read_csv(r'./InstanceGenerator-v03/csv/coords_data.csv', header=None)
missions = pd.read_csv(r'./InstanceGenerator-v03/csv/missions_data.csv', header=None, skiprows=1)
employees = pd.read_csv(r'./InstanceGenerator-v03/csv/employees_data.csv')


missions_count = missions.shape[0]
distances = [[0] * missions_count] * missions_count
for x in range(missions_count):
    x1, y1 = missions[6][x], missions[7][x]
    for y in range(missions_count):
        x2, y2 = missions[6][y], missions[7][y]
        print ("Mission ", x , ":", x1, y1)
        print ("Mission ", y , ":", x2, y2)
        print ("= ", np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

        distances[x][y] = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(distances[79][75])
