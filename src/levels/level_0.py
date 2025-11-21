from level import Level
from levels.lincoln_park import load_level_lincoln_park

def load_level_0():
    name = "Your House, in the middle of your street"
    description = "Homebase, where everything is. In the garage you have a bow and arrow."
    level_lincoln_park = load_level_lincoln_park()
    adjacent_levels = [level_lincoln_park]
    return Level(name, description, adjacent_levels)