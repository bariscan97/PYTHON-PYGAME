import pygame
import os
import time
import random
pygame.init()

kafa=[pygame.image.load(os.path.join("SNAKE","head_down.png")),pygame.image.load(os.path.join("SNAKE","head_up.png")),pygame.image.load(os.path.join("SNAKE","head_right.png")),pygame.image.load(os.path.join("SNAKE","head_left.png"))]

beden=[pygame.image.load(os.path.join("SNAKE","body_horizontal.png")),pygame.image.load(os.path.join("SNAKE","body_vertical.png"))]
kuyruk=[pygame.image.load(os.path.join("SNAKE","tail_right.png")),pygame.image.load(os.path.join("SNAKE","tail_left.png")),pygame.image.load(os.path.join("SNAKE","tail_down.png")),pygame.image.load(os.path.join("SNAKE","tail_up.png"))]
dönüş=[pygame.image.load(os.path.join("SNAKE","body_bottomleft.png")),pygame.image.load(os.path.join("SNAKE","body_bottomright.png")),pygame.image.load(os.path.join("SNAKE","body_topleft.png")),pygame.image.load(os.path.join("SNAKE","body_topright.png"))]
elma=pygame.image.load(os.path.join("SNAKE","apple.png"))
ekran=pygame.display.set_mode((1520,800))
FPS=1
class kafal:
        def __init__(self,img,x,y):
                self.x=x
                self.y=y
                self.img=img
                self.direk="right"
                self.mask=pygame.mask.from_surface(self.img)
        def draw(self):
                ekran.blit(self.img,(self.x,self.y))
class bodys:
        def __init__(self,img,x,y):
                self.x=x
                self.y=y
                self.img=img
                self.direk="right"
                self.mask=pygame.mask.from_surface(self.img)
        def draw(self):
                ekran.blit(self.img,(self.x,self.y))



skore=1
direk="right"



class food:
        def __init__(self,img,x,y):
                self.x=x
                self.y=y
                self.img=img
                self.mask=pygame.mask.from_surface(self.img)
        def draw(self):
                ekran.blit(self.img,(self.x,self.y))

def coll(obj,obj1):
    x=obj1.x-obj.x
    y=obj1.y-obj.y
    return obj.mask.overlap(obj1.mask,(x,y))

lego=False
konum2=[120,200]
konum3=[80,200]
konum4=[100,220]
konum5=[100,180]
font = pygame.font.SysFont("comicsans", 50)
font1 = pygame.font.SysFont("comicsans", 100)
food1=food(elma,100,100)
konum=[100,200]
kafa1=kafal(beden[1],konum[0],konum[1])
clock=pygame.time.Clock()
run=True
kafalar=[kafa1]
es=2
kafa1.direk="right"
while   run: 
                heads=kafal(beden[0],konum[0],konum[1])
                bodys1=kafal(kafa[1],konum2[0],konum2[1])
                clock.tick(45)
                ekran.fill((0,255,0))      
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                                
                
                
                for i in kafalar:
                    if kafalar[0].x>800 or kafalar[0].y>800 or kafalar[0].y<0 or kafalar[0].x<0 :
                
                                          
                        if run:         
                                kafalar=[kafa1]
                                konum=[100,200]
                                konum2=[120,200]
                                konum3=[80,200]
                                konum4=[100,220]
                                konum5=[100,180]
                                kafa1.direk="right"
                                direk="right"
                                skore=0
                                
                                clock.tick(6)

                                
                                        
                        
                        
                lives_label = font.render(f"Puan: {skore}", 1, (255,255,255))
                lives_label1 = font1.render("YANDIN !!!!", 1, (255,255,255))
                keys=pygame.key.get_pressed()
                if keys[pygame.K_w] and not kafa1.direk=="down":
                        kafa1.direk="up"       
                        kafa1.img=beden[1]
                        
                        direk="up"
                if keys[pygame.K_s] and not kafa1.direk=="up":
                        
                        kafa1.img=beden[1]
                        kafa1.direk="down"
                        
                        direk="down"
                if keys[pygame.K_d] and not kafa1.direk =="left":
                        direk="right"
                        kafa1.img=beden[0]
                        kafa1.direk="right"
                        
                if keys[pygame.K_a] and not kafa1.direk=="right":
                        direk="left"
                        kafa1.img=beden[0]
                        kafa1.direk="left"
                        
                
                if direk=="right":
                    
                    heads.direk="right"
                    bodys1.img=kafa[2]
                    konum[0]+=8
                    konum2[0]+=8
                    konum3[0]+=8
                    konum4[0]+=8
                    konum5[0]+=8
                    heads=kafal(beden[0],konum[0],konum[1])
                    bodys1=kafal(kafa[2],konum2[0],konum2[1])
                if direk=="left":
                    
                    bodys1.img=kafa[3]
                    konum[0]-=8
                    konum2[0]-=8
                    konum3[0]-=8
                    konum4[0]-=8
                    konum5[0]-=8
                    heads.direk="left"
                    heads=kafal(beden[0],konum[0],konum[1])
                    bodys1=kafal(kafa[3],konum3[0],konum3[1])
                if direk=="down":
                    bodys1.img=kafa[0]
                    
                    konum[1]+=8
                    heads.direk="down"
                    konum2[1]+=8
                    konum3[1]+=8
                    konum4[1]+=8
                    konum5[1]+=8
                    heads=kafal(beden[1],konum[0],konum[1])
                    bodys1=kafal(kafa[0],konum4[0],konum4[1])
                if direk=="up":
                    
                    bodys1.img=kafa[1]
                    konum[1]-=8
                    konum2[1]-=8
                    konum3[1]-=8
                    konum4[1]-=8
                    konum5[1]-=8
                    heads.direk="up"
                    heads=kafal(beden[1],konum[0],konum[1])
                    bodys1=kafal(kafa[1],konum5[0],konum5[1])          
                
                
                
                kafalar.insert(0,heads)
                
                if coll(food1,heads):
                       
                        food1.x=random.randint(1,600)
                        food1.y=random.randint(1,600)
                        skore+=1
                else:
                     
                        kafalar.pop()
                        
                

                              
                for i in kafalar:
                    i.draw()
                
                bodys1.draw()
                food1.draw()
                ekran.blit(lives_label, (10, 10))
                

                     
                for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                
                if run:
                        pygame.display.update()
                              
                                

                
pygame.quit()
