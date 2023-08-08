"""
U6-A1 Adventure Game
ICS3U-04
Chloe Wei
This file serves as my program for the U6-A1 Adventure Game

History:
Jan 12, 2023: Program Creation
Jan 16, 2023: Created functions for each location
Jan 18, 2023: Connected all the locations together as required by my adventure game plan
Jan 22, 2023: Added all neccesary dialogue
Jan 24, 2023: Finished mini games and submitted program
Feb 16, 2023: Broke up dialogue into smaller sections for easier processing by using the input() function, and made code accomodating for both uppercase and lowercase input

Resources:
How to clear the screen -> Provided by Mrs. Edwards
Wizard of Oz Trivia --> https://www.usefultrivia.com/movie_trivia/wizard_of_oz_trivia.html
"""

#-----VARIABLES AND IMPORTS-----#
#Import time to be used for counting down features, etc.
import time
#Import os feature to be used to clear screen
import os
#Import random feature to select a random value
import random

#Create choice variable to store the user's choice on where to go
choice = 0

#Create mark variable to mark at what point the user is at inside the adventure
mark = 0

#Create lists to store questions for Mini Game 1:
question1 = []
question2 = []
question3 = []


#-----FUNCTIONS-----#
#Define home function
def home():
  """
  Prints description of home
  Args:
    none
  Returns:
    none
  """
  print("You have arrived at: HOME 🏡")
  print("What a beautiful day to be at home! It's nice, peaceful, and quiet...")
  #Ask user to press "ENTER" to continue
  input("Press 'ENTER' to continue\n")
  #Clear the screen
  os.system('clear')

#Define trouble function
#Function dedicated to providing sound effects to indicate trouble
def trouble():
  """
  Prints onomatopoeia indicating trouble
  Args:
    none
  Returns:
    none
  """
  #Print booming sound effects in time intervals of 0.5
  for i in range (1, 5):
    print("BOOM")
    time.sleep(0.35)
  #Tell the user that they are in trouble
  print("\nUh Oh! Sounds like trouble!! ")
  #Ask user to press "ENTER" to continue
  input("Press 'ENTER' to continue\n")
  #Clear the screen
  os.system('clear')

#Define tornado function
def tornado():
  """
  Prints tornado description
  Args:
    none
  Returns:
    none
  """
  print("You have arrived at: THE TORNADO 🌪️")
  print("You are in the tornado - Goodness! Its grey, dark, and stormy. ")
  #Ask user to press "ENTER" to continue
  input("Press 'ENTER' to continue\n")
  #Clear the screen
  os.system('clear')

