'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = clean_pokemon_name(pokemon)
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

     # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

def clean_pokemon_name(pokemon_name):
    return str(pokemon_name).strip().lower()

def get_all_pokemon_names():
    """Gets a list of all Pokemon names from the PokeAPI.

    Returns:
        list: List of Pokemon names, if successful. Otherwise an empty list.
    """
    url = POKE_API_URL + "?limit=1000"
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        data = response.json()
        return [entry["name"] for entry in data["results"]]
    return []

def download_and_save_pokemon_artwork(pokemon_name, save_path):
    """Downloads and saves Pokemon artwork from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)
        save_path (str): Path to save the downloaded artwork

    Returns:
        bool: True if download and save are successful, False otherwise.
    """
    pokemon_name = clean_pokemon_name(pokemon_name)
    image_url = get_pokemon_info(pokemon_name)["sprites"]["other"]["official-artwork"]["front_default"]
    
    response = requests.get(image_url)
    if response.status_code == requests.codes.ok:
        with open(save_path, 'wb') as f:
            f.write(response.content)
            return True
    return False

if __name__ == '__main__':
    main()