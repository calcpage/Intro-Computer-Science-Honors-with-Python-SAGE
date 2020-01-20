#!/usr/bin/python
#orbits01.py    MrG     2013.0531
#copied from http://vpython.erikthompson.com
from __future__ import division
from visual import *

print"""
In this model we will attempt to figure out the speed of the moon orbiting the
earth using Newton's Law of Universal Gravitation.

The earths mass is 5.98 * 10**24 kg
The earths radius is 6,380 km

The moons mass is 7.36 * 10**22 kg
The moons radius is 1,740 km

The center of the moon is 384000 km from the center of the earth.
The hubble space telescope orbits 600 km from the earth surface.
The international space station orbits about 360 km from the earth surface.
Geostationary orbit is 35,786 km above the earth's surface (equator).
GPS satellites orbit 20,000 km above the earth's surface.

In this episode we'll pretend the earth is stationary and ignore the satellites gravitational
pool on the earth.

To use this program:

1.  It is recommended that you uncomment the lines that
    increase the radius of the earth and satellite.

2.  Ajust the initial speed of the satellite to different speeds.  Try
    to figure out what speed gives a circular orbit by adjusting the speed
    and rerunning the program.

3.  You may need to decrease the value of dt to smaller values if you are
    trying to model satellites close to the earth.
"""

##########################################################################################
#
# FUNCTIONS
#
##########################################################################################

# this converts totalseconds to a nice string (days, hours, minutes and seconds)
def make_time_string(t):
    "Accept a number of seconds, return a relative string."
    if t < 60: return "%02i seconds"%t
    mins,secs = divmod(t, 60)
    if mins < 60: return "%02i minutes %02i seconds"%(mins,secs)
    hours, mins = divmod(mins,60)
    if hours < 24: return "%02i hours %02i minutes"%(hours,mins)
    days,hours = divmod(hours,24)
    return "%02i days %02i hours"%(days,hours)


##########################################################################################
#
# INITIALIZE WINDOW & DECLARATIONS
#
##########################################################################################

scene.center = (0,0,0)
scene.width = 800
scene.height = 600

scene.range = (1.0e9,1.0e9,1.0e9)

# some approximate data from the internet in scientific notation
# note: the following are three different ways of writing the same number
# 123000
# 1.23 * 10**5
# 1.23e5
massOfEarth = 5.98e24   # kg
massOfSatellite = 7.36e22    # kg
radiusOfEarth = 6.38e6  # m
radiusOfSatellite = 1.74e6   # m
distanceEarthToSatellite = 3.84e8  # m - the moon
#distanceEarthToSatellite = radiusOfEarth + 

# if we want to model satellites close to earth we may
# need to lower the difference in time (dt) which will
# decrease the error in our calculations but will take
# longer to run.
dt = 100 # seconds (try 100 for the moon, 1 to 10 for lower satellites)
totalseconds = 0 

# Univsal Law of Gravitation
# Gravitational Force = G * (mass1 * mass2) / r**2
# G is the univasal gravitaion constant which is about 6.67 * 10**(-11)
# r is the distance between the centers of the two masses
G = 6.67e-11


##########################################################################################
#
# CREATE EARTH AND SATELLITE OBJECTS
#
##########################################################################################

earth = sphere(pos=(0,0,0),radius=radiusOfEarth,color=color.blue)
earth.mass = massOfEarth

satellite = sphere(pos=(0,distanceEarthToSatellite,0),radius=radiusOfSatellite,color=color.white)
satellite.mass = massOfSatellite

mylabel = label(pos=(0,distanceEarthToSatellite + 100000000,0))

# when we draw things to scale as above the moon is a little hard to see
# lets pretend the moon has a much larger radius so we can see it
#satellite.radius = satellite.radius * 3
#earth.radius = earth.radius * 3 # be careful with this one as low satellites will be hidden

##########################################################################################
#
# SET INITIAL MOTION OF SATELLITE
#
##########################################################################################

# the moon will have a starting velocity that we will provide
# the direction will be left to right
speedOfSatellite = 500 # change this to how fast we think the satellite is going in m/s

# Instead of guessing we could cheat and calculate what the speed instead
# Satellites's Acceleration = Gravitational Force / Mass
# This equation is often simplified by cancelling mass2 (the saellite.mass in this case)
#initialAcceleration = (G * earth.mass * satellite.mass / distanceEarthToSatellite**2) / satellite.mass  # UNCOMMENT TO CHEAT

# Uniform Circular Motion: a = v**2/R (a is centripetal acceleration, R is the distance from the center of the circle)
# v**2 = a * R
# v = (a * R)**.5

#calculatedVelocity = (initialAcceleration * distanceEarthToSatellite)**.5 # UNCOMMENT TO CHEAT
#speedOfSatellite = calculatedVelocity # UNCOMMENT TO CHEAT

satellite.velocity = speedOfSatellite * vector(1,0,0) # m/s from left to right  


##########################################################################################
#
# GO THRU OUR LOOP
#
##########################################################################################
finished = False # it's always false so an it's an infitite loop
while not finished:
    totalseconds += dt
    rate(10000) # a high number pretty much means go as fast as our computer can
    
    # the magnitude of a vector subtracted from another is 
    # the distance between the two vectors
    distEarthToSatellite = mag(earth.pos - satellite.pos)

    # the norm of a vector subtracted from another is a
    # one unit vector in the direction of the other vector
    # See diagram of vector subtraction on wikipedia:
    # http://en.wikipedia.org/wiki/Vector_(spatial)#Vector_addition_and_subtraction
    ForceGravityOnTheSatelliteDir = norm(earth.pos - satellite.pos)    

    # calculate force magnitude from Newton's Law of Universal Gravitation
    ForceGravityOnTheSatelliteMag = G * (earth.mass * satellite.mass) / distEarthToSatellite**2

    # point that force magnitude in the direction of Earth
    ForceGravityOnTheSatellite = ForceGravityOnTheSatelliteMag * ForceGravityOnTheSatelliteDir

    # move the satellite using the force, Newton's 2nd Law, and the position equations
    satellite.acceleration = ForceGravityOnTheSatellite / satellite.mass
    satellite.velocity += satellite.acceleration * dt
    satellite.pos += satellite.velocity * dt + .5 * satellite.acceleration * dt**2

    # Display info to the user
    message = "Satellite's distance from earth's surface: %3.f kilometers" % ((distEarthToSatellite-radiusOfEarth)/1000)
    message += "\nSatellite's speed: %.0f m/s" % mag(satellite.velocity)
    message += "\nSatellite's acceleration magnitude: %.4f m/s**2" % mag(satellite.acceleration)
    message += "\nTime: " + make_time_string(totalseconds)
    mylabel.text = message