#Define emerald palace function
def emeraldPalace(stage):
  """
  Prints emerald palace description, as well as certain commands depending on at which point in the game the user is at (aka. value of the stage variable)
  Args:
    stage:string
  Returns:
    stage:string
    choice:string
  """
  print("You have arrived at: THE EMERALD PALACE 🟢💎🏰💎🟢")
  print("A large palace filled with tall towering towers made of emeralds and other precious gems. What an opulecent place!")
  #Ask user to press "ENTER" to continue
  input("Press 'ENTER' to continue\n")

  #Boolean that runs commands depending on which stage of the adventure the user is at. The program will keep track of at what stage the user is at by using the variable 'stage'.
  if (stage == 0): #User's first time in Emerald Palace + Ozland
    #Print Welcome
    print("🧙: Welcome, distressed being! My name is the Wizard of Oz, and welcome to Ozland!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😮 (You): Ozland? What kind of blasphemy is this? How do I get back home?? I have a physics test I need to study for ASAP!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙: Physics test??? Oh my, I have seen nary such a tumultuous conquest! In order to get back, you will need to complete 3 missions for me. After you complete these missions, you can go back home using my PortKey.")
    print("\n🙂: Sounds great! What's my first mission?")
    print("\n🧙: Your first mission is to go to the shoe store and get yourself some nice red shoes, because let's be honest, your current footwear won't cut it.")
    print("\n😮: What to you mean it won't cut it!?!?! FINE FINE, I suppose i'll go get some new shoes....")
    #Print demand for user to go to shoe store for shoe store mission
    print("\n*MISSION 1: Go to the shoestore to get *red* shoes!*")
    #Set stage = 1 to allow for according changes to be made in the program to account for the change of stage of the game
    stage = 1
  elif (stage == 2): #User's second time in Emerald Palace, after completing shoe mission
    #Print greeting, applause, and instructions 
    print("🧙: Hooray! You did it! Nice Job! \nYour second mission is to go to the forest and fight the trees to collect apples. 5 apples will do.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😶: I'm sorry, did you say I need to FIGHT the trees?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙: Yes, now run along!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😮: What the-") 
    #Print demand for user to go to forest for tree mission
    print("\n*MISSION 2: Go get 5 apples from the trees in the forest!*")
    #Set stage = 3 to allow for according changes to be made in the program to account for the change of stage of the game
    stage = 3
  elif (stage == 4): #User's third time in Emerald Palace, after completing tree mission
    #Print greeting and applause
    print("🧙: Impeccable job! I knew you could do it! Now, I have one final mission for you. In the West, there is a Wicked Witch who has been known for centuries for being responsible for all the horrors of the world.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🙂: Ok and...? I need to fight the witch, I'm guessing?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙:...No. \nYou need to go help her come to terms with her evilness.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😮: I'm sorry, WHAT???? I've been Ozland for less than a day, and you expect me to somehow cure an evilness that has plagued your lands for centuries??")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙: Fear not, I know that you can do it if you try!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🙂:*Sigh* Okay, I suppose i'll give it a go.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙: Excellent! Good luck!!")
    #Tell users to face the wicked witch of the west
    print("\nMISSION 3: Help the witch turn good!")
    #Set stage = 5 to allow for according changes to be made in the program to account for the change of stage of the game
    stage = 5
  elif (stage == 8): #User's fourth time in Emerald Palace, after completing wicked witch mission
    #Print welcome message and tell them they can finally go back home
    print("🧙: You're back! Finally! I was worried that you were turned into a rat by the witch!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😮: WAIT WHAT? A RAT?!?!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙: By the way, I stole- I mean, found the PortKey you can use to get back home! Thank you very much for completing those missions! Safe travels, and goodbye!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😀: Oh, that's wonderful news. Thank you so much! Goodbye! \n*Meanwhile: A very confused Harry Potter looking for his PortKey ⚡🤓*")
    #Set stage = 9 to allow for according changes to be made in the program to account for the change of stage of the game
    stage = 9
    #Call function to take the user back home!
    home()
    #Set choice = 'q' and end program/adventure game
    choice = 'q'
    return choice, stage
  elif (stage == 10): #User lost in Mission 1
    #Print message from wizard to retry
    print("🧙: Oh no! You lost! No problem, there is a way to fix this. I will let you travel back in time to fix your mistakes and give you a chance to try again. Good luck, you got this!")
    #Set stage = 1 so user can go back in time to the shoestore and try again
    stage = 1
  else: #'Mark' variable does not match with any of the conditions above; the user is in the wrong place
    #Print message telling them that they are in the wrong place - they have an unaccomplished mission and that they should go back and fulfill it
    print("*Are you lost, weary traveller? You are in the wrong place - you currently have an unaccomplished mission elsewhere to finish. Come back here later when you're done, and maybe you can access this location then!")
    
  #Ask user where they would like to go.
  choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \nPress "w" to go to the Wicked Witch of the Wests Palace \n')
  #Validate user input. While input invalid, ask the user to type in a valid symbol for a valid location
  while (choice.lower() != "e" and choice.lower() != "s" and choice.lower() != "f" and choice.lower() != "w"):
    #Tell user that their input is invalid
    print("Your input is invalid. Please type a valid symbol for a valid location. ")
    #Re-ask user where they would like to go.
    choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \nPress "w" to go to the Wicked Witch of the Wests Palace \n')

  #Clear the screen
  os.system('clear')

  #Return choice and stage variables
  return choice, stage
  
