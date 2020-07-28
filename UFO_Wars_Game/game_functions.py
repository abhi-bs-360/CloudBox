import sys
import pygame
from pygame import display, image, event

from bullet import Bullet
from alien import Alien
from time import sleep


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    '''Ship being hit by UFO and former gets crashed'''

    if stats.ships_remaining > 0:
        stats.ships_remaining -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()

        #Create a new fleet and position new virtual ship at center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(1)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(e, ai_settings, screen, ship, bullets):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif e.key == pygame.K_LEFT:
        ship.moving_left = True
    elif e.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(e, ship):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif e.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''New game when the player clicks Play'''

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:

        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #Reset ScoreBoard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        #Create new fleet
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    '''Sensitive to mouse-clicks and key-presses'''

    current_events = event.get()
    for e in current_events:
        if (e.type == pygame.QUIT) or (e.type == pygame.K_q):
            sys.exit()

        elif e.type == pygame.KEYDOWN:
            check_keydown_events(e, ai_settings, screen, ship, bullets)

        elif e.type == pygame.KEYUP:
            check_keyup_events(e, ship)

        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, sb):
    '''Update imageson screen and flip to new screen'''
    #Set a background color
    screen.fill(ai_settings.background_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    #display most recent screen
    display.flip()


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    #If alien-UFO and bullets collide remove them from screen
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        #Destroy all bullets and call a new fleet of UFO
        bullets.empty()
        ai_settings.increase_speed()

        #Increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    #alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
     """Check if any aliens have reached the bottom of the screen."""
     screen_rect = screen.get_rect()
     for alien in aliens.sprites():
         if alien.rect.bottom >= screen_rect.bottom:
             # Treat this the same as if the ship got hit.
             ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
             break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Update the postions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
