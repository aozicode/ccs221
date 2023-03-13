import numpy as np
import cv2
import matplotlib.pyplot as plt

def read_image(filename):
    img = cv2.imread(filename)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def reflect_image(img):
    rows, cols, ch = img.shape
    m_reflection=np.float32([[1, 0, 0], [0,-1,rows],[0,0,1]])
    reflected_img=cv2.warpPerspective(img,m_reflection,(int(cols),int(rows)))
    plt.axis('off')
    plt.imshow(reflected_img)
    plt.title('Reflected Image')
    plt.show()
    
def rotate_image(img, angle):
    rows, cols, ch = img.shape
    angle = np.radians(angle)
    m_rotation = np.float32([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    rotated_img = cv2.warpPerspective(img, m_rotation, (cols, rows))
    plt.axis('off')
    plt.imshow(rotated_img)
    plt.title('Rotated Image')
    plt.show()
    
def shear_image(img, shear_factor):
    rows, cols, ch = img.shape
    m_shearing = np.float32([[1, shear_factor, 0], [0, 1, 0], [0, 0, 1]])
    sheared_img = cv2.warpPerspective(img, m_shearing, (int(cols * (1 + abs(shear_factor))), rows))
    plt.axis('off')
    plt.imshow(sheared_img)
    plt.title('Sheared Image')
    plt.show()
    
def translate_image(img, x_offset, y_offset):
    rows, cols, channels = img.shape
    M = np.float32([[1, 0, x_offset], [0, 1, y_offset]])
    translated_img = cv2.warpAffine(img, M, (cols, rows))
    plt.imshow(translated_img)
    plt.axis('off')
    plt.title('Translated Image')
    plt.show()

def scale_image(img):
    rows, cols, ch = img.shape
    m_scaling_ = np.float32([[1.5, 0, 0],[0, 1.8, 0], [0,0,1]])
    scaled_img_ = cv2.warpPerspective(img, m_scaling_, (cols*2, rows*2))
    plt.axis('off')
    plt.imshow(scaled_img_)
    plt.title('Scaled Image')
    plt.show()

images = ['original1.jpg', 'original2.jpg', 'original3.jpg']

for filename in images:

# Load an image
 img = read_image(filename)

# Apply transformations to the image
reflect_image(img)
rotate_image(img, 10)
shear_image(img, 0.5)
translate_image(img, 100, 50)
scale_image(img)
