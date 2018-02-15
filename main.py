from Mogi import *
import numpy as np
import matplotlib.pyplot as plt


# Create Mogi Point Configuration
sourceAConfig = MogiSourceConfig(0.25, 1e6, 500, 4e3, 2e3,-10.5e3)
#Create Point with that Configuration
sourceA = MogiPoint(sourceAConfig)

# Calculate a single point deformation
sourceA._mogi_point_engine(5e6, 500)

# Now we add this point source to the solver. It supports adding multiple sources, so you
# pass in the sources as an array
solver = CalculateDeformation(np.array(sourceA))

#create a spatial array
xgrid = np.linspace(0,5e3,100)
ygrid = np.linspace(0,5e3,100)

sol = sourceA.calculate2D(5e6, xgrid, ygrid)
print(sol)

fig2, ax = plt.subplots()
ax.contourf(xgrid, ygrid, sol)
ax.set(xlabel="Horizontal Distance, (m)", ylabel='Vertical Distance, (m)')
fig2.savefig("xy.pdf")
soltuion = sourceA.calculate1D(5e6, xgrid)


fig, ax = plt.subplots()
ax.plot(xgrid, soltuion)

ax.set(xlabel='Radial Distance (m)', ylabel='Vertical Deformation (m)',
       title='Deformation vs Distance')
fig.savefig("deformation.pdf")

plt.show()