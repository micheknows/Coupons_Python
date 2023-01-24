# Here is the site for the API:  https://spoonacular.com/food-api/docs#Get-Random-Recipes

#pip install requests
import requests
import json

def get_recipes():
    ####################################################################################################
    #######  The number below can be up to 100 but lowering it during experimentations
    ####################################################################################################
    howmany =5
    base = 'https://api.spoonacular.com/recipes/random?number=' + str(howmany) + '&limitLicense=true'
    apikey = '&apiKey=5d979222ba32497c9b0eb6f964db59e9'
    base += apikey

    json_filename = 'recipes.json'

    r = requests.get(base)
    json_data = r.json()

    for key, value in json_data.items():
        for item in value:
            print("Recipe:  " + item['title'])
            print("Servings:  " + str(item['servings']))
            print("Source URL:  " + item['sourceUrl'])
            print("\n" + item['summary'] + "\n\n")
            print("Ingredients: \n")
            for ingredient in item['extendedIngredients']:
                print(ingredient['original'])
            print("\nInstructions: \n" + item['instructions'])
            print("\nCredits:  " + item['creditsText'])
            print('\n\n\n')

    with open(json_filename, "w") as write_file:
        json.dump(json_data, write_file, indent=4)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_recipes()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
