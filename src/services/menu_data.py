from utils.csv_read import csv_data
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        data = csv_data(source_path)
        self.register_all_dishes(data)
    
    def register_all_dishes(self, data: list[list[str]]) -> None:
        for ingredient in data:
            ingredient_rep = f"Dish('{ingredient[0]}', R${ingredient[1]})"
            if ingredient_rep not in self.dishes:
                self.add_dish(Dish(ingredient[0], float(ingredient[1])))
            

    def add_dish(self, dish: Dish) -> None:
        self.dishes.add(dish)


menu_teste = MenuData('/home/bernardo/trybe/projetos/ciencia-da-computacao/sd-026-b-restaurant-orders/data/menu_base_data.csv')
print(menu_teste.dishes)