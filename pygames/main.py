"""
U8 Final Game
ICS3U-04
Chloe Wei
This file serves as my program for the U8 Final Game: The Perfect Potion! Use your arrow and keyboard keys to move around, interact with other characters, and play games! (Please Note: The game uses both the Output screen and the Console, so please make sure they are both open when you are playing!)

History:
April 4, 2023: Program Creation
April 6, 2023: Added backgrounds
April 12, 2023: Added player sprite and it's functionalities/features
April 14, 2023: Made sprite change images depending on direction of movement, resized player sprite images
April 18, 2023: Resized and added NPC sprites
April 20, 2023: Added dialogue and sprite collision features
April 24, 2023: Created functions for each individual scenario/screen to allow for efficiency while running
April 26, 2023: Reformatted code structure for efficiency
April 28, 2023: Created ability for player sprite to switch between backgrounds/settings
May 2, 2023: Resolved data type error in game, refined dialogue
May 4, 2023: Made sure program ran smoothly, added dialogue
May 8, 2023: Continuation of what was done on May 4th
May 10, 2023: Continuation of what was done on May 8th
May 12, 2023: Resolved text display delay issue, continuation of what was done on May 10th
May 16, 2023: Added invalid input features for user inputs (i.e. code that runs when the user provides invalid input)
May 18, 2023: Beta Test
May 23, 2023: Refined code based on feedback provided during Beta Test
May 25, 2023: Considered implementing a "shooter-based-game" for my ghost game, Created/designed vampire quiz screens on Canva platform, implemented vampire quiz screens into program, created vampire quiz game
May 29, 2023: Changed mind on ghost "shooter-based-game" and decided to make it a physics-based quiz game instead (to allow for "parallel between games"), Created/designed ghost quiz screens on Canva platform, implemented ghost quiz screens into program, created ghost quiz game
May 31, 2023: Created/designed sushi bar quiz screens on Canva platform, implemented sushi bar quiz screens into program, created vsushi bar quiz game
June 2, 2023: Made README file, polished up code
June 6, 2023: Added final touches, made sure documentation was up-to-date, submitted program

Resources:
Mad scientist lab background picture: https://www.behance.net/gallery/9784377/Background-Paintings-for-3-CISD-Mad-Scientist 
Vile volcano cave background picture: https://www.vecteezy.com/vector-art/1520391-infernal-dark-cave-with-lava-scene
Ghost graveyard background picture: https://elements.envato.com/graveyard-background-illustration-F8XG585
Wild woods background picture: https://www.freepik.com/premium-vector/cartoon-night-forest-nature-background-magical-wood-with-old-trees-bushes-fireflies-vector-illustration_33098812.htm#query=dark%20forest%20cartoon&position=6&from_view=keyword&track=ais 
Sushi bar background picture: https://www.freepik.com/premium-vector/japanese-food-cartoon-illustration-with-various-delicious-dishes-restaurant_29832434.htm 
User sprite images: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEQp-ZWADvQGctrUFJ873ov2512BCS5Bsr4Kr2jgI4k98KGT_XIN_LDzibpGYgmfWORZI&usqp=CAU 
"""
#======================== VARIABLES ========================
#Counter to keep track of where user is in the game
counter = 0

#Create choice variable to store the user's choice on where to go
choice = 0
#======================== IMPORTS & SETUP ========================
#Import to allow for screen to be cleared
import sys

#Import to allow clock feature to work
import time

#Import to allow "random" feature to work
import random

#Import os feature to be used to clear screen
import os

#Import to allow access to the pygame library
import pygame

#Import keyboard functions
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_RETURN,
    K_y,
    K_k,
    KEYDOWN,
    QUIT,
)

#======================== CLASSES ========================
#Create class for user
class User(pygame.sprite.Sprite):
  """
  Represents the user's sprite
  Attibutes:
    surf: sprite's surface
    rect: rectangular coordinates of the sprite
  """
  def __init__(self):
    """Initializes User attributes"""
    #Inherit all the attributes/methods from Sprite
    super().__init__() 
    #Load images associated with user sprite, which returns a surface. Convert makes it faster to blit
    self.upImg = pygame.image.load("mainC/back1.png").convert()
    self.downImg = pygame.image.load("mainC/front1.png").convert()
    self.leftImg = pygame.image.load("mainC/left1.png").convert()
    self.rightImg = pygame.image.load("mainC/right1.png").convert()
    #Make white colour on each image transparent
    self.upImg.set_colorkey((255,255,255), RLEACCEL) 
    self.downImg.set_colorkey((255,255,255), RLEACCEL) 
    self.leftImg.set_colorkey((255,255,255), RLEACCEL) 
    self.rightImg.set_colorkey((255,255,255), RLEACCEL) 
    #Initalize self.surf as a specific image (for now)
    self.surf = self.downImg
    #We want to use a rectangle for collisions, etc.. so create a rect with the size of the surf.
    self.rect = self.surf.get_rect() 
    #Initially place user sprite in the bottom left corner
    self.rect.x = 100
    self.rect.y = 200
  #Create function to move user based on pressed keys
  def update(self, keysPressed):
    """
    Move user sprite's rectangle based on what keyboard keys are pressed
    Args:
      self: User
      keysPressed: dictionary containing the pressed keys 
    """
    #Depending on what key is pressed, user sprite rectangle will move in a certain direction
    #Code will check if each value is true in the dictionary, and then move accordingly
    #Also change sprite image according to direction of travel
    if keysPressed[K_UP]: 
      self.rect.move_ip(0, -2)
      self.surf = self.upImg
    if keysPressed[K_DOWN]:
      self.rect.move_ip(0, 2)
      self.surf = self.downImg
    if keysPressed[K_LEFT]:
      self.rect.move_ip(-2, 0)
      self.surf = self.leftImg
    if keysPressed[K_RIGHT]:
      self.rect.move_ip(2, 0)
      self.surf = self.rightImg
    # Keep player on the screen by imposing borders
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT

