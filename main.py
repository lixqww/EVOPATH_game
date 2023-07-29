import pygame as pg

pg.init()

clock = pg.time.Clock()

pg.display.set_caption("EVOPATH")  # задали название приложению

bg_sound = pg.mixer.Sound('sounds/bg_sound.mp3')  # загрузили фоновый звук приложения
bg_sound.play()  # установили фоновый звук приложения

width = 700
heigt = 283
game_screen = pg.display.set_mode((width, heigt))  # описание игрового дисплея

icon_game = pg.image.load('images/player/lil(2)r.png')
pg.display.set_icon(icon_game)  # установили изображение "иконки" приложения

# Описание объектов игры (персонаж, враг, фон)
bg_game = pg.image.load('images/bg/bg_forest.jpg')  # загрузили фоновое изображение
bg_game_lose = pg.image.load('images/bg/bg_forest_2.jpg')
enemy = pg.image.load('images/enemy/enemy.png')  # загрузили изображение врага
bullet = pg.image.load('images/bullets/bullets.png')
n_bullet = pg.image.load('images/bullets/bullets_2.png')
replenish = pg.image.load('images/bullets/replenish.png')
bullets = []

enemy_list_in_game = []
replenish_list_in_game = []
walk_right = [pg.image.load('images/player/lil(1)r.png'),
              pg.image.load('images/player/lil(2)r.png'),
              pg.image.load('images/player/lil(3)r.png'), ]  # создали список из "спрайтсов" основного игрока вправо
walk_left = [pg.image.load('images/player/lil(1)l.PNG'),
             pg.image.load('images/player/lil(2)l.png'),
             pg.image.load('images/player/lil(3)l.png'), ]  # создали список из "спрайтсов" основного игрока налево

player_speed = 5  # скорость передвижения игрока в пикселях
player_x = 100  # координата изображения игрока по Икс
player_y = 180  # координата изображения игрока по Игрику
bg_x = 0  # координата фонового изображения по Икс

my_font =pg.font.Font('fonts/Roboto-Bold.ttf' , 25)
lose = my_font.render('Game Over' ,False ,(145, 26, 26))
restart = my_font.render(' Restart' , False,(26, 145, 88))

restart_rect = restart.get_rect(topleft=(270 ,180))


enemy_timer = pg.USEREVENT + 1
pg.time.set_timer(enemy_timer, 3500)

replenish_timer = pg.USEREVENT +3
pg.time.set_timer(replenish_timer , 10000)

bullet_count = 5
player_count = 0  # переменная счетчик для перебора спрайтсов в цикле
jump_count = 8  # высота передвижения игрока в пикселях

game_play = True  # переменная-флаг для определения состояния игры (запущена или проигрыш)
is_jump = False  # переменная-флаг для определения прыжка
run_game = True  # переменная-флаг для основного цикла

