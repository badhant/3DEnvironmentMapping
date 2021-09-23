import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("measurements.xyz",format='xyz')
print(pcd)


o3d.visualization.draw_geometries([pcd])


pt1 = 1
lines = []

for e in range(10):
    for x in range(63):
        pt1+=1
        lines.append([pt1,(pt1+1)])

pt1 = 1
do = 64

for f in range(9):
    for y in range(63):
        pt1 += 1
        lines.append([pt1,pt1+do])

line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)),lines=o3d.utility.Vector2iVector(lines))
o3d.visualization.draw_geometries([line_set])