#Define shoe store function
def shoeStore(point):
  """
  Prints shoe store description, as well as certain commands depending on at which point in the game the user is at (aka. value of the point variable)
  Args:
    point:string
  Returns:
    point:string
    choice:string
  """
  print("You have arrived at: THE SHOE STORE 👟🏪👟")
  print("Welcome to Ozzy's Shoes! The SHOE-perb stop for all things shoe! There are rows and rows of shoes galore - here, at Ozzy's shoes, rest assured that all your footwear-related problems will be solved!")
  #Ask user to press "ENTER" to continue
  input("Press 'ENTER' to continue\n")
  #Boolean that runs commands depending on which stage of the adventure the user is at. The program will keep track of at what stage the user is at by using the variable 'point'.
  if (point == 1): #User's first time in shoe store, during shoe store mission
    #Print Welcome and Instructions for Mission 1 Game
    print("👨: Welcome to the most glorious shoe store in all of OzLand! My name is Deshoemaker and I am the shoe maker at Ozzy's shoes! What can I help you wi- OH MY! THE DISGRACE! THE HORROR! THE MONSTROSITY!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😮 (You): What? What is it? What's wrong?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n👨: It's your shoes, they're....absolutely HORRENDOUS!!!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😑:........ \n*Sigh* OK ANYWAYS so I was tasked by the Wizard of Oz to get some nice red shoes. Could you please help me get some?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n👨: Why of course! You've come to the right place. Unfortunately, the red shoes are an exclusive that are only available to people who pass the following test. If you miss a question, you will completely lose your chance to get the red shoes. You think you've got the guts to do it?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😀: Well, I don't really have a choice, so let's do it! ")
    
    #Mission 1 quiz game - If the user wins they get the shoes. If they loose, they must restart from the emerald palace
    #QUESTION 1
    #Create a list to store question 1, its answer options, and the correct answer. All this will be used later to display the question to the user, and to check whether or not the user is correct.
    question1 = ["Question 1:  Which song was almost cut from The Wizard of Oz?", "A) We're off to see the wizard", "B) If only I had a brain", "C) The lollipop guild", "D) Over the rainbow", "A"]
    #Use for loop to print the questions and answer options (but not the actual answer)
    print("\n")
    for i in range(0, len(question1)-1):
      print(question1[i])
    #Ask for and get user input
    question1Input = input("\nPlease type your answer: ")
    #Validate user input using while loop. While users input is invalid, re-ask the question and make them type another answer
    while (question1Input.upper() != "A" and question1Input.upper() != "B" and question1Input.upper() != "C" and question1Input.upper() != "D"):
      #Tell the user that their iinput is invalid
      print("Your input is invalid. Please verify your input and try again.")
      #Re-ask the question to the user, using a for loop as done previously/originally
      for i in range(0, len(question1)-1):
        print(question1[i])
      #Ask for and get user input
      question1Input = input("\nPlease type your answer: ")
    #Depending on if the user answered correctly, print the according text
    #If user loses, send them back to the emerald palace
    if (question1Input.upper() == question1[5]):
      print("\nGood job! That is correct!")
    elif (question1Input != question1[5] or question1Input.upper() == "B" or question1Input.upper() == "C" or question1Input.upper() == "D"):
      print("\nThat is incorrect! You lose - better luck next time! \n")
      #Set choice = 'e' and point = 10 so the user can restart from the emerald palace
      choice = 'e'
      point = 10
      #Return choice and point so the user can switch locations and timelines accordingly
      return choice, point

    #QUESTION 2
    #Create a list to store question 2, its answer options, and the correct answer. All this will be used later to display the question to the user, and to check whether or not the user is correct.
    question2 = ["Question 2:  Who did Dorothy meet first?", "A) Cowardly Lion", "B) Scarecrow", "C) Patchwork Girl", "D) Tin Man", "B"]
    #Use for loop to print the questions and answer options (but not the actual answer)
    print("\n")
    for c in range(0, len(question2)-1):
      print(question2[c])
    #Ask for and get user input
    question2Input = input("\nPlease type your answer: ")
    #Validate user input using while loop. While users input is invalid, re-ask the question and make them type another answer
    while (question2Input.upper() != "A" and question2Input.upper() != "B" and question2Input.upper() != "C" and question2Input.upper() != "D"):
      #Tell the user that their iinput is invalid
      print("Your input is invalid. Please verify your input and try again.")
      #Re-ask the question to the user, using a for loop as done previously/originally
      for c in range(0, len(question2)-1):
        print(question2[c])
      #Ask for and get user input
      question2Input = input("\nPlease type your answer: ")
    #Depending on if the user answered correctly, print the according text
    #If user loses, send them back to the emerald palace
    if (question2Input.upper() == question2[5]):
      print("\nGood job! That is correct!")
    elif (question2Input != question2[5] or question2Input.upper() == "A" or question2Input.upper() == "C" or question2Input.upper() == "D"):
      print("\nThat is incorrect! You lose - better luck next time! \n")
      #Set choice = 'e' and point = 10 so the user can restart from the emerald palace
      choice = 'e'
      point = 10
      #Return choice and point so the user can switch locations and timelines accordingly
      return choice, point

    #QUESTION 3
    #Create a list to store question 3, its answer options, and the correct answer. All this will be used later to display the question to the user, and to check whether or not the user is correct.
    question3 = ["Question 3:  Are red shoes better than your old shoes?", "A) Hmm, a bit", "B) Yes, they are SO much bettter", "C) Nope, not at all", "D) Of course not!", "B"]
    #Use for loop to print the questions and answer options (but not the actual answer)
    print("\n")
    for v in range(0, len(question3)-1):
      print(question3[v])
    #Ask for and get user input
    question3Input = input("\nPlease type your answer: ")
    #Validate user input using while loop. While users input is invalid, re-ask the question and make them type another answer
    while (question3Input.upper() != "A" and question3Input.upper() != "B" and question3Input.upper() != "C" and question3Input.upper() != "D"):
      #Tell the user that their iinput is invalid
      print("Your input is invalid. Please verify your input and try again.")
      #Re-ask the question to the user, using a for loop as done previously/originally
      for v in range(0, len(question3)-1):
        print(question3[v])
      #Ask for and get user input
      question3Input = input("\nPlease type your answer: ")
    #Depending on if the user answered correctly, print the according text
    #If user loses, send them back to the emerald palace
    if (question3Input.upper() == question3[5]):
      print("\nGood job! That is correct!")
    elif (question3Input != question3[5] or question3Input.upper() == "A" or question3Input.upper() == "C" or question3Input.upper() == "D"):
      print("\nThat is incorrect! You lose - better luck next time! \n")
      #Set choice = 'e' and point = 10 so the user can restart from the emerald palace
      choice = 'e'
      point = 10
      #Return choice and point so the user can switch locations and timelines accordingly
      return choice, point
    
    #Print congratulations method if you finished
    print("Congratulations! You completed all the quiz questions correctly! As promised, here are your shoes!")
    #Tell user their mission is done and they can go back to the wizard now
    print("*MISSION 1: COMPLETE! Return back to the Emerald Palace.*")
    #Set point = 2 to allow for according changes to be made in the program to account for the change of stage of the game
    point = 2
  elif (point == 6): #User's second time in shoestore, during wicked witch mission
    #Print diologue telling user that they have gotten the shoes for the Wicked Witch
    print("👨: Oh hello there once again! How may I help you?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😀(You): Well, you see, I'm wondering if I could get a pair of blue shoes for the Wicked Witch of the West? It's for my mission, its a long story.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n👨: Well, you came at a good time! I just got a restock in blue shoes. Voila! Here are your shoes, good luck with your mission!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😀: Thanks so much! I will be on my way now!")
    #Tell user to go back to the witch now to finish their mission
    print("\n*Return back to the Wicked Witch of the West to make sure you brought her the right pair of shoes.*")
    #Set point = 7 to allow for according changes to be made in the program to account for the change of stage of the game
    point = 7
  else: #'Mark' variable does not match with any of the conditions above; the user is in the wrong place
    #Print message telling them that they are in the wrong place - they have an unaccomplished mission and that they should go back and fulfill it
    print("*Are you lost, weary traveller? You are in the wrong place - you currently have an unaccomplished mission elsewhere to finish. Come back here later when you're done, and maybe you can access this location then!")

  #Ask user where they would like to go.
  choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \nPress "w" to go to the Wicked Witch of the Wests Palace \n')
  #Validate user input. While input invalid, ask the user to type in a valid symbol for a valid location
  while (choice.lower() != "e" and choice.lower() != "s" and choice.lower() != "f" and choice.lower() != "w"):
    #Tell user that their input is invalid
    print("Your input is invalid. Please type a valid symbol for a valid location. ")
    #Re-ask user where they would like to go.
    choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \nPress "w" to go to the Wicked Witch of the Wests Palace \n')
  
  #Clear the screen
  os.system('clear')

  #Return choice variable
  return choice, point

