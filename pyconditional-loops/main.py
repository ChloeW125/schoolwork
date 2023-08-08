"""
U3-A1-ConditionsLoopsAssignment
ICS3U-04
Chloe Wei
Follow the instructions in the console to bake your own cake!
History:
Oct 13, 2022: Program Creation
Oct 17, 2022: Input code finished
Oct 19, 2022: Turtles cake-drawing feature started
Oct 21, 2022: Frosting swirl added, comments updated, last minute details added, and assignment submitted
"""

"""
Turtles links
Check out the official docs here: https://docs.python.org/3/library/turtle.html

References:
Code to give turtle pen drawings fill colour: https://drive.google.com/file/d/19Vs7MFY3c0JP5lrMpsj2ypxdQromu_r9/view (Given by Amelie Tam, who got it from Mrs. Edwards)
Code for circle cake frosting swirl: 
https://www.geeksforgeeks.org/draw-circle-in-python-using-turtle/ 
Color options/ideas for python program cake flavours/icing colours: https://matplotlib.org/stable/gallery/color/named_colors.html

Tutorial:
https://realpython.com/beginners-guide-python-turtle/
"""
#Initialize variable that will control whether the program continues to run or not. Ensure that this variable value is different from that used in the massive while loop that controls the amount of times the game is run (seen below). This way, the while loop's condition will automatically be true when the game starts (because when play = 'run', the while loop's condition that play != 'exit' is met), ensuring that the user is able to play the game.
play = 'run'

#Import turtle commands and programs
import turtle

#Create a turtle baker to draw the cake
turtleBaker = turtle.Turtle()

#Change the shape of the turtle to an arrow
turtleBaker.shape("arrow")

