# 1. Create a function that computes the area of a triangle using Heron's formula
def compute_triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    '''
    Calculate the area of a triangle its three sides.

    Args:
        side_a - The length of the first side of the triangle
        side_b - The length of the second side of the triangle
        side_c - The length of the third side of the triangle

    Return
        The calculated area of the triangle
    '''
    s = (side_a + side_b + side_c) / 2  # Half of perimeter
    area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** (1/2)

    return area


def main():
    print('Let\'s calculate the area of your triangle!')
    side_a = float(input('*Enter first side length: ').strip())
    side_b = float(input('*Enter second side length: ').strip())
    side_c = float(input('*Enter third side length: ').strip())

    triangle_area = compute_triangle_area(side_a, side_b, side_c)
    print(f'The total area of your triangle is {triangle_area} in whatever unit you want it to be!')


if __name__ == '__main__':
    main()