#Create class for vampire
class Sinisteca(pygame.sprite.Sprite):
  """
  Represents the mad scientist's sprite
  Attibutes:
    surf: sprite's surface
    rect: rectangular coordinates of the sprite
  """
  def __init__(scientist):
    """Initializes Mad Scientist Sinisteca's attributes"""
    #Inherit all the attributes/methods from Sprite
    super().__init__() 
    #Load images associated with user sprite, which returns a surface. Convert makes it faster to blit
    scientist.surf = pygame.image.load("npc/sinisteca.PNG").convert()
    #Make white colour on image transparent
    scientist.surf.set_colorkey((255,255,255), RLEACCEL) 
    #We want to use a rectangle  for collisions, etc.. so create a rect with the size of the surf.
    scientist.rect = scientist.surf.get_rect() 
    #Place mad scientist sinisteca in bottom left corner
    scientist.rect.x = 490
    scientist.rect.y = 215

#Create class for vampire
class Vampire(pygame.sprite.Sprite):
  """
  Represents the vampire's sprite
  Attibutes:
    surf: sprite's surface
    rect: rectangular coordinates of the sprite
  """
  def __init__(vamp):
    """Initializes Vampire attributes"""
    #Inherit all the attributes/methods from Sprite
    super().__init__() 
    #Load images associated with user sprite, which returns a surface. Convert makes it faster to blit
    vamp.surf = pygame.image.load("npc/vampire.PNG").convert()
    #Make white colour on image transparent
    vamp.surf.set_colorkey((255,255,255), RLEACCEL) 
    #We want to use a rectangle  for collisions, etc.. so create a rect with the size of the surf.
    vamp.rect = vamp.surf.get_rect() 
    #Place vampire in middle left part of the screen
    vamp.rect.x = 600
    vamp.rect.y = 60

#Create class for ghost
class Ghost(pygame.sprite.Sprite):
  """
  Represents the ghost's sprite
  Attibutes:
    surf: sprite's surface
    rect: rectangular coordinates of the sprite
  """
  def __init__(ghst):
    """Initializes Ghost attributes"""
    #Inherit all the attributes/methods from Sprite
    super().__init__() 
    #Load images associated with user sprite, which returns a surface. Convert makes it faster to blit
    ghst.surf = pygame.image.load("npc/ghst.PNG").convert()
    #Make white colour on image transparent
    ghst.surf.set_colorkey((255,255,255), RLEACCEL) 
    #We want to use a rectangle  for collisions, etc.. so create a rect with the size of the surf.
    ghst.rect = ghst.surf.get_rect() 
    #Place ghost in top right corner
    ghst.rect.x = 530
    ghst.rect.y = 10

#Create class for werewolf
class Werewolf(pygame.sprite.Sprite):
  """
  Represents the werewolf's sprite
  Attibutes:
    surf: sprite's surface
    rect: rectangular coordinates of the sprite
  """
  def __init__(wolf):
    """Initializes Werewolf attributes"""
    #Inherit all the attributes/methods from Sprite
    super().__init__() 
    #Load images associated with user sprite, which returns a surface. Convert makes it faster to blit
    wolf.surf = pygame.image.load("npc/werewolf.PNG").convert()
    #Make white colour on image transparent
    wolf.surf.set_colorkey((255,255,255), RLEACCEL) 
    #We want to use a rectangle  for collisions, etc.. so create a rect with the size of the surf.
    wolf.rect = wolf.surf.get_rect() 
    #Place wolf in middleground 
    wolf.rect.x = 430
    wolf.rect.y = 90

#Create class for chef
class Chef(pygame.sprite.Sprite):
  """
  Represents the chef's sprite
  Attibutes:
    surf: sprite's surface
    rect: rectangular coordinates of the sprite
  """
  def __init__(chf):
    """Initializes Chef attributes"""
    #Inherit all the attributes/methods from Sprite
    super().__init__() 
    #Load images associated with user sprite, which returns a surface. Convert makes it faster to blit
    chf.surf = pygame.image.load("npc/chef.PNG").convert()
    #Make white colour on image transparent
    chf.surf.set_colorkey((255,255,255), RLEACCEL) 
    #We want to use a rectangle  for collisions, etc.. so create a rect with the size of the surf.
    chf.rect = chf.surf.get_rect() 
    #Place chef in top right corner
    chf.rect.x = 350
    chf.rect.y = 50
#==========FUNCTIONS===========#
#First time user enters game
def splashscreen(count, pressed_keys):
  """
  Displays splashscreen
  Args:
    count: int
    pressed_keys: dictionary
  Returns:
    count: int
  """
  #Set count as 0
  count = 0
  #Load splashscreen
  splashScreen = pygame.image.load("background/splashscreen.png").convert()
  #Draw the background on the screen, display at (0, 0)
  screen.blit(splashScreen, (0,0)) 
  #Checks if the value for the K_RETURN key is True in the dictionary (i.e. the user pressed the enter key)
  if pressed_keys[K_RETURN]:
    count = 1
  #Update screen to draw new background
  pygame.display.flip()
  
  #Return count value
  return count

#Instructions 1 for user
def instructions1(part, pressed_keys):
  """
  Displays instruction 1 screen
  Args:
    part: int
    pressed_keys: dictionary
  Returns:
    part: int
  """
  #Load instructions 1 screen
  instructions1 = pygame.image.load("background/instruc1.png").convert()
  #Draw the background on the screen, display at (0, 0)
  screen.blit(instructions1, (0,0))
  #Checks if the value for the K_y key is True in the dictionary (i.e. the user pressed the y key)
  if pressed_keys[K_y]:
    part = 2
  #Update screen to draw new background
  pygame.display.flip()

  #Return part value
  return part

#Instructions 2 for user
def instructions2(turn, pressed_keys):
  """
  Displays instruction 2 screen
  Args:
    turn: int
    pressed_keys: dictionary
  Returns:
    turn: int
  """
  #Load instructions 2 screen
  instructions2 = pygame.image.load("background/instruc2.png").convert()
  #Draw the background on the screen, display at (0, 0)
  screen.blit(instructions2, (0,0)) 
  #Checks if the value for the K_RETURN key is True in the dictionary (i.e. the user pressed the enter key)
  if pressed_keys[K_RETURN]:
    turn = 3
  #Update screen to draw new background
  pygame.display.flip()

  #Return turn value
  return turn

