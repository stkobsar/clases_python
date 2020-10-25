import numpy as np

def asCartesian(rthetaphi):
    #takes list rthetaphi (single coord)
    r = rthetaphi[0]
    theta = rthetaphi[1] * np.pi/180 # to radian
    phi = rthetaphi[2] * np.pi/180
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return [x, y, z]

def asSpherical(xyz):
    #takes list xyz (single coord)
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r)*180/np.pi #to degrees
    phi = np.arctan2(y, x)*180/np.pi
    return [r, theta, phi]




if __name__ == "__main__":

    cartesian_coord = [20, 20, 20]
    spher = asSpherical(cartesian_coord)
    print(spher)
