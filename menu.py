import pygame

class Menu:

    def initial_menu(self, screen):

        (x, y) = (0, 0)
        clock = pygame.time.Clock()

        ball = pygame.image.load('golf-ball8.png')
        startmenu = pygame.image.load("Initialmenu.jpg")

        screen.blit(startmenu, (0, 0))

        while True:
            clock.tick(30)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return False

                if event.type == 4:
                    screen.blit(startmenu, (0, 0))
                    (x, y) = pygame.mouse.get_pos()

                if x >= 346 and y >= 224 and x <= 457 and y <= 252: #botão de start
                    screen.blit(ball, (333, 233))
                    screen.blit(ball, (459, 233))

                    if event.type == 5:
                        return True

                if x >= 362 and y >= 281 and x <= 441 and y <= 311: #botão de exit
                    screen.blit(ball, (351, 292))
                    screen.blit(ball, (443, 292))

                    if event.type == 5:
                        return False

            pygame.display.update()