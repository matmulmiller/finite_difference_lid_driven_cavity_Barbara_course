from boundary_conditions import u_bcs, v_bcs, p_bcs
from fractional_step import frac_advance_u, frac_advance_v
from pressure import b_build, poisson_eqn
import numpy as np
from residuals import u_resid


def solver(un, vn, p, nt, iters, dx, dy, nx, ny, dt, rho, nu, lid_speed, step, points):
    
    # Create snapshot collection matrices
    u_snaps = np.zeros(shape=(nx, ny, 101))
    v_snaps = np.zeros(shape=(nx, ny, 101))
    p_snaps = np.zeros(shape=(nx, ny, 101))


    i = 0  # set incrementor for collecting snapshots
    for t in range(nt):
        u_previous = np.array(un, copy=True)
        v_previous = np.array(vn, copy=True)
        p_previous = np.array(p, copy=True)
        p_nxt = poisson_eqn(p, un, vn, b_build, iters, dx, dy, dt, rho, nx, ny, p_bcs, step, points)

        u = frac_advance_u(un, vn, dx, dy, dt, nu) - (dt/rho)*(p_nxt[1:-1, 2:] - p_nxt[1:-1, 0:-2])/2/dx
        v = frac_advance_v(vn, un, dx, dy, dt, nu) - (dt/rho)*(p_nxt[2:, 1:-1] - p_nxt[0:-2, 1:-1])/2/dy

        un = u_bcs(u, nx, ny, step, lid_speed, points)
        vn = v_bcs(v, nx, ny, step, points)
        p = p_nxt

        if ((t+1) % 40) == 0 or (t==0):
            print(f"Iteration: {t+1}")
            print(u_resid(u_previous, v_previous, p_previous, un, vn, p, nu, dx, dy, dt, rho))
            u_snaps[:, :, i] = un
            v_snaps[:, :, i] = vn
            p_snaps[:, :, i] = p
            i += 1
    
    return u_snaps, v_snaps, p_snaps
        
