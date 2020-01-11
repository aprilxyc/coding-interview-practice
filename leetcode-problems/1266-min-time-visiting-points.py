def minTimeTovisitAllPoints(points: List[List[int]]) -> int:
    max_diagonal = 0
    i = 0

    # get the last points
    x1, y1 = points.pop() 

    # loop through the points
    while i < len(points):
        x2, y2 = points.pop() # get the second points
        max_diagonal += max(abs(x1 - x2), abs(y1 - y2)) # add the maximum diagional you can make
        # now move left
        x1, y1 = x2, y2
    return max_diagonal