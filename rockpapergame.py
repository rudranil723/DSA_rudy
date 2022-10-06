from tkinter import*
import random
from turtle import width

# part 3


root = Tk()
root.title("ROCK,PAPER,SCISSOR GAME")
width = 690
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)-(width/2)
y = (screen_height/2)-(height/2)
root.geometry("%dx%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg='blue')


# part 4

