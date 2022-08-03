import pygame, math

pygame.init()
size = [600,600] 
width, height = size
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Trigonometry")
#Fonts
font = pygame.font.SysFont(None, 24)
fontSurface = font.render('Sin:', True, (255,255,255))
fontSurface2 = font.render('Cos:', True, (255,255,255))
diaFont = font.render("Periodo:", True, (255,255,255))
periodoFont = font.render("Noite", True, (255,255,255))
credits = font.render("Facebook: CgStuffStudios :)", True, (255,255,255))
#Objects
imagens = (pygame.image.load("./Assets/Earth.png"), \
            pygame.image.load("./Assets/Moon.png"))
imagens[1].convert()            
imagens[0].convert()


quads = (imagens[0].get_rect(), imagens[1].get_rect())     
quads[0].center = width/2, height/2
quads[1].center = width/2 , height/2 
#ConifValues
vel = 1
dia = True
running = True
counter = 0

while running:
    #Draw the objects into the screen
    screen.fill((0,0,0))    
    pygame.draw.circle(screen,(255,255,255), (width/2, height/2), 210, 2)
    screen.blit(imagens[0],quads[0])
    screen.blit(imagens[1], quads[1])
    screen.blit(fontSurface, (20,20))
    screen.blit(fontSurface2, (20,40))
    screen.blit(diaFont, (20,60))
    screen.blit(periodoFont, (90,60))
    screen.blit(credits, (20, height -50))
    
    #Control the fps(it's a trick:) ))
    counter += 1
    if counter > 3:   

        cos = math.cos(math.radians(vel))
        sin = math.sin(math.radians(vel))

        quads[1].centerx  = width/2 + cos * 200
        quads[1].centery  = height/2 + sin * 200
        #Get the text objects
        fontSurface = font.render(f'Sin:{round(sin,3)}', True, (255,255,255) )
        fontSurface2 = font.render(f'Cos:{round(cos,3)}', True, (255,255,255) )
        #Day passed
        vel = vel+1 if vel < 360 else 0
        if vel == 360: 
            #print(vel)
            dia = not dia
            periodoFont =   font.render("Noite", True,(255,255,255)) if dia \
                            else font.render("Dia", True,(255,255,0))
        counter = 0

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
