from contextlib import redirect_stderr
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

ENVIRONMENT = {
    # Environment parameters
    'food_spwn': 20, #per day
    'danger_spwn': 10, #per day
}

BLUE_POPULATION = {
    'surv': 0.95, #Survival rate
    'reprd': 0.4, #Reproduction rate
    'gene': 1, #Gene Dominance
    'endurance': 2, #Endurance
    'max_age': 30, #Max age
}

RED_POPULATION = {
    'surv': 0.35, #Survival rate
    'reprd': 0.9, #Reproduction rate
    'gene': 2, #Gene Dominance
    'endurance': 1, #Endurance
    'max_age': 60, #Max age
}


class PopulationEnv():
    def __init__(self):

        fig = plt.figure()
        axes = fig.add_subplot(111, projection="3d")
        axes.grid(False)