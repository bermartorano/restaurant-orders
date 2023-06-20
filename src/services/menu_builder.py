from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.ingredient import Restriction


DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction: Restriction = None) -> List[Dict]:
        menu = []
        dishes = self.menu_data.dishes
        for dish in dishes:
            dish_menu = {
                'dish_name': dish.name,
                'ingredients': dish.recipe,
                'price': dish.price,
                'restrictions': dish.get_restrictions()
            }
            should_append = True
            for restrict in dish_menu['restrictions']:
                if restrict == restriction:
                    should_append = False
                    break
            menu.append(dish_menu) if should_append else None
        return menu
