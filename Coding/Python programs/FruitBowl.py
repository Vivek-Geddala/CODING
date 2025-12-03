import sys, math

def lower_hull(points):
    hull = []
    for p in points:
        while len(hull) >= 2:
            x1,y1 = hull[-2]; x2,y2 = hull[-1]; x3,y3 = p
            cross = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
            if cross <= 0:  # pop if not making a left turn
                hull.pop()
            else:
                break
        hull.append(p)
    return hull

def polyline_length(pts):
    return sum(math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1]) for i in range(len(pts)-1))

data = [line.strip() for line in sys.stdin if line.strip()]
n = int(data[0])
pts = [tuple(map(int, data[i].split())) for i in range(1, n+1)]
pts.sort()  # by x, then y
lh = lower_hull(pts)
perim = polyline_length(lh)
print(int(perim + 0.5))  # nearest integer
