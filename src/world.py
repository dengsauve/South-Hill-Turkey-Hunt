from level import Level

def build_world():
    world = {
        "home": Level(
            id="home",
            name="Your House, in the middle of your street",
            description="Homebase, where everything is. In the garage you have a bow and arrow.",
            adjacent_levels={"north": "lincoln_park", "west": "eggers"}
        ),
        "lincoln_park": Level(
            id="lincoln_park",
            name="Lincoln Park",
            description="A beautiful walking park with a nice pond. Plenty of turkeys about.",
            adjacent_levels={"south": "home", "west": "medical_park"}
        ),
        "medical_park": Level(
            id="medical_park",
            name="Medical Park",
            description="A modest set of parks set in between Spokane's hospitals.",
            adjacent_levels={"east": "lincoln_park", "west": "cda_park", "south": "manito_park"}
        ),
        "cda_park": Level(
            id="cda_park",
            name="Couer d'Alene Park",
            description="A lovely park in Spokane's Browne's Addition neighborhood.",
            adjacent_levels={"east": "medical_park"}
        ),
        "manito_park": Level(
            id="manito_park",
            name="Manito Park",
            description="Spokane's premier park, featuring ponds, rose gardens, courtyards, and a greenhouse conservatory.",
            adjacent_levels={"north": "medical_park", "west": "cliff_cannon_park", "south": "eggers"}
        ),
        "cliff_cannon_park": Level(
            id="cliff_cannon_park",
            name="Cliff Cannon Park",
            description="A small park surrounded by Spokane's elite.",
            adjacent_levels={"east": "manito_park", "south": "eggers"}
        ),
        "eggers": Level(
            id="eggers",
            name="Eggers Butcher",
            description="A friendly local butcher.",
            adjacent_levels={"south": "cliff_cannon", "southeast": "manito_park", "east": "eggers"}
        ),
    }

    # second pass: resolve neighbor references
    for lvl in world.values():
        lvl.link(world)

    return world