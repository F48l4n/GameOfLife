import math
import random
import pygame


class Cell:
    randomness = 30

    def __init__(self, alive, brightness, color):
        self.alive = alive
        self.brightness = brightness
        self.color = color

    def birth(self, neighbourColors=[(255, 255, 255), (255, 255, 255), (255, 255, 255)]):
        hues = []
        for i in neighbourColors:
            hues.append(pygame.Color(i).hsla[0])
        da, p1, p2 = randomCircleEdges(hues)
        hue = (random.uniform(0, da) + p1) % 360
        tmpColor = pygame.Color(255, 255, 255)
        tmpColor.hsla = (hue, 100, 50, 100)
        return Cell(True, 255, tmpColor)

    def dead(self):
        return Cell(False, 255, (0, 0, 0))

    def live(self):
        tmpColor = pygame.Color(self.color)
        return Cell(True, max(self.brightness - 5, 25), tmpColor)


def angle_between(p1, p2):
    angle_distance = p2 - p1
    if angle_distance < 0:
        angle_distance += 360
    return angle_distance


def distanceOnCircle(p1, p2):
    clockWise = (angle_between(p1, p2), p1, p2)
    counterClockWise = (angle_between(p2, p1), p2, p1)

    return clockWise, counterClockWise


def randomCircleEdges(hues):
    a, b, c = hues
    AB, BA = distanceOnCircle(a, b)
    AC, CA = distanceOnCircle(a, c)
    BC, CB = distanceOnCircle(b, c)

    ABC = (AB[0] + BC[0], a, c)
    ACB = (AC[0] + CB[0], a, b)
    BCA = (BC[0] + CA[0], b, a)
    CAB = (CA[0] + AB[0], c, b)
    CBA = (CB[0] + BA[0], c, a)
    BAC = (BA[0] + AC[0], b, c)

    tmp = [ABC, ACB, BCA, CAB, CBA, BAC]

    return min(tmp)


def runTick(tickGrid):
    newGrid = initiateGrid(len(tickGrid), len(tickGrid[0]))
    for i in range(len(tickGrid)):
        for j in range(len(tickGrid[i])):
            cell = tickGrid[i][j]
            neighbours, colorNeighbours = getNeighbours(i, j, tickGrid)  # here
            if neighbours == 3:
                newGrid[i][j] = tickGrid[i][j].birth(colorNeighbours)
            elif neighbours == 2:
                if cell.alive:
                    newGrid[i][j] = tickGrid[i][j].live()
                else:
                    newGrid[i][j] = tickGrid[i][j].dead()
            else:
                newGrid[i][j] = tickGrid[i][j].dead()
    return newGrid


def initiateGrid(height, width):
    return [[Cell(False, 0, (0, 0, 0)) for j in range(width)] for i in range(height)]


def initiateGridWithGrid(width, height, iGrid, offsetX, offsetY):
    def value(j, i):
        if not i < offsetX and not j < offsetY:
            if (i - offsetX <= len(iGrid) - 1 and j - offsetY <= len(iGrid[i - offsetX]) - 1 and
                    iGrid[i - offsetX][j - offsetY] == 1):
                tmpColor = pygame.Color(255, 255, 255)
                tmpColor.hsla = (random.uniform(0, 360), 100, 50, 100)
                return Cell(True, 255, tmpColor)
            else:
                return Cell(False, 255, (0, 0, 0))
        else:
            return Cell(False, 255, (0, 0, 0))

    newGrid = [[value(j, i) for j in range(width)] for i in range(height)]

    return newGrid


def stampGridOnGrid(grid, stamp, offsetX, offsetY):
    for i in range(len(stamp)):
        for j in range(len(stamp[0])):
            if stamp[i][j] == 1:
                tmpColor = pygame.Color(255, 255, 255)
                tmpColor.hsla = (random.uniform(0, 360), 100, 50, 100)
                grid[i + offsetX][j + offsetY] = Cell(True, 255, tmpColor)


def render(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            s = pygame.Surface((9, 9))
            s.fill(grid[i][j].color)
            s.set_alpha(grid[i][j].brightness)
            screen.blit(s, (i * 10, j * 10))

    return


def getNeighbours(x, y, grid):
    aliveNeighbours = 0
    colorsNeighbours = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i in range(0, len(grid)) and j in range(0, len(grid[0])):
                if grid[i][j].alive and not (x == i and y == j):
                    aliveNeighbours += 1
                    colorsNeighbours.append(grid[i][j].color)

    return aliveNeighbours, colorsNeighbours


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    height = 180
    width = 100

    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    screen = pygame.display.set_mode((height * 10, width * 10))
    clock = pygame.time.Clock()
    running = True
    updating = False

    initGrid = [[0, 1, 1],
                [1, 1, 0],
                [0, 1, 0]]

    initGrid2 = [[0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 1, 1],
                 [0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0]]

    initGrid3 = [[0, 1, 1, 1],
                 [0, 1, 0, 1],
                 [0, 1, 1, 1],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 0, 0, 1]]

    initGrid4 = [[1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0, 1],
                 [0, 1, 1, 0, 0, 0, 0, 1],
                 [0, 0, 1, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0]]

    grid = initiateGrid(height, width)
    stampGridOnGrid(grid, initGrid, 30, 30)
    stampGridOnGrid(grid, initGrid, 50, 60)
    stampGridOnGrid(grid, initGrid, 100, 80)

    stampGridOnGrid(grid, initGrid, 120, 30)
    stampGridOnGrid(grid, initGrid, 100, 60)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posX = math.trunc(pos[0] / 10)
                posY = math.trunc(pos[1] / 10)
                if grid[posX][posY].alive:
                    grid[posX][posY] = grid[posX][posY].dead()
                else:
                    color = pygame.Color(255, 255, 255)
                    color.hsla = (random.uniform(0, 360), 100, 50, 100)
                    grid[posX][posY] = Cell(True, 255, color)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    updating = not updating
        screen.fill((50, 50, 50))

        if updating:
            grid = runTick(grid)
        render(grid)

        pygame.display.flip()

        clock.tick(60)
