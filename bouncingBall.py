# experiments with visual Python (VPython)
# free download from http://vpython.org
# bounce a ball on the floor (no wind resistance)
# drag the right mouse button to change viewing angle
import visual as vs
vs.scene.width = 350
vs.scene.height = 500
vs.scene.center = (0,0.5,0)
vs.scene.title = "Bouncing Ball (drag right mouse button)"
# avoid autoscale (default)
vs.scene.autoscale = False
# a box object with attributes (x, y, z) or (length, height, width), color
floor = vs.box(pos=(0, -5.4, 0), size=(4, 0.2, 4), color=vs.color.green)
# a spherical object with attributes position (x, y, z), radius, color
ball = vs.sphere(pos=(0, 7.3, 0), radius=0.7, color=vs.color.red)
# ball moves in the y axis
ball.velocity = vs.vector(0, -1, 0)
# delta time
dt = 0.005
while 1:
    # set the rate of animation speed (update frequency)
    vs.rate(200)
    # change the position of ball based on the velocity on the y axis
    ball.pos = ball.pos + ball.velocity * dt
    # reverse ball direction within the y range
    if ball.y < -5:
        ball.velocity.y = -ball.velocity.y
    else:
        ball.velocity.y = ball.velocity.y - 9.8 * dt
