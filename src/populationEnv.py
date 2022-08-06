import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import populationParams as params

#General data
day = 0

class PopulationEnv():

    def __init__(self):

        fig = plt.figure()
        axes = fig.add_subplot(111, projection="3d")
        axes.grid(False)
        axes.set_xticklabels([])
        axes.set_yticklabels([])
        axes.set_zticklabels([])
        axes.text2D(0.45, 0.999, ("Day" + str(day)), transform=axes.transAxes)

        # day_text = axes.annotate("Day 0", xy=[np.pi / 2, 1], ha="center", va="bottom")