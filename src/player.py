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
    
    def shoot_arrow(self):
        self.inventory["arrow"] -= 1