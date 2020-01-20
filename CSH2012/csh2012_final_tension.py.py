#!/usr/bin/python
#tension.py    MrG     2013.0531
#copied from http://vpython.erikthompson.com
from __future__ import division # so 3/2 equals 1.5 instead of 1
from visual import *

print"""
A look at tension, static and kinetic friction.

This is a model of an experiment in which a book is placed on a flat table.
The book has a string tied to it with the other hand hanging off the side
of the table.  We will be adding weights to the string hanging off the edge
until the book starts sliding.

In this experiment the program will already know the coefficient of static
friction and the coefficient of kinetic friction.  When the user has added
enough mass to overcome static friction the book will slide accordingly.

The use of a pulley (not shown) helps negate friction on the string as well
as change the direction of force transmitted thru the string.  We are
approximating the the mass and friction of the string and pulley to be zero.
"""

# SET UP THE WINDOW
scene.width = 800
scene.height = 600

scene.autoscale = 1 # let vpython pick the range this time
scene.center = (1.5,.50,0) # center up and a little to the right of the origin

##########################################################################################
#
# CREATE THE OBJECTS ON OUR INITIAL SCENE
#
##########################################################################################

# CREATE A TABLE TO WORK ON
table = frame() # we want to make a table object that is built from a table top and leg.
tabletop = box(frame=table,pos=(0,1,0),size=(3,.2,1))
tableleg = cylinder(frame=table,pos=(0,0,0),axis=(0,1,0),radius=.3) # big round leg in the middle              

# CREATE THE GROUND
ground = box(size=(4,.2,1),pos=(0,-.1,0),color=color.yellow)

# CREATE OUR BOOK TO SLIDE
book = box(pos=(0,1.15,0),size=(.3,.1,.2), color=color.green)
book.mass = .1        # .1 kg
book.velocity = vector(0,0,0)
book.acceleration = vector(0,0,0)
book.force = vector(0,0,0)
book.moving = False     # it starts out at rest on the table

# ADD A STARTING MASS TO THE END OF THE STRING CREATED BELOW
weight = box(pos=(1.55,.5,0),size=(.1,.1,.1),color=color.green)
weight.mass = .02      # 20 grams = .020 kg
# we want the size of the mass to be roughly proportional to its mass
weight.size = vector(.1,weight.mass * 3,.1)  
# we want all of the increased size to be placed on top istead of
# half on top and half on the bottom so we adjust the position
weight.pos.y = .5 + (weight.size.y / 2)     
weight.velocity = vector(0,0,0)
weight.acceleration = vector(0,0,0)
weight.force = vector(0,0,0)

# TIE A STRING TO THE BOOK AND HANG THE STRING OVER THE TABLE TIED TO THE WEIGHT
string = curve(pos=[book.pos, (1.55,1.1,0)], color=color.red ) # string goes from book to slightly over edge
string.append( weight.pos ) # string goes straight down

# CREATE MASS OBJECTS TO CLICK AND LABEL DESCRIPTION
mass1 = sphere(pos=(3,2.3,.2),radius=.1,color=color.red)
mass1.mass = .001        # kg
message = "Click to add 1.0 grams."
mass1Label = label(pos=mass1.pos, text=message,yoffset=20)

mass2 = sphere(pos=(3,1.5,.2),radius=.13,color=color.blue)
mass2.mass = .005         # kg
message = "Click to add 5.0 grams."
mass2Label = label(pos=mass2.pos, text=message,yoffset=20)

# CREATE A LABEL FOR MESSAGES TO USER
mylabel = label(pos=(3.5,-1,0))

##########################################################################################
#
# CREATE VARIABLES FOR THE FORCES ACTING IN OUR PROGRAM
#
##########################################################################################

accelerationGravity = vector(0.0,-9.8,0.0)

gravityForceOnWeight = weight.mass * accelerationGravity
weight.force = gravityForceOnWeight

gravityForceOnBook = book.mass * accelerationGravity
normalForceOnBook = -1 * gravityForceOnBook

# The string pulls with the same force on both the book and weight.
# If the weight isn't moving, then the string tension (force) is equal to the
# force pulling the weight down (mass * gravity)
string.forceTensionMagnitude = mag(weight.force)

coefficientOfKineticFriction = .20      # constant for calculating kinetic friction between book and table
coefficientOfStaticFriction = .60       # constant for calculating static friction between book and table

directionBookIsBeingPulled = vector(1,0,0)

# FORMULA: magnitude of frictional force = coefficient * normal force
#          direction of frictional force = the direction opposing motion

