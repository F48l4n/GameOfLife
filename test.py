import random

def randomCircleEdges(hues):
    def distanceOnCircle(a1, a2):
        da = abs(a1 - a2)
        if (da > 180):
            da = 360 - da
            return da, (a1, a2)
        return da, a2, a1

    h1, h2, h3 = hues
    distancesWithParents = [distanceOnCircle(h1, h2), distanceOnCircle(h1, h3), distanceOnCircle(h2, h3)]
    maximum = 0
    for i, value in enumerate(distancesWithParents):
        if value[0] > maximum:
            maximum = value[0]
            index = i
    return distancesWithParents[index][1], distancesWithParents[index][2]

if __name__ == '__main__':

    print(min((10, 500, 23),(20, 5, 23)))