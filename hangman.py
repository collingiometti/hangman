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

def button(word,x,y,w,h,c1,c2,action=None):
  mouse_pos = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  
  if x+w > mouse_pos[0] > x and y+h > mouse_pos[1] > y:
    pygame.draw.rect(screen,c2,(x,y,w,h))
    if click[0] == 1 and action != None:
      action()
    else:
      pygame.draw.rect(screen,c1,(x,y,w,h))
      
  text = pygame.font.SysFont('Corbel',20)
  text_surface = text.render(word, True, black)
  text_rect = text_surface.get_rect()
  text_rect.center = ((x+(w/2)),(y+(h/2)))
  screen.blit(text_surface, text_rect)

def gamechoice():
  print("Hello World")

def hangman():
  print("success!!!!")

pygame.init()
while True:
  screen.fill(background)
  button('test',100,100,200,50,button_light,button_dark,hangman)
  pygame.display.flip()
  clock.tick(30)
