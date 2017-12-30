import pygame
from pygame.sprite import Group
from AlienInvasion.settings import Settings
from AlienInvasion.game_stats import GameStats
from AlienInvasion.scoreboard import Scoreboard
from AlienInvasion.button import Button
from AlienInvasion.ship import Ship
import AlienInvasion.game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    # 创建Play按钮
    play_button = Button(screen, "PLay")
    
    # 创建一个用于统计信息的实例，并创建计分板
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()
    
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 开始游戏主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == "__main__":
    run_game()
