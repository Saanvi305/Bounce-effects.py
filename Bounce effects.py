import pgzrun

WIDTH=500
HEIGHT=600



box=Rect((200,480),(20,20))
vx=1
vy=1
bat=Rect((150,480),(60,20))
def draw():
    screen.clear()
    screen.draw.filled_rect(box,"red")
    screen.draw.filled_rect(bat,"green")
    


def update():
    global vx,vy
    box.x=box.x+vx
    box.y=box.y+vy

    if box.x>WIDTH or box.left<1:
        vx=-vx
    
    #if box.bottom>HEIGHT or box.y<0:
        #vy=-vy
    if box.colliderect(bat) or box.top<0:
        vy=-vy
    if box.bottom>HEIGHT:
        exit()
    if (keyboard.left):
      

        bat.x-=2
        if bat.x>WIDTH or bat.x<0:
            bat.x=200
    if (keyboard.right):
        bat.x+=2





        



    



pgzrun.go()