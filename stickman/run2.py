from ursina import *

app = Ursina()

a = Animator(
    animations = {
        'run':Animation('run', loop=True, autoplay=False,position=(-4, -0.6, 0)),
        'jump':Animation('jump', loop=False, autoplay=False,position=(-4, -0.6, 0)),
        'shoot':Animation('shoot', loop=False, autoplay=False,position=(-3, -2, 0)),
    }
)
a.state = 'run'

def input(key):
    if key == 'space':
        a.state = 'jump'
        invoke(setattr, a, 'state', 'run', delay=a.animations['jump'].duration)
    elif key=='z':
        a.state = 'shoot'
        invoke(setattr, a, 'state', 'run', delay=a.animations['shoot'].duration*2)

window.fullscreen = False
window.color = color.white
app.run()

