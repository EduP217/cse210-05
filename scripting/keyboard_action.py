from scripting.action import Action
from utils.point import Point

class KeyboardAction(Action):
    """
    An input action that controls the cicle.
    
    The responsibility of KeyboardAction is to get the direction and move the cicle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service, cell_size):
        """Constructs a new KeyboardAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            cell_size (int): The size of a cell in the display grid.
        """
        self._keyboard_service = keyboard_service
        self._cell_size = cell_size
        self._direction = Point(cell_size, 0)


    def execute(self, collection, script):
        """Executes the control entities action.

        Args:
            collection (Collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        #left
        if self._keyboard_service.is_key_down('a') or self._keyboard_service.is_key_down('k'):
            self._direction = Point(-self._cell_size, 0)
        
        # right
        if self._keyboard_service.is_key_down('d') or self._keyboard_service.is_key_down('l'):
            self._direction = Point(self._cell_size, 0)


        # up
        if self._keyboard_service.is_key_down('w') or self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -self._cell_size)

        # down
        if self._keyboard_service.is_key_down('s') or self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, self._cell_size)

    
        cicle = collection.get_first_entity('cicles')
        cicle.turn_head(self._direction)
        