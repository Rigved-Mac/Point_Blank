import turtle

#Setting up the Turtle Pen
turtle.speed(2)
turtle.bgcolor("black")
turtle.color("green")
turtle.pensize(5)
turtle.teleport(-50,50)
turtle.delay(20)

#Drawing <
turtle.goto(-100,25)
turtle.goto(-50,0)
turtle.delay(20)

#Drawing .
turtle.teleport(-20,0)
turtle.dot(10,"green")
turtle.delay(20)

#Drawing >
turtle.teleport(50,50)
turtle.goto(100,25)
turtle.goto(50,0)
turtle.ht()

#Writing Point Blank
turtle.teleport(-80,-40)
turtle.write('Point', font=('Arial',24,'normal'))
turtle.teleport(-10,-40)
turtle.color('white')
turtle.write('Blank', font=('Arial',24, 'normal'))
turtle.exitonclick()
