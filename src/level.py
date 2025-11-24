class Level:
    def __init__(self, id, name, description, adjacent_levels, turkeys):
        self.id = id
        self.name = name
        self.description = description
        self.adjacent_levels = adjacent_levels
        self.turkeys = turkeys

    def link(self, world):
        for direction, key in self.adjacent_levels.items():
            self.adjacent_levels[direction] = world[key]

    def get_adjacent_levels(self):
        return self.adjacent_levels

    def get_adjacent_level(self, direction):
        return self.adjacent_levels[direction]

    def get_name(self):
        return self.name
    
    def get_observation(self):
        observation = f"You're at {self.name}\n{self.description}\n\n"
        
        if self.turkeys == 0:
            observation += f"You don't see any turkeys, it may be time to move on.\n"
        elif self.turkeys == 1:
            observation += f"You see one turkey here.\n"
        else:
            observation += f"You see {self.turkeys} turkeys roaming around, plenty of hunting here!\n"
        
        observation += f"\nAround you you see:\n"
        for direction, level in (self.get_adjacent_levels()).items():
            observation += f"- {direction}: {level.get_name()}\n"
        
        return observation
    
    def remove_turkey(self):
        self.turkeys -= 1

    def __str__(self):
        return f"""
ID: {self.id}, Name: {self.name}
Description: {self.description}
Adjacent Levels: {self.adjacent_levels}
"""
