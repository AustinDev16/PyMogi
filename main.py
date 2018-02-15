from Mogi import MogiSourceConfig, MogiPoint, MultipleSourceSolver
import numpy as np
import matplotlib.pyplot as plt


# Create Mogi Point Configuration
sourceAConfig = MogiSourceConfig(0.25, 1e6, 500, 4e3, 0, 0)
sourceBConfig = MogiSourceConfig(0.25, 1e6, 500, 5e3,8e3, 3e3)
#Create Point with that Configuration
sourceA = MogiPoint(sourceAConfig)
sourceB = MogiPoint(sourceBConfig)

# Calculate a single point deformation
sourceA._mogi_point_engine(5e6, 500)

# Now we add this point source to the solver. It supports adding multiple sources, so you
# pass in the sources as an array


#create a spatial array
xgrid = np.linspace(-5e3,10e3,100)
ygrid = np.linspace(-5e3,5e3,100)

sol = sourceA.calculate2D(5e6, xgrid, ygrid)


multi =  MultipleSourceSolver(np.array([sourceA, sourceB]))
sol3 = multi.calculate2D(5e6, xgrid, ygrid)
fig4, ax4 = plt.subplots()
ccf = ax4.contourf(xgrid, ygrid,sol3, cmap=plt.cm.Blues)
ax4.set(xlabel="Horizontal Distance, (m)", ylabel='Vertical Distance, (m)',
        title='Vertical deformation from 2 Mogi Sources')
fig4.colorbar(ccf)
ax4.set_aspect('equal', 'box')

fig4.savefig('multiple.pdf')
#mulSol = multi.calculate1D(5e6, xgrid)
#fig3, ax3 = plt.subplots()
#ax3.plot(xgrid, mulSol)

#fig2, ax = plt.subplots()
#cf = ax.contourf(xgrid, ygrid, sol)
#ax.set(xlabel="Horizontal Distance, (m)", ylabel='Vertical Distance, (m)')
#fig2.colorbar(cf)
#ax.set_aspect('equal', 'box')

# fig2.savefig("xy.pdf")
#soltuion = sourceA.calculate1D(5e6, xgrid)
#
#
#fig, ax = plt.subplots()
#ax.plot(xgrid, soltuion)
#
#ax.set(xlabel='Radial Distance (m)', ylabel='Vertical Deformation (m)',
#       title='Deformation vs Distance')
# fig.savefig("deformation.pdf")

plt.show()
