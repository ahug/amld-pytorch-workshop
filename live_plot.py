import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import torch
import time

fig = None
ax = None
delta = 0.5


def init_2dplot(x_range, func, delta_):
    global fig, ax, delta
    delta = delta_
    fig = plt.figure(figsize=(8, 6), dpi=120)
    ax = fig.gca()
    fig.canvas.draw()
    
    y = func(x_range)
    ax.plot(x_range.numpy(), y.numpy(), 'b')
    
def add_point_2d(x, y):
    global delta
    ax.scatter(x.data.numpy(), y.data.numpy(), c='r', edgecolors='k', linewidth=.5)
    fig.canvas.draw()
    time.sleep(delta)

    
##############################################

    
def init_3dplot(x_range, y_range, func, elev, azim, delta_):
    global fig, ax, delta
    delta = delta_
    fig = plt.figure(figsize=(8, 6), dpi=120)
    ax = fig.gca(projection='3d')
    ax.view_init(elev=elev, azim=azim)
    fig.canvas.draw() 
    
    X, Y = np.meshgrid(x_range.numpy(), y_range.numpy())
    Z = func(torch.from_numpy(X), torch.from_numpy(Y)).numpy()
    ax.plot_wireframe(X, Y, Z, linewidth=.01, antialiased=False)  #  plot_surface

def add_point_3d(x, y, z):
    global delta
    ax.scatter3D(x.data.numpy(), y.data.numpy(), z.data.numpy(), s=30, c='r', edgecolor='k', linewidth=.5)
    fig.canvas.draw()
    time.sleep(delta)