#Instructions 3 for user
def instructions3(area, pressed_keys):
  """
  Displays instruction 3 screen
  Args:
    area: int
    pressed_keys: dictionary
  Returns:
    area: int
  """
  #Load instructions 3 screen
  instructions3 = pygame.image.load("background/instruc3.png").convert()
  #Draw the background on the screen, display at (0, 0)
  screen.blit(instructions3, (0,0)) 
  #Checks if the value for the K_k key is True in the dictionary (i.e. the user pressed the k key)
  if pressed_keys[K_k]:
    area = 4
  #Update screen to draw new background
  pygame.display.flip()

  #Return area value
  return area

#Function for sinisteca lab screen scenarios
def laboratory(mark, pressed_keys, lab):
  """
  Displays lab screen, events that happen within the function depend on value of mark 
  Args:
    mark: int
    pressed_keys: dictionary
    lab: image
  Returns:
    mark: int
    choice: string
  """
  #Initalize choice
  choice = "l"
  #Draw the background on the screen, display at (0, 0)
  screen.blit(lab, (0,0)) 
  #Draw user
  screen.blit(user.surf, user.rect)
  #Draw sinisteca (mad scientist)
  screen.blit(sinisteca.surf, sinisteca.rect)
  #Run following if statement when user interacts with/touches sinisteca NPC sprite
  #Run according if statements based on value of mark and choice variables
  if (pygame.sprite.collide_rect(user, sinisteca)):
    #If mark is 4, run the following code
    if (mark == 4):
      #Welcome dialogue
      print("😮 (You): WOAH, where am I??")
      print("🐭 (Sinisteca): HEY! OVER HERE! \nHello there! I am the world-renowned mad scientist Doctor Sinisteca! All those who have dared to cross me or my hairline have suffered a despicable fate! YOU must be my new mortal assistant. What is your name?")
      #Ask user for name
      name = input("Type your name: ")
      print("😮: Um, my name is", name)
      #Introduce user to game 
      print("🐭: Ah, well nice to meet you,", name, "! I'm glad you have come! \nYou see, recently, the land around my lab has suffered a terrible plight, which has damaged the ecosystem around it and reduced caesar salad production rates *sniff sniff*. SO, our mission is to create a potion to heal the land! \nAs you have already signed my contract and agreed to be my assistant and help me in this endeavor, I expect you to help me carry out tasks to complete this mission! \nAny questions?")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Continue dialogue
      print("😕: Yeah well you see I was actually kinda forced into agreeing to be your assistant so I was wondering if I could cancel the contract and leave-")
      print("🐭: OH WONDERFUL! It seems like you have no questions! I'm glad we're both on the same page!")
      print("😕: UH no I don't think you understand, I don't want to be here-")
      print("🐭: .....I will assume that what you just said was simply a joke and you don't actually mean it....after all, at the end of the day, you DID sign the contract, and we both know what happens if you break it now...it would be TERRIBLE if something dreadful happened to your pet crocodile, wouldn't it?")
      print("🐭: How about this: After you help me make this potion, I will allow you to return back to your mortal world, and I won't bother you ever again. Deal?")
      print("😊: You have yourself a deal!")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Intro to first task to complete potion
      print("🐭: OK wonderful! Now that that's been settled, let's get started!!")
      print("🐭: In order to complete the potion, I need some extra ingredients that I do not have in my lab. Due to *ahem* height reasons, I am unable to collect these ingredients myself, so I need YOU to help collect them for me! In total, I will need 3 ingredients. I will ask you to get them one by one. ")
      print("🐭: The first ingredient I need is vampire ventricles. To get it, you must go to the Vile Volcano and confront the vampire that lives there. ")
      #Print task in console
      print("\n*TASK 1: Go to the Vile Volcano, go up to the vampire, and retrieve Vampire Ventricles!*")
      print("🐭: Good luck,", name, "! I'm counting on you!\n")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Change mark to 5
      mark = 5
      #Clear the screen
      os.system('clear')
    #If mark is 6, run this code
    if (mark == 6):
      #Welcome dialogue
      print("🐭: Ah- You're back! How was it?")
      print("🙂: You know, it wasn't actually as bad as I thought it would be")
      print("🐭: Right? Well I'm glad you think so.....BECAUSE THERES MORE FOR YOU TO DO!!")
      print("😐: ...")
      print("🐭: ...")
      #Intro to second task
      print("🐭: YES SO the second ingredient I need is green goldfish from the Ghost Graveyard. Talk to the ghost there - he should be able to help you.")
      #Print task in console
      print("\n*TASK 2: Go to the Ghost Graveyard, go up to the ghost, and retrieve Green Goldfish!*")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Change mark to 7
      mark = 7
    #If mark is 8, run this code
    if (mark == 8):
      #Welcome dialogue
      print("🐭: OOH welcome back! ")
      print("🙂: Here are your Green Goldfish.")
      print("🐭: Why thank you so very much!")
      print("🐭: Now listen, there is one final ingredient I need you to collect to make the potion.")
      print("😐: Really?? YAYYYYY!")
      #Intro to final task (task 3)
      print("🐭: Yes! I need you to go the Wild Woods and collect wasabi. When your in the woods, ask the werewolf for help; if anyone knows where to get good wasabi from, it's him.")
      print("🐭: Good luck, and goodbye!")
      #Print task in console
      print("\n*TASK 3: Go to the Wild Woods, go up to the werewolf, and retrieve Wasabi!*")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Change mark to 9
      mark = 9
    #If mark is 12, run this code
    if (mark == 12):
      #Welcome user back
      print("🙂: I'm back!")
      print("🐭: OOOH Welcome back!")
      print("🙂: I've brought back the wasabi you've requested!")
      print("🐭: OOOH wonderful, thank you! Now, I can finally make my ceasar salad potion! MWAHAHAHA!")
      print("🐭: Thank you very much for your help! You have done wonderfully!")
      print("🐭: So, as a reward, I will let you walk free; you no longer have to keep being my lab assistant!")
      print("🙂: REALLY?!?! Wow, I thought you were joking!")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Continue dialogue
      print("🐭: Of course not! I, Sinisteca, NEVER joke! Now that I can eat my ceasar salad in peace, there is no need for me to have a lab assistant to run errands! \nOH also, I would like to congratulate you for being the first mortal to survive being my assistant!")
      print("🙂: ...Oh...Wow, thanks so much!")
      #Easter egg for my U6-A1 Adventure Game Project :)
      print("🐭: Ahahaha! Anyways, I am guessing you better get going now, for my *mad scientist senses* tell me that soon, you will be whisked away on another mission involving the Wizard of Oz...")
      print("🙂: Seriously? *Sigh* Well then I better get going...")
      #Say goodbye!
      print("🙂: Thanks so much, and goodbye!")
      print("🐭: Byee!")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Set choice as "0" and mark as 13 and return it
      choice = 0
      mark = 13
      return choice, mark
    #Ask user where they would like to go, and change their location accordingly
    choice = input('Where would you like to go? \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods \n')
    #Validate user input. While input invalid (invalid input is input depicted in the while loop condition), ask the user to type in a valid symbol for a valid location. When user input becomes valid, break the while loop (by making the while loop condition false)
    while (choice.lower() != "v" and choice.lower() != "g" and choice.lower() != "w"):
      #Clear the screen
      os.system('clear')
      #Tell user that their input is invalid
      print("Your input is invalid. Please type a valid symbol for a valid location. ")
      #Re-ask user where they would like to go.
      choice = input('\nWhere would you like to go? \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods \n')
      #Clear the screen
      os.system('clear')
    #If user input is valid, clear the console and reset user sprite position to prepare for next screen scenario
    else:
      #Move user rect 300 steps left
      user.rect.x -= 300
      #Clear the screen
      os.system('clear')
  
  #Return choice and mark variables
  return choice, mark

