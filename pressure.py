import numpy as np

def b_build(un, vn, dx, dy, dt, rho):
    b = 1 / dt * ((un[1:-1, 2:] - un[1:-1, 0:-2]) / (2 * dx) + (vn[2:, 1:-1] - vn[0:-2, 1:-1]) / (2 * dy)) + ((un[1:-1, 2:] - un[1:-1, 0:-2])/dx)**2 + 2*((un[1:-1, 1:-1] - un[0:-2, 1:-1])/dy)*((vn[1:-1, 1:-1] - vn[1:-1, 0:-2])/dx) + ((vn[1:-1, 1:-1] - vn[0:-2, 1:-1])/dy)**2

    return rho*(dx**2)*(dy**2)*b

def poisson_eqn(p, un, vn, b_build, it, dx, dy, dt, rho, nx, ny, p_bcs, step, points):
    b = b_build(un, vn, dx, dy, dt, rho)
    for i in range(it):
        p_nxt = np.array(p, copy=True)
        p_nxt[1:-1, 1:-1] = (1/2/(dy**2 + dx**2))*((dy**2)*(p[2:, 1:-1] + p[0:-2, 1:-1]) + (dx**2)*(p[1:-1, 2:] + p[1:-1, 0:-2]) - b)
        p = p_nxt
        p = p_bcs(p, nx, ny, step, initialize=False, points=points)
    return p