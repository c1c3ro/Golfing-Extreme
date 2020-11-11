import pygame as pg
import sys
from collision import *
from terrain_generator import *

SCREENSIZE = (800,400)

screen = pg.display.set_mode(SCREENSIZE, pg.DOUBLEBUF|pg.HWACCEL)

v = Vector
vec = pg.math.Vector2

i = vec(80, 50)

p0 = Circle(v(i.x, i.y), 5)
#p1 = Concave_Poly(v(200,200), [v(-80,0), v(-20,20), v(0,80), v(20,20), v(80,0),  v(20,-20), v(0,-80), v(-20,-20)])
#print(p1.points)

terrain = TerrainGenerator(800, 400, 8, (200, 320))

points_v = []
for p in range(len(terrain.points)):
    if not(p == len(terrain.points) - 1):
        points_v.append(v(terrain.points[p][0], terrain.points[p][1]))
terrain_poly = Concave_Poly(v(0, 0), points_v)

print(terrain.points)



# for p in range(len(p1.points) - 1):
#     pg.draw.line(screen, (255, 255, 255), p1.points[p], p1.points[p + 1])
#     pg.display.flip()
#     pg.time.wait(3000)

clock = pg.time.Clock()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    screen.fill((0,0,0))

    p0.pos.x += 1
    p0.pos.y += 1
    #p0.angle += 0.005

    p0c, p1c = (0,255,255),(0,255,255)
    #p0bc = (255,255,255)
    #p1bc = (255,255,255)

    if collide(p0,terrain_poly): p1c = (255,0,0); p0c = (255,0,0);
    #if test_aabb(p0.aabb,p1.aabb): p1bc = (255,0,0); p0bc = (255,0,0);

    pg.draw.circle(screen, p0c, (int(p0.pos.x), int(p0.pos.y)), 5, 0)
    #pg.draw.polygon(screen, p1c, p1.points, 3)
    pg.draw.polygon(screen, p1c, terrain_poly.points, 3)

    #pg.draw.polygon(screen, p0bc, (p0.aabb[0],p0.aabb[1],p0.aabb[3],p0.aabb[2]), 3)
    #pg.draw.polygon(screen, p1bc, (p1.aabb[0],p1.aabb[1],p1.aabb[3],p1.aabb[2]), 3)

    pg.display.flip()


    clock.tick(50)