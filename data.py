import numpy as np
import matplotlib.pyplot as plt


def plot3D(yaw, pitch, wait):
   """# Change the Size of Graph using
    # Figsize
    # fig = plt.figure(figsize=(5, 5))

    # Generating a 3D sine wave
    ax = plt.axes(projection='3d')

    # Create axis
    axes = [3, 3, 3]

    # Create Data
    data = np.zeros(axes)
    data[0] = [[1, 0, 1], [0, 1, 1], [1, 0, 1]]
    data[1] = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    data[2] = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]

    # Controll Tranperency
    alpha = 1

    # Control colour
    colors = np.empty(axes + [4])

    colors[0] = [1, 0, 0, alpha]  # red
    colors[1] = [0, 1, 0, alpha]  # green
    colors[2] = [0, 0, 1, alpha]  # blue

    # trun off/on axis
    plt.axis('off')

    # Voxels is used to customizations of
    # the sizes, positions and colors.
    ax.voxels(data, facecolors=colors, edgecolors='grey')
    ax.view_init(pitch, yaw)

    plt.draw()
    plt.pause(wait)
    # plt.close()
    # plt.show() """
   fig = plt.figure(1)
   ax = fig.add_subplot(projection='3d')
   ax.set_axis_off()
   zdata = 15 * np.linspace(0, 5, 10)
   xdata = np.sin(zdata) + 0.1
   ydata = np.cos(zdata) + 0.1
   ax.scatter3D(xdata, ydata, zdata)
   ax.view_init(pitch, yaw)
   plt.pause(wait)
   plt.close()
   return 0


# voxel3D(15, 10, 1)
