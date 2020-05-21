import pygame #Imports a game library that lets you use specific functions in your program.
import random #Import to generate random numbers.

pygame.init()#Initialize the pygame modules to get everything started.


#Width and Height for the screen that will be created.
screenWidth = 1040
screenHeight = 680
screen = pygame.display.set_mode((screenWidth,screenHeight))

#Load images from the folder, and create objects for the game.
player = pygame.image.load('player.jpg')
enemy1 = pygame.image.load('monster.jpg')
enemy2 = pygame.image.load('monster.jpg')
enemy3 = pygame.image.load('monster.jpg')
prize = pygame.image.load('prize.jpg')


#Get the width and height of  the images.
playerHeight = player.get_height()
playerWidth = player.get_width()
enemy1Height = enemy1.get_height()
enemy1Width = enemy1.get_width()
enemy2Height = enemy2.get_height()
enemy2Width = enemy2.get_width()
enemy3Height = enemy3.get_height()
enemy3Width = enemy3.get_width()
prizeHeight = prize.get_height()
prizeWidth = prize.get_width()

print("This is the height of the player image: " + str(playerHeight)) 
print("This is the width of the player image: " + str(playerWidth))                                                                                                                                                                                                                


#Store the positions of the objects, player, enemies and prize.
playerXPosition = 520
playerYPosition = 300 
    
enemy1XPosition = 0
enemy1YPosition = random.randint(0,screenHeight - enemy1Height)

enemy2XPosition = random.randint(100, screenWidth - enemy2Width)
enemy2YPosition = 0

enemy3XPosition =random.randint(75, screenWidth - enemy3Width)
enemy3YPosition = -25

prizeXPosition = random.randint(10, screenWidth - prizeWidth)
prizeYPosition = random.randint(10, screenHeight - prizeHeight)

#Checks if the up, down, left or right is pressed.
keyUp = False
keyDown = False
keyLeft = False
keyRight = False


#Loops the indented code until you tell it to stop.
while 1:
    
    screen.fill(0) #Clears the screen.
    
    #Draws the images to the screen.
    screen.blit(player,(playerXPosition, playerYPosition))
    screen.blit(enemy1,(enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2,(enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3,(enemy3XPosition, enemy3YPosition))
    screen.blit(prize,(prizeXPosition, prizeYPosition))

    pygame.display.flip() #Updates the screen.
    
    #Loops through the events. 
    for event in pygame.event.get():

        #This event checks if the user quits the program.
        if event.type == pygame.QUIT: #If they quit, the program exits.
            pygame.quit()
            exit(0)
            
        #This event checks if the key entered is down.
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

                
        #this event checks if the key entered is up.
        if event.type == pygame.KEYUP:

            #test if the key released is the one we want. 
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

                
    #After checking the events, and values are set,check key pressed values and move  move player accordingly.
    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1

    if keyDown == True:
        if playerYPosition < screenHeight - playerHeight: # This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0: #This makes sure that the use does not move past the left side of the window
            playerXPosition -= 1

    if keyRight == True:
        if playerXPosition < screenWidth - playerWidth:#This makes sure that the use does not move past the right side of the window
            playerXPosition +=1


    #Bounding box for all the objects, to check collision between them,
    #and update the object's position.
            
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox =  pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition


    #If the boxes collides with the enemy ,the player loses.
    
    if playerBox.colliderect(enemy1Box):
        print("You lose!")

        pygame.quit() #Quite game and exit window.
        exit(0)

    if playerBox.colliderect(enemy2Box):
        print("You lose!")

        pygame.quit() #Quite game and exit window.
        exit(0)

    if playerBox.colliderect(enemy3Box):
        print("You lose!")

        pygame.quit() #Quite game and exit window
        exit(0)
        
    #If the user collides with the prize object, the player wins.
    if playerBox.colliderect(prizeBox):
        print("You win!")

        pygame.quit() #Quite game and exit window
        exit(0)


    #The enemy objects should approach the player at 1.5 speed and the prize object should not move.
    enemy1XPosition += 1.5
    enemy2XPosition += 1.5
    enemy3XPosition -= 1.5
        
