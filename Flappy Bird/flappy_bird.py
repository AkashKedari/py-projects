import pygame, sys , random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,450))
    screen.blit(floor_surface, (floor_x_pos + 288,512))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (288,random_pipe_pos))
    top_pipe =  pipe_surface.get_rect(midbottom = (288,random_pipe_pos - 140))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    # Takes the pipe rectangles and moves them to the left
    # Creates new list of new rectangles
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe,pipe)

def check_collsion(pipes):
    for pipe in pipes:
        # checking if bird rect is colliding with pipe rect
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 450:
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement*3,1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == "main_game":
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (144,95))
        screen.blit(score_surface,score_rect)
    if game_state == "game_over":
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (144,100))
        screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (144,60))
        screen.blit(high_score_surface,high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


# initiate pygame
pygame.init()
# the current resolution is the original resolution of 288x512
# The images are exactly half this size
screen = pygame.display.set_mode((288,512))
# Create a clock object to limit our framerate
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',30)


# Game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

# Importing game images
# import the background surface
bg_surface = pygame.image.load('assets/background-day.png').convert()
# double the size of the surface
# bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
# Double the size of floor
# floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = -16


# Scale2x for game if using 576x1024 resolution
bird_downflap = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,256))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


"""
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
# Gets surface and puts rectangle around it
bird_rect = bird_surface.get_rect(center = (100,512))
"""


pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
# pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
# Create event triggered every 1200 milliseconds
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
# Creating a list of random heights for the pipes made
pipe_height = [190,250,300,400,350,230,240,200,300,190,200,290,280]

game_over_surface = pygame.image.load('assets/message.png').convert_alpha()
# game_over_surface = pygame.transform.scale2x(game_over_surface)
game_over_rect = game_over_surface.get_rect(center = (144,256))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # unintialize the game
            pygame.quit()
            # Shutdown game after clicking x button
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # If someone presses space
            if event.key == pygame.K_SPACE and game_active:
                # disable effect of gravity
                bird_movement = 0
                bird_movement -= 5
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,256)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            # Create new pipe
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    # screen surface is on the orgin at the top-left
    # Y coordinate is inverted. To move down, increase Y value, vice versa
    screen.blit(bg_surface,(0,0))
    if game_active:
        bird_movement += gravity

        rotated_bird = rotate_bird(bird_surface)

        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collsion(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score += 0.01
        score_display("main_game")
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display("game_over")

    # Floor animation
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -32:
        floor_x_pos = -16

    # Takes anything that was drawn and updates it on the display surface
    pygame.display.update()
    # game is not going to run faster than 120 FPS
    clock.tick(75)
