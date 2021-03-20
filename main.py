from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


item_pick = 0
window.title = 'Pycraft'
window.fullscreen = True
window.color = color.color(180, 50, 80) # sky hsb color

punch = Audio('assets/sound/punch.wav', autoplay=False)

items = [
    load_texture('assets/texture/arm_texture.png'),  #0 hand
    load_texture('assets/texture/grass_block/grass_block.png'),  # 1 grass
    load_texture('assets/texture/grass_block/grass_block_break1.png'),
    load_texture('assets/texture/grass_block/grass_block_break2.png'),
    load_texture('assets/texture/grass_block/grass_block_break3.png'),
    load_texture('assets/texture/grass_block/grass_block_break4.png'),
    load_texture('assets/texture/grass_block/grass_block_break5.png'),  

    load_texture('assets/texture/stone_block/stone_block.png'),   # 7
    load_texture('assets/texture/stone_block/stone_block_break1.png'),
    load_texture('assets/texture/stone_block/stone_block_break2.png'),
    load_texture('assets/texture/stone_block/stone_block_break3.png'),
    load_texture('assets/texture/stone_block/stone_block_break4.png'),
    load_texture('assets/texture/stone_block/stone_block_break5.png'),  

    load_texture('assets/texture/brick_block/brick_block.png'),    # 13
    load_texture('assets/texture/brick_block/brick_block_break1.png'),
    load_texture('assets/texture/brick_block/brick_block_break2.png'),
    load_texture('assets/texture/brick_block/brick_block_break3.png'),
    load_texture('assets/texture/brick_block/brick_block_break4.png'),
    load_texture('assets/texture/brick_block/brick_block_break5.png'),

    load_texture('assets/texture/dirt_block/dirt_block.png'),  # 19
    load_texture('assets/texture/dirt_block/dirt_block_break1.png'),
    load_texture('assets/texture/dirt_block/dirt_block_break2.png'),
    load_texture('assets/texture/dirt_block/dirt_block_break3.png'),
    load_texture('assets/texture/dirt_block/dirt_block_break4.png'),
    load_texture('assets/texture/dirt_block/dirt_block_break5.png'),  
]

def update():
    global item_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        punch.play()
        hand.active()
    else:
        hand.passive() 

    if held_keys['0']: item_pick = 0 # hand
    if held_keys['1']: item_pick = 1
    if held_keys['2']: item_pick = 7
    if held_keys['3']: item_pick = 13
    if held_keys['4']: item_pick = 19
    
    hand.item_held()

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = items[1]):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/model/block.obj', 
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.white,
            scale = 0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if item_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = items[item_pick])
                if item_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = items[item_pick])
                if item_pick == 13: voxel = Voxel(position = self.position + mouse.normal, texture = items[item_pick])
                if item_pick == 19: voxel = Voxel(position = self.position + mouse.normal, texture = items[item_pick])

            if key == 'left mouse down':
                destroy(self)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/model/arm.obj',
            texture = items[0],
            scale = 0.07,
            rotation = Vec3(0, 70, 20),
            position = Vec2(0.8, -0.5)
        )

    def item_held(self):  # switching item for held ui
        if (item_pick == 0):
            self.model = 'assets/model/arm.obj'
            self.texture = items[0]
            self.scale = 0.07
        else:
            self.model = 'assets/model/block.obj'
            self.texture = items[item_pick]
            self.scale = 0.1

    def active(self):
        self.position = Vec2(0.7, -0.45)  

    def passive(self):
        self.position = Vec2(0.8, -0.5)

for z in range(-10, 10):  # map
    for x in range(-10, 10):
        for y in range(-2, 0):
            voxel = Voxel(position = (x,y,z))





player = FirstPersonController()
hand = Hand()

app.run()