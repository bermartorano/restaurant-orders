from utils.dishes_ingredients_type import Dish_Dict


def format_csv_to_dict(data: list[list[str]]) -> Dish_Dict:
    final_dict = {}
    for ingred_info in data:
        ingredient_to_add = {
                'ingredient_name': ingred_info[2],
                'ingredient_qnt': int(ingred_info[3])
            }
        try:
            final_dict[ingred_info[0]]['name'] = ingred_info[0]
            final_dict[ingred_info[0]]['price'] = float(ingred_info[1])
            final_dict[ingred_info[0]]['ingredients'].append(ingredient_to_add)
        except KeyError:
            final_dict[ingred_info[0]] = {
                'name': ingred_info[0],
                'price': float(ingred_info[1]),
            }
            final_dict[ingred_info[0]]['ingredients'] = [ingredient_to_add]
    return final_dict
