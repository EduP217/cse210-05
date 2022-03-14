from scripting.action import Action


class VideoAction(Action):
    """
    An output action that draws all the entities.
    
    The responsibility of VideoAction is to draw all the entities.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new VideoAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, collection, script):
        """Executes the draw entities action.

        Args:
            collection (collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        scores = collection.get_entities("scores")
        cicles = collection.get_entities("cicles")
        messages = collection.get_entities("messages")

        self._video_service.clear_buffer()
        for cicle in cicles:
            segments = cicle.get_segments()
            self._video_service.draw_entities(segments)
        self._video_service.draw_entities(scores)
        self._video_service.draw_entities(messages, True)
        self._video_service.flush_buffer()