#While loop that keep the game running over and over again until the user tells the program that it wants to stop playing. (In the case the user wants to stop playing, the while loop will break because the condition that runs the while loop will no longer be true (play will no longer not be equal to 'exit').)
while (play != 'exit'):
  #----------INTRODUCTION-----------#
  #Clear the screen
  turtleBaker.clear()
  
  #Print intro instructions
  print("Welcome to 'Bake-A-Cake'! The perfect place to bake your dream cake! Answer the prompts to decide what you want inside your cake, and when your ready to reveal your final cake product, sit back and wait for your turtle baker to make your a sweet surprise! Note: After answering a prompt, don't forget to press 'ENTER' on your keyboard to submit your answer to the turtle baker!")

  #----------INGREDIENT SELECTION AND SPECIFICATION-----------#
  #Print "line seperator" for print screen organization and asthetic purposes
  print("---------------------------------------------------")
  
  #Ask user if they want eggs in their cake
  eggs = input("Do you want eggs in your cake? \nIf you want eggs in your cake, enter 'y'. \nIf you do not want eggs, enter 'n'. ")

  #If the user gives invalid input for eggs, this while loop will run until the user gives valid input. Its condition includes a compound boolean. In this way, the while loop will run whenever a value that isn't one of the expected values is inputted by the user. In the while loop, the program will continue to tell the user that their given input was invalid and that they need to input a valid value. The while loop will keep running until the conditions of the while loop are no longer true - that is, when eggs = y or eggs = n
  while (eggs != 'y' and eggs!= 'n'):
    #Tell the user their input was invalid
    print("This input is invalid, please try again and enter a valid input.")
    #Re-prompt the user to enter input for the eggs ingredient prompt
    eggs = input("Do you want eggs in your cake? \nIf you want eggs in your cake, enter 'y'. \nIf you do not want eggs, enter 'n'. ")

  #Print "line seperator" for print screen organization and asthetic purposes
  print("---------------------------------------------------")

  #Ask user if what flavour they want their cake to be
  flavour = input("Do you want a vanilla, chocolate, or strawberry cake? .\nIf you want a vanilla cake, enter 'v'. \nIf you want a chocolate cake, enter 'c'. \nIf you want a strawberry cake, enter 's'. ")

  #If the user gives invalid input for flavour, this while loop will run until the user gives valid input. Its condition includes a compound boolean. In this way, the while loop will run whenever a value that isn't one of the expected values is inputted by the user. In the while loop, the program will continue telling the user that their given input was invalid and that they need to input a valid value. The while loop will only stop when the user is able to break out of the loop by providing a flavour input that does not meet the conditions of the while loop - that is, when flavour = v or flavour = c or flavour = s
  while (flavour != 'v' and flavour != 'c' and flavour != 's'):
    #Tell the user their input was invalid
    print("This input is invalid, please try again and enter a valid input.")
    #Re-prompt the user to enter input for the flavour ngredient prompt
    flavour = input("Do you want a vanilla, chocolate, or strawberry cake? .\nIf you want a vanilla cake, enter 'v'. \nIf you want a chocolate cake, enter 'c'. \nIf you want a strawberry cake, enter 's'. ")
 
  #Print "line seperator" for print screen organization and asthetic purposes
  print("---------------------------------------------------")

  #Ask user what kind of icing they want on their cake
  icing = input("Do you want vanilla, chocolate, or strawberry icing? .\nIf you want vanilla icing, enter 'v'. \nIf you want chocolate icing, enter 'c'. \nIf you want strawberry icing, enter 's'. ")

  #If the user gives invalid input for icing, this while loop will run until the user gives valid input. Its condition includes a compound boolean. In this way, the while loop will run whenever a value that isn't one of the expected values is inputted by the user. In the while loop, the program will continue telling the user that their given input was invalid and that they need to input a valid value. The while loop will only stop when the user is able to break out of the loop by providing a flavour input that does not meet the conditions of the while loop - that is, when flavour = v or flavour = c or flavour = s
  while (icing != 'v' and icing != 'c' and icing != 's'):
    #Tell the user their input was invalid
    print("This input is invalid, please try again and enter a valid input.")
    #Re-prompt the user to enter input for the icing ingredient prompt
    icing = input("Do you want vanilla, chocolate, or strawberry icing? .\nIf you want vanilla icing, enter 'v'. \nIf you want chocolate icing, enter 'c'. \nIf you want strawberry icing, enter 's'. ")

  #Print "line seperator" for print screen organization and asthetic purposes
  print("---------------------------------------------------")

  #Ask user how big they want their cake to be 
  #Specify the length input as an integer to ensure that the value can be used for the length of the cake later on.
  length = input("What length do you want your cake to be? Please enter an integer, most preferably between 100 and 300 for the best results. ")
  
  #If the user gives invalid input for the length, this while loop will run until the user gives valid input. Its condition tries and checks to see if the entered input is an integer. If it is not, the program will re-promtp the user to enter a valid length. The while loop will keep running until the user enters a valid length input
  #Initialize variable for validity of entered input
  invalid = True
  
  while (invalid == True):
    try:
      #Check to see if the entered input is an integer by using typecasting. This is integrated here through the use of the syntax "int()" around the length variable
      length = int(length)
      #Exit while loop if input is an integer
      invalid = False
    except:
      #In the case the input was not an integer, tell the user their input was invalid
      print("This input is invalid, please try again and enter a valid input.")
      length = input("What length do you want your cake to be? Please enter an integer, most preferably between 100 and 300 for the best results. ")
  
  #Print "line seperator" for print screen organization and asthetic purposes
  print("---------------------------------------------------")
  
  #Ask user what shape they want their cake to be
  cakeShape = input("What shape do you want your cake to be? \nIf you want your cake to be a circle, enter 'circle'. \nIf you want the cake to be a square, enter 'square'. ")

  #If the user gives invalid input for the shape of the cake, this while loop will run until the user gives valid input. Its condition includes a compound boolean. In this way, the while loop will run whenever a value that isn't one of the expected values is inputted by the user. In the while loop, the program will continue to tell the user that their given input was invalid and that they need to input a valid value. The while loop will keep running until the conditions of the while loop are no longer true - that is, when cakeShape = circle or cakeShape = square
  while (cakeShape != 'circle' and cakeShape != 'square'):
    #Tell the user their input was invalid
    print("This input is invalid, please try again and enter a valid input.")
    #Re-prompt the user to enter input for the shape prompt
    cakeShape = input("What shape do you want your cake to be? \nIf you want your cake to be a circle, enter 'circle'. \nIf you want the cake to be a square, enter 'square'. ")
  
  #-----------BAKE THAT CAKE!------------#
  #Set the turtle pen outline colour to black
  turtleBaker.pencolor('black')

  #Stop the turtle from drawing and move the turtle to the default "cake drawing space" centered at the coordinate (50, 50)
  turtleBaker.penup()
  turtleBaker.goto(50, 50)
  
  #Draw different things on the canvas depending on the user's selection.
  
  #Condition based on cake shape
  #All of the following lines of code are part of a nested loop. First, the program determines whether or not the cake shape should be a circle or a rectangle. This is determined by the users cakeShape input value. Depending on the user's inputted cakeShape value, one of the statements will be true and will be further persued. The other if statement that must then be false (because there are only two options - one must be true while the other must be false) will simply be skipped over by the program, because the statement's condition is not true/not met

  
  #If the user chooses a circular cake, the following if statement will run. If the user does not choose a circular cake, the following if statement will be skipped over by the program. 
  if (cakeShape == 'circle'):
    #The user's flavour input (from earlier) will determine the colour of the cake. Depending on what input the user gave for flavour, the cake's colour/flavour will change accordingly. (ex. If the user chooses the vanilla flavour and inputs 'v', the turtle's pen colour and cake colour will set to a beige colour representing vanilla. The other conditions in the if statement (i.e. elif flavour == 'c', elif flavour == 's' will be skipped over because they do not apply tp the situation (the user didn't pick them)).)
    #An if statement is used for these values to easily assign flavour values depending on the condition of the flavour input variable.
    if (flavour == 'v'):
      turtleBaker.pencolor('beige')
      cakeColour = 'beige'
    elif (flavour == 'c'):
      turtleBaker.pencolor('peru')
      cakeColour = 'peru'
    elif (flavour == 's'):
      turtleBaker.pencolor('pink')
      cakeColour = 'pink'

    #Draw circle cake
    #Put the turtle's pen down so it can draw objects once again
    turtleBaker.pendown()
    
    #Fill cake with flavour colour determined earlier in the conditional statement above (cakeColour variable). The source for this part of the code can be found at the top ofnthe program beneath the header.
    turtleBaker.fillcolor(cakeColour)
    turtleBaker.begin_fill()
    turtleBaker.circle(length/2)
    turtleBaker.end_fill()
    turtleBaker.color(cakeColour)
    turtleBaker.fillcolor('white')

     #Just like what was done for the previous group of condition statements, the user's icing input (from earlier) will determine the colour of the icing of the cake. Depending on what input the user gave for the icing, the cake's icing colour will change accordingly. (ex. If the user chooses the chocolate icing and inputs 'c', the turtle's pen colour and cake colour will set to a chocolate colour representing chocolate. The other conditions in the if statement (i.e. elif icing == 'v', elif icing == 's' will be skipped over because they do not apply tp the situation (the user didn't pick them)).)
    #Again, an if statement is used for these values to easily assign icing values depending on the condition of the icing input variable.
    if (icing == 'v'):
      turtleBaker.pencolor('goldenrod')
      icingColour = 'goldenrod'
    elif (icing == 'c'):
      turtleBaker.pencolor('sienna')
      icingColour = 'sienna'
    elif (icing == 's'):
      turtleBaker.pencolor('lightcoral')
      icingColour = 'lightcoral'

    #Draw icing on cake
    #Put the turtle's pen up so it cannot draw objects while it moves
    turtleBaker.penup()
    
    #Move the turtle to the default "cake drawing space" centered at the coordinate (50, 50)
    turtleBaker.goto(50, 50)
    
    #Put the turtles pen down so its drawing is visible again
    turtleBaker.pendown()

    #Change the pen weight to ensure that the frosting lines are clearly visible on the cake
    turtleBaker.pensize(3)
    
    #Fill icing with icing colour determined earlier in the condition above (icingColour variable) based on what icing the user inputted.
    #In order to draw the icing, which is a swirl, the program uses a for loop to execute repetitive tasks in an easy and concise way. The turtle draws a circle at half the value of the length (so it can use the randius as the diameter of the circle) and then subtracts it from the d value in the range. Because d grows with each "round of looping", the product of the equation length/2 - d shrinks over time, decreasing the radius of the swirl and allowing for the swirled frosting effect. The source used to create this part can be found at the top of the program, below the header.
    turtleBaker.fillcolor(icingColour)
    for d in range(75):
      turtleBaker.circle(length/2 - d, length/4)
    turtleBaker.color(icingColour)
    turtleBaker.fillcolor('white')

    #Else, if the user chooses a square cake rather than a circle cake, the following if statement will run. If the user does not choose a square cake, the following if statement will be skipped over by the program because the condition (cakeShape == 'square') is not being met. 
  elif (cakeShape == 'square'):
    #This code is the same code used for the conditional flavour statement for the circular cake, because the shape of the cake has no impact on the colour of the cake.
    #The user's flavour input (from earlier) will determine the colour of the cake. Depending on what input the user gave for flavour, the cake's colour/flavour will change accordingly. (ex. If the user chooses the vanilla flavour and inputs 'v', the turtle's pen colour and cake colour will set to a beige colour representing vanilla. The other conditions in the if statement (i.e. elif flavour == 'c', elif flavour == 's' will be skipped over because they do not apply tp the situation (the user didn't pick them)).)
    #An if statement is used for these values to easily assign flavour values depending on the condition of the flavour input variable.
    if (flavour == 'v'):
      turtleBaker.pencolor('beige')
      cakeColour = 'beige'
    elif (flavour == 'c'):
      turtleBaker.pencolor('peru')
      cakeColour = 'peru'
    elif (flavour == 's'):
      turtleBaker.pencolor('pink')
      cakeColour = 'pink'

    #Draw square cake
    #Put the turtle's pen down so it can draw objects once again
    turtleBaker.pendown()
    
    #Fill cake with flavour colour determined earlier in the conditional statement above (cakeColour variable). The source for this code can be found at the top of the program, beneath the header.
    turtleBaker.fillcolor(cakeColour)
    turtleBaker.begin_fill()
    
    #Move the turtle to the default "cake drawing space" centered at the coordinate (50, 50)
    turtleBaker.goto(50, 50)
    
    #For loop to make the drawing of the square cake more efficient. For every single value in the range 1 to 4 at an increasing interval of 1 and at a starting value of 1, the program will make the turtle draw the length of the cake and then make the turtle turn 90 degrees to the right so it can keep drawing these lines until the square shape of the cake is complete. This is much more efficient than repetitively directly asking the program to move forward a certain length, then turn 90 degrees, then move forward a certain length again, then turn 90 degrees...). 
    for i in range(1, 4):
      turtleBaker.forward(length)
      turtleBaker.right(90)
    turtleBaker.end_fill()
    turtleBaker.color(cakeColour)
    turtleBaker.fillcolor('white')

      #This code is the same code used for the conditional icing statement for the circular cake, because the shape of the cake has no impact on the colour of the icing of the cake. 
    #Just like what was done for the previous group of condition statements, the user's icing input (from earlier) will determine the colour of the icing of the cake. Depending on what input the user gave for the icing, the cake's icing colour will change accordingly. (ex. If the user chooses the chocolate icing and inputs 'c', the turtle's pen colour and cake colour will set to a chocolate colour representing chocolate. The other conditions in the if statement (i.e. elif icing == 'v', elif icing == 's' will be skipped over because they do not apply tp the situation (the user didn't pick them)).)
    #An if statement is used for these values to easily assign icing values depending on the condition of the icing input variable.
    if (icing == 'v'):
      turtleBaker.pencolor('goldenrod')
      icingColour = 'goldenrod'
    elif (icing == 'c'):
      turtleBaker.pencolor('sienna')
      icingColour = 'sienna'
    elif (icing == 's'):
      turtleBaker.pencolor('lightcoral')
      icingColour = 'lightcoral'

    #Draw icing on cake
    #Put the turtle's pen up so it cannot draw objects while it moves
    turtleBaker.penup()
    
    #Move the turtle to the default "cake drawing space" centered at the coordinate (50, 50)
    turtleBaker.goto(50, 50)
    
    #Make further adjustments to the turtle's pen starting position so as to ensure that the pen starts in the right place to draw the icing (that is, to ensure that the pen starts drawing while it is on the cake).
    turtleBaker.forward(-length/4)
    turtleBaker.right(90)
    turtleBaker.forward(length/4)
    turtleBaker.left(90)
    
    #Put the turtle's pen down so it can draw objects once again
    turtleBaker.pendown()
    
    #Fill icing with icing colour determined earlier in the condition above (icingColour variable). The source for this code can be found at the top of the program, beneath the header.
    turtleBaker.fillcolor(icingColour)
    turtleBaker.begin_fill()
    
    #Once again, use a for loop to draw the icing. The nature of this for loop is identical to that of the for loop used to draw the square cake in itself. The only difference between this for loop and the other for loop is that this for loop draws a smaller square. In this way, we can ensure that the cake is visible from beneath the icing
    for r in range(1, 4):
      turtleBaker.right(90)
      turtleBaker.forward(length/2)
    turtleBaker.end_fill()
    turtleBaker.color(icingColour)
    turtleBaker.fillcolor('white')

  #Statement that is printed after cake is finished
  print("\nYum yum, your cake is done!")

  #Prompt the user to play again
  play = input("\nWould you like to play again and make another cake? Enter any key to play again, and enter 'exit' if you would like to stop playing. ")

  #Use an if statement to check whether or not the program should stop running. If the user types exit, the program will stop running because the program's massive while loop's condition that play != 'exit' will not longer be true. Similarly, if the user does not type 'exit', the program will keep running because the condition of the program's massive while loop is still true (play will still not be equal to 'exit')
  if (play == 'exit'):
    break 