class Level():
    def __init__(self, id, name, description, adjacent_levels):
        self.id = id
        self.name = name
        self.description = description
        self.adjacent_levels = adjacent_levels
    

    def link(self, world):
        for direction, key in self.adjacent_levels.items():
            self.adjacent_levels[direction] = world[key]
    

    def get_adjacent_levels(self):
        return self.adjacent_levels
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"""
ID: {self.id}, Name: {self.name}
Description: {self.description}
Adjacent Levels: {self.adjacent_levels}
"""