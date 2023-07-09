import pygame as pg

pg.init()

clock = pg.time.Clock() #таймер

pg.display.set_caption("EVOPATH")
bg_sound = pg.mixer.Sound('sounds/bg_music.mp3') # загрузили фоновый звук приложения
bg_sound.play()

width = 700
heigt = 283
game_screen = pg.display.set_mode((width, heigt))#устанока экрана

bg_game = pg.image.load('images/bg/bg_winter.jpg')# задний фон
enemy = pg.image.load('images/enemy/enemy.png')#ваг
bullet = pg.image.load('images/bullets/bullets.png')#патроны

bullets = []
enemy_list_in_game = []

walk_right = [pg.image.load('images/player/lil(1)r.png'),
              pg.image.load('images/player/lil(2)r.png'),
              pg.image.load ('images/player/lil(3)r.png')]
walk_left = [pg.image.load('images/player/lil(1)l.png'),
             pg.image.load('images/player/lil(2)l.png'),
             pg.image.load('images/player/lil(3)l.png')]

player_speed = 5 # скорость играка
player_x = 100 #координаты игрока по х
player_y = 450 #координаты играка по у
bg_x = 0 #коорднаты фона по х

# my font =
# lose =   ('Game Over' , )
# restart = (' Restart' , )

# restart_rect = restart.get_rect(())

enemy_timer = pg.USEREVENT + 1 #таймер
pg.time.set_timer(enemy_timer, 3500)

bullet_count = 5
player_count = 0  # перебор спрайтсов
jump_count = 7  # высота прыжка играка

game_play = True
is_jump = False
run_game = True

while run_game:
    game_screen.blit(bg_game, (bg_x, 0))  # отображение фона 1
    game_screen.blit(bg_game, (bg_x + 700, 0))  # отбражение фона 2

    if game_play == True:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        # if enemy_list_in_game:
        #   for (i,el) in enumerate(enemy_list_in_game):
        #      if el.colidrect(enemy):
        #         enemy_list_in_game.pop(index)
        #        bullet.pop(i)

        pressed_keys = pg.key.get_pressed()#нажатие для перемещения игрока
        if pressed_keys[pg.K_LEFT]:
            game_screen.blit(walk_left[player_count], (player_x, player_y))
        else:
            game_screen.blit(walk_right[player_count], (player_x, player_y))

        if player_count == 2:  # счетчик спрайтсов
            player_count = 0  # если перебор окончен начинаем зново
        else:
            player_count += 1

    bg_x -= 4
    if bg_x == -700:
        bg_x = 0

    if pressed_keys[pg.K_w]:#нажатие для пояления патронов
        bullets.append(bullet.get_rect(topleft=(player_x + 100, player_y + 100)))
        # bullet.append(bullet,(el.x , el.y))

    if bullets:
        for (i, el) in enumerate(bullets): #перебор
            game_screen.blit(bullet, (el.x, el.y))
            el.x += 4

            if el.x > 910:
                bullets.pop(i) #чистка

            if enemy_list_in_game:
                for (index, enemy_el) in enumerate(enemy_list_in_game):
                    if el.colidrect(enemy_el):
                        enemy_list_in_game.pop(index)
                        bullets.pop(i)

    for event in pg.event.get():#перебор событий
        if event.type == pg.QUIT:
            run_game = False

        clock.tick(14)
        pg.display.update()
pg.quit()
