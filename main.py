#!/usr/bin/env python
"""Puray - a Pure Python Raytracer by Arun Ravindran, 2019"""
import argparse
import importlib
import os
from tkinter import *

from engine import RenderEngine
from scene import Scene
from engine import RenderEngine
from window import mainWindow


def main():
    root = Tk()
    app = mainWindow(root,'250x350')
    root.mainloop()
    """ parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (without .py extension)")#Ask for the name of the
    args = parser.parse_args()                                                     #module
    mod = importlib.import_module(args.scene) #Imports the module

    #Creates the scene unsing the mod information
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine() #Creates an instance of the render     
    image = engine.render(scene) #Creates a image rendering the data
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__))) #Creates a dir using the name in the mod
    with open(mod.RENDERED_IMG, "w") as img_file: #Open the ppm image and store the pixels
        image.write_ppm(img_file) """


if __name__ == "__main__":
    main()