from scripting.action import Action
from elements.entity import Entity
import utils.constants as constants
from utils.point import Point

class GameAction(Action):

    def __init__(self):
        self._is_game_over = False
        
    def execute(self, collection, script):
        """Executes the handle collisions action.

        Args:
            collection (collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            #pass
            #self._handle_food_collision(collection)
            self._handle_segment_collision(collection)
            self._handle_game_over(collection)
    
    def _handle_segment_collision(self, collection):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            collection (collection): The collection of entities in the game.
        """
        first_score = collection.get_entity("scores", 0)
        first_cicle = collection.get_entity("cicles", 0)
        first_cicle_head = first_cicle.get_head()
        first_cicle_segments = first_cicle.get_segments()[1:]
        
        second_score = collection.get_entity("scores", 1)
        second_cicle = collection.get_entity("cicles", 1)
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
            message.set_text("Game Over!")
            message.set_position(position)
            collection.add_entity("messages", message)
            
            for cicle in collection.get_entities("cicles"):
                for segment in cicle.get_segments():
                    segment.set_color(constants.WHITE)