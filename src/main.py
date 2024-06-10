import pygame
from pygame import Surface
from pygame.time import Clock

from src.tree import Tree

from .settings import Settings


class Pygame:
    def __init__(self, settings: Settings) -> None:
        self.running: bool = True
        self.clock: Clock = pygame.time.Clock()
        self.fps: int = settings.fps
        self.window_width: int = settings.window_width
        self.window_height: int = settings.window_height
        self.window_title: str = settings.window_title

    @property
    def current_fps(self) -> float:
        return self.clock.get_fps()

    def update_window_title(self, title: str) -> None:
        pygame.display.set_caption(title=title)

    def update_window_size(self, width: int, height: int) -> None:
        self.window: Surface = pygame.display.set_mode((width, height))

    def display_fps(self) -> None:
        font = pygame.font.Font(None, size=36)
        font_color: tuple[int, int, int] = (200, 200, 200)
        fps_text: Surface = font.render(f'FPS {self.current_fps}', True, font_color)
        self.window.blit(source=fps_text, dest=(10, 10))

    def run(self) -> None:
        pygame.init()
        self.update_window_size(width=self.window_width, height=self.window_height)
        self.update_window_title(title=self.window_title)

        tree: Tree = Tree(
            pos_x=self.window.get_width() / 2, pos_y=self.window.get_height() / 2
        )

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill(color=(30, 30, 30))
            self.display_fps()

            tree.update_frame_timer(value=tree.frame_timer + self.clock.get_time())
            tree.next_frame() if tree.time_for_next_frame else None
            tree.draw(window=self.window)

            self.clock.tick(self.fps)
            pygame.display.flip()

        pygame.quit()
