import pyray
import utils.constants as constants


class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_entity(self, entity, centered=False):
        """Draws the given entity's text on the screen.

        Args:
            entity (entity): The entity to draw.
        """ 
        text = entity.get_text()
        x = entity.get_position().get_x()
        y = entity.get_position().get_y()
        font_size = entity.get_font_size()
        color = entity.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_entities(self, entities, centered=False):
        """Draws the text for the given list of entities on the screen.

        Args:
            entities (list): A list of entities to draw.
        """ 
        for entity in entities:
            self.draw_entity(entity, centered)
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
    
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)