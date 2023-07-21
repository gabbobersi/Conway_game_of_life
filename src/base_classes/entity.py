class Entity:
    """
    Base class of all entities.
    """    
    def __init__(self, x, y):
        self.x = x
        self.y = y


class InteractiveEntity(Entity):
    """
    Base class of all interactive entities.
    """    
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width      # Width of the area that triggers the entity
        self.height = height    # Height of the area that triggers the entity

    def has_mouse_over(self, mouse_pos):
        """
        Check if the mouse is over the entity.
        """
        if self.x <= mouse_pos[0] <= self.x + self.width:           # Mouse is between the left and right side of the button
            if self.y <= mouse_pos[1] <= self.y + self.height:      # Mouse is between the top and bottom side of the button
                return True
        