import numpy as np


class Atom():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_xyz(self):
        return self.x, self.y, self.z

    def translate(self, module, direction):
        self.x = self.x + module * direction[0]
        self.y = self.y + module * direction[1]
        self.z = self.z + module * direction[2]

    def as_cartesian(self, rthetaphi):
        # takes list rthetaphi (single coord)
        r = rthetaphi[0]
        theta = rthetaphi[1] * np.pi / 180  # to radian
        phi = rthetaphi[2] * np.pi / 180
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)
        return [x, y, z]

    def as_spherical(self):
        # takes list xyz (single coord)
        self.x = x
        self.y = y
        self.z = z

        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        theta = np.arccos(z / r) * 180 / np.pi  # to degrees
        phi = np.arctan2(y, x) * 180 / np.pi
        return r, theta, phi

    def rotate(self, angle):
        self.as_spherical()





