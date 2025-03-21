# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def draw_rect(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))



def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    font = pygame.font.Font(None, 36)   # Uses the default font, size 36
 
    # Rectangle 1
    color1 = config.RED
    x1, y1 = 95, 325
    width1 = 250
    height1 = 125

    # Rectangle 2
    color2 = config.BLUE
    x2, y2 = 105, 425
    width2 = 350
    height2 = 225

    text_surface = font.render('HELLO', True, config.BLUE)
    text_surface2 = font.render('SUP', True, config.RED)

    text_width = text_surface.get_width() # Which text surface do you mean?  The first one or the second one?
    text_x = (config.WINDOW_WIDTH - text_width) // 2

    # Set a fixed y-coordinate for the text surface
    text_y = 50 # Text will be positioned 50 pixels down from the top of the window

    text_width2 = text_surface2.get_width() # Which text surface do you mean?  The first one or the second one?
    text_x2 = (config.WINDOW_WIDTH - text_width2) // 2

    # Set a fixed y-coordinate for the text surface
    text_y2 = 550 # Text will be positioned 50 pixels down from the top of the window

    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running
        value = 1
        # Fill the screen with a background color 
        screen.fill(config.WHITE) 

        draw_rect(screen, color1, x1, y1, width1, height1)
        draw_rect(screen, color2, x2, y2, width2, height2)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: # Move left
            x1 -= value
        if key[pygame.K_RIGHT]: # Move right
            x1 += value
        if key[pygame.K_UP]: # Move up
            y1 -= value
        if key[pygame.K_DOWN]: # Move down
            y1 += value

        key = pygame.key.get_pressed()
        if key[pygame.K_a]: # Move left
            x2 -= value
        if key[pygame.K_d]: # Move right
            x2 += value
        if key[pygame.K_w]: # Move up
            y2 -= value
        if key[pygame.K_s]: # Move down
            y2 += value

        screen.blit(text_surface, (text_x, text_y))

        screen.blit(text_surface2, (text_x2, text_y2))
        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































