import pygame

pygame.init()

screen = pygame.display.set_mode((320, 470))

color = (88, 89, 90)

color_light = (208, 0, 147)

color_text = (255, 255, 255)

color_dark = (174, 0, 255)

width = 500
height = 500

color_blue = (85, 182, 217)
color_orange = (255, 110, 63)
color_red = (255, 0, 0)

screen.fill((50, 50, 50))

smallfont = pygame.font.Font('Moderat-Black.ttf', 35)

text1 = smallfont.render('0', True, color_text)
text2 = smallfont.render('.', True, color_text)
text3 = smallfont.render('=', True, color_text)
text4 = smallfont.render('/', True, color_text)
text5 = smallfont.render('1', True, color_text)
text6 = smallfont.render('2', True, color_text)
text7 = smallfont.render('3', True, color_text)
text8 = smallfont.render('x', True, color_text)
text9 = smallfont.render('4', True, color_text)
text10 = smallfont.render('5', True, color_text)
text11 = smallfont.render('6', True, color_text)
text12 = smallfont.render('-', True, color_text)
text13 = smallfont.render('7', True, color_text)
text14 = smallfont.render('8', True, color_text)
text15 = smallfont.render('9', True, color_text)
text16 = smallfont.render('+', True, color_text)
textclear = smallfont.render('Clear', True, color_text)

calcScreen = pygame.draw.rect(screen, color, [20, 20, 280, 75])

# First Row Buttons
button7 = pygame.draw.rect(screen, color, [20, 120, 60, 50])
button8 = pygame.draw.rect(screen, color, [94, 120, 60, 50])
button9 = pygame.draw.rect(screen, color, [167.5, 120, 60, 50])
buttonAddition = pygame.draw.rect(screen, color_orange, [240, 120, 60, 50])

# Second Row Buttons
button4 = pygame.draw.rect(screen, color, [20, 190, 60, 50])
button5 = pygame.draw.rect(screen, color, [94, 190, 60, 50])
button6 = pygame.draw.rect(screen, color, [167.5, 190, 60, 50])
buttonSubtraction = pygame.draw.rect(screen, color_orange, [240, 190, 60, 50])

# Third Row Buttons
button1 = pygame.draw.rect(screen, color, [20, 260, 60, 50])
button2 = pygame.draw.rect(screen, color, [94, 260, 60, 50])
button3 = pygame.draw.rect(screen, color, [167.5, 260, 60, 50])
buttonMultiply = pygame.draw.rect(screen, color_orange, [240, 260, 60, 50])

# Fourth Row Buttons
button0 = pygame.draw.rect(screen, color, [20, 330, 60, 50])
buttonDecimal = pygame.draw.rect(screen, color_blue, [94, 330, 60, 50])
buttonEqual = pygame.draw.rect(screen, color_blue, [167.5, 330, 60, 50])
buttonDivide = pygame.draw.rect(screen, color_orange, [240, 330, 60, 50])

# Clear Button
buttonClear = pygame.draw.rect(screen, color_red, [20, 400, 282, 50])

#First Row Text
screen.blit(text1, (20 + 20, 330 + 3))
screen.blit(text2, (100 + 20, 330 + 3))
screen.blit(text3, (167.5 + 20, 330 + 3))
screen.blit(text4, (240 + 20, 330 + 3))

#Second Row Text
screen.blit(text5, (20 + 20, 260 + 3))
screen.blit(text6, (94 + 20, 260 + 3))
screen.blit(text7, (167.5 + 20, 260 + 3))
screen.blit(text8, (240 + 20, 260 + 3))

#Third Row Text
screen.blit(text9, (20 + 20, 190 + 3))
screen.blit(text10, (94 + 20, 190 + 3))
screen.blit(text11, (167.5 + 20, 190 + 3))
screen.blit(text12, (240 + 20, 190 + 3))

#Fourth Row Text
screen.blit(text13, (20 + 20, 120 + 3))
screen.blit(text14, (94 + 20, 120 + 3))
screen.blit(text15, (167.5 + 20, 120 + 3))
screen.blit(text16, (240 + 20, 120 + 3))

#Clear Text
screen.blit(textclear, (20 + 95, 282 + 120))

# GAME LOOP

answer = ""
blank = ""

while True:

    textanswer = smallfont.render(answer, True, color_text)
    screen.blit(textanswer, (20 + 15, 33 + 3))

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if 20 <= mouse[0] <= 80 and 120 <= mouse[1] <= 170:
                answer+="7"
            elif 94 <= mouse[0] <= 154 and 120 <= mouse[1] <= 170:
                answer += "8"
            elif 167.5 <= mouse[0] <= 227.5 and 120 <= mouse[1] <= 170:
                answer += "9"
            elif 240 <= mouse[0] <= 300 and 120 <= mouse[1] <= 170:
                answer += "+"
            elif 20 <= mouse[0] <= 80 and 190 <= mouse[1] <= 240:
                answer += "4"
            elif 94 <= mouse[0] <= 154 and 190 <= mouse[1] <= 240:
                answer += "5"
            elif 167.5 <= mouse[0] <= 227.5 and 190 <= mouse[1] <= 240:
                answer += "6"
            elif 240 <= mouse[0] <= 300 and 190 <= mouse[1] <= 240:
                answer += "-"
            elif 20 <= mouse[0] <= 80 and 260 <= mouse[1] <= 310:
                answer += "1"
            elif 94 <= mouse[0] <= 154 and 260 <= mouse[1] <= 310:
                answer += "2"
            elif 167.5 <= mouse[0] <= 227.5 and 260 <= mouse[1] <= 310:
                answer += "3"
            elif 240 <= mouse[0] <= 300 and 260 <= mouse[1] <= 310:
                answer += "*"
            elif 20 <= mouse[0] <= 80 and 330 <= mouse[1] <= 380:
                answer += "0"
            elif 94 <= mouse[0] <= 154 and 330 <= mouse[1] <= 380:
                answer += "."
            elif 167.5 <= mouse[0] <= 227.5 and 330 <= mouse[1] <= 380:
                print ("Equal")
                calcScreen1 = pygame.draw.rect(screen, color, [20, 20, 280, 75])
                answer = str(eval(answer))
            elif 240 <= mouse[0] <= 300 and 330 <= mouse[1] <= 380:
                answer += "/"
            elif 20 <= mouse[0] <= 302 and 400 <= mouse[1] <= 450:
                calcScreen2 = pygame.draw.rect(screen, color, [20, 20, 280, 75])
                answer = ""

    mouse = pygame.mouse.get_pos()

    pygame.display.update()



