

class Rect:
    def __init__(self, x1, y1, x2, y2):
        """
        bottom left point (x1, y1) 
        top right point (x2, y2) 

        ---------(x2, y2)
        |              |
        (x1, y1) -------

        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_top_left(self):
        return (self.x1, self.y2)

    def get_bottom_right(self):
        return (self.x2, self.y1)


def get_inter_x(A, B):
    """
    x-axis intersect size of two Rectangle
    """
    return max(0, min(A.x2, B.x2) - max(A.x1, B.x1))


def get_inter_y(A, B):
    """
    y-axis intersect size of two Rectangle
    """
    return max(0, min(A.y2, B.y2) - max(A.y1, B.y1))


def get_inter_rect(A, B):
    """
    intersect Rectangle size of two Rectangle
    """
    return get_inter_x(A, B) * get_inter_y(A, B)


def get_inter_square(A, B):
    """
    intersect Rectangle size of two Rectangle
    """
    return min(get_inter_x(A, B), get_inter_y(A, B)) ** 2


def min(x, y): return x if x < y else y


def max(x, y): return x if x > y else y
