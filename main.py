import math
import os
import numpy as np
from numpy import save 
import matplotlib.pyplot as plt
from numerical_checks import Re_calc, Pe_calc, CFL
from batching import generate_batch
from solver import solver
from meshing import mesher, define_step_shape



# Define the geometry of the box 
L = 0.005  # m
H = 0.005 # m

# Define the spatial spacing 
nx = 256
ny = 256
dx = L/nx  # mm
dy = H/ny  # mm

# Define temporal parameters
dt = 5e-6  # s
t_0 = 0  # s
t_f = 2e-2  # s
nt = int(math.ceil((t_f - t_0)/dt))

# Define rheology
mu = 1e-5 # kg/m/s
rho = 1  # kg/m^3
nu = mu/rho  # m^2 / s

mode = 'Validation'

Reynolds_number = 550

batch = generate_batch(Reynolds_number, mode)

# Define lid speed in m/s
lid_speed = Reynolds_number*nu/L

print(f"Courant Number {CFL(dx, dt, lid_speed)}")
print(f"Reynolds number {Re_calc(nu, lid_speed, L)}")
print(nt)

# Set pressure inner iterations
iters = 50

# Define parent directory based on mode
if mode == 'Train':
    parent_directory = "C:\\Users\\jacob\\OneDrive - University of Louisville\\Projects\\ROMAI_2022\\Cavity_DataGen\\Training_Data"
elif mode =="Validation":
    parent_directory = "C:\\Users\\jacob\\OneDrive - University of Louisville\\Projects\\ROMAI_2022\\Cavity_DataGen\\Validation_Data"
else:
    parent_directory = "C:\\Users\\jacob\\OneDrive - University of Louisville\\Projects\\ROMAI_2022\\Cavity_DataGen\\Testing_Data"



if __name__ == '__main__':
    batch_folder = os.path.join(parent_directory, str(Reynolds_number)+'Re_batch')
    os.mkdir(batch_folder)

    for step_height in batch['Sh']:
        if step_height == 0:
            step=False
            run_folder = os.path.join(batch_folder, f'Re{Reynolds_number}_Sh{step_height}_Sl{step_height}')
            os.mkdir(run_folder)

            u0, v0, p0, points = mesher(nx, ny, step_height, step_height, step, lid_speed, define_step_shape=define_step_shape)
            un, vn, p = solver(u0, v0, p0, nt, iters, dx, dy, nx, ny, dt, rho, nu, lid_speed, step, points)

            save(os.path.join(run_folder, 'u.npy'), un)
            save(os.path.join(run_folder, 'v.npy'), vn)
            save(os.path.join(run_folder, 'p.npy'), p)
        else:
            for step_length in batch['Sl']:
                step=True
                run_folder = os.path.join(batch_folder, f'Re{Reynolds_number}_Sh{step_height}_Sl{step_length}')
                os.mkdir(run_folder)

                u0, v0, p0, points = mesher(nx, ny, step_height, step_length, step, lid_speed, define_step_shape=define_step_shape)
                un, vn, p = solver(u0, v0, p0, nt, iters, dx, dy, nx, ny, dt, rho, nu, lid_speed, step, points)

                save(os.path.join(run_folder, 'u.npy'), un)
                save(os.path.join(run_folder, 'v.npy'), vn)
                save(os.path.join(run_folder, 'p.npy'), p)