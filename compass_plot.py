from __future__ import print_function
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from adjustText import adjust_text

def plot(file):
    # data from everyone who's posted their scores/images in thread
    # https://forums.civfanatics.com/threads/left-or-right-of-me.643849/
    df = pd.read_csv('coordinates.csv')
    people = [[p.user, p.econ, p.auth] for _, p in df.iterrows()]

    # average score
    average_x = sum(p[1] for p in people) / len(people)
    average_y = sum(p[2] for p in people) / len(people)
    print('Average: (%.2f, %.2f)' % (average_x, average_y))
    people.append(["Average", average_x, average_y])

    # grid and aesthetics
    ax = plt.gca()
    ax.fill([-10, 0, 0, -10], [0, 0, 10, 10], 'r', alpha=0.2)
    ax.fill([-10, 0, 0, -10], [-10, -10, 0, 0], 'g', alpha=0.2)
    ax.fill([0, 10, 10, 0], [-10, -10, 0, 0], 'purple', alpha=0.2)
    ax.fill([0, 10, 10, 0], [0, 0, 10, 10], 'blue', alpha=0.2)
    plt.axis([-10, 10, -10, 10])
    plt.xticks(np.arange(-10, 10, 1))
    plt.yticks(np.arange(-10, 10, 1))
    plt.grid()
    plt.axvline(linewidth=2, color='black', alpha=0.6)
    plt.axhline(linewidth=2, color='black', alpha=0.6)

    # plot OT gender-questioning commie-terrorist supercluster
    plt.scatter([p[1] for p in people], [p[2] for p in people], color='red', s=7)

    # username labels
    texts = [plt.text(p[1], p[2], p[0], fontsize=8) for p in people]
    adjust_text(texts)

    # axis labels
    ax1 = plt.plot()
    plt.xlabel('Libertarian', color='gray', fontsize='large')
    plt.ylabel('Left',color='gray', fontsize='large')
    ax2 = plt.gca().twiny()
    ax2.get_xaxis().set_ticks([])
    plt.xlabel('Authoritarian', color='gray', fontsize='large', labelpad=10)
    ax2 = plt.gca().twinx()
    ax2.get_yaxis().set_ticks([])
    plt.ylabel('Right', color='gray', rotation=-90, fontsize='large', labelpad=20)
    
    # done
    plt.savefig(file)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage:\n\tpython compass_plot.py [file name]\n"
            "Example:\n\tpython compass_plot.py ot_compass.png")
        exit()
    filename = sys.argv[1]
    plot(filename)
