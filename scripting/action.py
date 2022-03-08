class Action:
    """A thing that is done.
    
    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """
    def execute(self, collection, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            collection (Collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        pass