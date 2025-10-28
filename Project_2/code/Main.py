import pygame as py
py.init()

# Scherminstellingen
BREEDTE, HOOGTE = 420, 630
screen = py.display.set_mode((BREEDTE, HOOGTE))
clock = py.time.Clock()

# Player instellingen
Player_BREEDTE = 63
Player_HOOGTE = 63
Player_x = 0
Player_y = HOOGTE - Player_HOOGTE  # Start op de grond

Gravity = 0.5
Jump_strength = -10
Player_VelX = 5
Player_VelY = 0
on_ground = True

jump_cooldown = 0
cooldown_time = 30


Player_Image = py.image.load("images/Player.png").convert_alpha()
Player_Scaled_Image = py.transform.scale(Player_Image, (Player_BREEDTE, Player_HOOGTE))

Playing = True
while Playing:
    screen.fill((255,255,255))

    for event in py.event.get():
        if event.type == py.QUIT:
            Playing = False
            

    keys = py.key.get_pressed()

    
    # Springen
    if keys[py.K_SPACE] and jump_cooldown <= 0:
        Player_VelY = Jump_strength
        jump_cooldown = cooldown_time
        print(f"Cooldown is {jump_cooldown}")
      
    if jump_cooldown > 0:
        jump_cooldown -= 1
        print(jump_cooldown)
    
    # Gravity toepassen
    Player_VelY += Gravity
    Player_y += Player_VelY

    # Grond check
    if Player_y + Player_HOOGTE >= HOOGTE:
        Player_y = HOOGTE - Player_HOOGTE
        Player_VelY = 0
        on_ground = True

    # Rand check
    if Player_x + Player_BREEDTE >= BREEDTE:
        Player_x = BREEDTE - Player_BREEDTE
        Player_VelX = -10
    if Player_x < 0:
        Player_x = 0
        Player_VelX = 10
    if Player_y + Player_BREEDTE/2 < 0:
        Player_y = 0
        Player_VelY = 0
        jump_cooldown = 30

    # Beweging horizontaal
    Player_x += Player_VelX

    screen.blit(Player_Scaled_Image, (Player_x, Player_y))
    py.display.update()
    clock.tick(60)

py.quit()
