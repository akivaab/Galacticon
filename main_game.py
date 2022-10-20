import datetime
from itertools import cycle
from Game import *
from Player import *
from Enemies.Enemy import *
from Enemies.SideswiperEnemy import SideswiperEnemy
from Enemies.FranticEnemy import FranticEnemy
from Enemies.Gyga import Gyga

# initialize
ARCADE_FONT = 'assets/misc/PressStart2P-vaV7.ttf'
MAIN_GAME_MUSIC = "assets/music/deltarune_knock_you_down.wav"
GYGA_GAME_MUSIC = "assets/music/undertale_save_the_world.wav"
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# screen window caption and icon
pygame.display.set_caption("Galacticon")
icon = pygame.image.load("assets/misc/logo.png").convert_alpha()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
game = Game()


def begin_screen():
    # init
    pygame.mixer.music.load("assets/music/undertale_dating_tense.wav")
    pygame.mixer.music.play(-1)
    screen.fill((0, 0, 0))

    colors = [(62, 216, 18), (11, 50, 253)]
    iterator = cycle(range(2))

    # opening menu button options
    display_text("Press ENTER to play!", 16, (255, 255, 255), (240, 200))
    display_text("Press A for instructions!", 16, (255, 255, 255), (200, 230))
    display_text("Press S to see the scoreboard!", 16, (255, 255, 255), (170, 260))
    display_text("Press U for no reason whatsoever!", 16, (255, 255, 255), (150, 290))

    # screen loop
    begin_screen_running = True
    color_swap_time = datetime.datetime.now()
    while begin_screen_running:
        # alternating title colors
        if datetime.datetime.now() >= color_swap_time:
            color_swap_time = datetime.datetime.now() + datetime.timedelta(seconds=0.3)
            next(iterator)
            display_text("G L C I O", 64, colors[next(iterator)], (80, 80))
            display_text("A A T C N", 64, colors[next(iterator)], (144, 80))

        # keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:  # start
                    begin_screen_running = False
                if event.key == pygame.K_a:  # instructions
                    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(0, 350, 800, 400))

                    # how to move
                    display_image("assets/misc/arrow_keys.png", (50, 380))
                    display_text("press and hold the", 12, (255, 255, 255), (130, 380))
                    display_text("arrow keys to move", 12, (255, 255, 255), (130, 400))

                    # how to fire
                    display_image("assets/misc/space_bar.png", (40, 450), (128, 32))
                    display_text("press the space", 12, (255, 255, 255), (180, 450))
                    display_text("bar to fire", 12, (255, 255, 255), (180, 470))

                    # how to pause
                    display_image("assets/misc/p_key.png", (50, 510), (48, 48))
                    display_text("press P to pause", 12, (255, 255, 255), (125, 520))

                    # enemy warning
                    display_image("assets/enemies/sideswiper.png", (640, 370))
                    display_image("assets/enemies/splicer.png", (520, 450))
                    display_text("watch out for these guys!", 12, (255, 255, 255), (460, 435))

                if event.key == pygame.K_s:  # scoreboard
                    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(0, 350, 800, 600))
                    y_coord = 370
                    score_records = Game.read_scoreboard(5)
                    for score_record in score_records:
                        display_text(score_record[0], 16, (255, 255, 255), (290, y_coord))
                        display_text(str(score_record[1].rjust(7, "0")), 16, (255, 255, 255), (390, y_coord))
                        y_coord += 30

                if event.key == pygame.K_u:  # for fun
                    pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(0, 350, 800, 600))
                    display_text("Well that was pointless.", 20, (255, 255, 255), (130, 430))

        pygame.display.update()