#Function for vile volcano screen scenarios
def vileVolcano(place, pressed_keys, volcano, vamp1, vamp2, vamp3, vamp4):
  """
  Displays vile volcano screen, events that happen within the function depend on value of place
  Args:
    place: int
    pressed_keys: dictionary
    volcano: image 
    vamp1: image
    vamp2: image
    vamp3: image
    vamp4: image
  Returns:
    place: int
    choice: string
  """
  #Initialize choice
  choice = "v"
  #Draw the background on the screen, display at (0, 0)
  screen.blit(volcano, (0,0)) 
  #Draw user
  screen.blit(user.surf, user.rect)
  #Draw vampire
  screen.blit(vampire.surf, vampire.rect)
  #According dialogue plays when user interacts with vampire NPC sprite
  if (pygame.sprite.collide_rect(user, vampire)):
    #If place is 5, run this code
    if (place == 5):
      #Welcome dialogue
      print("😮 (You): AH! Um hiiii")
      print("🧛 (Paul the Vampire): Hello there! I am Paul the vampire! How may I help you? *hiss*")
      print("😐: Oh um hi! You see, I was sent by a mad scientist named “Doctor Sinisteca?” Does that name ring a bell?")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Continue dialogue
      print("🧛: …Who?")
      print("😐: Doctor Sinisteca. Small dude, AMAZING hairline? Has a (personally) worrisome addiction to Caesar salad?")
      print("🧛: AH! Yes, Sinisteca! I haven’t seen him in a while - tell him I send my regards!")
      print("🙂: I will!")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Intro to Task 1 Game
      print("🙂: Anyways, I was sent here to retrieve Vampire Ventricles. Do you happen to have any?")
      print("🧛: Yes, in fact, I do! The thing is, they are very rare, so I usually never give them to anybody....")
      print("🧛: ...BUT I will make an exception just this once; if you can successfully complete my quiz game, then I will give you the viper ventricles. If you lose, you will not. Deal?")
      print("🙂: Yes, you have yourself a deal!")
      #Task 1 Game instructions
      print("\nGame instructions: Answer the questions on the screen by typing 'A', 'B', 'C', or 'D' in the console.\n")
      print("🧛: Let the game begin!")
      #Start the game
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      
      #GAME 1
      #Set value for "correct" variable as not equal to true so that while loop will keep running until the user gets all the questions correct (in that case, the "correct" variable will be True and the loop will break)
      correct = 0
      while (correct != True):
        #Define variables for game
        question1 = 0
        question2 = 0
        question3 = 0
        question4 = 0
        #Question 1
        #Draw the first question's background on the screen, display at (0, 0)
        screen.blit(vamp1, (0,0)) 
        #Flip the display
        pygame.display.flip()
        #Ask user for answer to first question
        question1 = input("Please type your answer (one of the following capital letters: A, B, C, D): ")
        #If user's inputted answer matches the correct answer (which is, in this case, "A"), then tell the user they got the question correct and move on to the next question
        if (question1 == "A"):
          print("Correct!")
          #Question 2
          #Draw the second question's background on the screen, display at (0, 0)
          screen.blit(vamp2, (0,0)) 
          #Flip the display
          pygame.display.flip()
          #Ask user for answer to second question
          question2 = input("Please type your answer (one of the following capital letters: A, B, C, D): ")
          #If user's inputted answer matches the correct answer (which is, in this case, "C"), then tell the user they got the question correct and move on to the next question
          if (question2 == "C"):
            print("Correct!")
            #Question 3
            #Draw the third question's background on the screen, display at (0, 0)
            screen.blit(vamp3, (0,0)) 
            #Flip the display
            pygame.display.flip()
            #Ask user for answer to third question
            question3 = input("Please type your answer (one of the following capital letters: A, B, C, D): ")
            #If user's inputted answer matches the correct answer (which is, in this case, "A"), then tell the user they got the question correct and move on to the next question
            if (question3 == "A"):
              print("Correct! Now, time for the last question!")
              #Question 4
              #Draw the fourth question's background on the screen, display at (0, 0)
              screen.blit(vamp4, (0,0)) 
              #Flip the display
              pygame.display.flip()
              #Ask user for answer to fourth question
              question4 = input("Please type your answer (one of the following capital letters: A, B, C, D): ")
              #If user's inputted answer matches the correct answer (which is, in this case, "B"), then tell the user they got the question correct and move on to the next question
              if (question4 == "B"):
                print("Correct!")
                #Set loop condition as true so the while loop breaks (because while loop condition is no longer true)
                correct = True
              #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
              else:
                print("Sorry, you lose! Please try playing the quiz again!")
            #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
            else:
              print("Sorry, you lose! Please try playing the quiz again!")
          #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
          else:
            print("Sorry, you lose! Please try playing the quiz again!")
        #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
        else:
          print("Sorry, you lose! Please try playing the quiz again!")
      #When game is successfully, complete redraw the background on the screen, display at (0, 0)
      screen.blit(volcano, (0,0)) 
      #Flip the display
      pygame.display.flip()
      #Redraw user
      screen.blit(user.surf, user.rect)
      #Redraw vampire
      screen.blit(vampire.surf, vampire.rect)
      #Flip the display to update the screen
      pygame.display.flip()

      #Clear the screen
      os.system('clear')
      #Congratulate user and say bye!
      print("🧛: Congratulations! You have won! Here are your Viper Ventricles!")
      print("🙂: Thank you so much Paul! I'll get going now. Bye!")
      #Give user status update on task completion
      print("\n*TASK 1 COMPLETE! Go back to Sinisteca's Lab and talk to Sinisteca!*")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Change place to 6
      place = 6
    #Ask user where they would like to go
    choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods \n')
    #Validate user input. While input invalid (invalid input is input depicted in the while loop condition), ask the user to type in a valid symbol for a valid location. When user input becomes valid, break the while loop (by making the while loop condition false)
    while (choice.lower() != "l" and choice.lower() != "g" and choice.lower() != "w"):
      #Clear the screen
      os.system('clear')
      #Tell user that their input is invalid
      print("Your input is invalid. Please type a valid symbol for a valid location. ")
      #Re-ask user where they would like to go.
      choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods \n')
      #Clear the screen
      os.system('clear')
    #If user input is valid, clear the console and reset user sprite position to prepare for next screen scenario  
    else:
        #Move user rect 300 steps left
        user.rect.x -= 300
        #Clear the screen
        os.system('clear')
     
  #Return choice and place variables
  return choice, place

