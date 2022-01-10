# https://www.ursinaengine.org/cheat_sheet.html
from time import thread_time
from direct.showbase.PythonUtil import Default
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from perlin_noise import PerlinNoise

import keyboard
import matplotlib.pyplot as plt

app = Ursina()

# interepetacion del player
player = FirstPersonController()

player.health = HealthBar()
player.jump_duration=0.25
player.gravity=1

player.spawn = (0,20,0)

chunkRange = 16
# spawn = (0,2,0)


# Matriz equivalente al objeto tridimensional 
class Voxel(Button):
    def __init__(self, position=(0,0,0)): #x,y,z
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube', #grass
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
                # player.spawn = self.position
        if self.hovered:
            if key == 'right mouse down':
                destroy(self)
        if key == 'escape':
            exit()
        if key == 'shift':
            player.speed = 10
        if key == 'espace':
            player.gravity = 0



# RUIDO / NOISE GENERATION
    # noise_map = PerlinNoise(octaves=10)

    # xpix, ypix = 100, 100
    # pic = [[noise_map([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

    # plt.imshow(pic, cmap='gray')
    # plt.show()
#

#GENERACION DE TERRENO
noise1 = PerlinNoise(octaves=2.5) # 3

xpix, ypix = 50, 50
map = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        
        noise_val =  noise1([i/xpix, j/ypix])*10
        voxel = Voxel(position=(i, round(noise_val), j))

        # print("X="+str(voxel.position[0])+" Y="+str(voxel.position[1])+" Z="+str(voxel.position[2]))
        
        row.append(noise_val)
    map.append(row)


plt.imshow(map, cmap='gray')
plt.show()


# Edicion del mapa
# for z in range(chunkRange):
#     for x in range(chunkRange):
#         voxel = Voxel(position=(x,0,z))
#         voxel = Voxel(position=(-x,0,z))
#         voxel = Voxel(position=(x,0,-z))
#         voxel = Voxel(position=(-x,0,-z))
    # for y in range(chunkRange):
    #     voxel = Voxel(position=(x,y,z))


# Resetear posicion por caida o fuera del plano
def resetPosition():
    if player.position.y < -40:
        player.position = player.spawn
        #nota: Si no hay suelo este caera al infiito
        # Donde este el spawn hacer que el cubo,spawn no se pueda eliminar ni tapar 2 bloques por encima de este

# Refesco
def update():
    resetPosition()

app.run() # Aracarnar el juego