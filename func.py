import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plotFunc(num):
    fig = plt.plot([num]*4, [1,2,3,4])
    return fig
