from typing import Sequence, Tuple

def cross(o: Tuple[int , int],
          a: Tuple[int, int], 
          b: Tuple[int, int]) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points: Sequence[Tuple[int]]) -> Sequence[Tuple[int]]:
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

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
    hull = convex_hull(points)
    area = polygon_area(hull)

    print("Các điểm bao lồi:", hull)
    print("Diện tích bao lồi:", area)
