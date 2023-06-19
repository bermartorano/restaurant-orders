from utils.csv_read import csv_data

def format_csv_to_dict(data: list[list[str]]) -> dict:
    # final_dict = {}
    # for ingredient_info in data:
    #     final_dict[ingredient_info[0]] = {
    #         'nome': ingredient_info[0],
    #         'price': float(ingredient_info[1]),
    #     }
    #     ingredient_to_add = {
    #         'ingredient_name': ingredient_info[2],
    #         'ingredient_qnt': ingredient_info[3]
    #     }
    #     try:
    #         final_dict[ingredient_info[0]]['ingredients'].append(ingredient_to_add)
    #     except KeyError:
    #         final_dict[ingredient_info[0]]['ingredients'] = [ingredient_to_add]

    final_dict = {}
    for ingredient_info in data:
        ingredient_to_add = {
                'ingredient_name': ingredient_info[2],
                'ingredient_qnt': ingredient_info[3]
            }
        try:
            final_dict[ingredient_info[0]]['name'] = ingredient_info[0]
            final_dict[ingredient_info[0]]['price'] = float(ingredient_info[1])
            final_dict[ingredient_info[0]]['ingredients'].append(ingredient_to_add)
        except KeyError:
            final_dict[ingredient_info[0]] = {
                'name': ingredient_info[0],
                'price': float(ingredient_info[1]),
            }
            final_dict[ingredient_info[0]]['ingredients'] = [ingredient_to_add]
    return final_dict


print(format_csv_to_dict(csv_data('/home/bernardo/trybe/projetos/ciencia-da-computacao/sd-026-b-restaurant-orders/data/menu_base_data.csv'))['lasanha presunto'])
