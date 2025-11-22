test_settings = {
    'theme' : 'dark'

}
def add_setting(themes, new_pair):
    if not isinstance(themes, dict) and not isinstance(new_pair, tuple):
        return
    key , val = new_pair
    key, val = key.lower(), val.lower()
    if key in themes:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        themes[key] = val
        return f"Setting '{key}' added with value '{val}' successfully!"
    
def update_setting(themes, new_pair):
    key , val = new_pair
    key , val =  key.lower(), val.lower()
    if key in themes:
        themes[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(themes, key):
    key =  key.lower()
    if key in themes:
        del themes[key]
        return f"Setting '{key}' deleted successfully!"    
    else:
        return f"Setting not found!"

def view_settings(themes):
    string = 'Current User Settings:\n'
    if themes:
        for key,value in themes.items():
            string += f"{key.capitalize()}: {value}\n"
        return string
    else:
        return f"No settings available."

print(view_settings(test_settings))