from abc import ABC
import abc
class Shape(abc.ABC):
    @abc.abstractclassmethod # Chu Vi
    def perimeter(self):
        pass
    
    @abc.abstractclassmethod # Diện Tích
    def area(self):
        pass