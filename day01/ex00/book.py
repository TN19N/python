from datetime import datetime

class Book:
    def __init__(self, name):
        if type(name) != str or len(name) == 0 or name.isspace() :
            raise ValueError('Book name shold be non empty string !!')

        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {'starter': [], 'lunch' : [], 'dessert' : []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for key in self.recipes_list :
            for recipe in self.recipes_list[key] :
                if recipe.name == name :
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key in self.recipes_list :
            if recipe_type == key:
                for recipe in self.recipes_list[key] :
                    print(f'{recipe.name}')

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
    