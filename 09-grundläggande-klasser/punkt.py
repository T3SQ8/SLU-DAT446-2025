import math
class Punkt():
    def __init__(self, x_position, y_position):
        self.x_pos = x_position
        self.y_pos = y_position

    
    def avstånd(self, other_point: 'Punkt'):
        return math.sqrt((self.x_pos - other_point.x_pos)**2 + (self.y_pos - other_point)**2)