def play_game():
    # init
    pygame.mixer.music.load(MAIN_GAME_MUSIC)
    pygame.mixer.music.play(-1)
    enemies_grid = game.get_cur_enemy_setup()
    player = Player()

    # game loop
    game_running = True
    while game_running:
        level_is_completed = False
        player_x_change = 0
        player_y_change = 0

        # level loop
        level_running = True
        while level_running:
            screen.fill((0, 0, 0))

            # keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_x_change = -3
                    if event.key == pygame.K_RIGHT:
                        player_x_change = 3
                    if event.key == pygame.K_UP:
                        player_y_change = -3
                    if event.key == pygame.K_DOWN:
                        player_y_change = 3
                    if event.key == pygame.K_SPACE:
                        player.fire()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_y_change = 0
                    if event.key == pygame.K_p:
                        pause()

            # move and display the player
            player.move(player_x_change, player_y_change)
            player.display(screen)

            # move and display the player's bullets
            player.move_bullets()
            player.remove_offscreen_bullets()
            for bullet in player.bullets_fired:
                bullet.display(screen)

            # move and check if the player caught the bonuses, and display them
            game.random_bonus_drop()
            game.move_bonuses()
            game.remove_offscreen_bonuses()
            game.received_bonus(player)
            for bonus in game.bonuses_dropped:
                bonus.display(screen)

            # for each enemy
            for enemy_line in enemies_grid:
                for enemy in enemy_line:

                    # move and display the enemy's bullets
                    enemy.random_fire()
                    enemy.move_bullets()
                    enemy.remove_offscreen_bullets()
                    for bullet in enemy.bullets_fired:
                        bullet.display(screen)

                    # check if the enemy shot or collided with the player
                    if player.collided_with_bullet(enemy.bullets_fired) or player.collided_with_enemy(enemy):
                        player.lose_life()
                        level_running = False

                    # move the enemy
                    enemy.move() if not isinstance(enemy, Gyga) else enemy.track(player.x)

                    # check if the enemy was shot
                    colliding_bullet = enemy.collided_with_bullet(player.bullets_fired)
                    if colliding_bullet != -1:
                        enemy.hit()
                        player.bullets_fired.pop(colliding_bullet)
                        game.increase_score(enemy.score_value)

                    # display the enemy
                    enemy.display(screen)

                    # trigger FranticEnemies once a number of enemies have been defeated
                    if isinstance(enemy, FranticEnemy) and game.get_cur_level().get_num_enemies_defeated() > 8:
                        enemy.is_frantic = True

            # deploy the splicer
            game.random_splicer_deployment(player.x)

            # check if the player collided with the splicer's laserbeam
            if player.collided_with_bullet(game.splicer.laserbeam_components):
                player.lose_life()
                level_running = False

            # display the splicer and it's laserbeam
            for laserbeam in game.splicer.laserbeam_components:
                laserbeam.display(screen)
            game.splicer.display(screen)

            # update the game screen display
            game.display_data(screen, player.lives)
            clock.tick(75)
            pygame.display.update()

            # check if the level was completed
            level_is_completed = game.is_current_level_completed()
            if level_is_completed:
                level_running = False

        # end level

        # clear bullets and special enemies from screen
        player.bullets_fired.clear()
        for enemy_line in enemies_grid:
            for enemy in enemy_line:
                enemy.bullets_fired.clear()
                if isinstance(enemy, SideswiperEnemy):
                    enemy.move_offscreen()
                if isinstance(enemy, Gyga):
                    enemy.reset()
        game.splicer.move_offscreen()
        game.splicer_deployed = False

        wait_time = 2000
        if player.lives == 0:  # game over
            Game.game_over_message(screen)
            game_running = False
            play_ending_music("assets/music/deltarune_faint_courage.wav")
            wait_time += 4000
        elif game.is_completed():  # game won
            Game.game_completed_message(screen)
            game_running = False
            play_ending_music("assets/music/undertale_dating_fight.wav")
            wait_time += 4900
        elif level_is_completed:  # beat level
            game.go_to_next_level(screen)
            enemies_grid = game.get_cur_enemy_setup()
        elif game_running:  # lost life
            Game.resuscitation_message(screen)
            player.recenter()

        pygame.display.update()
        pygame.time.wait(wait_time)

        # why do I hear boss music?
        if game_running and level_is_completed and game.get_cur_level() == game.levels[-1]:
            gyga_cutscene(enemies_grid[0][0])

    # end game


def play_ending_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()


