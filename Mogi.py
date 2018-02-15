import numpy as np
        
class MogiSourceConfig:
    def __init__(self, poissonRatio, 
                 mu, radius, depth, centerX, centerY):
        self.poissonRatio = poissonRatio
        self.mu = mu
        self.radius = radius
        self.depth = depth
        self.centerX = centerX
        self.centerY = centerY
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MogiPoint:
    def __init__(self, sourceConfiguration):
        self.config = sourceConfiguration
        
    def convertCartesianToRadial2D(self, x, y):
        adjX = np.abs(x - self.config.centerX)
        adjY = np.abs(y - self.config.centerY)
        return np.sqrt(np.power(adjX,2) + np.power(adjY,2))
    
    def convertCartesianToRadial1D(self, x):
        adjX = np.abs(x - self.config.centerX)
        return adjX
    
    def _mogi_point_engine(self, dP, distance):
        return ( ((1-self.config.poissonRatio) * dP * np.power(self.config.radius, 3.0) )/
                (self.config.mu) ) * ((self.config.depth)/(np.power((np.power(distance, 2.0) + 
                             np.power(self.config.depth, 2.0)), 1.5)))

    def calculate1D(self, dP, grid):
        adjGrid = self.convertCartesianToRadial1D(grid)
        return self._mogi_point_engine(dP, adjGrid)

    def calculate2D(self, dP, xgrid, ygrid):
        yv, xv = np.meshgrid(ygrid, xgrid, sparse=False, indexing='ij')
        converted = self.convertCartesianToRadial2D(xv, yv)
        return self._mogi_point_engine(dP, converted)


class MultipleSourceSolver:
    def __init__(self, mogiPointArray = np.array([])):
        self.mogiPointArray = mogiPointArray
        
    def addSource(self, pointSource: MogiPoint):
        np.append(self.mogiPointArray, pointSource)

    def calculate1D(self, dP, grid):
        solution = np.zeros(len(grid))
        print(len(self.mogiPointArray))
        for source in self.mogiPointArray:
            solution += source.calculate1D(dP, grid)
        return solution

    def calculate2D(self, dP, xgrid, ygrid):
        yv, xv = np.meshgrid(ygrid, xgrid, sparse=False, indexing='ij')
        converted = self._zeroOutMeshGrid(xv, yv)
        for source in self.mogiPointArray:
            converted += source.calculate2D(dP, xgrid, ygrid)
        return converted

    def _zeroOutMeshGrid(self, xmesh, ymesh):
        return xmesh * 0 + ymesh * 0

       

