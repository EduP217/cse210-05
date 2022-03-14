from scripting.action import Action
from elements.entity import Entity
from utils.point import Point
import utils.constants as constants

class GameAction(Action):

    def __init__(self):
        self._is_game_over = False
        
    def execute(self, collection, script):
        """Executes the handle collisions action.

        Args:
            collection (collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        self._handle_reset_game(collection)
        if not self._is_game_over:
            self._handle_entity_growth(collection)
            self._handle_segment_collision(collection)
            self._handle_game_over(collection)
    
    def _handle_entity_growth(self, collection):
        """Add segment when the user have move 5 times.
        
        Args:
            collection (collection): The collection of entities in the game.
        """
        for cicle in collection.get_entities("cicles"):
            if cicle.get_qty_moves() >= 5:
                cicle.grow_tail(1)
                cicle.reset_moves()
    
    def _handle_segment_collision(self, collection):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            collection (collection): The collection of entities in the game.
        """
        first_score = collection.get_entity('scores', 0)
        first_cicle = collection.get_entity('cicles', 0)
        first_cicle_head = first_cicle.get_head()
        first_cicle_segments = first_cicle.get_segments()[1:]
        
        second_score = collection.get_entity('scores', 1)
        second_cicle = collection.get_entity('cicles', 1)
        second_cicle_head = second_cicle.get_head()
        second_cicle_segments = second_cicle.get_segments()[1:]
        
        for fsegment in first_cicle_segments:
            if second_cicle_head.get_position().equals(fsegment.get_position()):
                first_score.add_points(1)
                self._is_game_over = True
        
        for ssegment in second_cicle_segments:
            if first_cicle_head.get_position().equals(ssegment.get_position()):
                second_score.add_points(1)
                self._is_game_over = True
    
    def _handle_game_over(self, collection):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            collection (collection): The collection of entities in the game.
        """
        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            
            message = Entity()
            message.set_text("GAME OVER!")
            message.set_position(position)
            collection.add_entity("messages", message)
                        
            position2 = Point(x, y + (constants.CELL_SIZE*2))
            
            message2 = Entity()
            message2.set_text("Press Enter to continue...")
            message2.set_position(position2)
            collection.add_entity("messages", message2)
            
            for cicle in collection.get_entities("cicles"):
                cicle.set_restart_cicle(True)
                for segment in cicle.get_segments():
                    segment.set_color(constants.WHITE)
                    
    def _handle_reset_game(self, collection):
        if self._is_game_over:
            first_cicle = collection.get_entity('cicles', 0)
            second_cicle = collection.get_entity('cicles', 1)
            
            if first_cicle.get_restart_cicle() == False:
                collection.remove_all_entities("messages")
                first_cicle.init_cicle(constants.INITIAL_RED_CICLE_POSITION, constants.RED)
                second_cicle.init_cicle(constants.INITIAL_GREEN_CICLE_POSITION, constants.GREEN)
                self._is_game_over = False