#Function for ghost graveyard screen scenarios
def ghostGraveyard(point, pressed_keys, graveyard, ghost1, ghost2, ghost3, ghost4):
  """
  Displays ghost graveyard screen, events that happen within the function depend on value of point
  Args:
    point: int
    pressed_keys: dictionary
    graveyard: image 
    ghost1: image 
    ghost2: image 
    ghost3: image 
    ghost4: image 
  Returns:
    point: int
    choice: string
  """
  #Initialize choice
  choice = "g"
  #Draw the background on the screen, display at (0, 0)
  screen.blit(graveyard, (0,0)) 
  #Draw user
  screen.blit(user.surf, user.rect)
  #Draw ghost
  screen.blit(ghost.surf, ghost.rect)
  #According dialogue plays when user interacts with ghost NPC sprite
  if (pygame.sprite.collide_rect(user, ghost)):
    #If point is 7, run this code
    if (point == 7):
      #Welcome dialogue
      print("👻 (Willy Bubbles Aurora the 2nd): *fancily* BOO!")
      print("😮 (You): AHHHH!")
      print("😐: Who are YOU??")
      print("👻: My name is Bubbles Aurora the 2nd, although you may address me as Bubbles. How may I help you?")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Intro to Task 2 Game
      print("🙂: Ummm well I was sent here to retrieve Green Goldfish. I was told you could help me get some.")
      print("👻: Ah yes, in fact, I do! I would happily give them to you, BUT only if you can help me finish my physics homework. ")
      print("🙂: I mean sure, why not! It should be helpful, anyways, since I have a physics exam coming up!")
      print("👻: WONDERFUL! Thank you so much! However, I'm warning you - ghost physics homework is not for the faint of heart. In fact, only those who have a clear, true love for physics can successfully complete ghost physics questions. ")
      print("🙂: That's fine! When there's a will, there's a way! LET'S DO THIS!")
      print("👻: That's the spirit! Now, good luck!")
      #Print game instructions
      print("\nGame instructions: Answer the questions on the screen by typing in the console.\n")
      print("👻: Let the game begin!")
      #Start the game
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')

      #GAME 2
      #Set value for "correct" variable as not equal to true so that while loop will keep running until the user gets all the questions correct (in that case, the "correct" variable will be True and the loop will break)
      correct = 0
      while (correct != True):
        #Define variables for game
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        #Question 1
        #Draw the first question's background on the screen, display at (0, 0)
        screen.blit(ghost1, (0,0)) 
        #Flip the display
        pygame.display.flip()
        #Ask user for their answer
        q1 = int(input("Please type your answer (an integer value): "))
        #If user's inputted answer matches the correct answer (which is, in this case, 70), then tell the user they got the question correct and move on to the next question
        if (q1 == 70):
          print("Correct!")
          #Question 2
          #Draw the second question's background on the screen, display at (0, 0)
          screen.blit(ghost2, (0,0)) 
          #Flip the display
          pygame.display.flip()
          #Ask user for their answer
          q2 = int(input("Please type your answer (an integer value): "))
          #If user's inputted answer matches the correct answer (which is, in this case, 8437), then tell the user they got the question correct and move on to the next question
          if (q2 == 8437):
            print("Correct!")
            #Question 3
            #Draw the third question's background on the screen, display at (0, 0)
            screen.blit(ghost3, (0,0)) 
            #Flip the display
            pygame.display.flip()
            #Ask user for their answer
            q3 = int(input("Please type your answer (an integer value): "))
            #If user's inputted answer matches the correct answer (which is, in this case, 0), then tell the user they got the question correct and move on to the next question
            if (q3 == 0):
              print("Correct! Now, time for the last question!")
              #Question 4
              #Draw the fourth question's background on the screen, display at (0, 0)
              screen.blit(ghost4, (0,0)) 
              #Flip the display
              pygame.display.flip()
              #Ask user for their answer
              q4 = int(input("Please type your answer (an integer value): "))
              #If user's inputted answer matches the correct answer (which is, in this case, 50), then tell the user they got the question correct and move on to the next question
              if (q4 == 50):
                print("Correct!")
                #Set loop condition as true so the loop breaks
                correct = True
              #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
              else:
                print("Sorry, you lose! Please try playing the quiz again!")
            #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
            else:
              print("Sorry, you lose! Please try playing the quiz again!")
          #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
          else:
            print("Sorry, you lose! Please try playing the quiz again!")
        #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
        else:
          print("Sorry, you lose! Please try playing the quiz again!")
      #When game is successfully, completely redraw the background on the screen, display at (0, 0)
      screen.blit(graveyard, (0,0)) 
      #Flip the display
      pygame.display.flip()
      #Redraw user
      screen.blit(user.surf, user.rect)
      #Redraw ghost
      screen.blit(ghost.surf, ghost.rect)
      #Flip the display
      pygame.display.flip()

      #Congratulate the user and say bye!
      print("👻: Wow, your physics skills impress me! Congratulations on completing all the questions correctly, and thank you so much for your help! Here are your Green Goldfish!")
      print("🙂: Thank you so much bubbles! I'll get going now. Bye!")
      #Give user status update on task completion
      print("\n*TASK 2 COMPLETE! Go back to Sinisteca's Lab and talk to Sinisteca!*")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Change point to 8
      point = 8
    #Ask user where they would like to go
    choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "w" to go to the Wild Woods \n')
    #Validate user input. While input invalid (invalid input is input depicted in the while loop condition), ask the user to type in a valid symbol for a valid location. When user input becomes valid, break the while loop (by making the while loop condition false)
    while (choice.lower() != "l" and choice.lower() != "v" and choice.lower() != "w"):
      #Clear the screen
      os.system('clear')
      #Tell user that their input is invalid
      print("Your input is invalid. Please type a valid symbol for a valid location. ")
      #Re-ask user where they would like to go.
      choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "w" to go to the Wild Woods \n')
      #Clear the screen
      os.system('clear')
    #If user input is valid, clear the console and reset user sprite position to prepare for next screen scenario 
    else:
      #Move user rect 300 steps left
      user.rect.x -= 300
      #Clear the screen
      os.system('clear')
     
  #Return choice and point variables
  return choice, point

