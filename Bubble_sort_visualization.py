import pygame 

pygame.init()
 
height = []
n = int(input("Enter the number of lines : "))
print("Enter the numbers :")
for i in range(0,n):
    x = int(input())

    height.append(x)

win = pygame.display.set_mode((600,600))
 
pygame.display.set_caption("Bubble sort")
 
x = 40
y = 40
 
width = 20
  

 
run = True
 
def show(height):
 
    for i in range(len(height)):
        # print(height)
        pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, height[i]))
 
while run:
 
    execute = False
 
    pygame.time.delay(10)
 
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
 
            run = False
 
    # if space bar is pressed
    if keys[pygame.K_SPACE]:
        execute = True
 
    if execute == False:
 
        win.fill((0, 0, 0))

        show(height)

        pygame.display.update()

    else:

        for i in range(len(height) - 1):

            for j in range(len(height) - i - 1):

                if height[j] > height[j + 1]:
 

                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t
 
                win.fill((0, 0, 0))

                show(height)

                pygame.time.delay(50)

                pygame.display.update()

pygame.quit()