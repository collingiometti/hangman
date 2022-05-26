# collin giometti - hangman

import pygame
import sys

black = (0,0,0)
background = (166,191,188)
button_light = (218,224,224)
button_dark = (193,199,199)

width = 800
height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

def button(word,x,y,w,h,ic,ac,action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  
  if x+w > mouse[0] > x and y+h > mouse[1] > y:
    pygame.draw.rect(screen,ac,(x,y,w,h))
    if click[0] == 1 and action != None:
      action()
  else:
    pygame.draw.rect(screen,ic,(x,y,w,h))

  buttonText = pygame.font.SysFont("Corbel",40)
  buttonTextSurf = buttonText.render(word, True, black)
  buttonTextRect = buttonTextSurf.get_rect()
  buttonTextRect.center = ((x+(w/2)), (y+(h/2)))
  screen.blit(buttonTextSurf, buttonTextRect)

def gamechoice():
  print("Hello World")

def hangman():
  print("success!!!!")

pygame.init()
while True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
  screen.fill(background)
  button('test',100,100,200,50,button_light,button_dark,hangman)
  pygame.display.update()
  clock.tick(30)
