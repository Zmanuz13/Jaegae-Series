#Inizio progetti Jaegae (재개),che segnano la ripresa della programmazione,e più precisamente la programmazione con Python
#A seguito della serie Shibal (시발),i primi progetti sperimentali,e della serie Mirae (미래),la serie di progetti nata con l'intento di iniziare a programmare seriamente,nasce Jaegae (재개)
#Introduzione a Jaegae (재개):Questa serie di progetti segnà il mio nuovo inizio con la programmazione,dopo circa 2/3 mesi di pausa.
#Jaegae (재개) V2
#Primo programma ripresa,BAEM(뱀),gioco snake.
import pygame
import random as rd
pygame.init()
screen=pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
running = True
baem=pygame.draw.rect(screen, (157, 255, 20), pygame.Rect(25,25,25,25))
baem.x=150
baem.y=250
snake = [baem]
dx=25
dy=0
sagwa=pygame.draw.rect(screen, (157, 255, 20), pygame.Rect(25,25,25,25))
game_over=False
win=False
score=0
font = pygame.font.Font(None, 36)
testo_game_over = font.render("GAME OVER", True, (255, 0, 0))
testo_vittoria = font.render("VITTORIA", True, (255, 215, 0))
testo_restart = font.render("Premi SPAZIO per Rigiocare", True, (255, 255, 255))
def posiziona_sagwa():
    sagwa.x=rd.randint(0,19)*25
    sagwa.y=rd.randint(0,19)*25
    return sagwa
posiziona_sagwa()
while running:
    if score == 399:
        win = True
        game_over = True
    screen.fill((0, 0, 0))
    testo_score = font.render(f"Score: {score}/399", True, (255, 255, 255))
    clock.tick(5)
    pygame.draw.rect(screen, (255, 0, 0), sagwa)
    if game_over and not win:
        screen.blit(testo_game_over, (175, 150))
        screen.blit(testo_restart, (100, 185))
    if win and game_over:
        screen.blit(testo_vittoria, (175, 150))
        screen.blit(testo_restart, (100, 185))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            snake = [pygame.Rect(150, 250, 25, 25)]
            dx = 25
            dy = 0
            score = 0
            posiziona_sagwa()
            win = False
            game_over = False
        elif not game_over:

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP and dy!=25 or event.key == pygame.K_w and dy!=25:
                    dy = -25
                    dx=0
                if event.key == pygame.K_DOWN and dy!=-25 or event.key == pygame.K_s and dy!=-25:
                    dy = +25
                    dx=0
                if event.key == pygame.K_LEFT and dx!=25 or event.key == pygame.K_a and dx!=25:
                    dx = -25
                    dy=0
                if event.key == pygame.K_RIGHT and dx!=-25 or event.key == pygame.K_d and dx!=-25:
                    dx = +25
                    dy=0

    if not game_over:
        sae_meori = snake[0].copy()
        sae_meori.x += dx
        sae_meori.y += dy
        snake.insert(0, sae_meori)
        if snake[0].colliderect(sagwa):
            sagwa=posiziona_sagwa()
            score+=1
        else:
            snake.pop()
        if snake[0].x > 475 or snake[0].x < 0 or snake[0].y > 475 or snake[0].y < 0 or snake[0] in snake[1:]:
            game_over = True

    for goyangi in snake:
        pygame.draw.rect(screen, (157, 255, 20),goyangi)
    screen.blit(testo_score, (330, 0))
    pygame.display.flip()





