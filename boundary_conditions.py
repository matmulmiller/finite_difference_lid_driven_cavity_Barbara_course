import numpy as np

# Set boundary conditions and use to intialize snapshot arrays
def u_bcs(u, nx, ny, step, lid_speed, points):
    ghost_r = np.zeros((1, nx))
    ghost_c = np.zeros((ny-2, 1))
    u = np.append(ghost_c, u, axis=1)
    u = np.append(u, ghost_c, axis=1)
    u = np.append(ghost_r, u, axis=0)
    u = np.append(u, ghost_r, axis=0)

    if step == False:
        u[0, :] = lid_speed
    else:
        u[0, :] = lid_speed
        top, left, right = points
        u[top:, left:right] = 0
    return u


def v_bcs(v, nx, ny, step, points):
    ghost_r = np.zeros((1, nx))
    ghost_c = np.zeros((ny-2, 1))
    v = np.append(ghost_c, v, axis=1)
    v = np.append(v, ghost_c, axis=1)
    v = np.append(ghost_r, v, axis=0)
    v = np.append(v, ghost_r, axis=0)

    if step == False:
        v = v 
    else:
        top, left, right = points
        v[top:, left:right] = 0
    return v


def p_bcs(p, nx, ny, step, initialize=False, points=None):
    if initialize:
        ghost_r = np.zeros((1, nx))
        ghost_c = np.zeros((ny-2, 1))
        p = np.append(ghost_c, p, axis=1)
        p = np.append(p, ghost_c, axis=1)
        p = np.append(ghost_r, p, axis=0)
        p = np.append(p, ghost_r, axis=0)

        if step == False:
            p[:, 0] = p[:, 1]  # dp/dx = 0 @ x = 0
            p[:, -1] = p[:, -2]  # dp/dx = 0 @ x = L
            p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 0
            p[0, :] = 0  # p = 0 at y = L
        else: 
            # Wall boundary conditions
            p[:, 0] = p[:, 1]  # dp/dx = 0 @ x = 0
            p[:, -1] = p[:, -2]  # dp/dx = 0 @ x = L
            p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 0
            p[0, :] = 0  # p = 0 at y = L

            # Step bounday conditions
            top, left, right = points
            p[top+1: left+1:right-1] = 0  # p=0 everywhere inside the step
            p[top+1:, left] = p[top+1:, left-1]  #  dp/dx = 0 at left side of step
            p[top+1:, right-1] = p[top+1, right]  # dp/dx = 0 at right side of step
            p[top, left:right] = p[top-1, left:right]  # dp/dy = 0 at top of step

    else:
        if step == False:
            p[:, 0] = p[:, 1]  # dp/dx = 0 @ x = 0
            p[:, -1] = p[:, -2]  # dp/dx = 0 @ x = L
            p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 0
            p[0, :] = 0  # p = 0 at y = L
        else: 
            p[:, 0] = p[:, 1]  # dp/dx = 0 @ x = 0
            p[:, -1] = p[:, -2]  # dp/dx = 0 @ x = L
            p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 0
            p[0, :] = 0  # p = 0 at y = L

            # Step bounday conditions
            top, left, right = points
            p[top+1:, left+1:right-1] = 0  # p=0 everywhere inside the step
            p[top+1:, left] = p[top+1:, left-1]  #  dp/dx = 0 at left side of step
            p[top+1:, right-1] = p[top+1, right]  # dp/dx = 0 at right side of step
            p[top, left:right] = p[top-1, left:right]  # dp/dy = 0 at top of step
        
    return p