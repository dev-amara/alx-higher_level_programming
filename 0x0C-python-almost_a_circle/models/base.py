#!/usr/bin/python3
"""A class Base that defines a base of all other classes."""
import json
import csv
import turtle

class Base:
    """Module of a base


    Attributes:
        id (int): Describes the identity of each instance
        __nb_objects (int): Describes the number of instances of our class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base attributes


        Args:
          id (int): Describes the identity of each instance

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return(json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))
    
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        my_obj = []
        if list_objs is not None:
            for elm in list_objs:
                my_obj.append(cls.to_dictionary(elm))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(my_obj))
    
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        my_obj = []
        try:
            with open(filename, 'r') as file:
                my_obj = cls.from_json_string(file.read())
            for i, elm in enumerate(my_obj):
                my_obj[i] = cls.create(**my_obj[i])
        except (Exception):
            pass
        return(my_obj)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of rectangles or squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for elm in list_objs:
                    writer.writerow([elm.id, elm.width, elm.height, elm.x, elm.y])
            elif cls.__name__ == "Square":
                for elm in list_objs:
                    writer.writerow([elm.id, elm.size, elm.x, elm.y])
    
    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of rectanglesor squares in csv"""
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        window = turtle.Screen()
        turtle.speed(5)
        turtle.pensize(5)
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.color("black")
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for colors in ["red", "yellow", "purple", "blue"]:
                turtle.color(colors)
                turtle.forward(square.size)
                turtle.left(90)
        turtle.penup()
        
        window.exitonclick()
