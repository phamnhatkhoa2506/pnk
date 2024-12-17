import math

from typing import Sequence, Tuple

def cross(o: Tuple[int , int],
          a: Tuple[int, int], 
          b: Tuple[int, int]) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points: Sequence[Tuple[int]]) -> Sequence[Tuple[int]]:
    points = sorted(points)
    anchor = points[0]
    
    sorted_points = sorted(points[1:], key=lambda p: math.atan2(p[1] - anchor[1], p[0] - anchor[0]))
    
    hull = [anchor]
    for point in sorted_points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    
    return hull

def polygon_area(points: Sequence[Tuple[int]]) -> float:
    area = 0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2

if __name__ == '__main__':
    points = [(0, 0), (2, 0), (1, 1), (2, 2), (0, 2)]
    hull = graham_scan(points)
    area = polygon_area(hull)

    print("Các điểm bao lồi:", hull)
    print("Diện tích bao lồi:", area)
