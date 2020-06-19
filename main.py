"""Python Raytracer"""

from color import Color
from point import Point
from vector import Vector
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material

def main():
    WIDTH=320 #800
    HEIGHT=200 #500
    camera=Vector(0,0,-1)

    objects=[Sphere(Point(0,0,0),0.5,Material(Color.from_hex("#FF0000")))]
    lights=[Light(Point(1.5,-0.5,-10.0),Color.from_hex("#FFFFFF"))]
    scene= Scene(camera,objects,lights,WIDTH,HEIGHT)
    engine= RenderEngine()
    image=engine.render(scene)

    with open("test.ppm","w") as img_file:#Opens a file called test and activate the write function
        image.write_ppm(img_file)

if __name__== "__main__":
    main()