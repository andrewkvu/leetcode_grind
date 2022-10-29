class Solution:
    
    # compute area of both rectangles separately
    # get width and height of overlapping
    # width: minimum of the x2's - max of x1s
    # 3 - 0 = 3
    # height: min of y2's - max of y1's
    # 2 - 0 = 2
    # if either width or height are < 0, there are no overlaps so its just the sum of the separate rectangles
    # else, you subtract the overlap buffer from that total area

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # compute area of both rectangles separately
        widthA = abs(ax2 - ax1)
        heightA = abs(ay2 - ay1)
        widthB = abs(bx2 - bx1)
        heightB = abs(by2 - by1)

        areaA = widthA * heightA
        areaB = widthB * heightB

        # calculate overlapping area and subtract it
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)

        if overlapWidth <= 0 or overlapHeight <= 0:
            return areaA + areaB
        else:
            return areaA + areaB - (overlapWidth * overlapHeight)

