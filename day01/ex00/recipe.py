class Recipe:
    def __init__(self, name, cooking_lvl, coking_time, ingredients, description, recipe_type):

        if type(name) != str or len(name) == 0 or name.isspace() :
            raise ValueError('Recipe name shold be non empty string !!')
        if type(cooking_lvl) != int or int(cooking_lvl) < 1 or int(cooking_lvl) > 5 :
            raise ValueError('Recipe cooking_lvl shold be a number between 1 and 5 !!')
        if type(coking_time) != int or int(coking_time) < 0:
            raise ValueError('Recipe coking_time shold be no negative number !!')
        if type(ingredients) != list or len(ingredients) == 0 or not all(type(ing) == str for ing in ingredients):
            raise ValueError('Recipe ingredients shold be non empty string list !!')
        if type(description) != str:
            raise ValueError('Recipe description shold be a string !!')
        if type(recipe_type) != str or not recipe_type in ['starter', 'lunch', 'dessert']:
            raise ValueError('Recipe recipe_type shold be a string from types (starter, lunch, dessert) !!')

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.coking_time = coking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return self.description