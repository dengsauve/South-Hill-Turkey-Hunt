from level import Level

def build_world():
    world = {
        "home": Level(
            id="home",
            name="Your House, in the middle of your street",
            description="Homebase, where everything is. In the garage you have a bow and arrow.",
            adjacent_levels={"south": "lincoln_park"}
        ),
        "lincoln_park": Level(
            id="lincoln_park",
            name="Lincoln Park",
            description="A beautiful walking park with a nice pond. Plenty of turkeys about.",
            adjacent_levels={"north": "home"}
        )
    }

    # second pass: resolve neighbor references
    for lvl in world.values():
        lvl.link(world)

    return world