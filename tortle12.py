import turtle
import turtle

kria2=turtle.Turtle()
kria1=turtle.Turtle()
kria=turtle.Turtle()
guyn=("red","green","blue","yellow","magenta","cyan","violet")
kria.color(guyn[3])
kria2.color(guyn[0])
kria1.color(guyn[2])
k=50
i=0
d=1
w=300
def skzbnakan__keter():
    if i==0:
        kria1.left(90)
        kria1.forward(k)
        kria1.right(90)
        kria2.left(90)
        kria2.forward(k*2)
        kria2.right(90)
def nkarel(x):
    x.forward(w)
    x.left(90)
    x.forward(i*d)
    x.left(90)
while i<k:
    skzbnakan__keter()
    nkarel(kria2)
    nkarel(kria1)
    nkarel(kria)
    i+=1

