/*
cwei1-Active Learning
Chloe Wei
June 2022
Welcome to Active Learning! Catch assignments and study notes while avoiding distractions to successfully graduate!

Image assets courtesy of https://github.com/molleindustria/p5.play/
Player Sprite Image: https://stackoverflow.com/questions/45569580/sprite-sheet-animation-with-arrow-keys
Opening Screen Background: https://pngtree.com/freebackground/autumn-student-school-cartoon-doodle-white-banner_1129580.html
Text Screen Backgrounds: https://www.pinterest.ca/pin/816629344914889460/
Game Screen Backgrounds: https://id.pikbest.com/video/mg-animation-shows-the-rain-outside-window-video_1363118.html
Assignment Clipart: https://www.istockphoto.com/vector/pile-of-work-paper-gm484597696-70699341
Nintendo Switch Distraction: https://www.mgpl.org/things/nintendo-switch
Fidget Spinner Distraction: https://www.dreamstime.com/fidget-spinner-vector-illustration-cartoon-kid-s-red-toy-image104564076
Study Notes: https://www.dreamstime.com/concept-stack-book-school-stuff-isolated-white-cartoon-vector-illustration-study-material-university-textbook-volume-image183040218
Certificate Template: http://clipart-library.com/clipart/8ixrGGLBT.htm
*/

/*---create/declare variables---*/
//create levels variable, set levels variable to 1
var levels = 1;

//create player sprite variable
var player;

//create player image variable
var playerImage;

//create player animation variable
var playerAnimation;

//create background variables
var bgSplash;
var bgWelcome;
var bgInstr1, bgInstr2, bgInstr3;
var bgUncertain;
var bgGame;
var bgLevel1Lose;
var bgLevel1Win;
var bgLevel2Lose;
var bgLevel2Win;
var bgFinalWin;
var bgEnding;

//create collectibles variables
var assign1; //should be collected, for level 1
var assign1; //should be collected, for level 2
var distract1; //should not be collected
var distract2; //should not be collected
var studyNotes; //should be collected

//create collectibles image variables
var assignImage;
var distract1Image;
var distract2Image;
var studyNotesImage;

//create collectible array x and y values
var assign1X = [22, 150, 640, 300, 500]; //for level 1
var assign1Y = [-322, -800, -1300, -700, -76]; //for level 1
var assign2X = [210, 30, 421, 700, 800]; //for level 2
var assign2Y = [-22, -510, -931, -740, -2010]; //for level 2
var distract1X = [300, 500, 210, 30, 421];
var distract1Y = [-422, -276, -12, -210, -630];
var distract2X = [700, 800, 10, 666, 100];
var distract2Y = [-80, -500, -140, -20, -480];
var studyNotesX = [640, 500, 210, 30, 111];
var studyNotesY = [-170, -43, -171, -650, -100];

//create collectibles velocity variables
var velocity;

//create heart image variable
var heart;

//create and set score counts for assignments and hearts
var assignCount = 0;
var heartCount = 3;

//create confetti velocity variable
var conVelocity = 0;

/*---preload function---*/
function preload() {
  //add the images to the player animation
  playerAnimation = loadAnimation("./Sprites/run_side1.png", "./Sprites/run_side4.png");

  //add image to the player image for when the user is stationary
  playerImage = loadImage("./Sprites/standing.png");

  //add the background images to their corresponding variables
  bgSplash = loadImage("./Backgrounds/bgSplashscreen.png")
  bgWelcome = loadImage("./Backgrounds/bgWelcome.png")
  bgInstr1 = loadImage("./Backgrounds/bgInstruc1.png")
  bgInstr2 = loadImage("./Backgrounds/bgInstruc2.png")
  bgInstr3 = loadImage("./Backgrounds/bgInstruc3.png")
  bgUncertain = loadImage("./Backgrounds/bgUncertainty.png")
  bgGame = loadImage("./Backgrounds/bgGameScreen.png")
  bgLevel1Lose = loadImage("./Backgrounds/bgLevel1Lose.png")
  bgLevel1Win = loadImage("./Backgrounds/bgLevel1Win.png")
  bgLevel2Lose = loadImage("./Backgrounds/bgLevel2Lose.png")
  bgLevel2Win = loadImage("./Backgrounds/bgLevel2Win.png")
  bgFinalWin = loadImage("./Backgrounds/bgFinalWin.png")
  bgEnding = loadImage("./Backgrounds/bgEnding.png")

  //preload collectible images
  assignImage = loadImage("./Collectibles/Assign.png")
  distract1Image = loadImage("./Collectibles/Fidget.png")
  distract2Image = loadImage("./Collectibles/Nintendo.png")
  studyNotesImage = loadImage("./Collectibles/StudyNotes.png")
}

