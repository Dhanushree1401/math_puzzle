#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Dimensions and Colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
GREEN = (50, 205, 50)
RED = (255, 69, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 223, 0)
GOLD = (255, 215, 0)

# Fonts and Sounds
FONT = pygame.font.Font(None, 80)
SMALL_FONT = pygame.font.Font(None, 36)
BIG_FONT = pygame.font.Font(None, 120)
CORRECT_SOUND = pygame.mixer.Sound('correct.mp3')
WRONG_SOUND = pygame.mixer.Sound('incorrect.mp3')
CELEBRATION_SOUND = pygame.mixer.Sound('celebration.mp3')

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Puzzle Game")

# Load Assets
background_image = pygame.image.load("bg.jpg")  # Use a beach-like background
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
celebration_image = pygame.image.load("congrats.jpg")  # Celebration image
celebration_image = pygame.transform.scale(celebration_image, (WIDTH, HEIGHT))

# Generate a random math problem
def generate_problem(level):
    if level == 1:
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} + {b}", a + b
    elif level == 2:
        a, b = random.randint(10, 20), random.randint(1, 10)
        return f"{a} - {b}", a - b
    elif level == 3:
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} x {b}", a * b
    elif level == 4:
        a, b = random.randint(2, 10), random.randint(1, 10)
        return f"{a * b} ÷ {a}", b

# Generate multiple-choice options
def generate_options(correct_answer):
    options = [correct_answer]
    while len(options) < 3:
        option = random.randint(correct_answer - 10, correct_answer + 10)
        if option not in options and option > 0:
            options.append(option)
    random.shuffle(options)
    return options

# Draw button
def draw_button(rect, text, color):
    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, rect, width=3, border_radius=10)
    text_surface = FONT.render(text, True, WHITE)
    screen.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2, rect.y + (rect.height - text_surface.get_height()) // 2))

# Display celebration
def display_celebration():
    CELEBRATION_SOUND.play()
    for _ in range(3):
        screen.blit(celebration_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)

# Main Game Loop
def game():
    running = True
    level = 1
    score = 0
    problem, solution = generate_problem(level)
    options = generate_options(solution)

    while running:
        screen.blit(background_image, (0, 0))

        # Display the problem with background
        problem_bg = pygame.Rect(WIDTH // 2 - 150, 80, 300, 100)
        pygame.draw.rect(screen, BLUE, problem_bg, border_radius=10)
        pygame.draw.rect(screen, BLACK, problem_bg, width=3, border_radius=10)
        problem_text = FONT.render(f"{problem}", True, BLACK)
        screen.blit(problem_text, (problem_bg.x + (problem_bg.width - problem_text.get_width()) // 2, problem_bg.y + (problem_bg.height - problem_text.get_height()) // 2))

        # Display the options
        buttons = []
        colors = [ORANGE, GREEN, YELLOW]
        for i, option in enumerate(options):
            button_rect = pygame.Rect(WIDTH // 2 - 100, 250 + i * 100, 200, 70)
            buttons.append((button_rect, option))
            draw_button(button_rect, str(option), colors[i])

        # Display score and level with highlighting
        score_text = SMALL_FONT.render(f"Score: {score}", True, GOLD if score % 30 == 0 else BLACK)
        level_text = SMALL_FONT.render(f"Level: {level}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))

        # Display close button
        close_button_rect = pygame.Rect(WIDTH - 50, 10, 40, 40)
        pygame.draw.rect(screen, RED, close_button_rect, border_radius=10)
        pygame.draw.line(screen, WHITE, (WIDTH - 45, 15), (WIDTH - 15, 45), 3)
        pygame.draw.line(screen, WHITE, (WIDTH - 45, 45), (WIDTH - 15, 15), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for close button
                if close_button_rect.collidepoint(event.pos):
                    running = False
                # Check for option buttons
                for button, option in buttons:
                    if button.collidepoint(event.pos):
                        if option == solution:
                            CORRECT_SOUND.play()
                            score += 10
                            if score % 30 == 0:  # Level up every 30 points
                                level += 1
                                display_celebration()
                            problem, solution = generate_problem(level)
                            options = generate_options(solution)
                        else:
                            WRONG_SOUND.play()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game()


# In[2]:


pip install pygame


# In[ ]:




