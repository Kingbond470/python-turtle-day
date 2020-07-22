import turtle
import random
screen = turtle.Screen()                                           
turtle.title('Calendar Day')                           
screen.setup(width=1300,height=500)                      
screen.bgcolor('black')                              
screen.tracer(0)            # For refreshing the screen very fastly
turtle_pen = turtle.Turtle()                  # creation of pen
turtle_pen.hideturtle()                                                  # Hiding out the pen
#Colors list
colors_pen = ['green','blue', 'yellow', 'pink', 'purple','cyan','red','magenta','black']
colors_fill = ['green', 'blue','yellow', 'pink', 'purple','cyan','red','magenta','black']
turtle_pen.speed('fastest')                                       # Set turtle_pen pen Speed Very Fast
def calendar_day():
    for i in range(25):        #Stars creating in a loop to appear
        # random co ordinates of star
        x,y = random.randrange(-350,350),random.randrange(-230,230)
        turtle_pen1 = turtle.Turtle() 
        turtle_pen1.color(random.choice(colors_pen)) 
        # writing text
        turtle_pen1.write('Nelson Mandela International Day\n World Listening Day\n National Caviar Day\n ',font=('Arial',30,'italic bold'),align='center')
        turtle_pen1.clear()         # clearing pen for speed increse
        turtle_pen.penup()       # up the pen
        turtle_pen.goto(x,y)     # goto in the random co-ordinates
        turtle_pen.pendown()     # down the pen
        turtle_pen.begin_fill()  # star is in filled with color
        turtle_pen.color(random.choice(colors_pen)) # choose a random color for star
        for i in range(10): # create a star
            turtle_pen.forward(30)
            turtle_pen.right(144)
        turtle_pen.end_fill() 
while True: 
    calendar_day() 
    turtle_pen.clear() 
turtle.mainloop() 