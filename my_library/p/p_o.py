"""
This is a library to find the perimeter of shapes, circumferences, and now 3D shapes' volume and surface area.
Enhanced with NumPy for advanced calculations.
"""

import numpy as np

# 2D Shapes (Existing Functions)
def sqrp(s):
    return 4 * s

def rectp(l, b):
    return 2 * (l + b)

def gp(n, s):
    return n * s

def circle_circumference(r):
    return 2 * np.pi * r

def ecircum(a, b):
    return np.pi * (3 * (a + b) - np.sqrt((3 * a + b) * (a + 3 * b)))

# 3D Shapes
# Volume
def sphere_volume(r):
    return (4/3) * np.pi * (r**3)

def cube_volume(s):
    return s**3

def cylinder_volume(r, h):
    return np.pi * (r**2) * h

def cone_volume(r, h):
    return (1/3) * np.pi * (r**2) * h

def rectangular_prism_volume(l, w, h):
    return l * w * h

# Surface Area
def sphere_surface_area(r):
    return 4 * np.pi * (r**2)

def cube_surface_area(s):
    return 6 * (s**2)

def cylinder_surface_area(r, h):
    return 2 * np.pi * r * (r + h)

def cone_surface_area(r, h):
    return np.pi * r * (r + np.sqrt(h**2 + r**2))

def rectangular_prism_surface_area(l, w, h):
    return 2 * (l*w + w*h + h*l)

