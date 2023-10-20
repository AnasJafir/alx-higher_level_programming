#!/usr/bin/python3
"""Module for Base Class"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert data to JSON """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Save an object in file"""
        filename = "{}.json".format(cls.__name__)
        lst = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                lst.append(list_objs[i].to_dictionary())
        total = cls.to_json_string(lst)
        with open(filename, 'w') as f:
            f.write(total)

    @staticmethod
    def from_json_string(json_string):
        """JSON to Python data"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creating instance"""
        if cls.__name__ == "Rectangle":
            new_atr = cls(10, 10)
        else:
            new_atr = cls(10)
        new_atr.update(**dictionary)
        return new_atr

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r') as f:
            lst = f.read()
        list_cls = cls.from_json_string(lst)
        list_ins = []
        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))
        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a CSV file"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            dct = [0, 0, 0, 0, 0]
            keys = ['id', 'width', 'height', 'x', 'y']
        else:
            dct = ['0', '0', '0', '0']
            keys = ['id', 'size', 'x', 'y']
        matrix = []
        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for k_val in range(len(list_keys)):
                    list_dic[k_val] = obj.to_dictionary()[list_keys[k_val]]
                matrix.append(list_dic[:])
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Load a CSV file"""
        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            lst = list(reader)
        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']
        matrix = []
        for csv_elem in lst:
            dict_csv = {}
            for k_val in enumerate(csv_elem):
                dict_csv[list_keys[k_val[0]]] = int(k_val[1])
            matrix.append(dict_csv)
        list_ins = []
        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))
        return list_ins
