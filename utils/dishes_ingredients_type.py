from typing import TypedDict, Dict


class Ingredient_Type(TypedDict):
    ingredient_name: str
    ingredient_qnt: int


class Dish_Type(TypedDict):
    name: str
    price: float
    ingredients: list[Ingredient_Type]


Dish_Dict = Dict[str, Dish_Type]
