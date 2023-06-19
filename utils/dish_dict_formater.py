from utils.csv_read import csv_data

def format_csv_to_dict(data: list[list[str]]) -> list[dict]:
    final_list = []
    for ingredient_info in data:
        final_dict = {}
        final_dict['name'] = ingredient_info[0]
        final_dict['price'] = float(ingredient_info[1])
        try:
            final_dict['ingredients'] = [{
                'ingredient_name': ingredient_info[2],
                'ingredient_qnt': int(ingredient_info[3])
            }]
        except KeyError:
            final_dict['ingredients'].append({
                'ingredient_name': ingredient_info[2],
                'ingredient_qnt': int(ingredient_info[3])
            })
        final_list.append(final_dict)
    return final_list

print(format_csv_to_dict(csv_data('/home/bernardo/trybe/projetos/ciencia-da-computacao/sd-026-b-restaurant-orders/data/menu_base_data.csv')))
