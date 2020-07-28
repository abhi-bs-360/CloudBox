import pygame.font

class Button():

    def __init__(self, ai_settings, screen, message):
        '''Initialize button atributes'''

        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Dimensions and properties of button
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message needs to be prepped only once.
        self.prep_message(message)


    def prep_message(self, message):
        '''Convert message to image+text button'''

        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center


    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
