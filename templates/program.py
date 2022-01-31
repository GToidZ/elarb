def run(*args):
    """Runs the code which is stitiched together."""
    """Args are put as the constant variables if the problem has provided them."""

    """Main code block of a student."""
    from math import pi

    def rectangle_area(w,h):
        return w * h
    def circle_area(d):
        return pi*((d/2)**2)

    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
    d = float(input("Enter the value of d: "))
    print(f"Area of the lawn is {(rectangle_area(x, y) - circle_area(d)):.2f} sq.m.")