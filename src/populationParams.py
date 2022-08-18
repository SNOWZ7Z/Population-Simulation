import numpy as np

BLUE_POPULATION = {
    'death': 20, #1 out of X("death") is the chance of death
    'born': 10, #1 out of X("born") is the chance of birth
}

GREEN_POPULATION = {
    'death': 3, #1 out of X("death") is the chance of death
    'born': 3, #1 out of X("born") is the chance of birth
}

def b_dies() -> bool:
    """
    Returns:
        bool: True if the creature dies, False if they die.
    """
    return np.random.randint(0,BLUE_POPULATION["death"]) == 1

def g_dies() -> bool:
    """
    Returns:
        bool: True if the creature dies, False if they die.
    """
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