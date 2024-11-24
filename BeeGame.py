import pgzrun
import random

WIDTH = 500
HEIGHT = 500

score = 0
gameOver = False

bee = Actor("bee.png")
flower = Actor("flower.png")

bee.pos = WIDTH/2, HEIGHT/2
flower.pos = 100, 300

def draw():
    print(gameOver)
    screen.blit("background.jpg", (0,0))
    
    bee.draw()
    flower.draw()
    
    screen.draw.text("Score:" + str(score), color = "white", topleft = (10, 10))
    if gameOver:
        screen.fill(color = "red")
        screen.draw.text("Game Over! Your final score is"+str(score), color = "blue", fontsize = 40, center = (WIDTH/2, HEIGHT/2)) 
       
def gameState():
    global gameOver
    gameOver = True            
        
def update():
    global score
    global gameOver
    if not gameOver:
        if keyboard.left:
            bee.x -= 5
        elif keyboard.right:
            bee.x += 5
        elif keyboard.up:
            bee.y -= 5
        elif keyboard.down:
            bee.y += 5    
      
    if bee.colliderect(flower):
        score += 10
        flower.x = random.randint(50, WIDTH - 50)
        flower.y = random.randint(50, HEIGHT-50)
        
    if score > 100:
        gameState
        
clock.schedule(gameState, 30.0)                    
    
pgzrun.go()    