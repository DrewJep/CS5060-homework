import pyrosim.pyrosim as pyrosim

length=1
width=1
height=1
x=-2
y=-2
z=.5

pyrosim.Start_SDF("boxes.sdf")

for i in range(5):
    for j in range(5):
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+j,y+i,z+k] , size=[length, width, height])
            length=length*.9
            width=width*.9
            height=height*.9
        length=1
        width=1
        height=1
# pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length, width, height])

pyrosim.End()