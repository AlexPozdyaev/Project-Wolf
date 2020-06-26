import random
import pygame

pygame.init()

size = [400, 400] #Window size
screen = pygame.display.set_mode(size) #Creating window
pygame.display.set_caption("Wolf Game") #Window name

RED = (255, 0, 0) #RGB colours
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (111, 111, 111)
YELLOW = (225, 225, 0)
SKY = (0, 162, 232)
done = False
drop = 0

x1 = 5
y1 = 144
count1 = 0
x2 = 5
y2 = 244
count2 = 0
x3 = 395
y3 = 144
count3 = 0
x4 = 395
y4 = 244
count4 = 0
score = 0

x1_1 = 5
y1_1 = 144
count1_1 = 0
x2_1 = 5
y2_1 = 244
count2_1 = 0
x3_1 = 395
y3_1 = 144
count3_1 = 0
x4_1 = 395
y4_1 = 244
count4_1 = 0

bingo = 0
lifes = 3
A = ''
B = ''
speed = 1

nickname = ''

top1 = 'None'   #Scoreboard
top2 = 'None'
top3 = 'None'
top4 = 'None'
top5 = 'None'
top6 = 'None'
top7 = 'None'
top8 = 'None'
top9 = 'None'
top10 = 'None'
top11 = 'None'

score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
score7 = 0
score8 = 0
score9 = 0
score10 = 0
score11 = 0

m_top = [] * 20
i = 0

sb1 = ''
sb2 = ''
sb3 = ''
sb4 = ''
sb5 = ''
sb6 = ''
sb7 = ''
sb8 = ''
sb9 = ''
sb10 = ''

s1 = ''
s2 = ''
s3 = ''
s4 = ''
s5 = ''
s6 = ''
s7 = ''
s8 = ''
s9 = ''
s10 = ''

clock = pygame.time.Clock()

leftup_surf = pygame.image.load("up_left.bmp")                          #Wolf's positions
leftup_rect = leftup_surf.get_rect(bottomright = (400,400))

rightup_surf = pygame.image.load("up_right.bmp")
rightup_rect = rightup_surf.get_rect(bottomright = (400,400))

leftdown_surf = pygame.image.load("down_left.bmp")
leftdown_rect = leftdown_surf.get_rect(bottomright = (400,400))

rightdown_surf = pygame.image.load("down_right.bmp")
rightdown_rect = rightdown_surf.get_rect(bottomright = (400,400))

game_surf = pygame.image.load("game.bmp")
game_rect = game_surf.get_rect(bottomright = (400,400))

##penta_surf = pygame.image.load("penta.bmp")                       Easter egg (666)
##penta_rect = penta_surf.get_rect(bottomright = (400,400))         not complited

menu_surf = pygame.image.load("Menu.bmp")                           #main menu
menu_rect = menu_surf.get_rect(bottomright = (400,400))

screen.blit(menu_surf, menu_rect)
pygame.display.flip()

line = 20

#Скаты для яиц

#Волк

number = random.randrange(1,5)
number1 = random.randrange(1,5)
print(number)

bingo = 1

pygame.mixer.music.set_volume(0.2)

glass = pygame.mixer.Sound("Glass.wav")

n = 0
n1 = 0
n2 = 0

