
from time import sleep
from graphics import *
import random
w = GraphWin(" ", 700,560, autoflush=False)

def button(x,y, text, color):
    b = Rectangle(Point(x, y), Point(x+len(text)*10, y+50))  # points are ordered ll, ur
    b.setFill(color)
    text = Text(Point(x+(len(text)*5), y+20), text)
    text.setSize(13)
    text.setStyle("bold")
    b.draw(w)
    text.draw(w)
    return b

def inside(point, rectangle):
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

scene = 1
timer = 1
timess = 0
mode = 0
pointsint = 0

while True:
    if mode == 0:
        arr = [["Anya",10],[ "Alex",6],["Lino",1],["You", pointsint]]
        for item in w.items[:]:
            item.undraw()
            w.update()
        logo = Image(Point(350, 400), "ezgif.com-gif-maker (1).gif")
        logo.draw(w)
        logo1 = Image(Point(150, 400), "ezgif.com-gif-maker (1).gif")
        logo1.draw(w)
        logo2 = Image(Point(550, 400), "ezgif.com-gif-maker (1).gif")
        logo2.draw(w)
        points = button(100,100, "Points " + str(pointsint), "yellow")
        b = button(200,200, "Upload Mode", "lightblue1")
        btwo = button(400,200, "Rate Mode", "green1")
        print(arr)
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            less = [i for i in arr[1:] if i[1] > arr[0][1]]
            more = [i for i in arr[1:] if i[1] <= arr[0][1]]
            return quicksort(less) + [arr[0]] + quicksort(more)
        arr = quicksort(arr)
        print(arr)
        message0 = Text(Point(500, 80), "Leaderboard")
        message0.draw(w)
        message = Text(Point(500, 100), arr[0][0] + " " + str(arr[0][1]))
        message.draw(w)
        message1 = Text(Point(500, 120), arr[1][0] + " " + str(arr[1][1]))
        message1.draw(w)
        message2 = Text(Point(500, 140), arr[2][0] + " " + str(arr[2][1]))
        message2.draw(w)
        message4 = Text(Point(500, 160), arr[3][0] + " " + str(arr[3][1]))
        message4.draw(w)
        k = w.getMouse() 
        if inside(k, b):
            mode = 1 
    if mode == 1:
        x = random.randint(1, 7)
        print(x)
        timer = 1
        for item in w.items[:]:
            item.undraw()
            w.update()
        goodjob = Image(Point(350, 200), "tenor.gif")
        goodjob.draw(w)
        back = button(350,420,"Go Back", "lightblue1")
        prompt = ""
        if x == 1:
            prompt = "Pick up trash around your street"
            trash = Image(Point(350, 200), "Amazon.gif")
            trash.draw(w)
        if x == 2:
            prompt = "Plant a tree"
            tree = Image(Point(350, 200), "Homedepot.gif")
            tree.draw(w)
        if x == 3:
            prompt = "Donate to a charity"
            charity = Image(Point(350, 200), "ross.gif")
            charity.draw(w)
        if x == 4:
            prompt = "Pick up trash from a beach"
            trash1 = Image(Point(350, 200), "Hefty.gif")
            trash1.draw(w)
        if x == 5:
            prompt = "Donate food"
            food = Image(Point(350, 150), "Safeway.gif")
            food.draw(w)
        if x == 6:
            prompt = "Volunteer to help the homeless"
            homeless = Image(Point(350, 200), "Hope.gif")
            homeless.draw(w)
        if x == 7:
            prompt = "Adopt a pet"
            pet = Image(Point(350, 200), "Adopt.gif")
            pet.draw(w)

        inputBox = Entry(Point(200,400), 20)

        inputBox.draw(w)
        
        if scene == 1:
            if timer == 1:
                message = Text(Point(350,500), prompt)
                message.setFace("times roman")
                message.setStyle("bold")
                message.setSize(32)
                message.draw(w)
                b1 = button(20,20,"Upload", "yellow")
                timer = 2
            k1 = w.getMouse() 
            if inside(k1, b1):
                print("pressed")
                scene = 2
              
                pointsint = pointsint + 5
                
            if inside(k1, back):
                mode = 0
        if scene == 2:
            b.undraw()
            inputBox.undraw()
            message.undraw() 
            image = Image(Point(350, 150), inputBox.getText())
            image.draw(w)
         
            k1 = w.getMouse()
            if inside(k1, back):
                mode = 0
                scene = 1
            





