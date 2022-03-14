class Screen:
    """A person who directs the game. 
    
    The responsibility of a Screen is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Screen using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        
    def start_game(self, collection, script):
        """Starts the game using the given collection and script. Runs the main game loop.

        Args:
            collection (collection): The collection of entities.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", collection, script)
            self._execute_actions("update", collection, script)
            self._execute_actions("output", collection, script)
        self._video_service.close_window()

    def _execute_actions(self, group, collection, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            collection (collection): The collection of entities.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(collection, script)