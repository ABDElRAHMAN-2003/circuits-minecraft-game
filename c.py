from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import curve    
app = Ursina()
battery_but=Entity(model="light.obj",position=(1.4,1.7,6.2),scale=0.5,color=color.white)
battery_but1=Entity(model="light.obj",position=(1.4,-6.2,6.2),scale=0.5,color=color.white)
sky_texture=load_texture("skybox.png")
grass_texture=load_texture("grass_block.png")     
stone_texture=load_texture("stone_block.png")
dirt_texture=load_texture("dirt_block.png")
brick_texture=load_texture("brick_block.png")
punch_sound=Audio('mixkit-blow-breaking-the-air-2057.wav' , loop = False, autoplay = False)                #textures of models
punch_sound2=Audio('cloth-inventory.wav', loop=False, autoplay=False) 
arm_texture=load_texture("arm_texture.png")
#generator_sound=Audio('337447__ivolipa__compressor-motor.wav',loop=False,autoplay=False)
sound5=Audio('hold the line_0.flac', loop = True , autoplay = True)
block_pick = 1
window.fps_counter.enabled=False 
window.exit_button.visible=False                                                                     #some options for the interface
window.fullscreen=True
def update():                             
    global block_pick
    # raycast1=raycast(player.position)
    #  # mo=Vox.position
    # if not raycast1.hit:
    #     print("SDw")     
    # else:                           
    #    print("dsad")
    if held_keys["left mouse"] or held_keys["right mouse"]:                 
        hand.active()                                                       
    else:                                                                   
        hand.passive()                                                                                                   
    if held_keys['1'] :                                                      
        block_pick = 1
    if held_keys['2'] :                                                                     #block texture changer(S)
        block_pick = 2
    if held_keys['3'] :
        block_pick = 3
    if held_keys['4'] :
        block_pick = 4
class Vox(Button):
    def __init__(self,position=(0,0,0),texture=grass_texture):                                                               
        super().__init__(
            parent=scene,
            position=position,
            model="block",                                                  #the cubes (M)
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),                 
            origin_y=0,
            #highlight_color=color.lime,
            scale=0.5
        )
    def input(self,key):
        # print(player.position)
        # if (player.position==(0,0,0)):
        #     print("hello")
        # else:
        #     print("bye")
        if key=="t":
           battery_but.color=color.yellow
           battery_but1.color=color.yellow
           resis2.color=color.red
           resis.color=color.red
           resis4.color=color.orange
           resis3.color=color.orange
           resis.position=(7,-0.7,13)
           resis2.position=(3,-0.7,13)
           resis3.position=(6,-9,14)
           resis4.position=(6,-9,11)
        #  generator_sound.play()
        if key=="i":
            battery_but.color=color.white
            battery_but1.color=color.white
            resis.color=color.light_gray
            resis2.color=color.light_gray
            resis4.color=color.light_gray
            resis3.color=color.light_gray
            resis.position=(7,2,13)
            resis2.position=(3,2,13)
            resis3.position=(6,-5,14)
            resis4.position=(6,-5,11)
        if self.hovered:
            if key=="left mouse down":                                           
                #voxel=Vox(position=self.position + mouse.normal) 
                punch_sound.play()  
                if block_pick==1:
                    voxel=Vox(position=self.position + mouse.normal , texture = grass_texture)
                if block_pick==2:
                    voxel=Vox(position=self.position + mouse.normal , texture = dirt_texture)   # block texture changer(S)
                if block_pick == 3:
                    voxel=Vox(position=self.position + mouse.normal , texture = stone_texture)
                if block_pick==4:
                    voxel=Vox(position=self.position + mouse.normal , texture = brick_texture)
            if key=="right mouse down":                                                                                 #destroy sound(S)
                punch_sound2.play()
                destroy(self)
                #################################
            if key=="l":
                self.on_click=Func(player.animate_position,                     
                self.position,
                duration=0.5,
                curve=curve.linear   
                      # the hook function(A)
                )
class lamp(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model = 'sphere',
            texture="sun_softer.png",  #the sun function(S)
            scale=5,
            double_sided=True,
            rotation=(260,-220,20),
            position=(0,-300,-300)
        )
class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model ='arm.blend',                         #hand function (M)
			texture = arm_texture,
			scale = 0.21,
			rotation = Vec3(320,-10,0),
            position = Vec2(0.4,-0.6)
            )
	def active(self):
		self.position = Vec2(0.3,-0.5)                 #hand when active(A)
	def passive(self):
		self.position = Vec2(0.4,-0.6)                  #hand when passive(N)
