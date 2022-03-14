import utils.constants as constants

from elements.collection import Collection
from elements.score import Score
from elements.snake import Snake
from scripting.script import Script
from scripting.keyboard_action import KeyboardAction
from scripting.entity_action import EntityAction
from scripting.game_action import GameAction
from scripting.video_action import VideoAction
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from utils.color import Color
from utils.point import Point
from screen import Screen

def main():
    
    # create red entity
    red_score = Score()
    red_cicle = Snake()
    red_cicle.init_cicle(constants.INITIAL_RED_CICLE_POSITION, constants.RED)
    
    # create green entity
    green_score = Score()
    green_score.set_position(Point(int(constants.MAX_X/2),0))
    green_cicle = Snake()
    green_cicle.init_cicle(constants.INITIAL_GREEN_CICLE_POSITION, constants.GREEN)
    
    # create the collection
    collection = Collection()
    collection.add_entity("cicles", red_cicle)
    collection.add_entity("cicles", green_cicle)
    collection.add_entity("scores", red_score)
    collection.add_entity("scores", green_score)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    
    # declares keyboard for first player
    first_player_keyboard_action = KeyboardAction(keyboard_service, constants.CELL_SIZE, 0)
    
    # declares keyboard for second player
    second_player_keyboard_action = KeyboardAction(keyboard_service, constants.CELL_SIZE, 1)

    script = Script()
    script.add_action("input", first_player_keyboard_action)
    script.add_action("input", second_player_keyboard_action)
    script.add_action("update", EntityAction())
    script.add_action("update", GameAction())
    script.add_action("output", VideoAction(video_service))
    
    screen = Screen(video_service)
    screen.start_game(collection, script)


if __name__ == "__main__":
    main()