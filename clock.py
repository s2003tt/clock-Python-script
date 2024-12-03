# Saved as b1_baitass1.py

import turtle
import datetime
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor('orange')
screen.setup(width=600, height=600)
screen.title("Live Clock")
screen.tracer(0)

# Very basic clock face
face = turtle.Turtle()
face.shape("circle")
face.color("white")
face.fillcolor("black")
face.shapesize(stretch_wid=1, stretch_len=1)
face.penup()

#text
tex = turtle.Turtle()
tex.penup()
tex.goto(0, 250)
tex.write("Live Clock 2024", align='center', font=('Times New Roman', 25, 'bold'))
tex.color('blue')

# Hour hand
hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.color("green")
hour_hand.shapesize(stretch_wid=0.3, stretch_len=8)
hour_hand.penup()

# Minute hand
minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.color("yellow")
minute_hand.shapesize(stretch_wid=0.2, stretch_len=12)
minute_hand.penup()

# Second hand
second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.color("red")
second_hand.shapesize(stretch_wid=0.1, stretch_len=16)
second_hand.penup()

# Hour labels
hour_labels = turtle.Turtle()
hour_labels.color("darkblue")
hour_labels.penup()
hour_labels.hideturtle()

# Additional feature = Date display
date_display = turtle.Turtle()
date_display.color("darkgreen")
date_display.penup()
date_display.hideturtle()
date_display.goto(0, -270)  # Position below the clock face

# Display the current date
def display_date():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    date_display.clear()
    date_display.write(date_str, align="center", font=("Times New Roman", 25, "normal", "bold"))

# Draw the hour labels
def draw_hour_labels():
    for i in range(1, 13):
        angle = math.radians(30 * i)
        x = 200 * math.sin(angle)
        y = 200 * math.cos(angle)
        hour_labels.goto(x, y)
        hour_labels.write(str(i), align="center", font=("Times New Roman", 20, "normal", "bold"))
       
        
# Update the clock time
def update_clock():
    now = datetime.datetime.now()
    
    # Angles for each hand
    hour_angle = (now.hour % 12) * 30 + now.minute / 2
    
    # minute_angle = now.minute * 6
    minute_angle = now.minute * 6 + now.second * 0.1 # Consider the seconds here
    second_angle = now.second * 6
    
    # Rotate the hands 
    hour_hand.setheading(90-hour_angle)
    minute_hand.setheading(90-minute_angle)
    second_hand.setheading(90-second_angle)

    # Update the screen
    screen.update()

    # Call ontimer() again after 1 second
    screen.ontimer(update_clock, 1000)

display_date()    
     
# Draw the hour labels
draw_hour_labels()

# Update the clock
update_clock()

# Start main loop
screen.mainloop()
