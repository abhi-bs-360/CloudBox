import pygame
from pygame import display, event, image
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

from alien import Alien
from game_stats import GameStats
from button import Button

from scoreboard import ScoreBoard

def run_game():

    #Initialize game environment and create a screen object
    pygame.init()

    ai_settings = Settings()
    screen_dimensions = (ai_settings.screen_width, ai_settings.screen_height)

    screen = display.set_mode(screen_dimensions, 0, 32)
    display.set_caption("Galaxy Wars-Alien Invasion")

    #Craete a Ship on screen
    ship = Ship(ai_settings, screen)
    #Alien UFO on screen
    alien = Alien(ai_settings, screen)

    #Bullets and alien-fleet
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)

    #Button design
    message = "! PLAY !"
    play_button = Button(ai_settings, screen, message)

    #ScoreBoard
    sb = ScoreBoard(ai_settings, screen, stats)

    #Run a trivial game loop
    while True:

        #Monitoring mouse/keyboard events and updation
        #gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)


        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, sb)


run_game()
