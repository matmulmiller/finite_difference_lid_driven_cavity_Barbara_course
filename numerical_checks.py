
def Re_calc(nu, u, L):
    return L*u/nu

def CFL(dx, dt, u):
    return u*dt/dx

def Pe_calc(u, L, mu):
    return u*L/mu