/*---setup function*---*/
function setup() {
  //create canvas
  createCanvas(840, 480);

  //create all collectible sprites using groups
  assign1 = new Group();
  assign2 = new Group();
  distract1 = new Group();
  distract2 = new Group();
  studyNotes = new Group();

  //create player sprite
  player = createSprite(width / 2, 400);

  //scale player sprite
  player.scale = 2.3;

  //add the image to the player sprite
  player.addImage("standing", playerImage);

  //add the animation to the player sprite
  player.addAnimation("moving", playerAnimation);

  //make collectible groups
  for (var i = 0; i < 5; i++) {
    var tempAssign1 = createSprite(assign1X[i], assign1Y[i]);
    tempAssign1.addImage('standard', assignImage);
    tempAssign1.scale = 0.1;
    assign1.add(tempAssign1); //assignments for level 1

    var tempAssign2 = createSprite(assign2X[i], assign2Y[i]);
    tempAssign2.addImage('standard', assignImage);
    tempAssign2.scale = 0.12;
    assign2.add(tempAssign2); //assignments for level 2

    var tempDistract1 = createSprite(distract1X[i], distract1Y[i]);
    tempDistract1.addImage('standard', distract1Image);
    tempDistract1.scale = 0.2;
    distract1.add(tempDistract1);

    var tempDistract2 = createSprite(distract2X[i], distract2Y[i]);
    tempDistract2.addImage('standard', distract2Image);
    tempDistract2.scale = 0.25;
    distract2.add(tempDistract2);

    var tempStudyNotes = createSprite(studyNotesX[i], studyNotesY[i]);
    tempStudyNotes.addImage('standard', studyNotesImage);
    tempStudyNotes.scale = 0.25;
    studyNotes.add(tempStudyNotes);
  }
}

