class Rhombus:
    def __init__(self, side_a:int, angle_a:float):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError("Довжина сторони має бути більше 0")
            super().__setattr__(key, value)
        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах (0, 180)")
            super().__setattr__('angle_a', value)
            super().__setattr__('angle_b', 180 - value)
        elif key == 'angle_b':
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах (0, 180)")
            super().__setattr__('angle_b', value)
            super().__setattr__('angle_a', 180 - value)
        else:
            super().__setattr__(key, value)