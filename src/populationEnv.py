import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import populationParams as params
import random as rnd

#General data
day = 0
the_green_population = 0
the_blue_population = 0
blue_people = 'r'
green_people = 'g'

class PopulationEnv():

    def __init__(self):

        fig = plt.figure()
        axes = fig.add_subplot(111, projection="3d")
        
        # Style the environment
        axes.grid(False)
        axes.set_xticklabels([])
        axes.set_yticklabels([])
        axes.set_zticklabels([])
        
        # Add labels to the axes
        axes.text2D(0.45, 0.999, ("Day" + str(day)), transform=axes.transAxes, fontsize=20)
        axes.text2D(0.10, 0.1, ("The Green: " + str(the_green_population)), transform=axes.transAxes, color=green_people)
        axes.text2D(0.80, 0.1, ("The Blue: " + str(the_blue_population)), transform=axes.transAxes, color=blue_people)

        # X is horizontal, Y is depth, Z is vertical
        axes.scatter(rnd.randint(0,16), rnd.randint(0,16), rnd.randint(0,16), color=green_people, marker='o')       
        axes.scatter(rnd.randint(0,16), rnd.randint(0,16), rnd.randint(0,16), color=green_people, marker='o')        

