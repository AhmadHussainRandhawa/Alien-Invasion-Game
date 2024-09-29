import pygame.font


class Button:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.bg_color = 255, 0, 0  # button color.
        self.text_color = 255, 255, 255

        self.font = pygame.font.SysFont(None, 48)  # None used default style. Pass "Arial", "Cosmic Sans"
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # Creating a simple rectangle or a button.
        self.rect.center = self.screen_rect.center

        # The button msg needs to prepared only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)  # Focus on text and colors
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.bg_color, self.rect)  # draw button's background
        self.screen.blit(self.msg_image, self.msg_image_rect)

# Start understanding the whole class from draw_button().
# With antialiasing (True): The edges of the characters are smoother and more natural-looking.