#Function for wild woods screen scenarios
def wildWoods(progress, pressed_keys, woods):
  """
  Displays wild woods screen, events that happen within the function depend on value of progress
  Args:
    progress: int
    pressed_keys: dictionary
    woods: image
  Returns:
    progress: int
    choice: string
  """
  #Initialize choice
  choice = "w"
  #Draw the background on the screen, display at (0, 0)
  screen.blit(woods, (0,0)) 
  #Draw user
  screen.blit(user.surf, user.rect)
  #Draw werewolf
  screen.blit(werewolf.surf, werewolf.rect)
  #According dialogue plays when user interacts with werewolf NPC sprite
  if (pygame.sprite.collide_rect(user, werewolf)):
    #If progress is 9, run this code
    if (progress == 9):
      #Welcome dialogue
      print("🐺 (Big Bad Wolf): BOO!")
      print("😮 (You): AHHHH!")
      print("😮: WHY DOES EVERYONE KEEP TRYING TO SCARE ME!!")
      print("🐺: Ahahahaha, my apologies. It's been a while since someone has come to visit me. How can I help you? ")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Intro to Task 3.5
      print("🙂: Hi! I need help getting some wasabi. Do you know where I can get some? ")
      print("🐺: You're looking for wasabi? Well, you've come to the right place!")
      print("🐺: Because you are my first guest in a while, I will give you the honour of tasting my *finest* wasabi combo. ")
      print("🙂: Oh, um, thanks so much! Although I personally don't enjoy eating wasabi by itself...")
      print("🐺: What? NONESENSE! First, bring me wasabi from the sushi bar up the road, and then we'll talk.")
      #Print task in console
      print("\n*HIDDEN TASK 3.5: Go to the Sushi Bar, go up to the chef, and ask for wasabi! Then, bring it back to the werewolf in the Wild Woods!*")
      print("🐺: Make sure to come back after collecting the wasabi!")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Change progress to 10
      progress = 10
    #If progress is 11, run this code
    if (progress == 11):
      #Welcome dialogue
      print("🐺: OOOOH! You're back! Did you get the wasabi?")
      print("🙂: Yes I did! Here you are!")
      print("🐺: Wonderful! Thank you so much! Now, time to create my ultimate wasabi combo:")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #"Wasabi making" sounds
      print("*FLASH BANG BANG BAM WHAM BOOM*")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Continue dialogue
      print("🐺: VOILA! LO AND BEHOLD MY GODLY WASABI! ")
      print("🙂: WOAHHHH! It tastes SO GOOD!! ")
      print("🐺: Why of COURSE it does, its MY wasabi :).")
      print("🐺: Oh my! Look at the time! I have an appointment to go steal some cookies from a little girl now. Go on back home now, and take some wasabi back with you. ")
      print("🙂: ...steal? ")
      print("🐺: ...")
      #Say bye!
      print("🐺: ANYWAYS I'm guessing you must get going now! I will see you later then! It was a pleasure meeting you, goodbye!")
      print("🙂: Yes alright then! Goodbye!")
      #Give user status update on task completion
      print("\n*TASK 3 COMPLETE! Go back to Sinisteca's Lab and talk to Sinisteca!*")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Change progress to 12
      progress = 12
    #Ask user where they would like to go
    choice = input('Where would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \n*New Location*: Press "s" to go to the Sushi Bar\n')
    #Validate user input. While input invalid (invalid input is input depicted in the while loop condition), ask the user to type in a valid symbol for a valid location. When user input becomes valid, break the while loop (by making the while loop condition false)
    while (choice.lower() != "l" and choice.lower() != "v" and choice.lower() != "g" and choice.lower() != "s"):
      #Clear the screen
      os.system('clear')
      #Tell user that their input is invalid
      print("Your input is invalid. Please type a valid symbol for a valid location. ")
      #Re-ask user where they would like to go.
      choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \n*New Location*: Press "s" to go to the Sushi Bar\n')
      #Clear the screen
      os.system('clear')
    #If user input is valid, clear the console and reset user sprite position to prepare for next screen scenario
    else:
      #Move user rect 300 steps left
      user.rect.x -= 300
      #Clear the screen
      os.system('clear')
     
  #Return choice and progress variables
  return choice, progress