def menu():
    m_top[0] = top1
    m_top[1] = top2
    m_top[2] = top3
    m_top[3] = top4
    m_top[4] = top5
    m_top[5] = top6
    m_top[6] = top7
    m_top[7] = top8
    m_top[8] = top9
    m_top[9] = top10    


    m_top[10] = score1
    m_top[11] = score2
    m_top[12] = score3
    m_top[13] = score4
    m_top[14] = score5
    m_top[15] = score6
    m_top[16] = score7
    m_top[17] = score8
    m_top[18] = score9
    m_top[19] = score10

    print(m_top)

    i = 0

    f = open('Scoreboard.txt', 'w')
    while i < 20:
        print(i)
        f.write(str(m_top[i]) + '\n')
        i += 1
    f.close()
    global done
    done = False
    pygame.display.flip()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                print(mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_x >= 16 and mouse_x <= 385 and mouse_y >= 10 and mouse_y <= 77:
                    gameplay()
                if mouse_x >= 16 and mouse_x <= 385 and mouse_y >= 100 and mouse_y <= 167:
                    done = True
                    scoreboard()
                if mouse_x >= 18 and mouse_x <= 386 and mouse_y >= 190 and mouse_y <= 257:
                    done = True
                    control()
                if mouse_x >= 18 and mouse_x <= 386 and mouse_y >= 285 and mouse_y <= 352:
                    done = True
                    

def gameplay():
    
    global done
    global speed
    global y1
    global y2
    global y3
    global y4
    global score
    global number
    global x1
    global x2
    global x3
    global x4
    global count1
    global count2
    global count3
    global count4
    global lifes
    global bingo1
    global bingo2
    global bingo3
    global bingo4
    global bingo
    global n
    global n1
    global n2

    nick()

    screen.blit(leftup_surf, leftup_rect)
    pygame.display.flip()
    
    while not done:
##        pygame.mixer.music.set_endevent(REPLAY)
        
        pygame.display.flip() #Обновить окно

        clock.tick(speed)

        if y1 >= 199 or y1_1 >= 199:
            if bingo == 1:
                score += 1
            else:
                lifes -= 1

        if y2 >= 299 or y2_1 >= 299:
            if bingo == 2:
                score += 1
            else:
                lifes -= 1

        if y3 >= 199 or y3_1 >= 199:
            if bingo == 4:
                score += 1
            else:
                lifes -= 1

        if y4 >= 299 or y4_1 >= 299:
            if bingo == 3:
                score += 1

            else:
                lifes -= 1
        if score % 1 == 0 and score != 0:
            speed += 0.005

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    screen.blit(leftup_surf, leftup_rect)
                    bingo = 1
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    screen.blit(leftdown_surf, leftdown_rect)
                    bingo = 2
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    screen.blit(rightdown_surf, rightdown_rect)
                    bingo = 3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    screen.blit(rightup_surf, rightup_rect)
                    bingo = 4
#            if event.type == REPLAY:
#                pygame.mixer.music.play()
    ##    if score <= 10:
        if number == 1:
            pygame.draw.circle(screen, BLACK, [x1, y1], 5, 0)
            pygame.draw.circle(screen, SKY, [x1-10, y1-5], 5, 0)
            x1 += 10
            y1 += 5
            count1 += 1
            if count1 >= 12:

                #break
                x1 -= 10
                y1 += 5
                if y1 < 200:
                    pygame.draw.circle(screen, SKY, [x1, y1-10], 5, 0)
                    pygame.draw.circle(screen, BLACK, [x1, y1], 5, 0)
                elif y1 >= 200:
                    pygame.draw.circle(screen, SKY, [x1, y1-10], 5, 0)
                    x1 = 5
                    y1 = 144
                    count1 = 0
                    number = random.randrange(1,5)
                    print(number)
                    #break

        elif number == 2:
            pygame.draw.circle(screen, BLACK, [x2, y2], 5, 0)
            pygame.draw.circle(screen, SKY, [x2-10, y2-5], 5, 0)
            x2 += 10
            y2 += 5
            count2 += 1
            if count2 >= 12:
                #break
                x2 -= 10
                y2 += 5
                if y2 < 300:
                    pygame.draw.circle(screen, SKY, [x2, y2-10], 5, 0)
                    pygame.draw.circle(screen, BLACK, [x2, y2], 5, 0)
                elif y2 >= 300:
                    pygame.draw.circle(screen, SKY, [x2, y2-10], 5, 0)
                    x2 = 5
                    y2 = 244
                    count2 = 0
                    number = random.randrange(1,5)
                    print(number)
                    #break


        elif number == 3:
            pygame.draw.circle(screen, BLACK, [x3, y3], 5, 0)
            pygame.draw.circle(screen, SKY, [x3+10, y3-5], 5, 0)
            x3 -= 10
            y3 += 5
            count3 += 1
            if count3 >= 12:
                #break
                x3 += 10
                y3 += 5
                if y3 < 200:
                    pygame.draw.circle(screen, SKY, [x3, y3-10], 5, 0)
                    pygame.draw.circle(screen, BLACK, [x3, y3], 5, 0)
                elif y3 >= 200:
                    pygame.draw.circle(screen, SKY, [x3, y3-10], 5, 0)
                    x3 = 395
                    y3 = 144
                    count3 = 0
                    number = random.randrange(1,5)
                    print(number)
                    #break


        elif number == 4:
            pygame.draw.circle(screen, BLACK, [x4, y4], 5, 0)
            pygame.draw.circle(screen, SKY, [x4+10, y4-5], 5, 0)
            x4 -= 10
            y4 += 5
            count4 += 1
            if count4 >= 12:
                #break
                x4 += 10
                y4 += 5
                if y4 < 300:
                    pygame.draw.circle(screen, SKY, [x4, y4-10], 5, 0)
                    pygame.draw.circle(screen, BLACK, [x4, y4], 5, 0)
                elif y4 >= 300:
                    pygame.draw.circle(screen, SKY, [x4, y4-10], 5, 0)
                    x4 = 395
                    y4 = 244
                    count4 = 0
                    number = random.randrange(1,5)
                    print(number)


        A = 'Your score: ' + str(score)
        pygame.draw.rect(screen, WHITE, [20, 50, 110, 15], 0)
        font = pygame.font.Font(None, 22)
        text = font.render(A, True, BLACK)
        screen.blit(text, [20, 50])

        B = 'Lifes: '
        pygame.draw.rect(screen, WHITE, [290, 45, 93, 20], 0)
        font = pygame.font.Font(None, 22)
        text = font.render(B, True, BLACK)
        screen.blit(text, [290, 50])

        if score == 200 or score == 500:
            lifes = 3

        if lifes == 3:
            pygame.draw.circle(screen, BLACK, [375, 55], 8, 0)
            pygame.draw.circle(screen, BLACK, [357, 55], 8, 0)
            pygame.draw.circle(screen, BLACK, [339, 55], 8, 0)
        elif lifes == 2:
            if n == 0:
                glass.play()
            n += 1
            pygame.draw.circle(screen, BLACK, [357, 55], 8, 0)
            pygame.draw.circle(screen, BLACK, [339, 55], 8, 0)
        elif lifes == 1:
            if n1 == 0:
                glass.play(0)
            n1 += 1
            pygame.draw.circle(screen, BLACK, [339, 55], 8, 0)
        elif lifes == 0:
            if n2 == 0:
                glass.play(0)
            n2 += 1
        elif lifes < 0:
            if score == 666:
                screen.blit(penta_surf, penta_rect)
            else:
                screen.blit(game_surf, game_rect)
##            pygame.mixer.music.load("End.mp3")
##            pygame.mixer.music.play()
            pygame.display.flip()
            done = True

    top()
    done = False
    lifes = 3
    speed = 1
    screen.blit(menu_surf, menu_rect)
    menu()


def nick():
    global nickname
    nick_surf = pygame.image.load("Nick.bmp")
    nick_rect = nick_surf.get_rect(bottomright = (400,400))
    screen.blit(nick_surf, nick_rect)
    pygame.display.flip()
    nickname = str(input())
    print(nickname)
    top11 = nickname
    leftup_surf = pygame.image.load("верх_лево.bmp")
    leftup_rect = leftup_surf.get_rect(bottomright = (400,400))
    screen.blit(leftup_surf, leftup_rect)
    pygame.display.flip()
    print(top11)

def music():
    pygame.mixer.music.load("Popcorn.mp3")
    pygame.mixer.music.play(loops =- 1)

def top():
    global score
    global score1
    global score2
    global score3
    global score4
    global score5
    global score6
    global score7
    global score8
    global score9
    global score10
    global score11
    global nickname
    global top1
    global top2
    global top3
    global top4
    global top5
    global top6
    global top7
    global top8
    global top9
    global top10
    global top11
    
    print(1234567890)
    score11 = score
    top11 = nickname

    i = 0

    if top11 == top10:
        if score11 > score1:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score10 = score9
                score9 = score8
                score8 = score7
                score7 = score6
                score6 = score5
                score5 = score4
                score4 = score3
                score3 = score2
                score2 = score11

                top10 = top9
                top9 = top8
                top8 = top7
                top7 = top6
                top6 = top5
                top5 = top4
                top4 = top3
                top3 = top2
                top2 = top11
            else:
                if score11 > score3:
                    score10 = score9
                    score9 = score8
                    score8 = score7
                    score7 = score6
                    score6 = score5
                    score5 = score4
                    score4 = score3
                    score3 = score11

                    top10 = top9
                    top9 = top8
                    top8 = top7
                    top7 = top6
                    top6 = top5
                    top5 = top4
                    top4 = top3
                    top3 = top11
                else:
                    if score11 > score4:
                        score10 = score9
                        score9 = score8
                        score8 = score7
                        score7 = score6
                        score6 = score5
                        score5 = score4
                        score4 = score11

                        top10 = top9
                        top9 = top8
                        top8 = top7
                        top7 = top6
                        top6 = top5
                        top5 = top4
                        top4 = top11
                    else:
                        if score11 > score5:
                            score10 = score9
                            score9 = score8
                            score8 = score7
                            score7 = score6
                            score6 = score5
                            score5 = score11

                            top10 = top9
                            top9 = top8
                            top8 = top7
                            top7 = top6
                            top6 = top5
                            top5 = top11                            
                        else:
                            if score11 > score6:
                                score10 = score9
                                score9 = score8
                                score8 = score7
                                score7 = score6
                                score6 = score11

                                top10 = top9
                                top9 = top8
                                top8 = top7
                                top7 = top6
                                top6 = top11
                            else:
                                if score11 > score7:
                                    score10 = score9
                                    score9 = score8
                                    score8 = score7
                                    score7 = score11
                                        
                                    top10 = top9
                                    top9 = top8
                                    top8 = top7
                                    top7 = top11
                                else:
                                    if score11 > score8:
                                        score10 = score9
                                        score9 = score8
                                        score8 = score11
                                                                                    
                                        top10 = top9
                                        top9 = top8
                                        top8 = top11
                                    else:
                                        if score11 > score9:
                                            score10 = score9
                                            score9 = score11
                                                                                                                                    
                                            top10 = top9
                                            top9 = top11

    
    if top11 == top9:
        if score11 > score1:
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score9 = score8
                score8 = score7
                score7 = score6
                score6 = score5
                score5 = score4
                score4 = score3
                score3 = score2
                score2 = score11

                top9 = top8
                top8 = top7
                top7 = top6
                top6 = top5
                top5 = top4
                top4 = top3
                top3 = top2
                top2 = top11
            else:
                if score11 > score3:
                    score9 = score8
                    score8 = score7
                    score7 = score6
                    score6 = score5
                    score5 = score4
                    score4 = score3
                    score3 = score11

                    top9 = top8
                    top8 = top7
                    top7 = top6
                    top6 = top5
                    top5 = top4
                    top4 = top3
                    top3 = top11
                else:
                    if score11 > score4:
                        score9 = score8
                        score8 = score7
                        score7 = score6
                        score6 = score5
                        score5 = score4
                        score4 = score11

                        top9 = top8
                        top8 = top7
                        top7 = top6
                        top6 = top5
                        top5 = top4
                        top4 = top11
                    else:
                        if score11 > score5:
                            score9 = score8
                            score8 = score7
                            score7 = score6
                            score6 = score5
                            score5 = score11

                            top9 = top8
                            top8 = top7
                            top7 = top6
                            top6 = top5
                            top5 = top11                            
                        else:
                            if score11 > score6:
                                score9 = score8
                                score8 = score7
                                score7 = score6
                                score6 = score11

                                top9 = top8
                                top8 = top7
                                top7 = top6
                                top6 = top11
                            else:
                                if score11 > score7:
                                    score9 = score8
                                    score8 = score7
                                    score7 = score11
                                        
                                    top9 = top8
                                    top8 = top7
                                    top7 = top11
                                else:
                                    if score11 > score8:
                                        score9 = score8
                                        score8 = score11
                                                   
                                        top9 = top8
                                        top8 = top11
    
    if top11 == top8:
        if score11 > score1:
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score8 = score7
                score7 = score6
                score6 = score5
                score5 = score4
                score4 = score3
                score3 = score2
                score2 = score11

                top8 = top7
                top7 = top6
                top6 = top5
                top5 = top4
                top4 = top3
                top3 = top2
                top2 = top11
            else:
                if score11 > score3:
                    score8 = score7
                    score7 = score6
                    score6 = score5
                    score5 = score4
                    score4 = score3
                    score3 = score11

                    top8 = top7
                    top7 = top6
                    top6 = top5
                    top5 = top4
                    top4 = top3
                    top3 = top11
                else:
                    if score11 > score4:
                        score8 = score7
                        score7 = score6
                        score6 = score5
                        score5 = score4
                        score4 = score11

                        top8 = top7
                        top7 = top6
                        top6 = top5
                        top5 = top4
                        top4 = top11
                    else:
                        if score11 > score5:
                            score8 = score7
                            score7 = score6
                            score6 = score5
                            score5 = score11

                            top8 = top7
                            top7 = top6
                            top6 = top5
                            top5 = top11                            
                        else:
                            if score11 > score6:
                                score8 = score7
                                score7 = score6
                                score6 = score11

                                top8 = top7
                                top7 = top6
                                top6 = top11
                            else:
                                if score11 > score7:
                                    score8 = score7
                                    score7 = score11
                                        
                                    top8 = top7
                                    top7 = top11

    if top11 == top7:
        if score11 > score1:
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score7 = score6
                score6 = score5
                score5 = score4
                score4 = score3
                score3 = score2
                score2 = score11

                top7 = top6
                top6 = top5
                top5 = top4
                top4 = top3
                top3 = top2
                top2 = top11
            else:
                if score11 > score3:
                    score7 = score6
                    score6 = score5
                    score5 = score4
                    score4 = score3
                    score3 = score11

                    top7 = top6
                    top6 = top5
                    top5 = top4
                    top4 = top3
                    top3 = top11
                else:
                    if score11 > score4:
                        score7 = score6
                        score6 = score5
                        score5 = score4
                        score4 = score11

                        top7 = top6
                        top6 = top5
                        top5 = top4
                        top4 = top11
                    else:
                        if score11 > score5:
                            score7 = score6
                            score6 = score5
                            score5 = score11

                            top7 = top6
                            top6 = top5
                            top5 = top11                            
                        else:
                            if score11 > score6:
                                score7 = score6
                                score6 = score11

                                top7 = top6
                                top6 = top11

    if top11 == top6:
        if score11 > score1:
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score6 = score5
                score5 = score4
                score4 = score3
                score3 = score2
                score2 = score11

                top6 = top5
                top5 = top4
                top4 = top3
                top3 = top2
                top2 = top11
            else:
                if score11 > score3:
                    score6 = score5
                    score5 = score4
                    score4 = score3
                    score3 = score11

                    top6 = top5
                    top5 = top4
                    top4 = top3
                    top3 = top11
                else:
                    if score11 > score4:
                        score6 = score5
                        score5 = score4
                        score4 = score11

                        top6 = top5
                        top5 = top4
                        top4 = top11
                    else:
                        if score11 > score5:
                            score6 = score5
                            score5 = score11

                            top6 = top5
                            top5 = top11                            


    if top11 == top5:
        if score11 > score1:
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score5 = score4
                score4 = score3
                score3 = score2
                score2 = score11

                top5 = top4
                top4 = top3
                top3 = top2
                top2 = top11
            else:
                if score11 > score3:
                    score5 = score4
                    score4 = score3
                    score3 = score11

                    top5 = top4
                    top4 = top3
                    top3 = top11
                else:
                    if score11 > score4:
                        score5 = score4
                        score4 = score11

                        top5 = top4
                        top4 = top11

    if top11 == top4:
        if score11 > score1:
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score4 = score3
                score3 = score2
                score2 = score11

                top4 = top3
                top3 = top2
                top2 = top11
            else:
                if score11 > score3:
                    score4 = score3
                    score3 = score11

                    top4 = top3
                    top3 = top11

    if top11 == top3:
        if score11 > score1:
            score3 = score2
            score2 = score1
            score1 = score11

            top3 = top2
            top2 = top1
            top1 = top11
        else:            
            if score11 > score2:
                score3 = score2
                score2 = score11

                top3 = top2
                top2 = top11

    if top11 == top2:
        if score11 > score1:
            score2 = score1
            score1 = score11

            top2 = top1
            top1 = top11

    if top11 == top1:
        if score11 > score1:
            score1 = score11
    else:
        if score11 > score1:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score1
            score1 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top1
            top1 = top11
            

        elif score11 > score2:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score2
            score2 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top2
            top2 = top11


        elif score11 > score3:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score3
            score3 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top3
            top3 = top11

            
        elif score11 > score4:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score4
            score4 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top4
            top4 = top11


        elif score11 > score5:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score5
            score5 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top5
            top5 = top11

        elif score11 > score6:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score6
            score6 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top6
            top6 = top11
            

        elif score11 > score7:
            score10 = score9
            score9 = score8
            score8 = score7
            score7 = score11

            top10 = top9
            top9 = top8
            top8 = top7
            top7 = top11

                
        elif score11 > score8:
            score10 = score9
            score9 = score8
            score8 = score11

            top10 = top9
            top9 = top8
            top8 = top11

            
        elif score11 > score9:
            score10 = score9
            score9 = score11

            top10 = top9
            top9 = top11
            
        elif score11 > score10:
            score10 = score11

            top10 = top11
            
                
    score = 0
                    
def scoreboard():
    global done
    done = False
    
    scoreboard_surf = pygame.image.load("Scoreboard.bmp")
    scoreboard_rect = scoreboard_surf.get_rect(bottomright = (400,400))
    screen.blit(scoreboard_surf, scoreboard_rect)

    sb1 = top1
    s1 = str(score1)
    font = pygame.font.Font(None, 30)
    psb1 = font.render(sb1, True, WHITE)
    ps1 = font.render(s1, True, WHITE)
    screen.blit(psb1, [70, 87])
    screen.blit(ps1, [285, 87])
    
    sb2 = top2
    s2 = str(score2)
    font = pygame.font.Font(None, 30)
    psb2 = font.render(sb2, True, WHITE)
    ps2 = font.render(s2, True, WHITE)
    screen.blit(psb2, [70, 117])
    screen.blit(ps2, [285, 117])

    sb3 = top3
    s3 = str(score3)
    font = pygame.font.Font(None, 30)
    psb3 = font.render(sb3, True, WHITE)
    ps3 = font.render(s3, True, WHITE)
    screen.blit(psb3, [70, 147])
    screen.blit(ps3, [285, 147])

    sb4 = top4
    s4 = str(score4)
    font = pygame.font.Font(None, 30)
    psb4 = font.render(sb4, True, WHITE)
    ps4 = font.render(s4, True, WHITE)
    screen.blit(psb4, [70, 177])
    screen.blit(ps4, [285, 177])

    sb5 = top5
    s5 = str(score5)
    font = pygame.font.Font(None, 30)
    psb5 = font.render(sb5, True, WHITE)
    ps5 = font.render(s5, True, WHITE)
    screen.blit(psb5, [70, 207])
    screen.blit(ps5, [285, 207])

    sb6 = top6
    s6 = str(score6)
    font = pygame.font.Font(None, 30)
    psb6 = font.render(sb6, True, WHITE)
    ps6 = font.render(s6, True, WHITE)
    screen.blit(psb6, [70, 237])
    screen.blit(ps6, [285, 237])

    sb7 = top7
    s7 = str(score7)
    font = pygame.font.Font(None, 30)
    psb7 = font.render(sb7, True, WHITE)
    ps7 = font.render(s7, True, WHITE)
    screen.blit(psb7, [70, 267])
    screen.blit(ps7, [285, 267])

    sb8 = top8
    s8 = str(score8)
    font = pygame.font.Font(None, 30)
    psb8 = font.render(sb8, True, WHITE)
    ps8 = font.render(s8, True, WHITE)
    screen.blit(psb8, [70, 297])
    screen.blit(ps8, [285, 297])

    sb9 = top9
    s9 = str(score9)
    font = pygame.font.Font(None, 30)
    psb9 = font.render(sb9, True, WHITE)
    ps9 = font.render(s9, True, WHITE)
    screen.blit(psb9, [70, 327])
    screen.blit(ps9, [285, 327])

    sb10 = top10
    s10 = str(score10)
    font = pygame.font.Font(None, 30)
    psb10 = font.render(sb10, True, WHITE)
    ps10 = font.render(s10, True, WHITE)
    screen.blit(psb10, [70, 357])
    screen.blit(ps10, [285, 357])

    pygame.display.flip()
    
    while not done:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    menu_surf = pygame.image.load("Menu.bmp")
                    menu_rect = menu_surf.get_rect(bottomright = (400,400))
                    screen.blit(menu_surf, menu_rect)
                    pygame.display.flip()
                    done = True
                    menu()
                    
##        print(1)
        



       
def control():
    global done
    done = False
    
    ctrl_surf = pygame.image.load("control.bmp")
    ctrl_rect = ctrl_surf.get_rect(bottomright = (400,400))
    screen.blit(ctrl_surf, ctrl_rect)
    pygame.display.flip()
    while not done:
        
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    menu_surf = pygame.image.load("Menu.bmp")
                    menu_rect = menu_surf.get_rect(bottomright = (400,400))
                    screen.blit(menu_surf, menu_rect)
                    pygame.display.flip()
                    done = True
                    menu()
                    

def file_b():
    global i
    f = open('scoreboard.txt')
    for line in f:
        # top11 = line
        m_top.append(line.strip())
    print(m_top)
    f.close()

file_b()

top1 = m_top[0]
top2 = m_top[1]
top3 = m_top[2]
top4 = m_top[3]
top5 = m_top[4]
top6 = m_top[5]
top7 = m_top[6]
top8 = m_top[7]
top9 = m_top[8]
top10 = m_top[9]    
top11 = 'None'

score1 = int(m_top[10])
score2 = int(m_top[11])
score3 = int(m_top[12])
score4 = int(m_top[13])
score5 = int(m_top[14])
score6 = int(m_top[15])
score7 = int(m_top[16])
score8 = int(m_top[17])
score9 = int(m_top[18])
score10 = int(m_top[19])
score11 = 0

music()
menu()

m_top[0] = top1
m_top[1] = top2
m_top[2] = top3
m_top[3] = top4
m_top[4] = top5
m_top[5] = top6
m_top[6] = top7
m_top[7] = top8
m_top[8] = top9
m_top[9] = top10    


m_top[10] = score1
m_top[11] = score2
m_top[12] = score3
m_top[13] = score4
m_top[14] = score5
m_top[15] = score6
m_top[16] = score7
m_top[17] = score8
m_top[18] = score9
m_top[19] = score10

print(m_top)

i = 0

f = open('Scoreboard.txt', 'w')
while i < 20:
    print(i)
    f.write(str(m_top[i]) + '\n')
    i += 1
f.close()
pygame.quit()
