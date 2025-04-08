class Point:
    x: float
    y: float

    # creating methods
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """magic method that will print str representation of Point."""
        return f"({self.x}, {self.y})"  # plugs the literal values of the point class

    def dist_from_orgin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


pt: Point = Point(2.0, 1.0)
print(pt)
