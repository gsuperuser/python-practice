def caesar(text, shift, encrypt = True):
    if not isinstance(shift, int):
        return 'Shift must be an integer'
    if shift > 25 or shift < 1:
        return 'Shift must be between 1 and 25'

    if not encrypt:
        shift = -shift


    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_text = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper() , shifted_text+shifted_text.upper())
    return text.translate(translation_table)

encypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)

print(decrypt(encypted_text, 13))
