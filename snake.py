import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (30, 144, 255)
DARK_BLUE = (0, 0, 139)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
GOLD = (255, 215, 0)

# Direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.color = GREEN
        self.head_color = DARK_GREEN
        self.grow_pending = 2  # Start with length 3
        
    def get_head_position(self):
        return self.positions[0]
    
    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        
        if new in self.positions[1:]:
            return False  # Collision with self
        
        self.positions.insert(0, new)
        
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.positions.pop()
        
        return True
    
    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow_pending = 2
    
    def render(self, surface):
        for i, p in enumerate(self.positions):
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            if i == 0:
                pygame.draw.rect(surface, self.head_color, r)
                pygame.draw.rect(surface, WHITE, r, 2)
            else:
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, DARK_GREEN, r, 1)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    def render(self, surface):
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), 
                       (GRID_SIZE, GRID_SIZE))
        pygame.draw.ellipse(surface, self.color, r)
        pygame.draw.ellipse(surface, WHITE, r, 2)
        # Add a highlight
        highlight = pygame.Rect((self.position[0] * GRID_SIZE + 4, 
                                self.position[1] * GRID_SIZE + 4), 
                               (GRID_SIZE // 2, GRID_SIZE // 2))
        pygame.draw.ellipse(surface, (255, 200, 200), highlight)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game - Score: 0")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        self.small_font = pygame.font.Font(None, 24)
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.paused = False
        
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                elif event.key == pygame.K_UP and self.snake.direction != DOWN:
                    self.snake.direction = UP
                elif event.key == pygame.K_DOWN and self.snake.direction != UP:
                    self.snake.direction = DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != RIGHT:
                    self.snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != LEFT:
                    self.snake.direction = RIGHT
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.reset_game()
        return True
    
    def reset_game(self):
        self.snake.reset()
        self.food.randomize_position()
        self.score = 0
        self.game_over = False
        self.paused = False
        pygame.display.set_caption(f"Snake Game - Score: {self.score}")
    
    def update(self):
        if not self.game_over and not self.paused:
            if not self.snake.update():
                self.game_over = True
                return
            
            # Check if snake ate food
            if self.snake.get_head_position() == self.food.position:
                self.score += 10
                self.snake.grow_pending += 1
                self.snake.length += 1
                pygame.display.set_caption(f"Snake Game - Score: {self.score}")
                
                # Make sure food doesn't spawn on snake
                while self.food.position in self.snake.positions:
                    self.food.randomize_position()
    
    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, LIGHT_GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, LIGHT_GRAY, (0, y), (WINDOW_WIDTH, y))
    
    def render(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        
        if not self.game_over:
            self.food.render(self.screen)
            self.snake.render(self.screen)
            
            # Score display
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            # Pause indicator
            if self.paused:
                pause_text = self.big_font.render("PAUSED", True, GOLD)
                text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                self.screen.blit(pause_text, text_rect)
                hint_text = self.small_font.render("Press SPACE to resume", True, WHITE)
                hint_rect = hint_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
                self.screen.blit(hint_text, hint_rect)
        else:
            # Game over screen
            game_over_text = self.big_font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
            self.screen.blit(game_over_text, text_rect)
            
            final_score_text = self.font.render(f"Final Score: {self.score}", True, GOLD)
            score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(final_score_text, score_rect)
            
            restart_text = self.small_font.render("Press SPACE to restart or R to reset", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
            self.screen.blit(restart_text, restart_rect)
        
        # Instructions
        if not self.game_over:
            instructions = [
                "Use ARROW KEYS to move",
                "SPACE to pause",
                "R to restart"
            ]
            y_offset = WINDOW_HEIGHT - 80
            for i, instruction in enumerate(instructions):
                inst_text = self.small_font.render(instruction, True, LIGHT_GRAY)
                self.screen.blit(inst_text, (10, y_offset + i * 25))
        
        pygame.display.update()
    
    def run(self):
        running = True
        while running:
            running = self.handle_keys()
            self.update()
            self.render()
            self.clock.tick(10)  # Control game speed (10 FPS for smooth movement)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

