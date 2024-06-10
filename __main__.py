import dotenv

from src.main import Pygame
from src.settings import Settings


def main() -> None:
    dotenv.load_dotenv()
    settings: Settings = Settings()
    pygame: Pygame = Pygame(settings=settings)
    pygame.run()


if __name__ == '__main__':
    main()
