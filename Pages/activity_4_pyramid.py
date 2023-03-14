import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay
import tensorflow as tf
import streamlit as st

def plt_basic_object_(points):
    tri=Delaunay(points).convex_hull
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, lw=0.5, shade=True, color='yellow')
    ax.set_xlim3d(-6,6)
    ax.set_ylim3d(-6,6)
    ax.set_zlim3d(-6,6)
    st.pyplot (fig)

def pyramid_(side=6, height=8, bottom_lower=(0, 0, -2)):
    side = side / np.sqrt(2)  
    height = height # calculates the tip
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower + [-side, -side, 0], 
        bottom_lower + [side, -side, 0],  
        bottom_lower + [side, side, 0],  
        bottom_lower + [-side, side, 0],  
        bottom_lower + [0, 0, height],     
    ])
    return points

init_pyramid = pyramid_(side=6, height=8)
points = tf.constant(init_pyramid, dtype=tf.float32)

plt_basic_object_(points)
