def triangle(height: int, filled: bool):
    for i in range(height+1):
        for k in range(i):
            character = ''
            if filled or (not filled and (k == 0 or k == i-1)):
                character = '*'
            
            elif not filled and (i == height):
                character = '*'

            elif not filled and (k != 0 or k != i-1):
                character = ' '

            print(character, end="")
 

        print("")
    
def reversed_triangle(height: int, filled: bool):
    for i in range(height):
        for _ in range(height-(i+1)):
            print(" ", end="")
        
        for k in range(i+1):
            character = ''

            if filled or (not filled and (k == 0 or k == i)):
                character = '*'
            
            elif not filled and (i+1 == height):
                character = '*'

            else: 
                character = ' '

            print(character, end="")

        print("")

def menu(reversed: str, filled: str, height: int) -> None:
    filled_triangle = False
    if filled.__contains__('y'):
        filled_triangle = True
    
    if reversed.__contains__('y'):
        reversed_triangle(height)
        return
    
    triangle(height, filled_triangle)


reversed = input("Vill du att triangeln ska vara bakåtvänd?(y/n) ") 
filled = input("Ska triangeln vara ifylld? (y/n)")
height = int(input("Hur hög (och bred) vill du att triangeln ska vara? "))

menu(reversed, filled, height)

