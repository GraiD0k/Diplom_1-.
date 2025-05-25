from praktikum.database import Database
import pytest

class TestDatabase:
    @pytest.mark.parametrize('result',['black bun','white bun','red bun'])
    def test_available_buns(self,result):
        db = Database()
        buns = db.available_buns()
        buns_list = [bun.get_name() for bun in buns]
        assert result in buns_list, buns_list

    @pytest.mark.parametrize('result',['hot sauce','sour cream','chili sauce','cutlet','dinosaur','sausage'])
    def test_available_ingredients(self,result):
        db = Database()
        ingredients = db.available_ingredients()
        ingredients_list = [i.get_name() for i in ingredients]
        assert result in ingredients_list, ingredients_list