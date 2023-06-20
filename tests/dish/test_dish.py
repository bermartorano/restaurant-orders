from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
from pytest import raises


# Req 2
def test_dish():
    info_1 = ['macarrão', 20.00]
    info_2 = ['sushi', 100.00]
    dish_1 = Dish(info_1[0], info_1[1])
    dish_2 = Dish(info_1[0], info_1[1])
    dish_3 = Dish(info_2[0], info_2[1])

    ingredient = Ingredient('farinha')
    dish_1.add_ingredient_dependency(ingredient, 1.5)

    assert dish_1.name == info_1[0]
    assert hash(dish_1) == hash(dish_2)
    assert hash(dish_1) != hash(dish_3)
    assert dish_1 == dish_2
    assert dish_1 != dish_3
    assert dish_1.__repr__() == "Dish('macarrão', R$20.00)"

    with raises(TypeError, match='Dish price must be float.'):
        Dish('nome', 'preco_errado')
    with raises(ValueError, match='Dish price must be greater then zero.'):
        Dish('nome', -1.00)

    assert dish_1.get_restrictions() == {Restriction.GLUTEN}
    assert dish_1.get_ingredients() == {ingredient}
