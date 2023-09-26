"""
This module demonstrates how to do the following in PyGame:
  -- images
  -- text (with fonts)
  -- sound (via Sound, and also via pygame.mixer.music)

Authors: Dave Fisher, David Mutchler, many others before them, and
         SOLUTION by David Mutchler.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
# -----------------------------------------------------------------------------
# DONE: 2. IN-CLASS, WITH YOUR INSTRUCTOR, follow the instructions in the
#            Instructions.pdf   file.
# -----------------------------------------------------------------------------
import pygame
import sys

WHITE = pygame.Color("white")  # (255, 255, 255)
IMAGE_SIZE = 470
TEXT_HEIGHT = 30

# Temporary, to find the fonts on my computer:
fonts_on_my_computer = pygame.font.get_fonts()
for font in fonts_on_my_computer:
    print(font)
print(pygame.font.get_default_font())


def main():
    # Initialize:
    pygame.init()
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    dog_image = pygame.image.load("2dogs.jpg")
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))

    font1 = pygame.font.SysFont("rockwell", 40)
    font2 = pygame.font.SysFont("impact", 28)
    caption1 = font1.render("Two dogs", True, (255, 0, 255))
    caption2 = font2.render("This is MY human!", True, (0, 0, 0))

    bark = pygame.mixer.Sound("bark.mp3")
    pygame.mixer.music.load("whip-110235.mp3")
    pygame.mixer.music.play()

    # Game loop:
    while True:
        # Respond to events:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bark.play()

        # Draw things:
        screen.fill(WHITE)

        screen.blit(dog_image, (0, 0))

        screen.blit(caption1, (0, 0))

        center = (screen.get_width() - caption2.get_width()) // 2
        near_bottom = screen.get_height() - TEXT_HEIGHT - 2
        screen.blit(caption2, (center, near_bottom))

        pygame.display.update()


main()
