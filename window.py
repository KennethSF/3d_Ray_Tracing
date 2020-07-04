from tkinter import *
from tkinter import colorchooser
from tkinter import Canvas
import time
import utilities
import time

class mainWindow:
    floorColor1= "#f7e491"
    floorColor2= "#91f7ec"

    def __init__(self, master,geometry):
        self.floor=None
        self.sphere_colors= None
        self.light_colors= None
        self.light_positions= None        

        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry(geometry)
        self.master.resizable(False,False)
        self.master.config(background= "#FFFFFF")
        self.title=Label(text= "3D Ray Tracing creator",font=("Cambria",13), bg= "#000033",
                        fg="white",height="2",width="250").pack()
        #Floor
        self.btn_floor = Button(self.frame,text="Floor Color", command=self.get_floor,
                       width="20",height="1",bg="#000033",font=("Cambria",12),fg="#FFFFFF").place(x=30,y=45)
        #Spheres
        self.s_ammount= StringVar()
        self.spheres= Entry(self.frame,textvariable=self.s_ammount,
                      bg="#d1befa",width="3",font=("Cambria",14),justify="center").place(x=35,y=100)
        self.btn_spheres = Button(self.frame,text="Spheres", command=self.get_spheres,
                       width="15",height="1",bg="#000033",font=("Cambria",12),fg="#FFFFFF").place(x=75,y=95)
        #Lights
        self.l_ammount= StringVar()
        self.lights= Entry(self.frame,textvariable=self.l_ammount,
                      bg="#d1befa",width="3",font=("Cambria",14),justify="center").place(x=35,y=150)
        self.btn_light_color = Button(self.frame,text="Color", command=self.get_light_color,
                       width="6",height="1",bg="#000033",font=("Cambria",12),fg="#FFFFFF").place(x=75,y=145)
        self.btn_light_pos = Button(self.frame,text="Position", command=self.get_light_pos,
                       width="6",height="1",bg="#000033",font=("Cambria",12),fg="#FFFFFF").place(x=155,y=145)
        self.frame.pack(fill="both", expand=True)
        #Render image
        self.btn_render = Button(self.frame,text="Render Image", command=self.createScene,
                       width="20",height="1",bg="#000033",font=("Cambria",12),fg="#FFFFFF").place(x=30,y=230)

    #Stores the floor colors
    def floorColors(self,color1,color2):
        self.fcolor1=color1
        self.fcolor2=color2
        self.floor=[self.fcolor1,self.fcolor2]
        print("Color 1: ",self.fcolor1," Color2: ",self.fcolor2)
    
    def sphereColors(self,colors):
        self.sphere_colors= colors
        print(self.sphere_colors)
    
    def lightColors(self,colors):
        self.light_colors= colors
        print(self.light_colors)

    def lightPos(self,positions):
        self.light_positions= positions
        print(self.light_positions)

    #Create a toplevel window to get the floor colors
    def get_floor(self):
        self.floorWindow=Toplevel(self.master)
        self.app = floorWindow(self.floorWindow,'200x200',self.floorColors)

    def get_spheres(self):
        max=self.s_ammount.get()
        self.colorWindow=Toplevel(self.master)
        self.app = colorWindow(self.colorWindow,'200x200',max,self.sphereColors)
    
    def get_light_color(self):
        max=self.l_ammount.get()
        self.colorWindow=Toplevel(self.master)
        self.app = colorWindow(self.colorWindow,'200x200',max,self.lightColors)

    def get_light_pos(self):
        max=self.l_ammount.get()
        self.lightWindow=Toplevel(self.master)
        self.app = lightWindow(self.lightWindow,'700x394',max,self.lightPos)

    def createScene(self):
        print(self.light_positions)
        start_time= time.time()
        utilities.createScene(self.floor,self.sphere_colors,self.light_colors,self.light_positions)
        print("--- %s seconds ---" % (time.time() - start_time))
        #floorColors,sphereColors,lightColors,lightPositions
        #createScene(self.floor,self.sphere_colors,self.light_colors,self.lightPos):

class floorWindow:
    def __init__(self, master,geometry, color_action):
        self.master = master
        self.master.geometry(geometry)
        self.frame = Frame(self.master)
        self.successfull_colors= color_action
        self.floorColor1= "#f7e491"
        self.floorColor2= "#91f7ec"
        self.title= Label(self.master,text= "Select Floor colors",font=("Cambria",13), 
                        bg= "#000033",fg="white",height="2",width="20").pack()
    
        #Labels
        self.lbl_color1= Label(self.master,bg= "#f7e491",fg="white",
                        height="1",width="5",borderwidth=2, relief="groove").place(x=130,y=72)
        self.lbl_color2= Label(self.master,bg= "#91f7ec",fg="white",
                        height="1",width="5",borderwidth=2, relief="groove").place(x=130,y=122)
    
        #Buttons
        self.btn_color1 = Button(self.frame,text="Color 1", command=self.getColor1,width="10",
                    height="1",bg="#000033",font=("Cambria",9),fg="#FFFFFF")
        self.btn_color1.place(x=30,y=24)
        self.btn_color2 = Button(self.frame,text="Color 2", command=self.getColor2,width="10",
                    height="1",bg="#000033",font=("Cambria",9),fg="#FFFFFF").place(x=30,y=74)
        self.btn_done = Button(self.frame,text="Done", command=self.done,width="20",
                    height="1",bg="#000033",font=("Cambria",9),fg="#FFFFFF").place(x=30,y=115)
        
        self.frame.pack(fill="both", expand=True)

    #Sends the floor colors to the main window
    def done(self):
        self.successfull_colors(self.floorColor1,self.floorColor2)
        self.master.destroy()

    #The two functions picks the colors and update the labels to show what the user choose
    def getColor1(self):
        self.floorColor1=colorchooser.askcolor(parent=self.master)[1]
        self.lbl_color1= Label(self.master,bg= self.floorColor1,fg="white",
                        height="1",width="5",borderwidth=2, relief="groove").place(x=130,y=72)
    
    def getColor2(self):
        self.floorColor2=colorchooser.askcolor(parent=self.master)[1]
        self.lbl_color2= Label(self.master,bg= self.floorColor2,fg="white",
        height="1",width="5",borderwidth=2, relief="groove").place(x=130,y=122)

