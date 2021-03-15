from gamemap import GameMap
import requests

class MapRenderer:
    def __init__(self, gamemapper):
        if not isinstance(gamemapper, GameMap):
            raise Exception("Wrong type for {}, {} found instead".format(map, GameMap))

    def render(self):
        pass
