# collin giometti - hangman

import pygame
import sys
pygame.init()

black = (0,0,0)
red = (163,73,67)
background = (166,191,188)
button_light = (218,224,224)
button_dark = (193,199,199)

width = 800
height = 600
clock = pygame.time.Clock()
fps = 10
screen = pygame.display.set_mode((width, height))

def get_word():
  import random
  lines = []
  f = open('words.txt', 'r')
  for x in f:
    x = x.strip('\n')
    lines.append(x)
  randnumber = random.randint(0,len(lines) - 1)
  lines.pop(len(lines) - 1)
  return lines[randnumber].lower()

def write(word,size,x,y,color):
  text_surf = pygame.font.SysFont("Corbel",size).render(word,True,color)
  text_rect = text_surf.get_rect()
  text_rect.center = (x,y)
  screen.blit(text_surf,text_rect)
  

def button(word,x,y,w,h,ic,ac,action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  
  if x+w > mouse[0] > x and y+h > mouse[1] > y:
    pygame.draw.rect(screen,ac,(x,y,w,h))
    if click[0] == 1 and action != None:
      action()
  else:
    pygame.draw.rect(screen,ic,(x,y,w,h))
    
  write(word,40,(x+(w/2)),(y+(h/2)),black)
  

def gamechoice():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    screen.fill(background)
    
    write("Hangman!",110,400,200,black)
    
    button("1 Player",(width/5),(height/2),200,50,button_light,button_dark,one_player)
    button("2 Player",((width/5)*3),(height/2),200,50,button_light,button_dark,two_player)
    
    pygame.display.update()
    clock.tick(fps)

def one_player():
  hangman(get_word())

def two_player():
  word = ""
  def return_word():
    hangman(word)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      elif event.type == pygame.KEYDOWN:
        if pygame.key.name(event.key) == "backspace":
          word = word.rstrip(word[-1])
        elif pygame.key.name(event.key) == "return":
          return_word()
        else:
          word += pygame.key.name(event.key)
    
    screen.fill(background)
    
    write(word,40,(width/2),(height/2),black)
    
    button("Enter",((width/2)-100),((height/3)*2),200,50,button_light,button_dark,return_word)
    pygame.display.update()
    clock.tick(fps)

states = [
  pygame.image.load('no_guesses_left.png'),
  pygame.image.load('one_guess_left.png'),
  pygame.image.load('two_guesses_left.png'),
  pygame.image.load('three_guesses_left.png'),
  pygame.image.load('four_guesses_left.png'),
  pygame.image.load('five_guesses_left.png'),
  pygame.image.load('six_guesses_left.png'),
  pygame.image.load('seven_guesses_left.png'),
  pygame.image.load('eight_guesses_left.png')
  ]

def hangman(word):
  def end_game(result):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          
      screen.fill(background)
      
      screen.blit(states[guesses_left],(10,100))
      
      write(("You " + result + "!"),110,520,200,black)
      
      write(("the word was " + word.upper()),50,520,300,black)
      
      button("Play Again",425,370,200,50,button_light,button_dark,gamechoice)
      
      pygame.display.update()
      clock.tick(fps)
      
  def guess_word():
    phrase = []
    i = 0
    for j in range(len(word)):
      phrase.append("_")
    def return_phrase():
      str_phrase = ''.join(phrase)
      if str_phrase == word:
        end_game("Win")
      else:
        end_game("Lose")
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          if pygame.key.name(event.key) == "backspace":
            phrase[i-1] = "_"
            i -= 1
          elif pygame.key.name(event.key) == "return":
            return_phrase()
          else:
            phrase[i] = pygame.key.name(event.key)
            i+=1
            
      screen.fill(background)
      
      write(''.join(phrase).replace(""," "),40,(width/2),(height/2),black)
      
      button("Enter",((width/2)-100),((height/3)*2),200,50,button_light,button_dark,return_phrase)
      pygame.display.update()
      clock.tick(fps)
          
  guesses_left = 8
  incorrect_guesses = []
  guess = ""
  for i in range(len(word)):
    guess += "_"
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      elif event.type == pygame.KEYDOWN:
        guessed_letter = pygame.key.name(event.key)
        if guessed_letter not in incorrect_guesses:
          if guessed_letter in word:
            for i in range(len(word)):
              if word[i] == guessed_letter:
                guess_list = list(guess)
                guess_list[i] = guessed_letter
                guess = ''.join(guess_list)
            if guess == word:
              end_game("Win")
          else:
            incorrect_guesses.append(guessed_letter)
            guesses_left -= 1
            if guesses_left == 0:
              end_game("Lose")
        
    screen.fill(background)
    screen.blit(states[guesses_left],(10,100))
    
    write(("Guesses Left: " + str(guesses_left)),40,160,70,black)
    
    write(guess.replace(""," "),70,520,220,black)
    
    button("Guess Word",420,300,200,50,button_light,button_dark,guess_word)
    
    pygame.draw.rect(screen,black,(30,480,740,90),5)
    
    write((''.join(incorrect_guesses).replace("","  ")),80,400,525,red)
    
    pygame.display.update()
    clock.tick(fps)
  

gamechoice()
