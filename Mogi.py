import numpy as np
import math
import matplotlib.pyplot as plt
        
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
        
    def convertCartesianToRadial(self, x, y):
        adjX = np.abs(x - self.config.centerX)
        adjY = np.abs(y - self.config.centerY)
        return np.sqrt(np.power(adjX,2) + np.power(adjY,2))
    
    def _mogi_point_engine(self, dP, distance):
        return ( ((1-self.config.poissonRatio) * dP * np.power(self.config.radius, 3.0) )/
                (self.config.mu) ) * ((self.config.depth)/(np.power((np.power(distance, 2.0) + 
                             np.power(self.config.depth, 2.0)), 1.5)))

    def calculate1D(self, dP, grid):
        return self._mogi_point_engine(dP, grid)

    def calculate2D(self, dP, xgrid, ygrid):
        yv, xv = np.meshgrid(ygrid, xgrid, sparse=False, indexing='ij')
        converted = self.convertCartesianToRadial(xv, yv)
        return self._mogi_point_engine(dP, converted)

class CalculateDeformation:
    def __init__(self, mogiPointArray):
        self.mogiPointArray = mogiPointArray

    def calculate1D(self, dP: float, array: [])-> []:
        solution = np.zeros(len(array))

        mogi = self.mogiPointArray[0]
        sol = mogi._mogi_point_engine(dP,array) + 1
        return sol

    def calculate2D(self):
        pass


       

