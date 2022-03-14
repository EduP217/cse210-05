import utils.constants as constants
from elements.entity import Entity
from utils.point import Point


class Snake(Entity):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, position, color):
        super().__init__()
        self._segments = []
        self._qty_moves = 0
        self.set_position(position)
        self.set_color(color)
        self._prepare_body()
    
    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Entity()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self.get_color())
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = self.get_position().get_x()
        y = self.get_position().get_y()

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            #color = constants.YELLOW if i == 0 else self.get_color()
            
            segment = Entity()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self.get_color())
            self._segments.append(segment)
    
    def get_qty_moves(self):
        return self._qty_moves
    
    def add_moves(self, moves = 1):
        self._qty_moves += moves
    
    def reset_moves(self):
        self._qty_moves = 0