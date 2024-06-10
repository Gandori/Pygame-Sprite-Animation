import pygame
from pygame import Surface


class Tree:
    def __init__(self, pos_x: float, pos_y: float) -> None:
        self.pos_x: float = pos_x
        self.pos_y: float = pos_y
        self.current_frame_number: int = 0
        self.frame_timer: float = 0
        self.frame_duration: float = 1500
        self.frames: list[Surface] = [
            pygame.image.load('./assets/tree/Tree-1.png'),
            pygame.image.load('./assets/tree/Tree-2.png'),
            pygame.image.load('./assets/tree/Tree-3.png'),
            pygame.image.load('./assets/tree/Tree-4.png'),
        ]

    @property
    def is_time_for_next_frame(self) -> bool:
        if self.frame_timer >= self.frame_duration:
            return True
        return False

    @property
    def first_frame(self) -> int:
        return 0

    @property
    def last_frame(self) -> int:
        return len(self.frames) - 1

    def is_frame_last_frame(self, frame_number: int) -> bool:
        return frame_number == len(self.frames) - 1

    def draw(self, window: Surface) -> None:
        current_frame_h: int = self.frames[self.current_frame_number].get_height()
        current_frame_w: int = self.frames[self.current_frame_number].get_width()
        window.blit(
            self.frames[self.current_frame_number],
            (self.pos_x - current_frame_w / 2, self.pos_y - current_frame_h / 2),
        )

    def next_frame(self) -> None:
        self.update_frame_timer(value=0)
        if self.is_frame_last_frame(frame_number=self.current_frame_number):
            self.current_frame_number = self.first_frame
            return

        self.current_frame_number += 1

    def update_frame_timer(self, value: float) -> None:
        self.frame_timer = value