#________________________________________________________________________________
resis=Entity(model="resistance13.obj",position=(7,2,13),scale=0.4,color=color.light_gray)
resis2=Entity(model="resistance13.obj",position=(3,2,13),scale=0.4,color=color.light_gray)
resis3=Entity(model="resistance13.obj",position=(6,-5,14),scale=0.5,color=color.light_gray)
resis4=Entity(model="resistance13.obj",position=(6,-5,11),scale=0.5,color=color.light_gray)
resis.rotation_y =90
resis2.rotation_y=90
resis3.rotation_y=90
resis4.rotation_y = 90
Entity(model="battery2.obj",position=(14,2,8),scale=1.5,texture="battery222.png")
Entity(model="battery.obj",position=(14.8,-7,4.6),scale=4,texture="battery.png")
Entity(model="wire1.obj",position=(7,1,2),scale=4,color=color.orange)
Entity(model="wire2.obj",position=(1,1,9),scale=4,color=color.orange)
Entity(model="wire3.obj",position=(14,1,2),scale=4,color=color.orange)
Entity(model="wire4.obj",position=(14,1,13),scale=4,color=color.orange)
Entity(model="wire5.obj",position=(1,1,1.99),scale=4,color=color.orange)
######################################
Entity(model="wire1.obj",position=(7,-7,0.3),scale=4,color=color.red)
Entity(model="wire2.obj",position=(1,-7,7),scale=4,color=color.black)
Entity(model="wire3.obj",position=(14,-7,0.3),scale=4,color=color.red)
Entity(model="wire5.obj",position=(1,-7,0.3),scale=4,color=color.red)
Entity(model="wire6.obj",position=(0.97,-7,13),scale=4,color=color.red)
#################################################
Entity(model="Series_Connection.obj",position=(11,5,13),scale=0.5,color=color.blue)
Entity(model="Parallel_Connection.obj",position=(13,-5,13),scale=0.5,color=color.blue)
Entity(model="How_To_Play22",position=(12.5,26,40),scale=2,color=color.pink)
Entity(model="Hook22.obj",position=(12.5,60,12.5),scale=5,color=color.orange)
Entity(model="Destroy.obj",position=(12.5,18.5,15),scale=1.5,color=color.blue)
Entity(model="battery2.obj",position=(22,20,1),scale=1.5,rotation_y=90,texture="battery222.png")
Entity(model="battery.obj",position=(17,19,3),scale=4,texture="battery.png")
Entity(model="light.obj",position=(12,19,0),scale=1.5,color=color.yellow)
Entity(model="resistance13.obj",position=(2,21,0),rotation_y=90,scale=0.5,color=color.red)
Entity(model="series21_define.obj",position=(17,5,8),rotation_y=90,scale=0.5,color=color.red)
Entity(model="parallel21_define.obj",position=(-2,-4,8),rotation_y=-90,scale=0.5,color=color.red)
Entity(model="Resistance2332.obj",position=(2,25,0),scale=1.5,color=color.green)
Entity(model="Lightbulb2323.obj",position=(11,27,0),scale=1.5,color=color.green)
Entity(model="illustration32323.obj",position=(12,34,0),scale=1.5,color=color.green)
Entity(model="Battery2323.obj",position=(22,23,0),scale=1.5,color=color.green)
player=FirstPersonController(x=12 ,y=21, z=12)#,duration_y=5)         #the carachter controller
####################
for z in range(25):
    for x in range(25):
        voxel=Vox(position=(x,18,z),texture=stone_texture)
for z in range(17):
    for x in range(17):
        voxel=Vox(position=(x,0,z),texture=brick_texture)
for z in range(17):
    for x in range(17):
        voxel=Vox(position=(x,-8,z))
# for i in range(5):
#     voxel=Vox(position=(i,i,i))
voxel1=Vox(position=(1,1,7),texture=stone_texture)
voxe2=Vox(position=(1,-7,7),texture=stone_texture)
voxel=Vox(position=(10,1,13),texture=stone_texture)
voxel=Vox(position=(10,-7,13),texture=brick_texture)
voxel=Vox(position=(3,-7,13),texture=brick_texture)
# voxel=Vox(position=(21,2,8))
sky=Sky()
hand=Hand()
app.run()


