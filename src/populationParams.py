import numpy as np

BLUE_POPULATION = {
    'death': 20, #divide by 10 to get the chance of death
    'born': 10, #divide by 10 to get the chance of birth
}

GREEN_POPULATION = {
    'death': 3, #divide by 10 to get the chance of death
    'born': 3, #divide by 10 to get the chance of birth
}

def b_dies() -> bool:
    """
    Returns:
        bool: True if the creature dies, False if they die.
    """
    #TODO change to a 10% chance of dying
    return np.random.randint(0,BLUE_POPULATION["death"]) == 1

def g_dies() -> bool:
    """
    Returns:
        bool: True if the creature dies, False if they die.
    """
    #TODO change to a 10% chance of dying
    return np.random.randint(0,GREEN_POPULATION["death"]) == 1

def b_isBorn() -> bool:
    """
    Returns:
        bool: True if the creature is born, False if it is not.
    """
    return np.random.randint(0,BLUE_POPULATION["born"]) == 1

def g_isBorn() -> bool:
    """
    Returns:
        bool: True if the creature is born, False if it is not.
    """
    return np.random.randint(0,GREEN_POPULATION["born"]) == 1