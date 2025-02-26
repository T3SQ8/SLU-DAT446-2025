from punkt import Punkt

class Rectangle():
    def __init__(self, width, height, x_pos, y_pos):
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_perimeter(self) -> float:
        return (self.width * 2) + (self.height * 2)

    def get_area(self) -> float:
        return self.width * self.height

    def get_middle(self) -> Punkt:
        x_mid = self.x_pos + self.width/2
        y_mid = self.y_pos + self.height/2

        return Punkt(x_mid, y_mid)
    
    def get_right(self):
        return self.x_pos + self.width
    
    def get_top(self):
        return self.y_pos + self.height

    def intersects(self, other_rect: 'Rectangle') -> bool:
    # rectangle_2: Rectangle ser till att datatypen som tas in är en instans av Rectangle och inte något annat
    # När vi referar till klassen "inom sig själv" måste vi använda citatecken: 'Rectangle'. För externa klasser krävs inte detta 
    # -> bool säkerställer att funktionen returnerar en bool (alltså True/False)

        left_intersects = other_rect.x_pos <= self.x_pos <= other_rect.get_right()
        right_intersects = other_rect.x_pos <= self.get_right() <= other_rect.get_right()

        top_intersects = other_rect.get_top() >= self.get_top() >= other_rect.y_pos
        bottom_intersects = other_rect.get_top() >= self.y_pos >= other_rect.y_pos

        horizontally_intersects = left_intersects or right_intersects
        vertically_intersects = top_intersects or bottom_intersects
        
        # Debugging
        # print(f"Left: {left_intersects}")
        # print(f"Right: {right_intersects}")
        
        # print(f"Top: {top_intersects}")
        # print(f"Bottom: {bottom_intersects}")
        

        return (horizontally_intersects and vertically_intersects)
    

if __name__ == '__main__':
    rect_1 = Rectangle(50, 50, 0, 0)
    rect_2 = Rectangle(50, 50, 25, 25)

    print(rect_1.intersects(rect_2))