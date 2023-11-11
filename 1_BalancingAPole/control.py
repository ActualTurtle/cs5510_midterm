proportionalGain = 0
derivativeGain = 0
integralGain = 0
angleError = 0
lastError = 0

'''
This PID controller can be tuned using the above gain variables. It uses the current error, change in error, and accumulative error to calculate the force needed 
'''
def controlCartPole(angle):
    global angleError
    angleError += angle
    force = proportionalGain * angle + derivativeGain * (angle - lastError) + integralGain * angleError
    global lastError
    lastError = angle
    return force