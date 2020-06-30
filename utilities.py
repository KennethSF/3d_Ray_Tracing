import random
import argparse
import importlib
import os
from tkinter import *

from engine import RenderEngine
from scene import Scene
from engine import RenderEngine

from color import Color
from light import Light
from material import ChequeredMaterial, Material
from point import Point
from sphere import Sphere
from vector import Vector


def createScene(floorColors,sphereColors,lightColors,lightPositions):
    WIDTH = 960
    HEIGHT = 540
    RENDERED_IMG = "custom.ppm"
    CAMERA = Vector(0, -0.35, -1)
    OBJECTS = [
        # Ground Plane
        Sphere(
            Point(0, 10000.5, 1),
            10000.0,
            ChequeredMaterial(
                color1=Color.from_hex(floorColors[0]),
                color2=Color.from_hex(floorColors[1]),
                ambient=0.2,
                reflection=0.2,
            ),
        ),    
    ]
    createSpheres(OBJECTS,sphereColors)
    LIGHTS = []
    createLights(LIGHTS,lightColors,lightPositions)
    scene = Scene(CAMERA, OBJECTS, LIGHTS, WIDTH, HEIGHT)
    engine = RenderEngine() #Creates an instance of the render     
    image = engine.render(scene) #Creates a image rendering the data
    #os.chdir(os.path.dirname(os.path.abspath(mod.__file__))) #Creates a dir using the name in the mod
    with open(RENDERED_IMG, "w") as img_file: #Open the ppm image and store the pixels
        image.write_ppm(img_file)

#Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
def createSpheres(OBJECTS,sphereColors):
    spherePoints=[Point(0.75, -0.1, 1),Point(-0.75, -0.1, 2.25),Point(-0.80, -0.3, 0),
                 Point(0, -0.1, 4.75),Point(1.2, -0.1, 6)]
    i=0
    for color in sphereColors:
        OBJECTS.append(Sphere(spherePoints[i], 0.4, Material(Color.from_hex(color))))
        i+=1

#Light(Point(0, 1.5, 0), Color.from_hex("#FFFFFF")),
def createLights(LIGHTS,lightColors,lightPos):
    i=0
    for color in lightColors:
        x=(lightPos[i][0]*3.5/700)-1.75 # Gets a scale por the x axis
        y=(lightPos[i][1]*3.5/394)-1.75 # Gets a scale por the y axis
        print("X pos:" ,x, "Y pos: ",y)
        LIGHTS.append(Light(Point(x, y, random.randint(-10,0)), Color.from_hex(color)))
        i+=1
        
    pass

def getPoint(coordinates):
    pass