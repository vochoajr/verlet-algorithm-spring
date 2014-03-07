import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#initial conditions
v=1
r=0

dt=0.1 #time step
m=1    #constant mass
F=-2*r #force equation

#lists for data storage
tlist, rlist, vlist = [], [], []

#algorithm
for i in range(100):
	v = v + dt * F / m #update v
	r = r + dt * v     #update r
	F = -2*r + -0.1*v  #recalculate force, with damping
	v = v + dt * F / m #update v
	tlist.append(i)    #add time to list
	rlist.append(r)    #add position to list
	vlist.append(v)    #add velocity to list

#setup figures
fig = plt.figure(figsize=(13,5)) #figsize=(width, height)
fig_1 = fig.add_subplot(1,2,1)
fig_2 = fig.add_subplot(1,2,2)

#make a scatter plot for t,r and t,v
fig_1.scatter(tlist, rlist)
fig_2.scatter(tlist, vlist)

plt.show()