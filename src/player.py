class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {
            "bow": 1,
            "arrow": 20,
            "turkeys": 0,
        }
        self.health = 10
    
    def add_turkey(self):
        self.inventory["turkeys"] += 1
        return

    def get_turkey_status(self):
        if self.inventory["turkeys"] == 0:
            return "You have no turkeys!"
        if self.inventory["turkeys"] == 1:
            return "You have 1 turkey!"
        return f"You have {self.inventory["turkeys"]} turkeys!"
    
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
    
    def get_inventory(self):
        return f"""
In your bag, you have:
- bow    {self.inventory['bow']}
- arrow  {self.inventory['arrow']}
- turkey {self.inventory['turkeys']}
        """