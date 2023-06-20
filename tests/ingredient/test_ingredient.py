from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingred_1 = Ingredient('lasanha')
    ingred_2 = Ingredient('lasanha')
    ingred_3 = Ingredient('farinha')

    assert hash(ingred_1) == hash(ingred_2)
    assert hash(ingred_1) != hash(ingred_3)
    assert ingred_1 == ingred_2
    assert ingred_1 != ingred_3
    assert ingred_1.__repr__() == "Ingredient('lasanha')"
    assert ingred_1.name == 'lasanha'
    assert ingred_3.restrictions == {Restriction.GLUTEN}