/*---draw function---*/
function draw() {
  //play background music

  /*---SPLASHSCREEN---*/
  //if statement that runs when the levels variable = 1
  if (levels == 1) {
    //draw "splashscreen" background
    background(bgSplash);
    //if statement: 
    //if the ENTER key is pressed, levels variable = 2
    if (keyCode === 13) {
      levels = 2;
    }
  }

  /*---WELCOME SCREEN---*/
  //if statement that runs when the levels variable = 2
  if (levels == 2) {
    print("level 2");

    //draw "welcome screen" background
    background(bgWelcome);

    //reset the heart counter, assignment counter and collectibles for when the user plays level 1
    heartCount = 3;
    assignCount = 0;
    reset1();
  }

  /*---INSTRUCTIONS SCREENS---*/
  //if statement that runs when the levels variable = 3
  if (levels == 3) {
    print("level 3");

    //draw "instructions screen 1" background
    background(bgInstr1);

    //if statements:
    //if 2 is pressed, levels = 2, go back one screen
    if (keyCode === 50) {
      print("move to level 2");
      levels = 2;
    }

    //if 4 is pressed, levels = 4, move forward one screen
    if (keyCode === 52) {
      print("move to level 4");
      levels = 4;
    }
  }

  //if statement that runs when the levels variable = 4
  if (levels == 4) {
    print("level 4");

    //draw "instructions screen 2" background
    background(bgInstr2);

    //if statements:
    //if 3 is pressed, levels = 3, go back one screen
    if (keyCode === 51) {
      print("move to level 3");
      levels = 3;
    }

    //if 5 is pressed, levels = 5, move forward one screen
    if (keyCode === 53) {
      print("move to level 5");
      levels = 5;
    }
  }

  //if statement that runs when the levels variable = 5
  if (levels == 5) {
    print("level 5");

    //draw "instructions screen 3" background
    background(bgInstr3);

    //if statements:
    //if 7 is pressed, levels = 7, go to game screen
    if (keyCode === 55) {
      print("move to level 7");
      levels = 7;
    }

    //if 6 is pressed, levels = 6, go to uncertainty screen
    if (keyCode === 54) {
      print("move to level 6");
      levels = 6;
    }
  }

  /*---UNCERTAINTY SCREEN---*/
  //if statement that runs when levels variable = 6
  if (levels === 6) {
    print("level 6");

    //draw "uncertainty screen" background
    background(bgUncertain);

    //if statement:
    //if 7 is pressed, levels = 7 
    if (keyCode === 55) {
      print("move to level 7");
      levels = 7;

      //reset the heart , assignment counter, and collectibles for when the user plays level 1
      heartCount = 3;
      assignCount = 0;
      reset1();
    }
  }

  /*---LEVEL 1 GAME SCREEN---*/
  //if statement that runs when levels variable = 7
  if (levels === 7) {
    print("level 7");
    print(heartCount);
    print(assignCount);

    //draw "game screen" background
    background(bgGame);

    //put player sprite at the bottom of the center of the canvas
    player.position.y = 400;

    //make sure that the player is in stationary position
    player.changeImage("standing");

    //allow player sprite to move by using arrow keys (left and right)
    //depending on the key pressed, player will animate. If no key is pressed, player will not animate and will go to its "stationary pose" as no "keyIsDown" statements will be satisfied
    if (keyIsDown(37)) {
      player.position.x -= 4;
      player.position.y = 370;
      player.mirrorX(1);
      player.changeImage("moving");
    }
    if (keyIsDown(39)) {
      player.position.x += 4;
      player.position.y = 370;
      player.mirrorX(-1);
      player.changeImage("moving");
    }

    //draw assignments and make them fall
    for (var d = 0; d < assign1.length; d++) {
      assign1[d].velocity.y = 1.5;

      //if any assignment touches the bottom of the canvas, the user loses a heart
      if (assign1[d].position.y >= 480) {
        heartCount = 0;
        assign1[d].position.y = -2000;
      }

      //if the user catches an assignment, the assignment counter goes up by one. this helps the program see whether or not a user has beat the level yet
      if (player.collide(assign1[d])) {
        assignCount += 1;
        assign1[d].position.y = -2000;
      }
    }

    //draw distractions and make them fall
    for (var o = 0; o < 3; o++) {
      //make distraction fall
      distract1[o].velocity.y = 0.75;
      //if player sprite collides with a distraction, user loses a heart and the heart counter decreases the heart count by one
      if (player.collide(distract1[o])) {
        heartCount -= 1;
        distract1[o].position.y = -2000;
      }

      //make distraction fall
      distract2[o].velocity.y = 0.65;

      //if player sprite collides with a distraction, user loses a heart and the heart counter decreases the heart count by one
      if (player.collide(distract2[o])) {
        heartCount -= 1;
        distract2[o].position.y = -2000;
      }

      //draw study notes and make them fall
      studyNotes[o].velocity.y = 0.75;

      //if player sprite collides with a study note, user gains a heart and the heart counter increases the heart count by one
      if (player.collide(studyNotes[o])) {
        heartCount += 1;
        studyNotes[o].position.y = -2000;
      }
    }

    //set barriers so the player sprite cannot move offscreen 
    if (player.position.x <= 0) {
      player.position.x = 0;
    }
    if (player.position.x >= width) {
      player.position.x = width;
    }

    //if the heart counter equals 0 (meaning that the user has 0 hearts left), the user loses, levels variable = 8
    if (heartCount < 0 || heartCount === 0) {
      levels = 8;
    }

    //if the assignment counter equals 2 (meaning that the user has collected at least 2 assignments), the user wins, levels variable = 9
    if (assignCount > 5 || assignCount === 5) {
      levels = 9;
    }

    //draw all sprites
    drawSprites();

    //put heart counter at the top righthand corner of the canvas
    fill(0);
    textSize(25);
    text("Heart Count:" + heartCount, width / 2 + 200, 40);
  }

  /*---LEVEL 1 LOSE SCREEN---*/
  //if statement that runs when levels variable = 8
  if (levels == 8) {
    print("level 8");

    //draw "level 1 lose screen" background
    background(bgLevel1Lose);
  }

  /*---LEVEL 1 WIN SCREEN---*/
  //if statement that runs when levels variable = 9
  if (levels == 9) {
    print("level 9");

    //draw "level 1 win screen" background
    background(bgLevel1Win);

    //if statements:
    //if user presses 7, levels variable = 7, level 1 game restarts
    if (keyCode === 55) {
      levels = 7;
      heartCount = 3;
      assignCount = 0;
      reset1();
    }

    //if user presses R, levels variable = 10, user moves on to level 2 game
    if (keyCode === 82) {
      levels = 10;
      heartCount = 3;
      assignCount = 0;
      reset2();
    }
  }

  /*---LEVEL 2 GAME SCREEN---*/
  //if statement that runs when levels variable = 10
  if (levels == 10) {
    print("level 10");

    print(heartCount);
    print(assignCount);

    //draw "game screen" background
    background(bgGame);

    //put player sprite at the bottom of the center of the canvas
    player.position.y = 400;

    //make sure that the player is in stationary position
    player.changeImage("standing");

    //allow player sprite to move by using arrow keys (left and right)
    //depending on the key pressed, player will animate. If no key is pressed, player will not animate and will go to its "stationary pose" as no "keyIsDown" statements will be satisfied
    if (keyIsDown(37)) {
      player.position.x -= 4;
      player.position.y = 370;
      player.mirrorX(1);
      player.changeImage("moving");
    }
    if (keyIsDown(39)) {
      player.position.x += 4;
      player.position.y = 370;
      player.mirrorX(-1);
      player.changeImage("moving");
    }

    //draw assignments and make them fall
    for (var d = 0; d < assign1.length; d++) {
      assign1[d].velocity.y = 1.5;
      assign2[d].velocity.y = 2;

      //if any assignment touches the bottom of the canvas, the user loses
      if (assign1[d].position.y >= 480) {
        heartCount = 0;
      }

      if (player.collide(assign1[d])) {
        assignCount += 1;
        assign1[d].position.y = -1000000;
      }

      if (assign2[d].position.y >= 480) {
        heartCount = 0;
      }

      if (player.collide(assign2[d])) {
        assignCount += 1;
        assign2[d].position.y = -1000000;
      }

      distract1[d].velocity.y = 0.75;
      //if player sprite collides with a distraction, user loses a heart and the heart counter decreases the heart count by one
      if (player.collide(distract1[d])) {
        heartCount -= 1;
        distract1[d].position.y = -2000;
      }

      distract2[d].velocity.y = 0.65;

      //if player sprite collides with a distraction, user loses a heart and the heart counter decreases the heart count by one
      if (player.collide(distract2[d])) {
        heartCount -= 1;
        distract2[d].position.y = -2000;
      }

      //draw study notes and make them fall
      studyNotes[d].velocity.y = 0.75;

      //if player sprite collides with a study note, user gains a heart and the heart counter increases the heart count by one
      if (player.collide(studyNotes[d])) {
        heartCount += 1;
        studyNotes[d].position.y = -2000;
      }
    }

    //set barriers so the player sprite cannot move offscreen 
    if (player.position.x <= 0) {
      player.position.x = 0;
    }
    if (player.position.x >= width) {
      player.position.x = width;
    }

    //if the heart counter equals 0 (meaning that the user has 0 hearts left), the user loses, levels variable = 8
    if (heartCount < 0 || heartCount === 0) {
      levels = 11;
    }

    //if the assignment counter equals 2 (meaning that the user has collected at least 2 assignments), the user wins, levels variable = 9
    if (assignCount > 10 || assignCount === 10) {
      levels = 12;
    }

    //draw all sprites
    drawSprites();

    //put heart counter at the top righthand corner of the canvas
    fill(0);
    textSize(25);
    text("Heart Count:" + heartCount, width / 2 + 200, 40);
  }

  /*---LEVEL 2 LOSE SCREEN---*/
  //if statement that runs when levels variable = 11
  if (levels == 11) {
    print("level 11");

    //draw "level 2 lose screen" background
    background(bgLevel2Lose);
  }

  /*---LEVEL 2 WIN SCREEN---*/
  //if statement that runs when levels variable = 12
  if (levels == 12) {
    print("level 12");

    //draw "level 2 win screen" background
    background(bgLevel2Win);

    //if statement:
    //if the "P" key is pressed, levels variable = 13, user moves on to the celebration screen
    if (keyCode === 80) {
      levels = 13;
    }

    //if user presses R, levels variable = 10, level 2 game restarts
    if (keyCode === 82) {
      levels = 10;
      heartCount = 3;
      assignCount = 0;
      reset2();
    }
  }

  /*---FINAL WIN SCREEN---*/
  //if statement that runs when levels variable = 13
  if (levels == 13) {
    print("level 13");

    //draw "final win screen" background
    background(bgFinalWin);

    //use a "for loop" to draw confetti (rectangles) falling from the sky. 
    for (var d = 0; d < 15; d++) {
      fill(random(0, 255), random(0, 255), random(0, 255))
      rect(random(0, width), random(-450, -10) + conVelocity, 30, 15)
    }

    //increase confetti velocity by 1 to make confetti fall
    conVelocity += 0.85;

    //if statement:
    //if user presses "E" key, levels variable = 14, program moves to ending screen
    if (keyCode === 69) {
      levels = 14;
    }
  }

  /*---ENDING SCREEN---*/
  //if statement that runs when the levels variable = 14
  if (levels == 14) {
    print("level 14");

    //draw "ending screen" background
    background(bgEnding);

    //if statement: 
    //if the ENTER key is pressed, levels variable = 2, game restarts
    if (keyCode === 13) {
      levels = 2;
    }
  }
}

