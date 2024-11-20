import p.p_o as p

# 3D Volumes
print(f"Sphere Volume (r=5): {p.sphere_volume(5)}")  # Sphere
print(f"Cube Volume (s=4): {p.cube_volume(4)}")  # Cube
print(f"Cylinder Volume (r=3, h=7): {p.cylinder_volume(3, 7)}")  # Cylinder
print(f"Cone Volume (r=3, h=7): {p.cone_volume(3, 7)}")  # Cone
print(f"Rectangular Prism Volume (l=4, w=5, h=6): {p.rectangular_prism_volume(4, 5, 6)}")  # Prism

# 3D Surface Areas
print(f"Sphere Surface Area (r=5): {p.sphere_surface_area(5)}")  # Sphere
print(f"Cube Surface Area (s=4): {p.cube_surface_area(4)}")  # Cube
print(f"Cylinder Surface Area (r=3, h=7): {p.cylinder_surface_area(3, 7)}")  # Cylinder
print(f"Cone Surface Area (r=3, h=7): {p.cone_surface_area(3, 7)}")  # Cone
print(f"Rectangular Prism Surface Area (l=4, w=5, h=6): {p.rectangular_prism_surface_area(4, 5, 6)}")  # Prism
