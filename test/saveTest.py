import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

mylines = [np.array([[1,2], [3,4]]), np.array([[5,6], [7,8], [9,10]])]

fig, ax = plt.subplots()

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

# There's some code here to set the layout (some background plots etc)
# I omitted it in this question

myplot, = ax.plot([], [], '.', markersize=5)


delay = 500
breaking = 1 

def update_plot(i, data, myplot):
    myplot.set_data(data[:i, 0], data[:i, 1])
    if i == breaking:
        # do some other stuff
        print("breaking")
        myplot.set_color("red")
    return myplot,

data = np.append(mylines[0],mylines[1], axis=0)
# data = mylines[1]

ani = animation.FuncAnimation(fig, update_plot, frames=data.shape[0],
                              fargs=(data, myplot), interval=delay,
                              blit=True, repeat=False)
plt.show()