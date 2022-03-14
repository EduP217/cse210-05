from utils.color import Color
from utils.point import Point


COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Snake"
SNAKE_LENGTH = 8
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)

INITIAL_RED_CICLE_POSITION = Point(int(MAX_X/5),int(MAX_Y/3))
INITIAL_GREEN_CICLE_POSITION = Point(int(MAX_X/2) + int(MAX_X/5),int(MAX_Y/3))