#Define forest function
def forest(stg):
  """
  Prints forest description, as well as certain commands depending on at which point in the game the user is at (aka. value of the stg variable)
  Args:
    stg:string
  Returns:
    stg:string
    choice:string
  """
  print("You have arrived at: THE FOREST 🌲🌳")
  print("Welcome to the forest, thick, green, and abundant in fighting trees! Watch your step, lest you get hit with apples!")
  #Ask user to press "ENTER" to continue
  input("Press 'ENTER' to continue\n")

  #Boolean that runs commands depending on which stage of the adventure the user is at. The program will keep track of at what stage the user is at by using the variable 'stg'.
  if (stg == 3): #User's first time in forest
    #Print Welcome
    print("*Tree Noises* \n🍁: WHO GOES THERE! I AM THE TREE SPIRIT! ANYONE WHO CROSSES ME SHALL BE CUT DOWN IMMEDIATELY!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😑 (You):...I did NOT sign up for this. \nAnyways, hello Mr. Tree Spirit. I am REALLY sorry to bother you, but I need to get 5 of your apples so I can complete my missions and head back to my house so I can study for my physics test.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🍁: NO WAY- Wait, did you say physics test??? Alright, then I suppose I shall make an exception for you. If you can beat me in a battle, then I will give you 5 of my apples, deal?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😀: Fine! You have a deal!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    #Mission 2 game - Math battle with tree spirit through math calculations. If user wins, user gets apples. If user loses, user must restart whole game.
    #Print instructions for game for user
    print("😀:...Um so how are we going to fight? Like, am I gonna get a sword or something?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🍁: What could you possibly be thinking! Do you assume that this will be a fight with swords or weapons? PREPOSTEROUS! This will be a fight between intellectuals, hence, a fight between....MATH.")
    
    #QUESTION 1
    #Print question
    print("\nQuestion 1: You are standing 5m away from the tree. The tree is perfectly straight/perpendicular to the ground, and it has a height of 12m. Calculate the angle of elevation from you to the top of the tree. Please input your answer in degrees, as an integer to 0 decimal places. ")
    question1Answer = int(input("Your answer: "))
    #If the user got the answer correct (aka question1Answer = the actual answer), they can continue. While they have the answer wrong, they need to try again:
    while (question1Answer != 67):
      print("That is incorrect. Please try again. ")
      print("\nQuestion 1: You are standing 5m away from the tree. The tree is perfectly straight/perpendicular to the ground, and it has a height of 12m. Calculate the angle of elevation from you to the top of the tree. Please input your answer in degrees, as an integer to 0 decimal places. ")
      question1Answer = int(input("Your answer: "))
    print("\nRight-On! That is correct!")
    
    #QUESTION 2
    #Print question
    print("\nQuestion 2: In total, the tree has x number of apples. If 0 = (x+4)(x-2), calculate the value of x. Please input your answer as an integer, to 0 decimal places. ")
    question2Answer = int(input("Your answer: "))
    #If the user got the answer correct (aka question2Answer = the actual answer), they can continue. While they have the answer wrong, they need to try again:
    while (question2Answer != 2):
      print("That is incorrect. Please try again. ")
      print("\nQuestion 2: In total, the tree has x number of apples. If 0 = (x+4)(x-2), calculate the value of x. ")
      question2Answer = int(input("Your answer: "))
    print("\nRight-On! That is correct!")

    #Print congratulations for winning statement
    print("🍁: Congratulations! You won our fight! I am most impressed with your mathematics skills! As promised, here are your 5 apples. \n😀: Thank you, I will be on my way now! Farewell!")
    #Tell user their mission is complete and they can go back to the wizard now
    print("*MISSION 2: COMPLETE! Return back to the Emerald Palace.*")
    #Set stg = 4 to allow for according changes to be made in the program to account for the change of stage of the game
    stg = 4
  else: #'Mark' variable does not match with any of the conditions above; the user is in the wrong place
    #Print message telling them that they are in the wrong place - they have an unaccomplished mission and that they should go back and fulfill it
    print("*Are you lost, weary traveller? You are in the wrong place - you currently have an unaccomplished mission elsewhere to finish. Come back here later when you're done, and maybe you can access this location then!")

  #Ask user where they would like to go.
  choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \n')
  #Validate user input. While input invalid, ask the user to type in a valid symbol for a valid location
  while (choice.lower() != "e" and choice.lower() != "s" and choice.lower() != "f" and choice.lower() != "w"):
    #Tell user that their input is invalid
    print("Your input is invalid. Please type a valid symbol for a valid location. ")
    #Re-ask user where they would like to go.
    choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \n')

  #Clear the screen
  os.system('clear')

  #Return choice variable
  return choice, stg
  
#Define wicked witch function
def wickedWitch(place):
  """
  Prints wicked witch's palace's description, as well as certain commands depending on at which point in the game the user is at (aka. value of the place variable)
  Args:
    place:string
  Returns:
    place:string
    choice:string
  """
  print("You have arrived at: THE WICKED WITCH OF THE WEST'S PALACE 🧙‍♀️")
  print("A dark, deep violet palace, with a strange scent of plums. Beware, for this witch is not fair. Regarded as cruel, cold, mean, and old, the Wicked Witch of the West is someone you do NOT want to cross.")
  #Ask user to press "ENTER" to continue
  input("Press 'ENTER' to continue\n")
  
  #Boolean that runs commands depending on which stage of the adventure the user is at. The program will keep track of at what stage the user is at by using the variable 'place'.
  if (place == 5): 
    #User intro
    print("🧙‍♀️: WHO DARES DISTURB ME DURING MY BEAUTY SLEEP! I am the Wicked Witch of the West, and such a crime will not go unpunished!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😬: Um, hi...That would be me. But before you do anything, please allow me to explain myself. I am stuck in Ozland and need to return home. However, I have been told by the Wizard of Oz that I cannot return home until I complete some missions. My last mission is to help you turn good and stop your evil ways.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙‍♀️: HAH, that's funny. Hundreds have been sent to accomplish this mission why do you think YOU can, then?")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😬: Could you please please try to co-operate? I have a physics test I need to study for and I really need to get back home so I can study for it.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n🧙‍♀️: WHAT? REALLY? Why didn't you say so earlier? FINE, if you are able to get me some nice blue shoes from the Deshoemaker's store, I will turn good.")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😀: Really? OK, SOUNDS AWESOME! That's surprisingly easy...")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    #Print demand for mission 3.1
    print("\n*MISSION 3.1: Go to the shoestore to get *blue* shoes!*")
    #Set stage = 1
    #Set place = 6 to allow for according changes to be made in the program to account for the change of stage of the game
    place = 6
  elif (place == 7):
    #Tell user thanks and goodbye
    print("🧙‍♀️: Thank you very much! These are indeed the shoes I want! I will turn good now, thank you! Ta-ta now!")
    #Ask user to press "ENTER" to continue
    input("Press 'ENTER' to continue\n")
    print("\n😀: You are welcome! Wow, that was easier than I thought it would be...")
    #Tell user their mission is complete and they can go back to the wizard now
    print("*MISSION 3: COMPLETE! Return back to the Emerald Palace.*")
    #Set place = 8 to allow for according changes to be made in the program to account for the change of stage of the game
    place = 8
  else: #'Mark' variable does not match with any of the conditions above; the user is in the wrong place
    #Print message telling them that they are in the wrong place - they have an unaccomplished mission and that they should go back and fulfill it
    print("*Are you lost, weary traveller? You are in the wrong place - you currently have an unaccomplished mission elsewhere to finish. Come back here later when you're done, and maybe you can access this location then!")
        
  #Ask user where they would like to go.
  choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \n')
  #Validate user input. While input invalid, ask the user to type in a valid symbol for a valid location
  while (choice.lower() != "e" and choice.lower() != "s" and choice.lower() != "f" and choice.lower() != "w"):
    #Tell user that their input is invalid
    print("Your input is invalid. Please type a valid symbol for a valid location. ")
    #Re-ask user where they would like to go.
    choice = input('\nWhere would you like to go? \nPress "e" to go to the Emerald Palace \nPress "s" to go the Shoe Store \nPress "f" to go to the Forest \n')

  #Clear the screen
  os.system('clear')

  #Return choice variable
  return choice, place

