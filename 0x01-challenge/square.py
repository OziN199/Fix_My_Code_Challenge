#!/usr/bin/python3

class Square():
    
    width = 1
    height = 1

    
    def __init__(self, *args, **kwargs):
        if 'width' in kwargs and kwargs['width'] > 0:
        self.width = kwargs['width']
    else:
        self.width = 1
        
    if 'height' in kwargs and kwargs['height'] > 0:
        self.height = kwargs['height']
    else:
        self.height = 1
            setattr(self, key, value)

    def area_of_my_Square(self):
        """ Area of the Square """
        return self.width * self.height

    def PerimeterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_Square())
    print(s.PerimeterOfMySquare())
