from game.shared.color import Color
from game.shared.point import Point
from game.casting.cast import Cast

CAST = Cast()

FRAME_RATE = 20
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 30
COLS = 60
ROWS = 40
CAPTION = "Cross Road"
WHITE = Color(255, 255, 255)
BLUE = Color(22, 22, 212)

# SCREEN
SCREEN_WIDTH = MAX_X
SCREEN_HEIGHT = MAX_Y
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 0
FIELD_BOTTOM = MAX_Y - (2 * CELL_SIZE)
FIELD_LEFT = 0
FIELD_RIGHT = MAX_X - CELL_SIZE

# Areas
AREA_GROUP = "areas"
# ROAD AREA
START_HEIGHT_ROAD = 2
END_HEIGHT_ROAD = 17

# GREEN AREA
GREEN = Color(20, 85, 25)

# CAR
CAR_GROUP = "cars"
CAR_AMOUNT = 30
CAR_LEFT_TEXT = "x" #must be in low caps because the fontype differentiates it.
CAR_RIGHT_TEXT = "I" #must be in low caps because the fontype differentiates it.
CAR_BLUE = Color(0, 102, 204)
CAR_ORANGE = Color(200, 150, 20)

# FROG
FROG_GROUP = "frogs"
FROG_START = Point(MAX_X / 2, MAX_Y - 30)
FROG_JUMP_DISTANCE = 30
FROG_TEXT = "v" #letter corresponding to a frog at froggy.ttf font type file.
FROG_SPEED = 0.15 # This is the delayed amount of time, in seconds, between the frog's jumps.
LEFT_FROG_COLLISION = 15 # Distance in pixels (from the center of the frog) for it to interact and be hit by a car.
RIGHT_FROG_COLLISION = 75
FROG_GREEN = Color(40,150,50)

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# FONT
FONT_FILE = "cross_road/assets/fonts/PressStart2P-Regular.ttf"
FONT_SMALL = 32
FONT_LARGE = 72

# FONT FROG
FONT_FILE_FROG = "cross_road/assets/fonts/froggy.ttf"
FONT_SMALL = 32
FONT_LARGE = 72

# FONT CARS
FONT_FILE_CAR = "cross_road/assets/fonts/transport.ttf"
FONT_SMALL = 20
FONT_LARGE = 28

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "CROSS THE ROAD!"
WAS_GOOD_GAME = "GAME OVER"