class Component:
    def __init__(self, id, type_name):
        self.id = id
        self.type_name = type_name

    def __str__(self):
        return f"id={self.id}, name = {self.type_name}"