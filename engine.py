from image import Image
from ray import Ray
from point import Point
from color import Color
import random
import time

class RenderEngine:
    MAX_DEPTH= 10#random.randint(1,5)
    MIN_DISPLACE=0.0001
    #Renders 3d objects into 2d objects using ray tracing        

    def prepareRender(self, scene):
        #Creates the scene
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)
        
        return self.throughRender(width,height,camera,pixels,scene,y0,ystep,x0,xstep) #Return the image

    def fullRender(self,width,height,camera,pixels,scene,y0,ystep,x0,xstep):
        #Gets a pixel
        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep  #The raytrace of the pixel, otherwise creates a black pixel
                ray = Ray(camera, Point(x, y) - camera) #Creates a ray from the camera to the point
                pixels.set_pixel(i, j, self.ray_trace(ray, scene)) #Raytracing method
            print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r") #Progress bar
        return pixels

    def probRender(self,width,height,camera,pixels,scene,y0,ystep,x0,xstep):
        #Gets a pixel
        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                if(self.probability()):      #Monte Carlo method, calculates a probability, if return true calculates
                    x = x0 + i * xstep  #The raytrace of the pixel, otherwise creates a black pixel
                    ray = Ray(camera, Point(x, y) - camera) #Creates a ray from the camera to the point
                    pixels.set_pixel(i, j, self.ray_trace(ray, scene)) #Raytracing method
                else:
                    pixels.set_pixel(i, j, Color.from_hex("#000000"))#Creates a black pixel
            print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r") #Progress bar
        return pixels

    def maxPixelRender(self,width,height,camera,pixels,scene,y0,ystep,x0,xstep): #Only raytraces a maximun ammount of
        #Gets a pixel                                                              pixels
        max= width*height*0.75
        flag= True

        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep  
                pixels.set_pixel(i, j, Color.from_hex("#000000"))#Creates a black pixel
        print("Terminado")
        while flag:
        #for j in range(height):
            j=random.randint(0,height-1)
            y = y0 + j * ystep
            i=random.randint(0,width-1)
            x = x0 + i * xstep  #The raytrace of the pixel, otherwise creates a black pixel
            ray = Ray(camera, Point(x, y) - camera) #Creates a ray from the camera to the point
            pixels.set_pixel(i, j, self.ray_trace(ray, scene)) #Raytracing method
            max-=1 #Decreases the max pixels allowed
            if(max<=0):
                flag=False
        #print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r") #Progress bar
        return pixels

    def throughRender(self,width,height,camera,pixels,scene,y0,ystep,x0,xstep):
        #Gets a pixel
        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep  
                if(i%2!=0):
                    pixels.set_pixel(i, j, Color.from_hex("#000000"))#Creates a black pixel
                else:
                    ray = Ray(camera, Point(x, y) - camera) #Creates a ray from the camera to the point
                    pixels.set_pixel(i, j, self.ray_trace(ray, scene)) #Raytracing method
        return pixels
    
    

    def ray_trace(self, ray, scene, depth=0):
        color = Color(0, 0, 0)
        # Find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None: 
            return color
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene) #Gets the color of the pixel
        if depth<self.MAX_DEPTH:
            new_ray_pos= hit_pos + hit_normal * self.MIN_DISPLACE
            new_ray_dir= ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            new_ray= Ray(new_ray_pos,new_ray_dir)
            #Attenuate the reflected ray by the reflection coefficient
            color += self.ray_trace(new_ray,scene,depth+1) * obj_hit.material.reflection 
        return color

    def find_nearest(self, ray, scene): #Find the narest object hitted by the ray
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min): #Ensure that the object hitted is
                dist_min = dist                                           #the nearest
                obj_hit = obj
        return (dist_min, obj_hit)

    def color_at(self, obj_hit, hit_pos, normal, scene):
        material = obj_hit.material 
        obj_color = material.color_at(hit_pos)#Gets the color of the shere
        to_cam = scene.camera - hit_pos
        specular_k = 50
        color = material.ambient * Color.from_hex("#000000")
        # Light calculations
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # Diffuse shading (Lambert)
            color += (
                obj_color
                * material.diffuse
                * max(normal.dot_product(to_light.direction), 0)
            )
            # Specular shading (Blinn-Phong)
            half_vector = (to_light.direction + to_cam).normalize()
            color += (
                light.color
                * material.specular
                * max(normal.dot_product(half_vector), 0) ** specular_k
            )
        return color

    def probability(self):
        x=random.randint(0,100)/100.0
        if(x>=0.30):
            return True
        else:
            return False