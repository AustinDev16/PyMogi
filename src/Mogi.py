import numpy
import math
        
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
        
    def convertCartesianToRadial(self, x, y) -> float:
        return math.sqrt( math.pow(x,2) + math.pow(y,2))
    
    def _mogi_point_engine(self, dP, distance) -> float:
        return ( ((1-self.config.poissonRatio) * dP * math.pow(self.config.radius, 3.0) )/
                (self.config.mu) ) * ((self.config.depth)/(math.pow((math.pow(distance, 2.0) + 
                             math.pow(self.config.depth, 2.0)), 1.5)));

