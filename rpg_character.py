full_dot = '●'
empty_dot = '○'

def create_character(ch_name, strength, intelligence, charisma):
    # Name Validations
    if not isinstance(ch_name, str):
        return "The character name should be a string"
    elif len(ch_name) > 10:
        return "The character name is too long"
    elif " " in ch_name:
        return "The character name should not contain spaces"
        
    # Stat Type Check
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
        
    # Stat Minimum Check (FIXED: Used 'or' instead of 'and')
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
        
    # Stat Maximum Check
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
        
    # Stat Sum Check
    elif (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"  
    
    # Success Case
    else:
        # Building the final output string
        str_line = f"STR {full_dot*strength}{empty_dot*(10-strength)}"
        int_line = f"INT {full_dot*intelligence}{empty_dot*(10-intelligence)}"
        cha_line = f"CHA {full_dot*charisma}{empty_dot*(10-charisma)}"
        
        return f"{ch_name}\n{str_line}\n{int_line}\n{cha_line}"
    