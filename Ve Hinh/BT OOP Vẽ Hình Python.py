from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

class Shape(ABC):
    @abstractmethod
    def __init__(self,color,x_position,y_position):
        self.color = color
        self.x_position = x_position
        self.y_position = y_position

    def Draw(self):
        pass

class Circle(Shape):
    def __init__(self,color,x_position,y_position,radius):
        super().__init__(color,x_position,y_position)
        self.__radius = radius


    def Draw(self):
        figure, axes = plt.subplots()
        c = plt.Circle((self.x_position, self.y_position), self.__radius, color=self.color)
        axes.set_aspect(1)
        axes.add_artist(c)
        plt.title('Vẽ Hình Tròn ')
        plt.show()

class Elilipse(Shape):
    def __init__(self,color,x_position,y_position,angel,height,width):
        super().__init__(color,x_position,y_position)
        self.__angel = angel
        self.__height = height
        self.__width = width

    def Draw(self):
        figure, axes = plt.subplots()
        e = Ellipse((self.x_position, self.y_position), self.__width, self.__height, self.__angel, color=self.color)
        axes.add_artist(e)
        plt.title('Vẽ Hình Elip ')
        plt.show()


class Rectangle(Shape):
    def __init__(self,color,x_position,y_position,height,width):
        super().__init__(color,x_position,y_position)
        self.__height = height
        self.__width = width

    def Draw(self):
        figure, axes = plt.subplots()
        r = plt.Rectangle((self.x_position, self.y_position), self.__width, self.__height, color=self.color)
        axes.add_artist(r)
        plt.title('Vẽ Hình Chũ Nhật ')
        plt.show()


ht = Circle('pink',0.6,0.6,0.2)
ht.Draw()
h1 = Elilipse('red',0.3,0.4,60,0.2,0.4)
h1.Draw()
hcn = Rectangle('blue',0.1,0.2,0.4,0.6)
hcn.Draw()






