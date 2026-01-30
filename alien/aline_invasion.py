import sys
import pygame

from alien.ship import Ship
from setting import Setting
class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环重绘屏幕
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == "__main__":
    alien = AlienInvasion()
    alien.run_game()