# static frictional force acts on book when it isn't moving
# this is a maxiumum value.  It is the force that needs to be overcome
forceStaticFrictionOnBook = coefficientOfStaticFriction * mag(normalForceOnBook) * directionBookIsBeingPulled * -1
# kinetic frictional force acts on book when it is moving
forceKineticFrictionOnBook = coefficientOfKineticFriction * mag(normalForceOnBook) * directionBookIsBeingPulled * -1

##########################################################################################
#
# INITITIALIZE SOME MORE VARIABLES AND GO INTO OUR LOOP
#
##########################################################################################

book.startXpos = book.pos.x     # just to keep track of some stats
weight.startYpos = weight.pos.y # just to keep track of some stats
distanceBookTraveled = 0        # just to keep track of some stats
distanceWeightTraveled = 0      # just to keep track of some stats
dt = .01    # seconds
Finished = False
while not Finished:
    rate(100) # go thru loop no more than 100 times/sec
    if scene.mouse.events: # detect mouse events
        mouse = scene.mouse.getclick()
        if mouse.pick == mass1 or mouse.pick==mass2: # was a mass clicked?
            weight.mass += mouse.pick.mass  # add clicked mass to total mass
            weight.size = vector(.1,weight.mass * 3,.1) # same code as above
            weight.pos.y = .5 + (weight.size.y / 2)     # same code as above      

    # do we have enough force to move the book?
    if not book.moving:
        string.forceTensionMagnitude = mag(weight.mass * accelerationGravity)
        if string.forceTensionMagnitude > mag(forceStaticFrictionOnBook):
            book.moving = True # we have enough pulling force to overcome static friction

    if book.moving: # if so, we need to move everything
        # how fast are the weight and mass accelerating
        if weight.pos.y - weight.size.y/2 > 0: # if the weight hasn't landed
            # Let's write the equations that we know
            # 1. force on the weight = force pulling down - force pulling up
            # 2. force on the book = force pulling right - force holding back
            # otherwise written:
            # 1. mass of the weight * acceleration = mass of the weight * gravity - tension 
            # 2. mass of the book * acceleration = tension - frictional force on book 
            # There are two unknowns (acceleration and tension)
            # Using a bunch of algebra we get the acceleration

            # from equation 2: tension = mass of the book * acceleration + frictional force on book
            # substitute that into equation 1:
            # mass of the weight * gravity - (mass of the book * acceleration + frictional force on book) = mass of the weight * acceleration
            # use algebra to isolate acceleration variable
            # mass of the weight * acceleration + mass of the book * acceleration = mass of the weight * gravity - frictional force on book
            # acceleration (mass of the weight + mass of the book) = mass of the weight * gravity - frictional force on book
            # acceleration = (mass of the weight * gravity - frictional force on book) / (mass of the weight + mass of the book)
            accelerationMagnitude = (weight.mass * 9.8 - mag(forceKineticFrictionOnBook)) / (weight.mass + book.mass)
            weight.acceleration = accelerationMagnitude * vector(0,-1,0)
            book.acceleration = accelerationMagnitude * vector(1,0,0)            
        else: # weight has landed
            book.acceleration = forceKineticFrictionOnBook / book.mass
            string.forceTensionMagnitude = 0
            
        # move the book and weight according to their acceleration
        book.velocity += book.acceleration * dt
        book.pos += (book.velocity * dt + .5 * book.acceleration * dt**2) 
        distanceBookTraveled = book.pos.x - book.startXpos

        if weight.pos.y - weight.size.y/2 > 0: # if weight hasn't landed
            weight.velocity += weight.acceleration * dt
            weight.pos += (weight.velocity * dt + .5 * weight.acceleration * dt**2) 
            distanceWeightTraveled = weight.startYpos - weight.pos.y
       
        # keep string attached to end of book and weight
        string.pos = [ book.pos, (1.55,1.1,0), weight.pos ]

        if book.velocity.x < 0:
            Finished = True

    message = "String Tension: " + str(string.forceTensionMagnitude)
    message += "\nMax Static Frictional Force: " + str(forceStaticFrictionOnBook)
    message += "\nMax Kinetic Frictional Force: " + str(forceKineticFrictionOnBook)
    message += "\nTotal mass on string: " + str(weight.mass*1000) + " grams."
    message += "\nAcceleration of Book: " + str(book.acceleration)
    message += "\nAcceleration of Weight: " + str(weight.acceleration)
    message += "\nDistance Book Traveled: %.2f meters" % distanceBookTraveled
    message += "\nDistance Weight Traveled: %.2f meters" % distanceWeightTraveled

    mylabel.text =  message