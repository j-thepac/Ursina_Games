from ursina import *
import random as r

# def newCactus():
#   new = duplicate(cactus,x=12+r.randint(0,5))
#   cacti.append(new)
#   invoke(newCactus, delay=2)

# def update():
#   global points
#   points += 1
#   label.text = f'Points: {points}'
#   for ground in pair:
#     ground.x -= 6*time.dt
#     if ground.x < -35:ground.x += 100
#   for c in cacti:
#     c.x -= 6*time.dt
#   if tiger.intersects().hit:
#     tiger.texture= 'hit'
#     application.pause()

# def input(key):
#   if key == 'space':
#     if tiger.y < 0.01:
#       sound.play()
#       tiger.animate_y(2,duration=0.4,curve= curve.out_sine)
#       tiger.animate_y(0,duration=0.4,delay=0.4,curve = curve.in_sine)

app = Ursina()
window.fullscreen = False
window.color = color.white


box = Entity(model='quad',texture='brick',color=color.red,collider='box',scale=(1.5,1.5,1),position=(-9, -0.8, 1))
tiger = Animation('sprites-cat-running',collider='box',position=(-4, -0.6, 0))
ground1 = Entity(model='quad',texture='brick',scale=(20,0.2,0),position=(0, -2, 0))
sun = Entity(model='sphere', color=color.orange, scale=(1.5,1.5,1),position=(5, 3, 0))



def input(key):
  if key == 'space':
      #Audio('beep', autoplay=False)#beep.wav
    tiger.animate_y(2,duration=0.4,curve= curve.out_sine)
    tiger.animate_y(-.8,duration=0.4,delay=0.4,curve = curve.in_sine)


def update():
    box.x = box.x-6*time.dt
    if(box.x<-9):box.x=9
#   if dino.intersects().hit:
#     dino.texture= 'hit'
    # application.pause()

# ground2 = duplicate(ground1, x=50)
# pair = [ground1, ground2]
# ground1 = Entity(model='quad',texture='ground',scale=(50,0.5,1),z=1)
# ground2 = duplicate(ground1, x=50)
# pair = [ground1, ground2]

# cactus = Entity(model='quad',texture='cacti',x = 20,collider='box')
# cacti = []
# newCactus()

# label = Text( text = f'Points: {0}', color=color.black,position=(-0.5, 0.4))
# points = 0

camera.orthographic = True
camera.fov = 10
app.run()
