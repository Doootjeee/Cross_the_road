# Learning how to use pygame

#first we import pygame
import pygame

#We set the title and size of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


#we set some RGB colors
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (0, 0, 255)

#Clock is how often the frames get refreshed
CLOCK = pygame.time.Clock()

#making the game Object Oriented, after you import the library (pygame in this example) before you initialise
class Game:
    
    #Typical rate of 60, equivalent to FPS
    TICK_RATE = 60


    
    #Initializer for the game class to set up the width, height and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        #creating the window of the specified size to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        #Set the game window colour (background colour) to white
        self.game_screen.fill(WHITE_COLOR)
        #changing the name of the screen that pop-ups
        pygame.display.set_caption(title)

    def run_game_loop(self):
        #determing if the game is over
        is_game_over = False

        #variable for direction
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        #this is the main game loop, used to update all gameplay such as movement, checks and graphics
        #it runs until is_game_over = False
        while not is_game_over:


            #getting a way to get out of the loop
            #This loop is used to get all of the events
            # Events are most often mouse movement, mouse and/or button clicks or exit events
            for event in pygame.event.get():
                # If we have an exit event we want to quit the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                #Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # Move up if the up key is pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # move down if the down key is pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                #Detect when key is released   
                elif event.type == pygame.KEYUP:
                    #stop movement when key is no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                    

                
                print(event)

            #redrawing the background
            self.game_screen.fill(WHITE_COLOR)
            
            #drawing the treasure
            treasure.draw(self.game_screen)
            
            # update the player position
            player_character.move(direction, self.height)
            #draw the player at the new position
            player_character.draw(self.game_screen)
            #make enemy move
            enemy_0.move(self.width)
            #draw the enemy
            enemy_0.draw(self.game_screen)

            #collision detection 
            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True
            #update all the game graphics
            pygame.display.update()
            #tick the clock to update everything within the game
            CLOCK.tick(self.TICK_RATE)

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        
        #loading in our own images
        object_image = pygame.image.load(image_path)
        #Scaling the size of the image
        self.image = pygame.transform.scale(object_image, (width, height))


        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height


    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

#This is the character that is controlled by the player
class PlayerCharacter(GameObject):

    #how many tiles does the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
                      

    #This makes the character move up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        #make sure the char never goes past bottom of screen
        if self.y_pos >= max_height - (20 + self.height):
            self.y_pos = max_height - (20 + self.height)

    # Return False (no collision) if y position and x position do not overlap
    # Return True if x and y positions do overlap
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True
            
#This is the enemy character 
class EnemyCharacter(GameObject):

    #how many tiles does the character moves per second
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
                      

    #This makes the character move up if direction > 0 and down if < 0
    def move(self, max_width ):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - (20 + self.width):
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
        
                    

pygame.init()


new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()



#Quit pygame and the program
pygame.quit()
quit()




#loading in our own images
#player_image = pygame.image.load('player.png')
#Scaling the size of the image
#player_image = pygame.transform.scale(player_image, (50, 50))

#drawing something on the screen (in this case a red square) (x, y, width, height)
#pygame.draw.rect(game_screen, RED_COLOR, [650, 350, 100, 100 ] )

#drawing a circle on top op of the square (x, y, radius)
#pygame.draw.circle(game_screen, GREEN_COLOR, (100,400), 50)

#calling our own image in the game, using the blit function (x, y)
#this has to be done within the game loop because it has to be updated/rendered every tick
#game_screen.blit(player_image, (375, 375))
