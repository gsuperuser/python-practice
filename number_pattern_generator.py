def number_generator(n):
    string = ''
    if isinstance(n, int):
        if n > 0:
            for i in range(1 , n):
                string += f"{i} "
            string += str(n)
        else:
            return "Argument must be an integer greater than 0"
    else:
        return "Argument must be an integer value"
    return string


print(number_generator(4))
