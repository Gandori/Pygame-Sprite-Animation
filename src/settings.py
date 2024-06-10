from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    fps: int = Field(default=60, alias='FPS')
    window_width: int = Field(default=1280, alias='WINDOW_WIDTH')
    window_height: int = Field(default=720, alias='WINDOW_HEIGHT')
    window_title: str = Field(default='Pygame', alias='WINDOW_TITLE')
