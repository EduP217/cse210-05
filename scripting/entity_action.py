from scripting.action import Action

class EntityAction(Action):
    
    def execute(self, collection, script):
        """Executes the move entities action.

        Args:
            collection (collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        self._handle_entity_moves(collection)
        self._handle_entity_growth(collection)
    
    def _handle_entity_moves(self, collection):
        for cicle in collection.get_entities("cicles"):
            cicle.move_next()
    
    def _handle_entity_growth(self, collection):
        """Add segment when the user have move 5 times.
        
        Args:
            collection (collection): The collection of entities in the game.
        """
        for cicle in collection.get_entities("cicles"):
            if cicle.get_qty_moves() >= 5:
                cicle.grow_tail(1)
                cicle.reset_moves()