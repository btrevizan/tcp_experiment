import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
from pandas import read_csv

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(frame):
    log_data = read_csv('traffic.log', header=None, index_col=None)
    # log_data.iloc[:, 1] = log_data.iloc[:, 1] / (8 * pow(2, 20))

    ax1.clear()
    ax1.plot(log_data.iloc[:, 0], log_data.iloc[:, 1], '-o')

    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("bit/s")


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
