#%%
#imports
import numpy as np
#imports

#variables
#variables

#functions
#functions

#classes


class Constants:
    def __init__(self,pos,symbol):
        self.pos = np.array(pos)
        self.symbol = symbol


class GameMap:
    def __init__(self, dims, actors, render):
        self.dimensions = dims
        self.actors = actors
        self.constants = []
        self.render = render
        self.map = np.zeros(dims)
        self.generateWalls()

    def show(self):
        self.render.draw(self.map)

    def update(self):
        self.map = np.zeros(self.dimensions)
        for const in self.constants:
            self.map[const.pos[0],const.pos[1]] = const.symbol

        for actor in self.actors:
            actor.getNearbyActors()
            if self.map[actor.pos[0], actor.pos[1]] == 0:
                self.map[actor.pos[0], actor.pos[1]] = actor.symbol

        self.show()

    def generateWalls(self):
        corners = [(0,0),
                   (0,self.dimensions[0]),
                   (self.dimensions[0],self.dimensions[1]),
                   (self.dimensions[1],0)]
        while True:
            points = []
            for _ in range(2):
                fc = np.random.randint(3)
                sc = (fc+1) % 4
                pair = [np.array(corners[fc]),np.array(corners[sc])]
                vec = pair[1]-pair[0]
                maxSize = np.max(np.abs(vec))
                scale = np.random.randint(maxSize - 1)
                newPoint = (pair[0] + (vec / np.linalg.norm(vec)) * scale) % maxSize
                points.append(newPoint.astype(int))
            if (points[0] != points[1]).all():
                self.constants.append(Constants(points[0],2))
                self.constants.append(Constants(points[1],3))
                break

#classes


#main
class Render:

    @staticmethod
    def draw(matrix):
        print(matrix)


def main():
    gm = GameMap((5,5),[],Render())
    gm.update()
    return gm


if __name__ == '__main__':
    main()