while run_game:

    game_screen.blit(bg_game, (bg_x, 0))  # отобразили фоновое изображение в 0, 0 координатах
    game_screen.blit(bg_game, (bg_x + 700, 0))  # отобразили фоновое изображение в координатах икс + 700 (700- кол-во пискселей в ширину экрана)

    if bullet_count == 5:
        game_screen.blit(bullet, (10, 10))
        game_screen.blit(bullet, (50, 10))
        game_screen.blit(bullet, (90, 10))
        game_screen.blit(bullet, (130, 10))
        game_screen.blit(bullet, (170, 10))
    elif bullet_count == 4:
        game_screen.blit(bullet, (10, 10))
        game_screen.blit(bullet, (50, 10))
        game_screen.blit(bullet, (90, 10))
        game_screen.blit(bullet, (130, 10))
        game_screen.blit(n_bullet, (170, 10))
    elif bullet_count == 3:
        game_screen.blit (bullet,(10, 10))
        game_screen.blit(bullet, (50, 10))
        game_screen.blit(bullet, (90, 10))
        game_screen.blit(n_bullet, (130, 10))
        game_screen.blit(n_bullet, (170, 10))
    elif bullet_count == 2:
        game_screen.blit(bullet, (10, 10))
        game_screen.blit(bullet, (50, 10))
        game_screen.blit(n_bullet, (90, 10))
        game_screen.blit(n_bullet, (130, 10))
        game_screen.blit(n_bullet, (170, 10))
    elif bullet_count == 1:
        game_screen.blit(bullet,(10, 10))
        game_screen.blit(n_bullet, (50,10))
        game_screen.blit(n_bullet, (90, 10))
        game_screen.blit(n_bullet, (130, 10))
        game_screen.blit(n_bullet, (170, 10))
    else:
        game_screen.blit(n_bullet,(10 ,10))
        game_screen.blit(n_bullet, (50, 10))
        game_screen.blit(n_bullet, (90, 10))
        game_screen.blit(n_bullet, (130, 10))
        game_screen.blit(n_bullet, (170, 10))

    if game_play == True:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if enemy_list_in_game:  # ([x, y] [x1,y2])
            for (i, el) in enumerate(enemy_list_in_game):
                game_screen.blit(enemy, el)
                el.x -= 12

                if el.x < -12:
                    enemy_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    game_play = False


        if replenish_list_in_game:
            for (i ,el) in enumerate(replenish_list_in_game):
                game_screen.blit(replenish,(el))
                el.x -= 12

                if el.x < -12:
                    replenish_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    bullets = 5


        pressed_keys = pg.key.get_pressed()  # переменная pressed_keys проверяет на действие нажатие клавиши

        if pressed_keys[pg.K_LEFT]:
            game_screen.blit(walk_left[player_count], (player_x, player_y))  # отобразили спрайтс игрока с индексом [счетчик] в координатах из "дано"
        else:
            game_screen.blit(walk_right[player_count], (player_x, player_y))

        if player_count == 2:  # если счетчик равен 4 (4 потому что спрайтсов в списке 5, а перебор начинается с 0, т е индексы в списке: 0-4)
            player_count = 0  # то обнуляем счетчик для того, чтобы начать перебор спрайтсов заново
        else:
            player_count += 1

        bg_x -= 4  # кол-во пикселей по координате икс на которое смещается фоновая картинка при каждой итерации
        if bg_x == -700:  # если фон сместился на 700 пикселей
            bg_x = 0  # cново поставить координату по икс=0

       # if pressed_keys[pg.K_w]:
        #    bullets.append(bullet.get_rect(topleft=(player_x + 80, player_y + 20)))

        #if bullets:
          #  for (i, el) in enumerate(bullets):
           #     game_screen.blit(bullet, (el.x, el.y))
            #    el.x += 4

              #  if el.x > 910:
               #     bullets.pop(i)
#
 #               if enemy_list_in_game:
  #                  for (index, enemy_el) in enumerate(enemy_list_in_game):
   #                     if el.colliderect(enemy_el):
    #                        enemy_list_in_game.pop(index)
     #                       bullets.pop(i)

      #          if replenish_list_in_game:
       #             for (index_b, enemy_el_b) in enumerate(replenish_list_in_game):
        #                if el.colliderect(enemy_el_b):
         #                   replenish_list_in_game.pop(index_b)
          #                  bullets.pop(i)

        if pressed_keys[pg.K_LEFT] and player_x > 50:  # если нажата кнопка влево и координата игорка по иксу больше 50
            player_x -= player_speed  # смещение координат игорка по иксу на кол-во пикселей указанных как скорость игрока влево
        elif pressed_keys[pg.K_RIGHT] and player_x < 800:
            player_x += player_speed

        if not is_jump:  # проверака на значение, уходим в первую ветку только если is_jump = False
            if pressed_keys[pg.K_SPACE]:
                is_jump = True
        else:  # ветка запускается сразу после замены значения is_jump  на True
            if jump_count >= -8:  # если высота передвижения игрока в пикселях >= -7

                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2  # смещение координат игорка по игреку на кол-во пикселей указанных как высотапрыжка (формула для плавности прыжка) вверх
                else:
                    player_y += (jump_count ** 2) / 2  # вниз
                jump_count -= 1

            else:
                is_jump = False
                jump_count = 8

        pg.display.update()
    else:
        game_screen.blit(bg_game_lose, (0,0 ))
        game_screen.blit(lose, (270, 110))
        game_screen.blit(restart, restart_rect)


        mouse = pg.mouse.get_pos()
        if restart_rect.collidepoint(mouse) and pg.mouse.get_pressed()[0]:
            game_play = True
            player_x = 100
            enemy_list_in_game.clear()
            bullets.clear()
            bullet_count = 5
            replenish_list_in_game.clear()
    # Цикл закрытия приложения

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_game = False
            pg.quit

        if event.type == replenish_timer:
            replenish_list_in_game.append(replenish.get_rect(topleft=(900, 120)))


        if event.type == enemy_timer:
            enemy_list_in_game.append(enemy.get_rect(topleft=(705, 200)))

        if event.type == pg.KEYUP and game_play and event.key == pg.K_w and bullet_count > 0:
            bullets.append(bullet.get_rect(topleft= (player_x +80 , player_y +20 )))
            bullet_count-=1

    clock.tick(14)  # 14 - колво фреймов (смен картинок) в секунду
    pg.display.update()
pg.quit()


