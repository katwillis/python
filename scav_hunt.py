import pygame
import random

#initialize all modules in pygame
pygame.init()

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
FUSCHIA = (191, 29, 124)
MINT = (31, 237, 120)

color_list = [BLACK, WHITE, RED, BLUE, GREY, FUSCHIA, MINT]

#set width and height of the screen (x, y)

screen = pygame.display.set_mode((700, 500))

#include a caption on screen
pygame.display.set_caption("The Great Game")

#loop until user clicks "close" button
done = False

#clock is used to manage how fast your screen updates
clock = pygame.time.Clock()


#----- Main Loop -----#

been_clicked = False
while not done:
	# Main event loop #
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			print("Here!")
			x = pygame.mouse.get_pos()[0]
			y = pygame.mouse.get_pos()[1]
			x = 350
			y = 250
			ball_size = random.randint(20, 80)
			x_speed = random.randint(-10, 10)
			y_speed = random.randint(-10, 10)
			been_clicked = True
		if been_clicked:
			color_index = random.randint(0, len(color_list)-1)
			pygame.draw.circle(screen, color_list[color_index], (x, y), ball_size)
		
		
	#if you want a background image, replace this clear with 
	#blit'ing the background image using pygame.blit()
	screen.fill(GREEN)
	
	if been_clicked:
		color_index = random.randint(0, len(color_list)-1)
		pygame.draw.circle(screen, color_list[color_index], (x, y), ball_size)
	
	x += x_speed
	y += y_speed
	
	if x >=700 or x <=0:
		x_speed *= -1
	if y >=500 or y <= 0:
		y_speed *= -1
		
	#Update screen with drawing
	pygame.display.flip()
	#pygame.display.update(rect)
	
	# limit to 60 frames per second
	clock.tick(60)

pygame.quit()
exit()
		
