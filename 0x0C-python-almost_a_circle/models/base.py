#!/usr/bin/python3
'''Creating a Base Model Class.'''

import json
import csv
import turtle


class Base:
    """
    Basic model with serialization, file handling, and drawing functionality.

    Attributes:
        __nb_objects (int): Number of instantiated bases.
        id (int): Identifier for an instance.
    """

    __nb_objects = 0

    def __init__(self, instance_id=None):
        """
        Initialize a base instance.

        Args:
            instance_id (int): Identifier for the instance.
			If None, auto-generates a unique ID.
        """
        self.id = instance_id if instance_id is not None
		else Base.__nb_objects + 1
        Base.__nb_objects += 1

    @classmethod
    def from_json(cls, json_str):
        """
        Convert a JSON string to a Python object.

        Args:
            json_str (str): JSON string.

        Returns:
            list: List of dictionaries representing objects.
        """
        return [] if not json_str or json_str == '[]' else json.loads(json_str)

    @classmethod
    def to_json(cls, obj_list):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            obj_list (list): List of dictionaries representing objects.

        Returns:
            str: JSON string.
        """
        return '[]' if not obj_list else json.dumps(obj_list)

    @classmethod
    def load(cls):
        """
        Load objects from a JSON file and create instances using the
		create method.

        Returns:
            list: List of created instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                obj_list = cls.from_json(file.read())
                return [cls.create(**obj) for obj in obj_list]
        except IOError:
            return []

    @classmethod
    def save(cls, obj_list):
        """
        Save objects to a JSON file.

        Args:
            obj_list (list): List of objects to be saved.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            obj_list = [obj.to_dict() for obj in obj_list] if obj_list else []
            file.write(cls.to_json(obj_list))

    @classmethod
    def load_csv(cls):
        """
        Load objects from a CSV file and create instances using the create
		method.

        Returns:
            list: List of created instances.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = cls.get_fieldnames()
                obj_list = csv.DictReader(csvfile, fieldnames=fieldnames)
                obj_list = [cls.cast_to_int(obj) for obj in obj_list]
                return [cls.create(**obj) for obj in obj_list]
        except IOError:
            return []

    @classmethod
    def save_csv(cls, obj_list):
        """
        Save objects to a CSV file.

        Args:
            obj_list (list): List of objects to be saved.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if obj_list:
                fieldnames = cls.get_fieldnames()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in obj_list:
                    writer.writerow(obj.to_dict())

    @staticmethod
    def draw(rect_list, square_list):
        """
        Draw rectangles and squares using Turtle graphics.

        Args:
            rect_list (list): List of rectangles to be drawn.
            square_list (list): List of squares to be drawn.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#aabbcc")
        turt.pensize(3)
        turt.shape("turtle")

        Base.draw_objects(turt, rect_list, "#ffcc00")
        Base.draw_objects(turt, square_list, "#3366ff")

        turtle.exitonclick()

    @staticmethod
    def draw_objects(turtle_obj, obj_list, color):
        """
        Draw a list of objects using Turtle graphics.

        Args:
            turtle_obj (turtle.Turtle): Turtle graphics object.
            obj_list (list): List of objects to be drawn.
            color (str): Color of the objects.
        """
        turtle_obj.color(color)
        for obj in obj_list:
            turtle_obj.showturtle()
            turtle_obj.up()
            turtle_obj.goto(obj.x, obj.y)
            turtle_obj.down()
            for _ in range(2):
                turtle_obj.forward(obj.width)
                turtle_obj.left(90)
                turtle_obj.forward(obj.height)
                turtle_obj.left(90)
            turtle_obj.hideturtle()

    @staticmethod
    def get_fieldnames():
        """
        Get the fieldnames for CSV file handling.

        Returns:
            list: List of fieldnames.
        """
        return ['id', 'width', 'height', 'x', 'y']
		if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']

    @staticmethod
    def cast_to_int(obj):
        """
        Cast dictionary values to integers.

        Args:
            obj (dict): Input dictionary.

        Returns:
            dict: Dictionary with values cast to integers.
        """
        return {k: int(v) for k, v in obj.items()}
