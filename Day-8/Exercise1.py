# Area Calculation 
wall_height = int(input("Enter the height : "))
wall_width = int(input("Enter the width :  "))
wall_coverage = int(input("Enter the coverage area : "))

def area_paint(wall_height, wall_width, wall_coverage):
    number_of_cans = (wall_height * wall_width) / wall_coverage 
    print(f"You'll need {round(number_of_cans)} cans of paint.")

area_paint(wall_height, wall_width, wall_coverage)