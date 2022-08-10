import numpy as np

oncex = True
def dies() -> bool:
    """
    Returns:
        bool: True if the creature dies, False if they die.
    """
    global oncex
    #TODO change to a 10% chance of dying
    if oncex:
        oncex = False
        return True

    return False

nbr_iterations = 5
nbr_elements = 2

dims = (3,1)

# Random initial positions.
gaussian_mean = np.zeros(dims)
gaussian_std = np.ones(dims)

#Vectorizer for parsing to int
vector = np.vectorize(int)

start_positions = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [nbr_elements] * dims[0]))).T
start_positions = vector(start_positions)
print(start_positions)

print("//////////Start Position//////////////")

# Random speed
# X is horizontal, Y is depth, Z is vertical (For manual manipulation) of the speed values (Mental Note only)

# start_speed = np.array([[-1,0,0] * nbr_elements]).T

# Computing trajectory
data = [start_positions]

#TODO Change for a Big period of time.
for iteration in range(nbr_iterations):
    
    start_speed = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [nbr_elements] * dims[0]))).T
    
    previous_positions = data[-1]
    new_positions = previous_positions + start_speed
    for i in range(nbr_elements):#Code for bounce off walls
        for j in range(3):
            if new_positions[i][j] >= 50:
                start_speed[i][j] = -abs(start_speed[i][j])
            elif new_positions[i][j] <= -50:
                start_speed[i][j] = abs(start_speed[i][j])
    print("\n//////////New Position//////////////")
    print(new_positions)
    print("\n////////////Grab////////////")
    print(new_positions[0])
    print("///////////And Delete/////////////\n")

    if dies():
        new_positions[0][0] += 199
        nbr_elements -= 1
        print("\n//////////New Position with Delete//////////////")
        print(new_positions)
        print("////////////////////////\n")
    



    data.append(new_positions)
