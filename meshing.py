'''

    [] Implement simple cases for when Sh = 0
    [] Create algorithm for determing step dimensions in terms of grid points given 
    [] Validate most extreme case against OpenFOAM

'''
import numpy as np
from boundary_conditions import u_bcs, v_bcs, p_bcs


def define_step_shape(Sh, Sl):
    point_library = {0.0: 0, 
                0.015625: 4, 
                0.03125: 8,
                0.0625: 16,
                0.125: 32,
                0.1875: 48,
                0.25: 64,
                0.3125: 80,
                0.375: 96,
                0.4375: 112,
                0.5: 128,
                0.5625: 144,
                0.625: 160,
                0.6875: 176,
                0.75: 192}

    top = 256 - point_library[Sh]
    col_num = point_library[Sl]
    left_point = (256 - col_num)/2
    right_point = 256 - left_point
    return top, int(left_point), int(right_point)

def mesher(nx, ny, Sh, Sl, step, lid_speed, define_step_shape):
    # Initialize velocity and pressure arrays
    u = np.zeros((nx-2, ny-2))
    v = np.zeros((nx-2, ny-2))
    p = np.zeros((nx-2, ny-2))
    if step==False:
        points=None
        u = u_bcs(u, nx, ny, step, lid_speed, points)
        v = v_bcs(v, nx, ny, step, points=points)
        p = p_bcs(p, nx, ny, step, initialize=True, points=points)
    else:
        top, left, right = define_step_shape(Sh, Sl)
        points = [top, left, right]
        u = u_bcs(u, nx, ny, step, lid_speed, points=points)
        v = v_bcs(v, nx, ny, step, points=points)
        p = p_bcs(p, nx, ny, step, initialize=True, points=points)

    return  u, v, p, points