function keyPressed() {
  //if statements: 
  //if the "S" key is pressed, levels variable = 7, program goes to the level 1 game screen
  if (keyCode === 83) {
    levels = 7;
  }
  //if the "I" key is pressed, levels variable = 3, program goes to the instructions screens
  if (keyCode === 73) {
    levels = 3;
  }

  //if statements:
  //if user presses 7, levels variable = 7, program goes to level 1 game screen
  if (keyCode === 55 && levels === 8) {
    levels = 7;
    heartCount = 3;
    assignCount = 0;
    reset1();
  }
  //if user presses R and levels = 11, levels variable = 10, program goes to level 2 game screen
  if (keyCode === 82 && levels === 11) {
    levels = 10;
    heartCount = 3;
    assignCount = 0;
    reset2();
  }
}

//reset the positions of all collectibles for level 1
function reset1() {
  for (var r = 0; r < 5; r++) {
    assign1[r].position.x = assign1X[r];
    assign1[r].position.y = assign1Y[r];
  }

  for (var w = 0; w < 3; w++) {
    distract1[w].position.x = distract1X[w];
    distract1[w].position.y = distract1Y[w];
    distract2[w].position.x = distract2X[w];
    distract2[w].position.y = distract2Y[w];
    studyNotes[w].position.x = studyNotesX[w];
    studyNotes[w].position.y = studyNotesY[w];
  }
}

//reset the positions of all collectibles for level 2
function reset2() {
  for (var u = 0; u < 5; u++) {
    assign1[u].position.x = assign1X[u];
    assign1[u].position.y = assign1Y[u];
    assign2[u].position.x = assign2X[u];
    assign2[u].position.y = assign2Y[u];
    distract1[u].position.x = distract1X[u];
    distract1[u].position.y = distract1Y[u];
    distract2[u].position.x = distract2X[u];
    distract2[u].position.y = distract2Y[u];
    studyNotes[u].position.x = studyNotesX[u];
    studyNotes[u].position.y = studyNotesY[u];
  }
}