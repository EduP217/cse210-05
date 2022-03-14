from scripting.action import Action
from utils.point import Point

class KeyboardAction(Action):
    """
    An input action that controls the cicle.
    
    The responsibility of KeyboardAction is to get the direction and move the cicle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service, cell_size, cicle_idx):
        """Constructs a new KeyboardAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            cell_size (int): The size of a cell in the display grid.
        """
        self._keyboard_service = keyboard_service
        self._cell_size = cell_size
        self._direction = Point(cell_size, 0)
        self._cicle_idx = cicle_idx

    def execute(self, collection, script):
        """Executes the control entities action.

        Args:
            collection (Collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        cicle = collection.get_entity('cicles', self._cicle_idx)
        is_key_pressed = False
        
        if self._cicle_idx == 0:
            #left
            if self._keyboard_service.is_key_down('a'):
                self._direction = Point(-self._cell_size, 0)
                is_key_pressed = True
            # right
            if self._keyboard_service.is_key_down('d'):
                self._direction = Point(self._cell_size, 0)
                is_key_pressed = True
            # up
            if self._keyboard_service.is_key_down('w'):
                self._direction = Point(0, -self._cell_size)
                is_key_pressed = True
            # down
            if self._keyboard_service.is_key_down('s'):
                self._direction = Point(0, self._cell_size)
                is_key_pressed = True
        
        elif self._cicle_idx == 1:
            #left
            if self._keyboard_service.is_key_down('j'):
                self._direction = Point(-self._cell_size, 0)
                is_key_pressed = True
            # right
            if self._keyboard_service.is_key_down('l'):
                self._direction = Point(self._cell_size, 0)
                is_key_pressed = True
            # up
            if self._keyboard_service.is_key_down('i'):
                self._direction = Point(0, -self._cell_size)
                is_key_pressed = True
            # down
            if self._keyboard_service.is_key_down('k'):
                self._direction = Point(0, self._cell_size)
                is_key_pressed = True
        
        if self._keyboard_service.is_key_down('enter'):
            if cicle.get_restart_cicle():
                cicle.set_restart_cicle(False)
        
        if is_key_pressed:
            cicle.add_moves()
            cicle.turn_head(self._direction)
            cicle.move_next()
        