#Function for sushi bar screen scenarios
def sushiBar(space, pressed_keys, sushiRest, sushi1, sushi2, sushi3, sushi4):
  """
  Displays sushi bar screen, events that happen within the function depend on value of space
  Args:
    space: int
    pressed_keys: dictionary
    sushiRest: image
    sushi1: image
    sushi2: image
    sushi3: image
    sushi4: image
  Returns:
    space: int
    choice: string
  """
  #Initialize choice
  choice = "s"
  #Draw the background on the screen, display at (0, 0)
  screen.blit(sushiRest, (0,0)) 
  #Draw user
  screen.blit(user.surf, user.rect)
  #Draw chef
  screen.blit(chef.surf, chef.rect)
  #According dialogue plays when user interacts with chef NPC sprite
  if (pygame.sprite.collide_rect(user, chef)):
    #If space is 10, run this code
    if (space == 10):
      #Welcome dialogue
      print("👩‍🍳 (Chef): HIII! Welcome to 'Something's Fishy' Sushi Bar!")
      print("😄 (You): FINALLY!! Someone who isn't trying to scare me!")
      print("👩‍🍳: Scare you? Of course not! That is no way to treat a guest! ")
      print("👩‍🍳: Anyways, let me introduce myself: My name is Chef Fylype! How may I help you today? ")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Intro to Task 3.5 Game
      print("🙂: Hi! Could I please get some wasabi! ")
      print("👩‍🍳: Wasabi! Of course!.....")
      print("👩‍🍳: HOWEVER, this wasabi isn't for the faint of heart.")
      print("👩‍🍳: So, for *safety purposes*, I have created a test for customers to take to check whether or not they can safely handle the wasabi.")
      print("👩‍🍳: Would you like to take the test to find out? If you do, you'll get the wasabi!")
      print("🙂: Sure, I guess. Why not? I need to eventually get the wasabi, anyways.")
      print("👩‍🍳: Great! I admire your spirit!")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')
      #Continue dialogue
      print("👩‍🍳: However, I have to warn you that this test is *extremely* difficult. That ghost's physics homework is CHILD'S PLAY compared to this. Even facing an angry Sinisteca is EASY compared to this! Are you sure you still want to try the test?")
      print("🙂: YES! BRING IT ON!")
      print("👩‍🍳: Ok, well then good luck and have fun! ")
      #Give user game instructions
      print("\nGame instructions: Answer the questions on the screen by typing in the console.")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Clear the screen
      os.system('clear')

      #GAME 3
      #Set value for "correct" variable as not equal to true so that while loop will keep running until the user gets all the questions correct (in that case, the "correct" variable will be True and the loop will break)
      correct = 0
      while (correct != True):
        #Define variables for game
        ques1 = 0
        ques2 = 0
        ques3 = 0
        ques4 = 0
        #Question 1
        #Draw the first question's background on the screen, display at (0, 0)
        screen.blit(sushi1, (0,0)) 
        #Flip the display
        pygame.display.flip()
        #Ask user for their answer
        ques1 = int(input("Please type your answer (an integer value): "))
        #If user's inputted answer matches the correct answer (which is, in this case, 3), then tell the user they got the question correct and move on to the next question
        if (ques1 == 3):
          print("Correct!")
          #Question 2
          #Draw the second question's background on the screen, display at (0, 0)
          screen.blit(sushi2, (0,0)) 
          #Flip the display
          pygame.display.flip()
          #Ask user for their answer
          ques2 = int(input("Please type your answer (an integer value): "))
          #If user's inputted answer matches the correct answer (which is, in this case, 0), then tell the user they got the question correct and move on to the next question
          if (ques2 == 0):
            print("Correct!")
            #Question 3
            #Draw the third question's background on the screen, display at (0, 0)
            screen.blit(sushi3, (0,0)) 
            #Flip the display
            pygame.display.flip()
            #Ask user for their input
            ques3 = int(input("Please type your answer (an integer value): "))
            #If user's inputted answer matches the correct answer (which is, in this case, 5), then tell the user they got the question correct and move on to the next question
            if (ques3 == 5):
              print("Correct! Now, time for the last question!")
              #Question 4
              #Draw the fourth question's background on the screen, display at (0, 0)
              screen.blit(sushi4, (0,0)) 
              #Flip the display
              pygame.display.flip()
              #Ask user for their answer
              ques4 = int(input("Please type your answer (an integer value): "))
              #If user's inputted answer matches the correct answer (which is, in this case, 2), then tell the user they got the question correct and move on to the next question
              if (ques4 == 2):
                print("Correct!")
                #Set loop condition as true so the loop breaks
                correct = True
              #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
              else:
                print("Sorry, you lose! Please try playing the quiz again!")
            #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
            else:
              print("Sorry, you lose! Please try playing the quiz again!")
          #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
          else:
            print("Sorry, you lose! Please try playing the quiz again!")
        #Else, if user's inputted answer is wrong, let them know and restart game (because while loop condition has not been broken yet and so the while loop will keep running)
        else:
          print("Sorry, you lose! Please try playing the quiz again!")
      #When game is successfully, completely redraw the background on the screen, display at (0, 0)
      screen.blit(sushiRest, (0,0)) 
      #Flip the display
      pygame.display.flip()
      #Redraw user
      screen.blit(user.surf, user.rect)
      #Redraw chef
      screen.blit(chef.surf, chef.rect)
      #Flip the display
      pygame.display.flip()
      
      #Congratulations for completing test successfully and say bye!
      print("👩‍🍳: Oh my! I can't believe it! You completed the test successfully! Wasn't that the most difficult, brain-squeezing test you've ever taken? Congratulations! You have won! Here is your wasabi!")
      print("🙂: Thank you so much Chef Fylype! I'll get going now. Bye!")
      #Give user status update on task completion
      print("\n*TASK 3.5 COMPLETE! Go back to the Wild Woods and talk to the werewolf!*")
      #Ask user to press "ENTER" to continue
      input("Press 'ENTER' to continue\n")
      #Change space to 11
      space = 11
    #Ask user where they would like to go
    choice = input('Where would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods \n')
    #Validate user input. While input invalid (invalid input is input depicted in the while loop condition), ask the user to type in a valid symbol for a valid location. When user input becomes valid, break the while loop (by making the while loop condition false)
    while (choice.lower() != "l" and choice.lower() != "v" and choice.lower() != "g" and choice.lower() != "w"):
      #Clear the screen
      os.system('clear')
      #Tell user that their input is invalid
      print("Your input is invalid. Please type a valid symbol for a valid location. ")
      #Re-ask user where they would like to go.
      choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods \n')
      #Clear the screen
      os.system('clear')
    #If user input is valid, clear the console and reset user sprite position to prepare for next screen scenario
    else:
      #Move user rect 300 steps left
      user.rect.x -= 300
      #Clear the screen
      os.system('clear')
     
  #Return choice and space variables
  return choice, space
