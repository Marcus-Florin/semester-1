
# function implementation

def rectangle_area(length,width):  
    area = length * width
    return area   

valid = False

while not valid:
    try:
        length = int(input("Enter Length: "))
        width = int(input("Enter Width: "))
        if length <= 0 or width <= 0:
            raise exception()
        else:
            valid = True
    except:
        print("Invalid Input")

print(f"Area is {rectangle_area(length,width)}")   # provide suitable data matching your inputs
