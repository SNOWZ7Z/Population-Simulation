from matplotlib import pyplot as plt, animation

fig = plt.figure()
axes = fig.add_subplot(projection="3d")

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
text = ax.text(.5, .5, 'First Text')
def action(event):
   if event.key == "z":
      text.set_text("zoom")
   elif event.key == "c":
      text.set_text("cool")

fig.canvas.mpl_connect('key_press_event', action)
fig.canvas.draw()
animation = animation.ArtistAnimation(fig, [(text,)])


plt.show()
