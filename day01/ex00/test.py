from recipe import Recipe
from book import Book
if __name__ == '__main__':

    try: 

        tajin = Recipe('tajin', 5, 60, ['tifya', 'maticha', 'batata', 'khizo', '...'], '10/10', 'lunch')
        disir = Recipe('disir', 1, 0, ['banan', 'tfah', 'dlah', 'swihla', '...'], '10/10', 'dessert')
        sfa = Recipe('sfa', 3, 30, ['???'], '8/10', 'starter')
        koskos = Recipe('koskos', 3, 30, ['smid', 'takhsayt', 'dnjal', '...'], '10/10', 'lunch')

        book = Book('wasfati Siro Sa3adity')
        print(book.creation_date)

        book.add_recipe(tajin)
        book.add_recipe(disir)
        book.add_recipe(sfa)
        book.add_recipe(koskos)

        book.get_recipes_by_types('lunch')
        recipe = book.get_recipe_by_name('disir')
        print (f'\n{str(recipe)}\n')
        book.get_recipes_by_types('starter')
        print(book.last_update)

    except ValueError as error :

        print(error)
        exit(1)