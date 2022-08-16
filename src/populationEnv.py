from turtle import color
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import populationParams as params
import random

#General data
day = 0
day_text = "Day 0"
the_green_population = 0
the_blue_population = 0
blue_people = 'b'
green_people = 'g'
fig = plt.figure()
axes = fig.add_subplot(projection="3d")
text = axes.text2D(0.45, 0.999, (day_text), transform=axes.transAxes, fontsize=20)

def update_day(event):
    global day
    global day_text
    global text
    day += 1
    day_text = "Day " + str(day)   
    text = axes.text2D(0.45, 0.999, (day_text), transform=axes.transAxes, fontsize=20)
    print(day_text)


class PopulationEnv():

    def dies(self) -> bool:
        """
        Returns:
            bool: True if the creature dies, False if they die.
        """
        #TODO change to a 10% chance of dying
        return np.random.randint(0,10) == 1
    
    def isBorn(self) -> bool:
        """
        Returns:
            bool: True if the creature is born, False if it is not.
        """
        return np.random.randint(0,10) == 1

    def generate_data(self, nbr_iterations, nbr_elements):
        """
        The elements will be assigned random initial positions and speed.
        Args:
        nbr_iterations (int): Number of iterations data needs to be generated for. Aka length of the animation.
        nbr_elements (int): Number of elements (or points) that will move.
        Returns:
        list: list of positions of elements. (Iterations x (# Elements x Dimensions))
        """
        dims = (3,1)
        global day
        
        # Random initial positions.
        gaussian_mean = np.zeros(dims)
        gaussian_std = np.ones(dims)

        #Vectorizer for parsing to int
        vector = np.vectorize(int)
        
        start_positions = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [nbr_elements] * dims[0]))).T
        start_positions = vector(start_positions)

        # Random speed
        # X is horizontal, Y is depth, Z is vertical (For manual manipulation) of the speed values (Mental Note only)
        start_speed = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [nbr_elements] * dims[0]))).T

        
        # start_speed = np.array([[-1,0,0] * nbr_elements]).T

        # Computing trajectory
        data = [start_positions]

        #TODO Change for a Big period of time.
        for iteration in range(nbr_iterations):

            previous_positions = data[-1]
            new_positions = previous_positions + start_speed
            for i in range(nbr_elements):#Code for bounce off walls
                for j in range(3):
                    if new_positions[i][j] >= 50:
                        start_speed[i][j] = -abs(start_speed[i][j])
                    elif new_positions[i][j] <= -50:
                        start_speed[i][j] = abs(start_speed[i][j])
                # if self.dies():
                #     new_positions = np.delete(new_positions, i)

            #TODO make it grab a random creature, not the first one Same for born
            if self.dies():
                new_positions[0][0] += 199  #Sends the creature to oblivion if it dies.

            if self.isBorn():
                new_positions[0][0] = 0 #It's changing the positions of thew X position only

            data.append(new_positions)

        return data   
    
    def animate_scatters(self, iteration, data, scatters, data2, scatters2):
        """
        Update the data held by the scatter plot and therefore animates it.
        Args:
            iteration (int): Current iteration of the animation
            data (list): List of the data positions at each iteration.
            scatters (list): List of all the scatters (One per element)
        Returns:
            list: List of scatters (One per element) with new coordinates
        """
        for i in range(data[0].shape[0]):
            scatters[i]._offsets3d = (data[iteration][i,0:1], data[iteration][i,1:2], data[iteration][i,2:])
        self.animate_sctrs(iteration, data2, scatters2)
        return scatters

    def animate_sctrs(self, iteration, data, scatters):
        print("Scatters: " + str(len(scatters)))
        print("Data: " + str(len(data)))
        print("Iteration: " + str(len(data[iteration])))
        
        for i in range(data[0].shape[0]):
            scatters[i]._offsets3d = (data[iteration][i,0:1], data[iteration][i,1:2], data[iteration][i,2:])
            print("Current index: " + str(i))
        animation = ani.FuncAnimation(fig, self.animate_sctrs, iteration, fargs=(data, scatters), interval=50, blit=False, repeat=True)
        return scatters
      
    def __init__(self):
        global day_text
        global axes
        global fig
        # fig = plt.figure()
        # axes = fig.add_subplot(projection="3d")
        
        # Style the environment
        axes.grid(False)
        axes.set_xlim3d([-50, 50])
        axes.set_ylim3d([-50, 50])
        axes.set_zlim3d([-50, 50])
        #TODO Add at the end for styling
        # axes.set_xticklabels([])
        # axes.set_yticklabels([])
        # axes.set_zticklabels([])
        
        # Add labels to the axes
        # text = axes.text2D(0.45, 0.999, (day_text), transform=axes.transAxes, fontsize=20)
       

        fig.canvas.mpl_connect('button_press_event', update_day)
        fig.canvas.draw()

        animation = ani.ArtistAnimation(fig, [(text,)])

        #This will need an independent generate data for each population        
        axes.text2D(0.10, 0.1, ("The Green: " + str(the_green_population)), transform=axes.transAxes, color=green_people)
        axes.text2D(0.80, 0.1, ("The Blue: " + str(the_blue_population)), transform=axes.transAxes, color=blue_people)

        # X is horizontal, Y is depth, Z is vertical
        # axes.scatter(rnd.randint(0,16), rnd.randint(0,16), rnd.randint(0,16), color=green_people, marker='o')       
        # axes.scatter(rnd.randint(0,16), rnd.randint(0,16), rnd.randint(0,16), color=blue_people, marker='o')

        #This is sectioned so that the data generated is only used for one color.    
        data_g = self.generate_data(100, 3)
        data_b = self.generate_data(100, 3)

        full_data = np.concatenate((data_g, data_b), axis=0)

        iterations_g = len(data_g)
        iterations_b = len(data_b)
        full_iterations = iterations_g + iterations_b

        scatters_green_people = [ axes.scatter(data_g[0][i,0:1], data_g[0][i,1:2], data_g[0][i,2:], color=green_people) for i in range(data_g[0].shape[0]) ]
        scatters_blue_people = [ axes.scatter(data_b[0][i,0:1], data_b[0][i,1:2], data_b[0][i,2:], color=blue_people) for i in range(data_b[0].shape[0]) ]

        full_scatters = np.concatenate((scatters_blue_people, scatters_green_people), axis=0)
        
        # animation_g = ani.FuncAnimation(fig, self.animate_scatters, iterations_g, fargs=(data_g, scatters_green_people), interval=50, blit=False, repeat=True)
        # animation_b = ani.FuncAnimation(fig, self.animate_scatters, iterations_b, fargs=(data_b, scatters_blue_people), interval=50, blit=False, repeat=True)
        # animation_xd = animation_g + animation_b
        animation = ani.FuncAnimation(fig, self.animate_scatters, iterations_g, fargs=(data_g, scatters_green_people, data_b, scatters_blue_people), interval=50, blit=False, repeat=True)


        plt.rcParams['animation.ffmpeg_path'] ='C:\\PATH_Programs/ffmpeg.exe'
        FFwriter=ani.FFMpegWriter(fps=40, extra_args=['-vcodec', 'libx264'])
        animation.save('animation.mp4', writer=FFwriter)

        plt.show()
        
        

    

