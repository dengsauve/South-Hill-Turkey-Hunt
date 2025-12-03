import random

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {
            "bow": 1,
            "arrow": 20,
            "turkeys": 0,
        }
        self.health = 10
        self.enough_turkeys = self.inventory["turkeys"] > 4
        self.stars = 0
    
    def add_turkey(self):
        self.inventory["turkeys"] += 1
        return

    def get_turkey_status(self):
        if self.inventory["turkeys"] == 1:
            return "You have 1 turkey!"
        turkey_count = self.inventory["turkeys"]
        return f"You have {turkey_count} turkeys!"
    
    def get_turkey_count(self):
        return self.inventory["turkeys"]
    
    def take_damage(self, damage_points):
        self.health -= damage_points
    
    def get_health_status(self):
        if self.health == 10:
            return f"You're in perfect health with {self.health} health points."
        elif self.health > 5:
            return f"You've taken some damange, you have {self.health} health points."
        elif self.health == 1:
            return f"Better call Kenny Loggins, you're in the danger zone with {self.health} health point remaining."
        else:
            return f"You're in bad shape with {self.health} health points."
    
    def shoot_arrow(self):
        self.inventory["arrow"] -= 1
        # Check stars vs Cops
        if self.stars > 2:
            if random.uniform(0,1) * self.stars / 5 > .5:
                print("You've been arrested, game over punk!")
                print("Next time, try not to shoot so many turkeys in the same place!\n\n")
                exit()
    
    def get_inventory(self):
        return f"""
In your bag, you have:
- bow    {self.inventory['bow']}
- arrow  {self.inventory['arrow']}
- turkey {self.inventory['turkeys']}
        """
    
    def increase_stars(self):
        self.stars += 1
        print(f"You disturb the locals, you have {self.stars} stars.")
    
    def decrease_stars(self):
        if self.stars > 0:
            self.stars -= 1
        print(f"You avoid some detection, you have {self.stars} stars.")