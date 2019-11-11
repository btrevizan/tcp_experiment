import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
from pandas import read_csv
from glob import glob

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

color = ['r', 'b', 'g', 'y', 'c', 'm']


def animate(frame):
    ax1.clear()

    logs = glob('traffic*.log')
    legends = []
    plots = []
    for log_file in logs:
        i = int(log_file[7]) - 1
        c = color[i]

        log_data = read_csv(log_file, header=None, index_col=None)
        # log_data.iloc[:, 1] = log_data.iloc[:, 1] / (8 * pow(2, 20))  # convert bps to mbps

        plot, = ax1.plot(log_data.iloc[:, 0], log_data.iloc[:, 1], c)
        plots.append(plot)

        legends.append(log_file.replace('traffic', 'Cliente ')[:-4])

    ax1.legend(plots, legends)
    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("bit/s")


ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
