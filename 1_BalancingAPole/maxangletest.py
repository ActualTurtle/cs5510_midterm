from cartpole import CartPoleObj
import math

cart = CartPoleObj()
maxAngle = 0   # Radians
maxAngleFound = False

while not maxAngleFound:

    # angle before step/force is applied 
    theta_0 = cart.theta

    # Double step to account for a float edge case
    cart.step()
    cart.step()

    # If the pole arm rotates more in the 'falling' direction
    if cart.theta > theta_0:
        maxAngleFound = True
        break
    
    maxAngle = cart.theta

    cart.x = 0
    cart.x_dot = 0
    cart.theta += 0.01
    cart.theta_dot = 0


print(f"Max Angle is {maxAngle} Radians, {maxAngle * 180 / math.pi} Degrees, with max force applied {cart.force_mag}")