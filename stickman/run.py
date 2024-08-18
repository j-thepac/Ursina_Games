from ursina import *

app = Ursina()
window.fullscreen = False
window.color = color.white


mainChar = Animation(name='run',collider='box',position=(-4, -0.6, 0))
ground1 = Entity(model='quad',texture='brick',scale=(20,0.2,0),position=(0, -2.8, 0))


def input(key):
  if key == 'space':
    mainChar.animate_y(2,duration=0.4,curve= curve.out_sine)
    mainChar.animate_y(-.8,duration=0.4,delay=0.4,curve = curve.in_sine)

camera.orthographic = True
camera.fov = 10
app.run()
