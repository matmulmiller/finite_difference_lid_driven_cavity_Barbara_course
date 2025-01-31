import numpy as np

# Advance u velocity without considering pressure term
def frac_advance_u(un, vn, dx, dy, dt, nu):
    u_frac = np.array(un, copy=True)
    u_frac = un[1:-1, 1:-1] + dt*(nu*((un[2:, 1:-1] - 2*un[1:-1, 1:-1] + un[0:-2, 1:-1])/(dy**2) + (un[1:-1, 2:] - 2*un[1:-1, 1:-1] + un[1:-1, 0:-2])/(dx**2)) \
     - un[1:-1, 1:-1]*(un[1:-1, 2:] - un[1:-1, 0:-2])/dx/2 - vn[1:-1, 1:-1]*(un[2:, 1:-1] - un[0:-2, 1:-1])/dy/2)

    return u_frac

# Advance y velocity without considering pressure term
def frac_advance_v(vn, un, dx, dy, dt, nu):
    v_frac = np.array(vn, copy=True)
    v_frac = vn[1:-1, 1:-1] + dt*(nu*((vn[2:, 1:-1] - 2*vn[1:-1, 1:-1] + vn[0:-2, 1:-1])/(dy**2) + (vn[1:-1, 2:] - 2*vn[1:-1, 1:-1] + vn[1:-1, 0:-2])/(dx**2)) \
    - un[1:-1, 1:-1]*(vn[1:-1, 2:] - vn[1:-1, 0:-2])/dx/2 - vn[1:-1, 1:-1]*(vn[2:, 1:-1] - vn[0:-2, 1:-1])/dy/2)
    return v_frac