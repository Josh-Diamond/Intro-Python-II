# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):  # equivalent to JS constructor
        self.name = name
        self.description = description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None

    def __repr__(self):
        return f'Name: {self.name}, Description: {self.description}'
        # __repr__ is for debugging and development
    def __str__(self):
        # __str__ is for end user
        return f'{self.name} - {self.description}'