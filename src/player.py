# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name):  # equivalent to JS constructor
        self.name = name
        self.current_room = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"You picked up the {item.name}.")

