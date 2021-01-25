import pygame
background_colour = (255,255,255)
(width, height) = (750, 750)
position = (0, 0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Checkers')
screen.fill(background_colour)

ball = pygame.image.load("Checkers_board.jpg")
screen.blit(ball, position)
def purple_piece(x, y):
    pygame.draw.circle(screen, (103,26,241), (x, y), 37)
    pygame.draw.circle(screen, (0,0,0), (x, y), 37, 3)
purple_piece(105, 640)
purple_piece(258, 640)
purple_piece(412, 640)
purple_piece(565, 640)
purple_piece(641.5, 563)
purple_piece(488.5, 563)
purple_piece(335.5, 563)
purple_piece(182.5, 563)
purple_piece(108, 486)
purple_piece(261, 486)
purple_piece(412, 486)
purple_piece(565, 486)
def blue_piece(x, y):
    pygame.draw.circle(screen, (26,236,241), (x, y), 37)
    pygame.draw.circle(screen, (0,0,0), (x, y), 37, 3)
blue_piece(113, 107)
blue_piece(263, 107)
blue_piece(414, 107)
pygame.display.flip()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
