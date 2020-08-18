import pygame

pygame.init()
window = pygame.display.set_mode([800, 580])

while True:
  window.fill((255, 255, 255))

  pygame.draw.circle(
    window,
    (255, 255, 0),
    [650, 150],
    70
  )

  pygame.draw.polygon(
    window,
    (255, 0, 0),
    [[100, 300], [250, 200], [400, 300]]
  )

  pygame.draw.rect(
    window,
    (0, 0, 0),
    [100, 300, 300, 200],
    3
  )

  pygame.draw.rect(
    window,
    (150, 50, 0),
    [150, 400, 50, 100]    
  )  

  pygame.draw.rect(
    window,
    (204, 204, 255),
    [250, 370, 100, 70]    
  )  

  pygame.display.update()