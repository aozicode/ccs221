import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

def plt_basic_object(points):
    
    tri=Delaunay(points).convex_hull
    
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, shade=True, lw=0.5, color='purple')
    
    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)
    plt.show()
    
def rectangle(bottom_lower=(-2,-1,-2), side_lengths=(5, 3, 4)):
    
    bottom_lower=np.array(bottom_lower)
    side_lengths = np.array(side_lengths)
    points=np.vstack([
        bottom_lower,
        bottom_lower + [0, side_lengths[1], 0],
        bottom_lower + [side_lengths[0], side_lengths[1], 0],
        bottom_lower + [side_lengths[0], 0, 0],
        bottom_lower + [0, 0, side_lengths[2]],
        bottom_lower + [0, side_lengths[1], side_lengths[2]],
        bottom_lower + [side_lengths[0], side_lengths[1], side_lengths[2]],
        bottom_lower + [side_lengths[0], 0, side_lengths[2]],
        ])

    return points

init_rectangle = rectangle(side_lengths=(2, 4, 2)) #here we can customize the rectangle
points = tf.constant(init_rectangle, dtype=tf.float32)

plt_basic_object(points)