#-----MAIN PROGRAM-----#
#-----Welcome-----#
#Print game welcome/introduction for user
print("Welcome to the OzLand Adventure! You will be transported to OzLand, and will need to complete a series of missions in order to return back home! Are you ready? Do you have what it takes? Good luck!")

#Ask user to press "ENTER" to continue
input("Press 'ENTER' to continue\n")

#Clear the screen for organization purposes
os.system('clear')
#-----Introduction-----#
#Run home function
home()
#Run trouble function
trouble()
#Run tornado function
tornado()
#-----Core Program-----#
#Run emerald palace function. Use choice of destination to run choice function
choice, mark = emeraldPalace(mark)
#Continue taking the values of the choice variable throughout the game to control the location of the user
#While loop - as long as the user does not finish the game (i.e. choice is not equal to 'q'), this boolean will continue running
while (choice.lower() != 'q'):
  if (choice.lower() == 'e'):
    choice, mark = emeraldPalace(mark)
  elif (choice.lower() == 's'):
    choice, mark = shoeStore(mark)
  elif (choice.lower() == 'f'):
    choice, mark = forest(mark)
  elif (choice.lower() == 'w'):
    choice, mark = wickedWitch(mark)
#-----Ending-----#
#When while loop breaks (i.e. user finishes game and choice = 'q', print ending message
print("The end! Thanks for playing!")