#======================== MAIN PROGRAM ========================
#Set up game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

#Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Set user as user class
user = User()

#Set Sinisteca NPC as sinisteca class
sinisteca = Sinisteca()

#Set vampire as vampire class
vampire = Vampire()

#Set ghost as ghost class
ghost = Ghost()

#Set werewolf as werewolf class
werewolf = Werewolf()

#Set chef as chef class
chef = Chef()

#Load sinisteca lab screen
lab = pygame.image.load("background/lab.png").convert()

#Load vile volcano screen
volcano = pygame.image.load("background/vileVolcano.png").convert()

#Load ghost graveyard screen
graveyard = pygame.image.load("background/ghostGraveyard.png").convert()

#Load wild woods screen
woods = pygame.image.load("background/wildWoods.png").convert()

#Load sushi bar screen
sushiRest = pygame.image.load("background/sushiBar.png").convert()

#Load vampire game screens
vamp1 = pygame.image.load("vampGame/Vgame1.png").convert()
vamp2 = pygame.image.load("vampGame/Vgame2.png").convert()
vamp3 = pygame.image.load("vampGame/Vgame3.png").convert()
vamp4 = pygame.image.load("vampGame/Vgame4.png").convert()

#Load ghost game screens
ghost1 = pygame.image.load("ghostGame/Ggame1.png").convert()
ghost2 = pygame.image.load("ghostGame/Ggame2.png").convert()
ghost3 = pygame.image.load("ghostGame/Ggame3.png").convert()
ghost4 = pygame.image.load("ghostGame/Ggame4.png").convert()

#Load sushi restaurant game screens
sushi1 = pygame.image.load("sushiGame/Sgame1.png").convert()
sushi2 = pygame.image.load("sushiGame/Sgame2.png").convert()
sushi3 = pygame.image.load("sushiGame/Sgame3.png").convert()
sushi4 = pygame.image.load("sushiGame/Sgame4.png").convert()

#Run loop until user quits, or game ends
running = True

#Infinite loop
while running:
  #Check for events
  for event in pygame.event.get(): 
      #If user pressed down on a key, run through according if statements to perform appropriate actions
    if event.type == KEYDOWN:
      #Check if the user clicked the escape key, if yes, end 'running' loop
      if event.key == pygame.K_ESCAPE:
        running = False
      #If user clicked x button in top-right corner, end 'running' loop
      elif event.type == pygame.QUIT: 
        running = False
  
  #Get a dictionary of keys pressed 
  pressed_keys = pygame.key.get_pressed()
  #Conditional statements: Run if statements, screens and scenarios for the game depending on the values of counter and choice
  if (counter == 0):
    counter = splashscreen(counter, pressed_keys)
  elif (counter == 1):
    counter = instructions1(counter, pressed_keys)
  elif (counter == 2):
    counter = instructions2(counter, pressed_keys)
  elif (counter == 3):
    counter = instructions3(counter, pressed_keys)
  elif (counter == 4):
    choice, counter = laboratory(counter, pressed_keys, lab)
  #Set booleans for the values of counter
  #Set booleans for the values of choice
  elif (choice == "l" and counter == 4 or choice == "l" and counter == 6 or choice == "l" and counter == 8 or choice == "l" and counter == 12):
    choice, counter = laboratory(counter, pressed_keys, lab)
  elif (choice == "v" and counter == 5):
    choice, counter = vileVolcano(counter, pressed_keys, volcano, vamp1, vamp2, vamp3, vamp4)
  elif (choice == "g" and counter == 7):
    choice, counter = ghostGraveyard(counter, pressed_keys, graveyard, ghost1, ghost2, ghost3, ghost4)
  elif (choice == "w" and counter == 9 or choice == "w" and counter == 11):
    choice, counter = wildWoods(counter, pressed_keys, woods)
  elif (choice == "s" and counter == 10):
    choice, counter = sushiBar(counter, pressed_keys, sushiRest, sushi1, sushi2, sushi3, sushi4)
  elif (choice == 0 and counter == 13):
    running = False
  #Run this elif statement if the user is in the wild woods and they enter input that does not correspond to their game scenario (ex. user tries to access lab from wild woods when they are not supposed to)
  elif (counter == 10 and choice != "s"):
    print("Are you lost, weary traveller? It appears you are trying to go to the wrong location. ")
    #Re-ask user where they would like to go.
    choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods \n*New Location*: Press "s" to go to the Sushi Bar\n')
    #Clear the screen
    os.system('clear')
  #Run this else statement if the user enters input that does not correspond to their game scenario (ex. user tries to access ghost graveyard from vile volcano when they are not supposed to)
  else:
    print("Are you lost, weary traveller? It appears you are trying to go to the wrong location. ")
    #Re-ask user where they would like to go.
    choice = input('\nWhere would you like to go? \nPress "l" to go to Sinistecas lab \nPress "v" to go the Vile Volcano \nPress "g" to go to the Ghost Graveyard \nPress "w" to go to the Wild Woods\n')
    #Clear the screen
    os.system('clear')

  #Create a clock using import time function
  clock = pygame.time.Clock()
  #Set frame rate to be 80 to slow sprite movement down
  clock.tick(80)

  #Update user position based on key presses
  user.update(pressed_keys)

  #Flip the display
  pygame.display.flip()
  
#Quit game
pygame.quit()

#-----Ending-----#
#When while loop breaks (i.e. user finishes game and choice = 'q', xclear screen and print ending message
#Clear the screen
os.system('clear')
print("The end! Thanks for playing!") 