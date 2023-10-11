import turtle


W = 3.048  # 10ft in meters
L = 10.668  # 35ft in meters

SCALE = 10

t = turtle.Turtle() 
t.screen.register_shape("truck", ((W/2 * SCALE,L/2 * SCALE), (W/2 * SCALE,-L/2 * SCALE), (-W/2 * SCALE,-L/2 * SCALE), (-W/2 * SCALE,L/2 * SCALE)))

t.shape("truck")
t.color("red")

t.up()
t.setpos(0, -18 * SCALE)
t.down()
t.circle(18 * SCALE) 

turtle.done()