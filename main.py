from Mogi import MogiSourceConfig, MogiPoint

settings = MogiSourceConfig(0.5, 1e6, 500, 4e3, 0,0)

mogiPoint = MogiPoint(settings)
print(mogiPoint.config.poissonRatio)

print(mogiPoint.convertCartesianToRadial(4,0))

print(mogiPoint._mogi_point_engine(5e6, 5))

mogiPoint.config.depth