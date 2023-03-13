import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def change(x, y, ColorVal, MoveDirection, two_d_arr):
    if MoveDirection not in ["u", "d", "l", "r"]:
        st.warning("Invalid MoveDirection. Try again.")
        return

    if MoveDirection == "u" and x > 0:
        two_d_arr[x][y] = ColorVal
        change(x - 1, y, ColorVal, MoveDirection, two_d_arr)
    elif MoveDirection == "d" and x < two_d_arr.shape[0] - 1:
        two_d_arr[x][y] = ColorVal
        change(x + 1, y, ColorVal, MoveDirection, two_d_arr)
    elif MoveDirection == "r" and y < two_d_arr.shape[1] - 1:
        two_d_arr[x][y] = ColorVal
        change(x, y + 1, ColorVal, MoveDirection, two_d_arr)
    elif MoveDirection == "l" and y > 0:
        two_d_arr[x][y] = ColorVal
        change(x, y - 1, ColorVal, MoveDirection, two_d_arr)

    img = plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    img.set_clim([0, 50])
    plt.colorbar()
    st.pyplot()

def app():
    plt.title("Flood Fill")

    two_d_arr = np.array([[1, 0, 1], 
                          [0, 1, 0],
                          [1, 0, 1]])

    st.write("### Input")
    column = st.slider("Column", 0, 2, 1)
    row = st.slider("Row", 0, 2, 1)
    color = st.slider("Color", 0, 50, 1)
    direction = st.selectbox("Direction", ["u", "d", "l", "r"])

    st.write("### Output")
    change(column, row, color, direction, two_d_arr)

if __name__ == '__main__':
    app()
