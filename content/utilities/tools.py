import pygame as pg
from button import Button

# Initialize pygame
pygame.init()

# 1-1. Screen dimensions to full screen
WIDTH, HEIGHT = pygame.display.set_mode().get_size()
WIDTH = round(WIDTH / 10.0) * 10
HEIGHT = round(HEIGHT / 10.0) * 10
# 1-2. Subtract bazel for mac
if platform.system() == 'Darwin':
    HEIGHT -= 70

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Game clock
clock = pygame.time.Clock()

# Fonts for display
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("consolas", 35)


# Display the score on screen
def display_score(score, color, position = None):
    score_txt = "Your Score: " + str(score)
    txt_size = pygame.font.Font.size(score_font, score_txt) # gives out in order of width(txt_size[0]) and height(txt_size[1])
    value = score_font.render(score_txt, True, color)

    if position is not None:
        screen.blit(value, [position[0] - txt_size[0] / 2, position[1] - txt_size[1]])
    else:
        screen.blit(value, [0, 0])

# Draw the snake on screen
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


# Display messages on screen
def message(msg, color):
    txt_size = pygame.font.Font.size(font_style, msg) # gives out in order of width(txt_size[0]) and height(txt_size[1])
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 2 - txt_size[0] / 2, HEIGHT / 2 + txt_size[1]])


# Game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting coordinates of the snake
    x = round(WIDTH / 2 / 10.0) * 10
    y = round(HEIGHT / 2 / 10.0) * 10

    # Movement coordinates
    x_change = 0
    y_change = 0

    # Snake parameters
    snake_list = []
    snake_length = 1

    # Place food randomly on the screen
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1, WHITE, [WIDTH / 2, HEIGHT / 2])
            pygame.display.update()

            # Handle quitting or restarting the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Boundary checks
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # Snake movement logic
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(snake_length - 1, YELLOW, [0, 0])

        pygame.display.update()

        # Check if snake has eaten food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


# Start the game
game_loop()
