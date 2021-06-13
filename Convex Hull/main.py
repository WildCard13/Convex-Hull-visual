import numpy as np
import pygame

pnt_colour = (255, 255, 255)
hull_colour = (253, 184, 0)
line_colour = (254, 107, 222)

def solve(p1, p2, p3):
    return (((p2[0]-p1[0]) * (p3[1]-p1[1]) - (p2[1]-p1[1]) * (p3[0]-p1[0])) < 0)


def main():
    pygame.init()
    window = pygame.display.set_mode((800,700))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Convex-Hull")

    num = 16
    points  = np.random.randint(30, 650, size= 2*num)

    coordinates = []
    hulls = []

    for i in range(0, len(points)-1, 2):
        pygame.draw.circle(window, pnt_colour, (points[i], points[i+1]), 5)
        coordinates.append([points[i], points[i+1]])
        pygame.display.update()

    left_x = min([x_coordinate[0] for x_coordinate in coordinates])
    left_point = [x for x in coordinates if left_x is x[0]][0]
    pygame.draw.circle(window, hull_colour, left_point, 4)
    pygame.display.update()

    hull_point = left_point

    while(True):
        hulls.append(hull_point)
        subsequent_point = coordinates[((coordinates.index(hull_point))+1) % num]
        for check_point in coordinates:
            pygame.draw.line(window, line_colour, hull_point, check_point, 1)
            clock.tick(20)
            pygame.display.update()
            if (solve(hull_point, subsequent_point, check_point)):
                subsequent_point = check_point

        pygame.draw.line(window, hull_colour, hull_point, subsequent_point, 4)
        pygame.display.update()
        hull_point = subsequent_point


        if (hull_point == hulls[0]):
            break




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
