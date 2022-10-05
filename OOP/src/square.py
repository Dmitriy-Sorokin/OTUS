from .rectangle import Rectangle


class Square(Rectangle):
    
    def __init__(self, side, name="Square") -> None:
        super().__init__(side, side, name)
