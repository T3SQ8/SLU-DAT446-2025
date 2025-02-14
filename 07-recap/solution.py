
import os

def get_favorites(persons):
    favorites = {}
    for name in persons:
        fav_number, fav_color = None, None
        if os.path.isfile(color_file := f'fav_colors/{name}'):
            with open(color_file, 'r') as f:
                fav_color = f.read().strip()
        if os.path.isfile(num_file := f'fav_numbers/{name}'):
            with open(num_file, 'r') as f:
                fav_number = int(f.read().strip())
        if fav_number and fav_color:
            favorites[name] = (fav_color, fav_number)
    return favorites



print(get_favorites(['emma', 'liam', 'julia']))
