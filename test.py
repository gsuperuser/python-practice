def caesar(text, shift):
    if not isinstance(shift, int):
        return 'Shift must be an integer'
    if shift > 25 or shift < 1:
        return 'Shift must be between 1 and 25'
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_text = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper() , shifted_text+shifted_text.upper())
    return text.translate(translation_table)

print(caesar('freeCodeCamp' ,1))