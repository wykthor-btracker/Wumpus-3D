#imports
#imports

#functions
def vectorOp(vecA, vecB, op):
    return map(op, zip(vecA, vecB))
#functions

#classes

class Actor:
    def __init__(self):
        self.pos = [None, None]
        self.health = None
        self.score = None
        self.speed = (1, 1)

    def moveUp(self):
        up = [0, -self.speed[1]]
        self.pos = vectorOp(self.pos,up,sum)

    def moveDown(self):
        down = [0, self.speed[1]]
        self.pos = vectorOp(self.pos, down, sum)

    def moveLeft(self):
        left = [-self.speed[0], 0]
        self.pos = vectorOp(self.pos, left, sum)

    def moveRight(self):
        right = [-self.speed[0], 0]
        self.pos = vectorOp(self.pos, right, sum)

    def changeHealth(self, delta):
        self.health += delta

    def isAlive(self):
        return self.health == 0

    def getScore(self):
        raise NotImplementedError("Function call on a abstract method.")

def main():
    pass


if __name__ == '__main__':
    main()
