#Snake Game
import pygame
import random
import os

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

width = 900 
height = 600

window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake Game")

pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def screen_text(text, color, x, y):
    screen_text = font.render(text, True, color) 
    window.blit(screen_text, [x, y])
    
def snake(window, color, snake_list, snake_size):

    for x, y in snake_list:
        pygame.draw.rect(window, color, [x, y, snake_size, snake_size])
         
def gameloop():
    exit_game = False
    game_over = False

    # for snake head
    snake_x = 450
    snake_y = 300

    velocity_x = 0
    velocity_y = 0

    init_velocity = 10

    food_x = random.randint(20, width/2)
    food_y = random.randint(20, height/2)

    score = 0

    snake_size = 25
    food_size = 20

    fps = 30        

    snake_list = [ ]

    snake_length = 1

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:

            f.write("0")
            

    with open("highscore.txt", "r") as f:
   
        highscore = f.read()
    
    while not exit_game:
        if game_over:
            
            with open("highscore.txt", "w") as f:

                f.write(str(highscore))
            

            window.fill(white)
         
            screen_text("Game is Over!! Press Enter to play.", black, 130,250)
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    exit_game = True
                    with open("highscore.txt", "w") as f:
  
                        f.write(str(highscore))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
     
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
     
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
          
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
           
            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12 :
 
                score = score + 2
   
                food_x = random.randint(20, width/2)
                food_y = random.randint(20, height/2)
      
                snake_length = snake_length + 4
        
                if score > int(highscore):
                    highscore = score
                          
            window.fill(white)
     
            screen_text(f"Score : {str(score)}", black, 15, 5)
            screen_text(f"High Score: {str(highscore)}", black, 600, 5)
       
            pygame.draw.rect(window, red, [ food_x, food_y, food_size, food_size])
        
            head = [ ]
  
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head) 

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[0:-1]:
                game_over = True
            
            conditions = [snake_x < 0, snake_x > width, snake_y < 0, snake_y > height]
            if any(conditions):
                game_over = True

            snake(window, black, snake_list, snake_size)

        pygame.display.update()

        clock.tick(fps)
            
    pygame.quit()
    quit()
gameloop()
