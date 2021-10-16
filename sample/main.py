# https://www.youtube.com/watch?v=T71dXmb2ClU
import turtle
squirtle = turtle.Turtle()
# squirtle.shape('turtle')
squirtle.forward(50)
squirtle.left(90)
squirtle.forward(50)
squirtle.left(90)
squirtle.forward(50)
squirtle.left(90)
squirtle.forward(50)

dict1 = {'shortside': 100, 'longside': 300}
squirtle.forward(dict1.get('shortside'))
squirtle.left(90)
squirtle.forward(dict1.get('longside'))
squirtle.left(90)
squirtle.forward(dict1.get('shortside'))
squirtle.left(90)
squirtle.forward(dict1.get('longside'))
turtle.done()

