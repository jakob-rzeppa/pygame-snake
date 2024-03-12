import pygame
import random

pygame.init()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (50, 153, 213)

dis_width = 400
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))

clock = pygame.time.Clock()

def run():
  x1 = dis_width / 2
  y1 = dis_height / 2
  dir = [0, 0]
  snake_list = []
  snake_len = 1
  foodx = 30
  foody = 30

  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir = [-10, 0]
            elif event.key == pygame.K_RIGHT:
                dir = [10, 0]
            elif event.key == pygame.K_UP:
                dir = [0, -10]
            elif event.key == pygame.K_DOWN:
                dir = [0, 10]

    x1 += dir[0]
    y1 += dir[1]
    dis.fill(blue)
    pygame.draw.rect(dis, green, [foodx, foody, 10, 10])

    snake_list.append([x1, y1])
    if len(snake_list) > snake_len:
      del snake_list[0]

    if ([x1, y1] in snake_list[:-1]):
      run()

    if (x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0):
      run()

    for x in snake_list:
      pygame.draw.rect(dis, red, [x[0], x[1], 10, 10])

    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
      foody = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0
      snake_len += 1

    pygame.display.update()
    clock.tick(10)

run()