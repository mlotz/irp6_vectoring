#!/usr/bin/env python      
import Tkinter as tk       
import rospy
from irpos import *
from exirpos import *
import numpy as np
from std_msgs.msg import *
from visualization_msgs.msg import Marker

class Application(tk.Frame):              
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)   
		#self.grid()                       
		#self.createWidgets()
		self.x=0
		self.y=0
		self.id = self.after(1000, self.callback)
		#self.y=0
		self.width=2
		self.w = tk.Canvas(self, width=600, height=400)
		self.w.create_line(0, 0, 200, 100)
		self.w.pack()
		self.w.grid()
		
	#def createWidgets(self):
		#self.quitButton = tk.Button(self, text='Quit',
		#    command=self.quit)            
		#self.quitButton.grid()
		
		

		#self.w.create_line(0, 0, 200, 100)
		#self.w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

		#self.w.create_rectangle(50, 25, 150, 75, fill="blue")
		#self.w.create_line(0, 0, 200, 100)
		
	#def draw_stuff(self):
		#self.w.create_oval(self.x,self.y,self.x+self.width,self.y+self.width)
		#self.w.create_line(0, 0, 200, 100)
		#self.w.pack()
		#self.w.grid()
		#self.x=self.x+1
		#self.y=self.y+1
		#app.after(2000,self.draw_stuff())  
	def callback(self):
		self.x +=1
		print(self.x)
		self.w.create_line(0,0,200+self.x,100+self.y)
		self.w.pack()
		self.w.grid()
		self.id=self.after(1000,self.callback)
app = Application()
app.mainloop()
	          

#app = Application()                       
#app.master.title('Sample application')  
#app.draw_stuff()
#app.mainloop()   



