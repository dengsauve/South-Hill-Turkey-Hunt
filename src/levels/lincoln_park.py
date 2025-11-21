from level import Level

def load_level_lincoln_park():
    name = "Upper Lincoln Park"
    description = "A beautiful walking park with a nice pond. Plenty of turkeys about."
    adjacent_levels = []
    return Level(name, description, adjacent_levels)