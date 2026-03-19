import math

class Circle:
    def __init__(self, radius: float) -> None:  # two parameters: object itself and the radius of the circle
        try:
            radius_value = float(radius)
        except (TypeError, ValueError) as exc:
            raise TypeError("radius must be a real number") from exc
        if radius_value < 0:
            raise ValueError("radius must be non-negative")
        self.radius = radius_value

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius  # 2πr

    def area(self) -> float:
        return math.pi * self.radius ** 2  # πr²