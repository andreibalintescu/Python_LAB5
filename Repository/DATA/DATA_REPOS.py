import json
from Modelle.DISHES.FOOD_BEVERAGE import Beverage
class DataRepo:
    def __init__(self,file):
        self.file = file

    def save(self,file,data):
        with open(file,"w") as file:
            json.dump(data,file)

    def load(self,file):
        with open(file,'r') as file:
            return json.load(file)

    def read_file(self):
        pass
    def write_to_file(self):
        pass
    def convert_to_string(self):
        pass
    def convert_from_string(self):
        pass
class CookedDishRepo(DataRepo):
    def convert_to_string(self):
        pass
    def convert_from_string(self):
        pass
class DrinkRepo(DataRepo):
    def convert_to_string(self, list_of_drinks):
        def json_format(object):
            dict = json.dumps(object.__dict__)
            return dict

        converted = list(map(json_format, list_of_drinks))
        return str(converted)
    def convert_from_string(self, string):
        list_of_str_dicts = json.loads(string)
        list_of_drinks = [Beverage(**json.loads(item)) for item in list_of_str_dicts]
        return list_of_drinks

class CustomerRepo(DataRepo):
    def convert_to_string(self):
        pass
    def convert_from_string(self):
        pass
class OrderRepo(DataRepo):
    def convert_to_string(self):
        pass
    def convert_from_string(self):
        pass