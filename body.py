class Body:
    def __init__(self, x, y, mass, radius, name, speed=None, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.speed = speed
        if self.speed is None:
            self.speed = [0, 0]
        self.mass = mass
        self.radius = radius
        self.color = color
        self.name = name

    def __repr__(self):
        return f"object Body. Properties: x = {self.x}, y = {self.y}, speed = {self.speed}, mass = {self.mass}, " \
               f"radius = {self.radius} "

    # F = G * (M1 * M2) / r**2
    # F = m*a
    # a = F/m
    def acceleration(self, bodies: list) -> list[float, float]:
        import math
        resforce = [0, 0]
        G = 6.67 * 10 ** -11
        for body in bodies:
            if body.name == self.name:
                continue
            dx = body.x - self.x
            dy = body.y - self.y
            hypotenuse = math.sqrt((dx ** 2 + dy ** 2))
            sin = dx / hypotenuse
            cos = dy / hypotenuse
            f = G * self.mass * body.mass / hypotenuse ** 2
            if abs(dx) > 1e10:
                resforce[0] += f * sin
            if abs(dy) > 1e10:
                resforce[1] += f * cos

        resacceleration = [
            resforce[0] / self.mass,
            resforce[1] / self.mass
        ]
        return resacceleration

    def update(self, bodies: list):
        a = self.acceleration(bodies)
        self.speed[0] += a[0]
        self.speed[1] += a[1]

        self.x += self.speed[0] * 10 ** 9
        self.y += self.speed[1] * 10 ** 9

        return a
