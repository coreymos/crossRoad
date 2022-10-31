class Cast:
    """A collection of actors and areas (that is a type of actors).

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        self._areas = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def add_area(self, group, area):
        """Adds an area to the given group.
        
        Args:
            group (string): The name of the group.
            area (Area): The area to add.
        """
        if not group in self._areas.keys():
            self._areas[group] = []
            
        if not area in self._areas[group]:
            self._areas[group].append(area)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results

    def get_areas(self, group):
        """Gets the areas in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The areas in the group.
        """
        results = []
        if group in self._areas.keys():
            results = self._areas[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_all_areas(self):
        """Gets all of the areas in the cast.
        
        Returns:
            List: All of the areas in the cast.
        """
        results = []
        for group in self._areas:
            results.extend(self._areas[group])
        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)
            
    def clear_actors(self, group):
        """Clears actors from the given group.
        
        Args:
            group: A string containing the name of the group.
        """
        if group in self._actors:
            self._actors[group] = []
    
    def clear_all_actors(self):
        """Clears all actors."""
        for group in self._actors:
            self._actors[group] = []