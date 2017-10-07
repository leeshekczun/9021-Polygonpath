from argparse import ArgumentParser
from itertools import count
from re import sub
import os
import math
import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
import numpy

parser = ArgumentParser()
parser.add_argument('-print', dest='print', action='store_true')
parser.add_argument('--file', dest='filename', required=True)
args = parser.parse_args()

file_name = args.filename

try:
    grim = []
    with open(file_name) as file:
        for line in file:
            if not line.strip():
                continue
            grim.append([])
            new_line = line.replace(' ', '')
            for i in new_line.strip():
                if i != '0':
                    if i != '1':
                        raise ValueError
                else:
                    grim[-1].append(int(i))
        if not 2 <= len(grim) <= 50:
            raise ValueError

except FileNotFoundError:
    print('Sorry, there is no such file.')
    sys.exit()

except ValueError:
    print('Incorrect input.')
    sys.exit()



def southeast(grim,i,j,former_i,former_j,patha):
    if 0 <= i+1 < len(grim) and 0 <= j+1 < len(grim[i+1]) and grim[i+1][j+1] != 0 and (former_i != i+1 or former_j != j+1):
        if [i+1,j+1] == default[0]:
            return patha
        for k in default:
            if k == [i+1,j+1]:
                break
        else:
            ahead = go_next(grim,i+1,j+1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def south(grim,i,j,former_i,former_j,patha):
    if 0 <= i+1 < len(grim) and 0 <= j < len(grim[i+1]) and grim[i+1][j] != 0 and (former_i != i+1 or former_j != j):
        if [i+1,j] == default[0]:
            return patha
        for k in default:
            if k == [i+1,j]:
                break
        else:
            ahead = go_next(grim,i+1,j,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def southwest(grim,i,j,former_i,former_j,patha):
    if 0 <= i+1 < len(grim) and 0 <= j-1 < len(grim[i+1]) and grim[i+1][j-1] != 0 and (former_i != i+1 or former_j != j-1):
        if [i+1,j-1] == default[0]:
            return patha
        for k in default:
            if k == [i+1,j-1]:
                break
        else:
            ahead = go_next(grim,i+1,j-1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def west(grim,i,j,former_i,former_j,patha):
    if 0 <= i < len(grim) and 0 <= j-1 < len(grim[i]) and grim[i][j-1] != 0 and (former_i != i or former_j != j-1):
        if [i,j-1] == default[0]:
            return patha
        for k in default:
            if k == [i,j-1]:
                break
        else:
            ahead = go_next(grim,i,j-1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def northwest(grim,i,j,former_i,former_j,patha):
    if 0 <= i-1 < len(grim) and 0 <= j-1 < len(grim[i-1]) and grim[i-1][j-1] != 0 and (former_i != i-1 or former_j != j-1):
        if [i-1,j-1] == default[0]:
            return patha
        for k in default:
            if k == [i-1,j-1]:
                break
        else:
            ahead = go_next(grim,i-1,j-1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def north(grim,i,j,former_i,former_j,patha):
    if 0 <= i-1 < len(grim) and 0 <= j < len(grim[i-1]) and grim[i-1][j] != 0 and (former_i != i-1 or former_j != j):
        if [i-1,j] == default[0]:
            return patha
        for k in default:
            if k == [i-1,j]:
                break
        else:
            ahead = go_next(grim,i-1,j,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def northeast(grim,i,j,former_i,former_j,patha):
    if 0 <= i-1 < len(grim) and 0 <= j+1 < len(grim[i]) and grim[i-1][j+1] != 0 and (former_i != i-1 or former_j != j+1):
        if [i-1,j+1] == default[0]:
            return patha
        for k in default:
            if k == [i-1,j+1]:
                break
        else:
            ahead = go_next(grim,i-1,j+1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def east(grim,i,j,former_i,former_j,patha):
    if 0 <= i < len(grim) and 0 <= j+1 < len(grim[i]) and grim[i][j+1] != 0 and (former_i != i or former_j != j+1):
        if [i,j+1] == default[0]:
            return patha
        for k in default:
            if k == [i,j+1]:
                break
        else:
            ahead = go_next(grim,i,j+1,i,j)
            if ahead:
                patha = patha + ahead
                return patha


def find_all_path(grim):
    path_all = []
    for i in range(len(grim)):
        for j in range(len(grim[i])):
            single_path = go_start(grim, i, j)
            if single_path:
                path_all.append(single_path)
                for k in single_path:
                    grim[k[0]][k[1]] = 0
    return path_all


def go_start(grim, i, j):
    global default
    default = []
    if grim[i][j] == 0:
        return
    else:
        global highest_height
        highest_height = i
        path = [[i, j]]
        if 0 <= i < len(grim) and 0 <= j + 1 < len(grim[i]) and grim[i][j + 1] != 0:
            ahead = go_next(grim, i, j + 1, i, j)
            if ahead:
                path = path + ahead
                return path
        if 0 <= i + 1 < len(grim) and 0 <= j + 1 < len(grim[i]) and grim[i + 1][j + 1] != 0:
            ahead = go_next(grim, i + 1, j + 1, i, j)
            if ahead:
                path = path + ahead
                return path
        if 0 <= i + 1 < len(grim) and 0 <= j < len(grim[i]) and grim[i + 1][j] != 0:
            ahead = go_next(grim, i + 1, j, i, j)
            if ahead:
                path = path + ahead
                return path
        if 0 <= i + 1 < len(grim) and 0 <= j - 1 < len(grim[i]) and grim[i + 1][j - 1] != 0:
            ahead = go_next(grim, i + 1, j - 1, i, j)
            if ahead:
                path = path + ahead
                return path
        return



def go_next(grim, i, j, former_i, former_j):
    if 0 <= i < len(grim) and 0 <= j < len(grim[i]):
        if grim[i][j] == 0:
            return
        else:
            default.append([former_i, former_j])
            patha = [[i, j]]
            if i == highest_height:

                if 0 <= i < len(grim) and 0 <= j+1 < len(grim[i]) and grim[i][j+1] != 0:
                    for k in default:
                        if k == [i, j+1]:
                            break
                    else:
                        ahead = go_next(grim, i, j+1, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha

                if 0 <= i+1 < len(grim) and 0 <= j+1 < len(grim[i+1]) and grim[i+1][j+1] != 0:
                    for k in default:
                        if k == [i+1, j+1]:
                            break
                    else:
                        ahead = go_next(grim, i+1, j+1, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha

                if 0 <= i+1 < len(grim) and 0 <= j < len(grim[i+1]) and grim[i+1][j] != 0:
                    for k in default:
                        if k == [i+1, j]:
                            break
                    else:
                        ahead = go_next(grim, i+1, j, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha

                if 0 <= i+1 < len(grim) and 0 <= j-1 < len(grim[i+1]) and grim[i+1][j-1] != 0:
                    for k in default:
                        if k == [i+1, j-1]:
                            break
                    else:
                        ahead = go_next(grim, i+1, j-1, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha
                return
            else:
                if i - 1 == former_i and j == former_j:
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    return
                elif i - 1 == former_i and j + 1 == former_j:
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    return
                elif i == former_i and j + 1 == former_j:
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    return
                elif i + 1 == former_i and j + 1 == former_j:
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    return
                elif i + 1 == former_i and j == former_j:
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    return
                elif i + 1 == former_i and j - 1 == former_j:
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    return
                elif i == former_i and j - 1 == former_j:
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    return
                else:
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    return
                return
    else:
        return



def depth_count(polygon_all, polygon):
    po = polygon_all[::-1]
    depth = 0
    for l in range(len(po)):
        if po[l] == polygon:
            index = l
            break
    for k in range(l+1,len(po)):
        if po[k][0][0][0] == polygon[0][0][0]:
            continue
        check = 0
        for j in range(len(polygon)):
            count = 0
            for i in range(len(po[k])):
                start_x = po[k][i][0][1]
                start_y = po[k][i][0][0]
                end_x = po[k][i][-1][1]
                end_y = po[k][i][-1][0]
                if (polygon[j][0][0] >= start_y and polygon[j][0][0] < end_y) or (
                        polygon[j][0][0] <= start_y and polygon[j][0][0] > end_y):
                    if polygon[j][0][1] < (
                                (end_x - start_x) * (polygon[j][0][0] - start_y) / (end_y - start_y) + start_x):
                        count += 1
            if not count % 2 == 1:
                check += 1
        if check == 0:
            depth = depth_count(polygon_all,po[k]) + 1
            return depth
    return depth


def area(polygon):
    area = 0
    for i in range(len(polygon)):
        i1 = (i+1)%n
        area += polygon[i][0][0]*polygon[i1][1][0] - polygon[i1][0][0]*polygon[i][1][0]
    area *= 0.08
    return abs(area)

def convex(polygon):
    check_con = []
    for i in range(len(polygon)):
        check_con.append(numpy.dot(list(map(lambda x: x[0]-x[1], zip(polygon[i][1], polygon[i][0]))),list(map(lambda x: x[0]-x[1], zip(polygon[(i+1)%len(polygon)][1], polygon[(i+1)%len(polygon)][0])))))
    if abs(sum(check_con)) == sum(map(abs, check_con)):
        return 'yes'
    else:
        return 'no'

def rotation(polygon):
    for i in range(len(polygon)):
        elenth = []
        for i in range(len(polygon)):
            x1 = polygon[i][0][0]
            y1 = polygon[i][0][1]
            x2 = polygon[i][1][0]
            y2 = polygon[i][1][1]
            if x1 == x2 or y1 == y2:
                elenth.append((abs(x1 - x2) + abs(y1 - y2)))
            else:
                elenth.append(abs(x1 - x2)*1.4)
    if len(set(elenth)) == 1:
        return len(polygon)
    elif len(polygon) % 2 == 1:
        return 1
    else:
        center = [(polygon[0][0][0]+polygon[len(polygon)/2][0][0])/2, (polygon[0][0][1]+polygon[len(polygon)/2][0][1])/2]
        comparepoint=[]
        points=[]
        angle = 45
        for i in range(len(polygon)):
            points.append(polygon[i])
            comparepoint.append([(center[0] + math.cos(angle) * (polygon[i][0][0] - center[0]) - math.sin(angle) * (polygon[i][0][1] - center[1])),((center[1] + math.sin(angle) * (polygon[i][0][0] - center[0]) + math.cos(angle) * (polygon[i][0][1] - center[1])))])
        if set(comparepoint) == set(points):
            return 8
        comparepoint=[]
        points=[]
        angle = 90
        for i in range(len(polygon)):
            points.append(polygon[i])
            comparepoint.append([(center[0] + math.cos(angle) * (polygon[i][0][0] - center[0]) - math.sin(angle) * (polygon[i][0][1] - center[1])),((center[1] + math.sin(angle) * (polygon[i][0][0] - center[0]) + math.cos(angle) * (polygon[i][0][1] - center[1])))])
        if set(comparepoint) == set(points):
            return 4
        comparepoint=[]
        points=[]
        angle = 180
        for i in range(len(polygon)):
            points.append(polygon[i])
            comparepoint.append([(center[0] + math.cos(angle) * (polygon[i][0][0] - center[0]) - math.sin(angle) * (polygon[i][0][1] - center[1])),((center[1] + math.sin(angle) * (polygon[i][0][0] - center[0]) + math.cos(angle) * (polygon[i][0][1] - center[1])))])
        if set(comparepoint) == set(points):
            return 2
        return 1


def perimeter(polygon):
    int = 0
    sqr = 0
    for i in range(len(polygon)):
        x1 = polygon[i][0][0]
        y1 = polygon[i][0][1]
        x2 = polygon[i][1][0]
        y2 = polygon[i][1][1]
        if x1 == x2 or y1 == y2:
            int += (abs(x1-x2) + abs(y1-y2))
        else:
            sqr += abs(x1-x2)
    length_int = round(0.4*int,1)
    if sqr == 0:
        return str(length_int)
    elif int == 0:
        return str(sqr)+'*'+'sqrt(.32)'
    else:        
        length_sqr = str(sqr)+'*'+'sqrt(.32)'
        return str(length_int) + ' + ' + length_sqr

def changingpath(path):
    polygon = [[]]
    for i in range(len(path)):
        point1 = path[i]
        point2 = path[i - 1]
        point3 = path[i - 2]
        if (point2[1] - point1[1])/(point2[0]-point1[0]) - (point3[1] - point1[1])/(point3[0]-point1[0]) != 0:
            polygon[-1].append(point2)
            polygon.append([point2])
    polygon[-1].append(polygon[0][0])
    polygon.pop(0)
    if polygon[0][0] != path[0]:
        polygon = polygon[1:] + [polygon[0]]
    return polygon


polygon_all = []
path_all = find_all_path(grim)
for i in path_all:
    polygon_all.append(changingpath(i))   

for i in grim:
    for j in i:
        if j == 1:
            print('Cannot get polygons as expected.')
            sys.exit()

if not args.print:
    for i in range(len(polygon_all)):
        p = perimeter(polygon_all[i])
        a = area(polygon_all[i])
        c = convex(polygon_all[i])
        n = rotation(polygon_all[i])
        d = depth_count(polygon_all, polygon_all[i])
        print(f'Polygon {i+1}:\n'
              f'    Perimeter: {p}\n'
              f'    Area: {a:.2f}\n'
              f'    Convex: {c}\n'
              f'    Nb of invariant rotations: {n}\n'
              f'    Depth: {d}')

else:
    image_name = sub('\..*$', '', file_name)
    if os.path.isfile(image_name + '.tex'):
        for i in count():
            image_name = image_name + str(i)
            if not os.path.isfile(image_name + '.tex'):
                break
    tex_filename = image_name + '.tex'

    y_max = len(grim) - 1
    x_max = len(grim[0]) - 1
    hightlen = defaultdict(list)
    arealist = []
    for polygon in polygon_all:
        arealist.append(area(polygon))
        d = depth_count(polygon_all, polygon)
        hightlen[d].append(polygon)
    max_area = max(arealist)
    min_area = min(arealist)
    differ = max_area - min_area

    with open(tex_filename, 'w') as tex_file:
        print('\\documentclass[10pt]{article}\n'
              '\\usepackage{tikz}\n'
              '\\usepackage[margin=0cm]{geometry}\n'
              '\\pagestyle{empty}\n'
              '\n'
              '\\begin{document}\n'
              '\n'
              '\\vspace*{\\fill}\n'
              '\\begin{center}\n'
              '\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]\n'
              '\\draw[ultra thick] (0, 0) -- ({}, 0)'.format(x_max) +' -- ({}, {})'.format(x_max,y_max) +' -- (0, {})'.format(y_max) + ' -- cycle;', file = tex_file),

        for i in hightlen:
            print(f'%Depth {i}', file=tex_file)
            for j in hightlen[i]:
                color = round(100 - ((area(j) - min_area) * 100 / differ))
                print(f'\\filldraw[fill=orange!{color}!yellow] ', end='', file=tex_file)
                for k in j:
                    x = k[0][1]
                    y = k[0][0]
                    print(f'({x}, {y}) -- ', end='', file=tex_file)
                print('cycle;', file=tex_file)

        print('\\end{tikzpicture}\n'
              '\\end{center}\n'
              '\\vspace*{\\fill}\n'
              '\n'
              '\\end{document}', file=tex_file)
