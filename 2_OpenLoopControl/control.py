import math
# import matplotlib.pyplot as plt


W = 3.048  # 10ft in meters, width of vehicle
L = 10.668  # 35ft in meters, length of vehicle

SCALE = 10

'''
ackerman_kin
Returns (x_new, y_new, theta_new) position based on normal car steering.
Overload 1
'''
def ackerman_kin(v, x, y, alpha, theta, dt=1.0):
    x_new = x + -v * math.sin(theta) * dt
    y_new = y + v * math.cos(theta) * dt
    theta_new = theta + v/L * math.tan(alpha) * dt
    return (x_new, y_new, theta_new)

# '''
# ackerman_kin
# Returns (x_new, y_new, theta_new) position based on normal car steering.
# '''
# def ackerman_kin(v, alpha, dt=1.0):
#     theta = v / L * math.tan(alpha)
#     x = -v * math.sin(theta)
#     y = v * math.cos(theta)
#     return ackerman_kin(v, x, y, alpha, theta, dt)

'''
skid_steer_kin
Returns (x_new, y_new, theta_new) position based on skid steer.
'''
def skid_steer_kin(v_left, v_right, x, y, theta, dt=1.0):
    x_new = x - 1/2 * (v_left + v_right) * math.sin(theta) * dt
    y_new = y + 1/2 * (v_right + v_left) * math.cos(theta) * dt
    theta_new = theta + 1/W * (v_right - v_left) * dt
    return (x_new, y_new, theta_new)