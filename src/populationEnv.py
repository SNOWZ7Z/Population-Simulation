from turtle import color
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import populationParams as params
import random

#General data
blue_people = 'b'
green_people = 'g'
fig = plt.figure()
axes = fig.add_subplot(projection="3d")

#To change values of the population generation use the following:
iterations_anim = 100 #Length of animation
nbr_creatures = 5 #Nmber of creatures in the population
#Please take in consideration that nbr_creatures is the maximum of the population in one color.
#Animation will start with less nbr_creatures.

#For best visualization of experiment use aproximately 60 creatures.

class PopulationEnv():

    def generate_data(self, nbr_iterations, nbr_elements, creature):
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
        
        #A portion of the elements will not be shown in the beguinng of the animation.
        for i in range(nbr_elements):
            if i <= (nbr_iterations/4):
                start_positions[i][0] += 400

        # Computing trajectory
        data = [start_positions]

        #TODO Change for a Big period of time. must not be TRUE
        for iteration in range(nbr_iterations):
            
            previous_positions = data[-1]
            new_positions = previous_positions + start_speed
            
            for i in range(nbr_elements):#Code for bounce off walls
                for j in range(3):
                    if new_positions[i][j] >= 50:
                        start_speed[i][j] = -abs(start_speed[i][j])
                    elif new_positions[i][j] <= -50:
                        start_speed[i][j] = abs(start_speed[i][j])
                    if new_positions[i][j] >= 200:
                        start_speed[i][j] = abs(start_speed[i][j])
                    elif new_positions[i][j] <= -200:
                        start_speed[i][j] = -abs(start_speed[i][j])   

            #Random Pickers for creatures who die are created
            rand_picker = np.random.randint(nbr_elements)
            rand_v_picker = np.random.randint(3)

            if creature == 'b':
                if params.b_dies():
                    new_positions[rand_picker][rand_v_picker] += 400  #Sends the creature to oblivion if it dies.

                if params.b_isBorn():
                    new_positions[rand_picker][rand_v_picker] = 0 #It's changing the positions of thew X position only

            elif creature == 'g':
                if params.g_dies():
                    new_positions[rand_picker][rand_v_picker] += 400
                
                if params.g_isBorn():
                    new_positions[rand_picker][rand_v_picker] = 0

            data.append(new_positions)
        return data   
    
    #Animation of the scatter points
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

    #Second animation of the scatter points that is triggered by the first one. animate_scatters
    def animate_sctrs(self, iteration, data, scatters):
        """
        This animation is triggered by the first one.
        Args:
            iteration (int): Current iteration of the animation
            data (list): List of the data positions at each iteration.
            scatters (list): List of all the scatters (One per element)
        Returns: updated scatters
        """
        for i in range(data[0].shape[0]):
            scatters[i]._offsets3d = (data[iteration][i,0:1], data[iteration][i,1:2], data[iteration][i,2:])
        animation = ani.FuncAnimation(fig, self.animate_sctrs, iteration, fargs=(data, scatters), interval=50, blit=False, repeat=True)
        return scatters
      
    def __init__(self):
        global axes
        global fig
        
        # Style the environment
        axes.grid(False)
        axes.set_xlim3d([-50, 50])
        axes.set_ylim3d([-50, 50])
        axes.set_zlim3d([-50, 50])
        #TODO Add at the end for styling
        axes.set_xticklabels([])
        axes.set_yticklabels([])
        axes.set_zticklabels([])
        
        #This is sectioned so that the data generated is only used for one color.    
        data_g = self.generate_data(iterations_anim, nbr_creatures, 'g')
        data_b = self.generate_data(iterations_anim, nbr_creatures, 'b')

        #Nunber of iterations is the length of the animation.
        iterations_g = len(data_g)
        iterations_b = len(data_b)

        #Creating the scatter points for the g creatures
        scatters_green_people = [ axes.scatter(data_g[0][i,0:1], data_g[0][i,1:2], data_g[0][i,2:], color=green_people) for i in range(data_g[0].shape[0]) ]
        scatters_blue_people = [ axes.scatter(data_b[0][i,0:1], data_b[0][i,1:2], data_b[0][i,2:], color=blue_people) for i in range(data_b[0].shape[0]) ]
        
        #Animation of the scatter points
        animation = ani.FuncAnimation(fig, self.animate_scatters, iterations_g, fargs=(data_g, scatters_green_people, data_b, scatters_blue_people), interval=50, blit=False, repeat=True)

        #Saving the animation to a file
        plt.rcParams['animation.ffmpeg_path'] ='C:\\PATH_Programs/ffmpeg.exe'
        FFwriter=ani.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
        animation.save('animation.mp4', writer=FFwriter)

        #This line can be  shown if the user wishes to visualize the animation. (It is not shown by default) (It runs slower, at the cpu's capacity)
        # plt.show()
        
        

    

