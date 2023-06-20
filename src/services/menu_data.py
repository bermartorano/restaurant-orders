from utils.csv_read import csv_data
from utils.dish_dict_formater import format_csv_to_dict
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.register_all_dishes(source_path)

    def register_all_dishes(self, file_path: str) -> None:
        data = csv_data(file_path)
        dishes_dict = format_csv_to_dict(data)
        for dish in dishes_dict.values():
            new_dish = Dish(dish['name'], dish['price'])
            for ingredient in dish['ingredients']:
                new_ingredient = Ingredient(ingredient['ingredient_name'])
                new_dish.add_ingredient_dependency(
                    new_ingredient,
                    ingredient['ingredient_qnt']
                    )
            self.dishes.add(new_dish)

    def add_dish(self, dish: Dish) -> None:
        self.dishes.add(dish)
