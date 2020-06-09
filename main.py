import pygame,sys
import time
import random
import time

ancho=900
largo=900

class Enemie():
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load("/billete.png")
        
        self.image = pygame.transform.scale(self.image1,(50,25))
        self.rect=self.image.get_rect()
        self.speed=0.5  
        self.rect.top=posy
        self.rect.left=posx
        x=random.randint(-4,4)
        if x==0 : x=2
        y=random.randint(2,7)
        self.pendy=y
        self.pendx=x
     
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    
    

    def trayectoria(self):
        self.rect.top=self.rect.top+self.speed*self.pendy
        self.rect.left=self.rect.left+self.speed*self.pendx
    
    def crash(self,shot):
        return self.rect.colliderect(shot)

class Journey(pygame.sprite.Sprite):

    def __init__(self):
        self.point=0
        self.enemies=[]
        self.maxenemi=8


    def createEnemies(self):
        if self.maxenemi>=0:
            self.maxenemi-=1
            x=random.randint(0, largo )       
            enemie=Enemie(x,10)
            self.enemies.append(enemie)

    
        
  




class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image1,(300,300))
        self.rect=self.image.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=largo-50
        self.speed=83
        self.shots=[]
        self.life=10

    def draw(self,screen):
        screen.blit(self.image, self.rect)
        
    def trayectoria(self):
        self.rect.top
    
    def shot(self,x,y):
        shot=Bullet(x,y)
        self.shots.append(shot)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image1,(25,25))
        self.rect=self.image.get_rect()
        self.speed=20     
        self.rect.top=posy
        self.rect.left=posx
        self.remove=False

    def trayectoria(self):
        self.rect.top=self.rect.top-self.speed

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def crash(self,enemie):
            return self.rect.colliderect(enemie)

def main():       
    #from naves import Player 

    # Inicializamos pygame
    pygame.init()
    # Muestro una ventana de 800x
    size = 900,900
    screen = pygame.display.set_mode(size)
    # Cambio el título de la ventana
    pygame.display.set_caption("prueba")
    # Comenzamos el bucle del juego
 
    #billetico=pygame.transform.scale(billete,(100,50))
    posx=250
    posy=600
    speed=100
    fuente = pygame.font.Font(None,40)
    texto = fuente.render('Prueba', 1, (255,255, 255))
    screen.blit(texto, (10, 10))
    run=True
    player=Nave()
    journey=Journey()
    time=0
    boo=False
    mun=50 
    while run:          
        screen.fill((20,36,50))
        texto = fuente.render(str(journey.point), 1, (255,255, 255))
        screen.blit(texto,(790,10))
        texto2 = fuente.render(str(player.life), 1, (255,255, 255))
        screen.blit(texto2,(10,10))
        journey.point+=1
        time+=1
        if (time ==10) :
            journey.createEnemies()
            time=2
            boo=True
        # Capturamos los eventos que se han producido
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                run=False
            
            elif event.type==pygame.KEYDOWN:
                #derecha e izquierda
                if event.key==pygame.K_LEFT:
                    player.rect.centerx-=player.speed
                    
                
                elif event.key==pygame.K_RIGHT:
                    player.rect.centerx+=player.speed

                elif event.key==pygame.K_UP:
                   player.rect.centery-=player.speed

                elif event.key==pygame.K_DOWN:
                    player.rect.centery+=player.speed
               
                elif event.key==pygame.K_SPACE :  
                   
                    x,y=player.rect.center
                    player.shot(x,y)
               
                  
        player.draw(screen) 

        if len(player.shots)>0:
            for shot in player.shots:
                shot.draw(screen)
                shot.trayectoria()

                if shot.rect.top<-5:
                    player.shots.remove(shot)                
                

        if boo:
            for enemie in journey.enemies:
                enemie.draw(screen)
                enemie.trayectoria()
                if enemie.rect.top>=900 or enemie.rect.left>=900:
                    journey.enemies.remove(enemie)
                    journey.maxenemi+=1
                for shot in player.shots:
                   if shot.crash(enemie) and shot.rect.top>-10:
                        journey.maxenemi+=1
                        journey.enemies.remove(enemie)
                        player.shots.remove(shot)
                if enemie.crash(player):
                    journey.maxenemi+=1
                    player.life-=1
                    journey.enemies.remove(enemie) 
                

                      
                        
                      
                      
                       


                                   
                    
        
        if player.life<=0:
           
            screen.fill((0,0,0))
            texto = fuente.render("Perdiste Veneco", 1, (255,255, 255))
            
            time.sleep(5)
            screen.blit(texto,(790,10))
            run=False




        pygame.display.update()
    # Salgo de pygame
    pygame.quit()


if __name__ == "__main__":
    main()