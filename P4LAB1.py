import turtle             # Allows us to use turtles

win = turtle.Screen()      # Creates a playground for turtles
win.bgcolor("navyblue")   # Match background color

t = turtle.Turtle()        # Create a turtle, assign to t
t.pensize(5)
t.pencolor("purple")
t.shape("turtle")

# Draw the square or house base
t.penup()
t.goto(-50,-100)     # Bottom left corner of square
t.pendown()

for _ in range(4):
    t.forward(50)
    t.left(90)

# Draw the triangle or house roof

# Move to top-left corner of square
t.penup()
t.goto(-50, -50)  # Top left of square
t.pendown()

t.fillcolor("grey")
t.begin_fill()
t.forward(50)              # Base of roof and top of square
t.left(120)
t.forward(50)              # Left roof side
t.left(120)
t.forward(50)              # Right roof side back to start
t.end_fill()

win.mainloop()             # Wait for user to close window