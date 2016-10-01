import turtle

def shape(x):
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.left(10+x)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)


count =0
x=0
while(count<50):
    x=x+10
    shape(x)
    count+=1