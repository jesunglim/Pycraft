from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


block_pick = 0
window.title = 'Pycraft'
window.fullscreen = True
window.color = color.color(180, 50, 80) # sky hsb color

punch = Audio('assets/sound/punch.wav', autoplay=False)

items = [
    [
        load_texture('assets/texture/arm_texture.png')  #0 hand
    ],
    
    [
    load_texture('assets/texture/grass_block/grass_block.png'),  # 1 grass
    load_texture('assets/texture/grass_block/grass_block_break1.png'),
    load_texture('assets/texture/grass_block/grass_block_break2.png'),
    load_texture('assets/texture/grass_block/grass_block_break3.png'),
    load_texture('assets/texture/grass_block/grass_block_break4.png'),
    load_texture('assets/texture/grass_block/grass_block_break5.png') 
    ],

    [
        load_texture('assets/texture/stone_block/stone_block.png'),   # 2 stone
        load_texture('assets/texture/stone_block/stone_block_break1.png'),
        load_texture('assets/texture/stone_block/stone_block_break2.png'),
        load_texture('assets/texture/stone_block/stone_block_break3.png'),
        load_texture('assets/texture/stone_block/stone_block_break4.png'),
        load_texture('assets/texture/stone_block/stone_block_break5.png')  
    ],

    [
        load_texture('assets/texture/brick_block/brick_block.png'),    # 3 brick
        load_texture('assets/texture/brick_block/brick_block_break1.png'),
        load_texture('assets/texture/brick_block/brick_block_break2.png'),
        load_texture('assets/texture/brick_block/brick_block_break3.png'),
        load_texture('assets/texture/brick_block/brick_block_break4.png'),
        load_texture('assets/texture/brick_block/brick_block_break5.png')
    ],

    [
        load_texture('assets/texture/dirt_block/dirt_block.png'),  # 4 dirt
        load_texture('assets/texture/dirt_block/dirt_block_break1.png'),
        load_texture('assets/texture/dirt_block/dirt_block_break2.png'),
        load_texture('assets/texture/dirt_block/dirt_block_break3.png'),
        load_texture('assets/texture/dirt_block/dirt_block_break4.png'),
        load_texture('assets/texture/dirt_block/dirt_block_break5.png')  
    ]
]



def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        punch.play()
        hand.active()
    else:
        hand.passive() 

    if held_keys['0']: block_pick = 0 # hand
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    
    hand.item_held()

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = items[1][0]):
        self.block_id = 1
        self.block_health = 100
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
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = items[block_pick][0]) # items[ block id][nomal block texture]
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = items[block_pick][0])
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = items[block_pick][0])
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = items[block_pick][0])
                self.block_id = block_pick

            if key == 'left mouse down':
                self.block_health -= 16
                if self.block_health <= 5:
                    destroy(self)
                elif self.block_health <= 20:
                    self.texture = items[self.block_id][5]
                elif self.block_health <= 40:
                    self.texture = items[self.block_id][4]
                elif self.block_health <= 55:
                    self.texture = items[self.block_id][3]
                elif self.block_health <= 70:
                    self.texture = items[self.block_id][2]
                elif self.block_health <= 85:
                    self.texture = items[self.block_id][1]
                elif self.block_health == 100:
                    self.texture = items[self.block_id][0]
                    

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/model/arm.obj',
            texture = items[0][0],
            scale = 0.07,
            rotation = Vec3(0, 70, 20),
            position = Vec2(0.8, -0.5)
        )

    def item_held(self):  # switching item for held ui
        if (block_pick == 0):
            self.model = 'assets/model/arm.obj'
            self.texture = items[0][0]
            self.scale = 0.07
        else:
            self.model = 'assets/model/block.obj'
            self.texture = items[block_pick][0]
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