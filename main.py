# Here is the site for the API:  https://spoonacular.com/food-api/docs#Get-Random-Recipes
# So far when I do the maximum of 100 recipes per 1 request, my data file is only about 2.2mb.
# With the free account I can do up to 60 requests in one minute  -- and each request of 100 recipes counts
# for somewhere between 1 and 2 pts.  On the free account, I can have 150 points in one day.  Even if I multiply this
# by 100 that's only 220mb of data in one day.  But, that's not counting the couponing data.  So, will this work?


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

    json_filename = 'recipes.json'           # where to save the data for now.  This can definitely be different later.

    r = requests.get(base)                  # send the request
    json_data = r.json()                    # read it as json

    for key, value in json_data.items():                        # go through and print major points of each recipe to
        for item in value:                                      # the screen
            print("Recipe:  " + item['title'])
            print("Servings:  " + str(item['servings']))
            print("Source URL:  " + item['sourceUrl'])
            print("\n" + item['summary'] + "\n\n")
            # this isn't the best way to do the ingredients. It needs to be parsed out from the different keys to
            # get the amounts and the ingredient.  This is just the most simple for right now
            print("Ingredients: \n")
            for ingredient in item['extendedIngredients']:
                print(ingredient['original'])
            print("\nInstructions: \n" + item['instructions'])
            print("\nCredits:  " + item['creditsText'])
            print('\n\n\n')

    with open(json_filename, "w") as write_file:                # save the entire data to a file with indents
        json.dump(json_data, write_file, indent=4)


if __name__ == '__main__':
    get_recipes()

