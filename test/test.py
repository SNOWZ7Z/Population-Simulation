import numpy as np

dims = (3,1)

# Random initial positions.
gaussian_mean = np.zeros(dims)
gaussian_std = np.ones(dims)
# start_positions = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [2] * dims[0]))).T        
# print(start_positions)
np.random.seed(0)
start_positions = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [3] * dims[0]))).T
vector = np.vectorize(int)
start_positions = vector(start_positions)
print(start_positions)
print("////////StartSpeed////////")
start_speed = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [3] * dims[0]))).T
# start_speed = np.array([[1,1,1],[1,1,1],[1,1,1]])
print(start_speed)


data = [start_positions]
print("////////DATA")
print(data)
print("////////")
#Iterations
iterations = 3
for i in range(iterations):
    previous_positions = data[-1]
    new_positions = previous_positions + start_speed
    print("New positions\n")
    print(new_positions)
    
    for i in range(iterations):
        for j in range(3):
            if new_positions[i][j] >= 50:
                start_speed[i][j] = -abs(start_speed[i][j])
                # new_positions[i][j] = 50

    data.append(new_positions)

print(data)
