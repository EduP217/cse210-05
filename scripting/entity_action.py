from scripting.action import Action

class EntityAction(Action):
    
    def execute(self, collection, script):
        """Executes the move entities action.

        Args:
            collection (collection): The collection of entities in the game.
            script (Script): The script of Actions in the game.
        """
        self._handle_entity_moves(collection)
    
    def _handle_entity_moves(self, collection):
        for cicle in collection.get_entities("cicles"):
            cicle.move_next()