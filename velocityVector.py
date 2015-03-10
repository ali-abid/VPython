# Represend velocity vector in 3D
# Version 1.0 (Feb, 2015).
# Abid Ali,
# IMaR Gateway Technology, Institute of Technology Tralee

from visual import *
side = 6.0
thk = 0.3
s2 = 2*side -thk
s3 = 2*side + thk

wallR = box(pos= (side,0,0), size=(thk,s2,s3),color=color.white)
wallL = box(pos= (-side,0,0), size=(thk,s2,s3), color=color.white)
wallB = box(pos= (0,-side,0), size=(s3,thk,s3), color=color.green)
wallT = box(pos= (0,side,0), size=(s3,thk,s3), color=color.black)
wallBK = box(pos= (0,0,-side), size=(s2,s2,thk), color=color.green)

ball = sphere(pos = (0,-5.5,4), radius = 0.3, color=color.cyan)

ball.velocity = vector(5,10,0)
deltat = 0.005
t= 0
#Create arrow vector
vscale = 0.1
varr = arrow(pos= ball.pos, axis=vscale*ball.velocity, color=color.yellow)
#Turn off autoscalling
scene.autuscale = False
#Leaving a trail
ball.trail = curve(color=ball.color)

#Continuous updating of the position of the ball
while t < 60:
    rate(100)
    #Bounce ball to walls
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.y > wallT.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.y < wallB.pos.y:
        ball.velocity.y = -ball.velocity.y

    #This is ball final position
    ball.pos = ball.pos + ball.velocity*deltat
    #Update arrow vector moving along ball
    varr.pos = ball.pos
    varr.axis = vscale*ball.velocity
    ball.trail.append(pos=ball.pos)
    t = t + deltat