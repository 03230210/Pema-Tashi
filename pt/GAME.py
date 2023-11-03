import pygame
from pygame.locals import  *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('platformer')

#load images
bg = pygame.image.load('image/bhutan image.jpg').convert_alpha()

#define game variable
tile_size = 200

 
def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(screen, (25, 255, 255), (0, line * tile_size), (screen_height, line * tile_size))
        pygame.draw.line(screen, (25, 255, 255), (line * tile_size, 0), (line *tile_size, screen_height)) 



class World():
    def __init__(self, data):
        self.tile_list = []
    
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(bg, (tile_size, tile_size))
                    img_rect = img.get_react()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1




world_data = [
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
]


#world =World(world_data)
run = True
while run:

    
    draw_grid()

    screen.blit(bg, (0 , 0))
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()        

pygame.quit()            