class colorWindow:
    def __init__(self,master,geometry,max,sphere_action):
        self.master= master
        self.max=int(max)
        self.master.geometry(geometry)
        self.frame = Frame(self.master)
        self.successfull_spheres= sphere_action
        self.title= Label(self.master,text= "Sphere Colors",font=("Cambria",13), 
                        bg= "#000033",fg="white",height="2",width="23").place(x=0,y=0)
        self.sphere_color="#f30707" #In case ser doesn't get a color 
        self.sphere_control=1 #Sphere_control has to be less than max
        #Buttons
        self.btn_color = Button(self.frame,text=("Color ",self.sphere_control), command=self.getColor,width="10",
                    height="1",bg="#000033",font=("Cambria",9),fg="#FFFFFF")
        self.btn_color.place(x=42,y=70)
        self.btn_aux = Button(self.frame,text="Accept", command=self.accept,width="10",
                    height="1",bg="#000033",font=("Cambria",9),fg="#FFFFFF")
        self.btn_aux.place(x=62,y=140)  
        #Labels
        self.lbl_color= Label(self.master,bg= "#f30707",fg="white",
                        height="1",width="5",borderwidth=2, relief="groove")
        self.lbl_color.place(x=125,y=70)
        self.colors=[]
        self.frame.pack(fill="both", expand=True)

    
    def getColor(self):
        self.sphere_color=colorchooser.askcolor(parent=self.master)[1]    
        self.lbl_color.destroy()
        self.lbl_color= Label(self.master,bg= self.sphere_color,fg="white",
                        height="1",width="5",borderwidth=2, relief="groove")
        self.lbl_color.place(x=125,y=70)
    
    def accept(self):
        self.colors.append(self.sphere_color)
        self.sphere_control+=1
        self.control()

    #Controls the GUI to help user to select the right ammount of colors
    def control(self):
        self.btn_color.destroy()
        self.lbl_color.destroy()
        self.sphere_color="#f30707"
        self.lbl_color= Label(self.master,bg= self.sphere_color,fg="white",
                        height="1",width="5",borderwidth=2, relief="groove")
        self.lbl_color.place(x=125,y=70)
        self.btn_color = Button(self.frame,text=("Color ",self.sphere_control), command=self.getColor,width="10",
                                height="1",bg="#000033",font=("Cambria",9),fg="#FFFFFF")
        self.btn_color.place(x=42,y=70)
        if(self.sphere_control>=self.max):
            self.btn_aux.destroy()
            self.btn_aux = Button(self.frame,text=("Finish"), command=self.done,width="10",
                                    height="1",bg="#000033",font=("Cambria",9),fg="#FFFFFF")
            self.btn_aux.place(x=62,y=140)
        
    def done(self):
        self.colors.append(self.sphere_color)
        self.successfull_spheres(self.colors)
        self.master.destroy()

class lightWindow:
    def __init__(self,master,geometry,max,light_action):
        self.master= master
        self.max=int(max)
        self.lightpos=[]
        self.master.geometry(geometry)
        self.frame = Frame(self.master)
        self.successfull_lights= light_action
        self.frame.pack(fill="both", expand=True)
        self.canvas=Canvas(self.master, width=700, height=394, bg='white')
        self.canvas.place(x=0,y=0)
        self.canvas.create_rectangle(0, 0, 700, 394, fill="white", tag='rectangle')
        self.canvas.create_rectangle(140,79,560 ,315 , fill="black", tag='rectangle')
        #self.lbl_instr=self.canvas.create_text((110,10),text="Click the positions where you want to put the lights")
        self.canvas.tag_bind('rectangle', '<Button 1>', self.getPos)

    def getPos(self,event):
        self.max-=1
        if(self.max==-1):
            self.done()
        else:
            self.lightpos.append([event.x,event.y])
            self.create_circle(self.canvas,event.x,event.y)

    def create_circle(self,canvas,x,y):
        r=5
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1,fill="#f33207")
    
    def done(self):
        self.successfull_lights(self.lightpos)
        time.sleep(2)
        self.master.destroy()