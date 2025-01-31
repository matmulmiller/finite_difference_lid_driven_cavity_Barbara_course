from fractional_step import frac_advance_u
import numpy as np

def u_resid(up, vp, pp, un, vn, p, nu, dx, dy, dt, rho):
    convective = un[1:-1, 1:-1]*(un[1:-1, 1:-1] - un[1:-1, 0:-2])/dx + vn[1:-1, 1:-1]*(un[1:-1, 1:-1] - un[0:-2, 1:-1])/dy
    diffusive = nu*((un[2:, 1:-1] - 2*un[1:-1, 1:-1] + un[0:-2, 1:-1])/(dy**2) + (un[1:-1, 2:] - 2*un[1:-1, 1:-1] + un[1:-1, 0:-2])/(dx**2))
    pressure = (1/rho)*((p[1:-1, 2:] - p[1:-1, 0:-2])/(dx/2))
    temporal = (un[1:-1, 1:-1] - up[1:-1, 1:-1])/dt
    total = (temporal + convective + pressure - diffusive)
    l1 = np.abs(total)/(256*256)
    mse = np.sqrt(total**2)/np.sqrt(256*256)
    return np.sum(l1)/np.sum(un)