def end_screen():
    # init
    pygame.mixer.music.load("assets/music/undertale_bird_that_carries_you_over_a_disproportionately_small_gap.wav")
    pygame.mixer.music.play(-1)
    screen.fill((0, 0, 0))
    score_records = Game.read_scoreboard(10)

    # display "HIGH SCORE" on top of the screen if one was achieved
    achieved_high_score = len([record[1] for record in score_records if int(record[1]) > game.current_score]) == 0
    if achieved_high_score:
        display_text("HIGH SCORE", 48, (255, 215, 0), (160, 80))

    # display instructions for submitting initials
    display_text("Enter your initials:", 24, (255, 255, 255), (170, 200))
    display_text("(three, specifically)", 16, (255, 255, 255), (235, 230))
    display_text("Press ENTER to continue.", 16, (255, 255, 255), (215, 400))

    # enter the player's initials / alternate score display colors
    initials = ""
    colors = [(255, 215, 0), (255, 235, 42)]
    iterator = cycle(range(2))
    color_swap_time = datetime.datetime.now()
    entering_initials = True
    while entering_initials:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.TEXTINPUT and event.text.isalpha() and len(initials) < 3:  # type letter
                initials += event.text.capitalize()
                display_text(initials, 64, (255, 255, 255), (300, 300))
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:  # submit initials
                entering_initials = len(initials) < 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:  # remove letter
                pygame.draw.rect(screen, (0, 0, 0), pygame.rect.Rect(300, 300, 200, 64))
                initials = initials[:-1]
                display_text(initials, 64, (255, 255, 255), (300, 300))

        # alternate score display colors
        if datetime.datetime.now() >= color_swap_time:
            color_swap_time = datetime.datetime.now() + datetime.timedelta(seconds=0.3)
            next_color = colors[next(iterator)]
            # display the player's score
            display_text("You scored:", 42, next_color, (175, 450))
            display_text(str(game.current_score).rjust(7, "0"), 42, next_color, (250, 510))

        pygame.display.update()

    # Easter Egg!
    if initials == "WHY":
        display_text("because.", 24, (255, 0, 0), (500, 400))
        pygame.display.update()
        pygame.time.wait(200)

    # submitted initials

    pygame.time.wait(400)

    # re-init
    screen.fill((0, 0, 0))
    new_score = game.write_scoreboard(initials)
    score_records = Game.read_scoreboard(10)
    y_coord = 100
    highlight_score = True

    # display the top 10 scores
    for score_record in score_records:
        color = (255, 255, 255)
        if score_record[0] == new_score[0] and int(score_record[1]) == int(new_score[1]) \
                and highlight_score:  # color the just-achieved score gold if in the top 10
            color = (255, 215, 0)
            highlight_score = False
        display_text(score_record[0], 24, color, (250, y_coord))
        display_text(str(score_record[1]).rjust(7, "0"), 24, color, (380, y_coord))
        y_coord += 36
        pygame.display.update()
        pygame.time.wait(100)

    # display the just-achieved score
    display_text(new_score[0], 24, (255, 215, 0), (250, 500))
    display_text(str(new_score[1]).rjust(7, "0"), 24, (255, 215, 0), (380, 500))

    # instruction display
    display_text("Press ENTER to play again.", 16, (255, 255, 255), (200, 560))
    pygame.display.update()

    # wait to end loop
    scoreboard_running = True
    while scoreboard_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                scoreboard_running = False


def pause():
    # init
    pygame.display.set_caption("Soothing alien invasion noises")
    pygame.mixer.music.load("assets/music/deltarune_thrash_machine.wav")
    pygame.mixer.music.play(-1)

    # wait to unpause
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                paused = False

    # reset music
    pygame.display.set_caption("Galacticon")
    pygame.mixer.music.load(MAIN_GAME_MUSIC if not game.get_cur_level() == game.levels[-1] else GYGA_GAME_MUSIC)
    pygame.mixer.music.play(-1)


def gyga_cutscene(gyga):
    # Opening cutscene
    music_end = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(music_end)
    pygame.mixer.music.load("assets/music/undertale_last_episode.wav")
    pygame.mixer.music.play()

    playing = True
    while gyga.y <= 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))
        gyga.y += 0.04
        gyga.display(screen)
        pygame.display.update()
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == music_end:
                playing = False

    pygame.mixer.music.load(GYGA_GAME_MUSIC)
    pygame.mixer.music.play(-1)


def display_text(text, font_size, text_color, text_coordinates):
    font = pygame.font.Font(ARCADE_FONT, font_size)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, text_coordinates)


def display_image(image_path, image_coordinates, scale_factor=(0, 0)):
    image = pygame.image.load(image_path).convert()
    if scale_factor != (0, 0):
        image = pygame.transform.scale(image, scale_factor)
    screen.blit(image, image_coordinates)


if __name__ == "__main__":
    while True:
        begin_screen()
        play_game()
        end_screen()
        game = Game()
