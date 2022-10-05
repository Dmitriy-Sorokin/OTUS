from .figure import Figure


class Rectangle(Figure):
    
    def __init__(self, width, height, name="Rectangle") -> None:
        super().__init__(width, name)
        self.width = width
        self.height = height
        
    @property
    def perimeter(self) -> int:
        return 2 * (self.width + self.height)

    @property
    def area(self) -> int:
        return self.width * self.height
