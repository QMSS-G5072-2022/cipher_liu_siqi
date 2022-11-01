def cipher(text, shift, encrypt=True):
    """
    description:
    The Caesar cipher is one of the simplest and most widely known encryption techniques.
    In short, each letter is replaced by a letter some fixed number of positions down the alphabet.
    Apparently, Julius Caesar used it in his private correspondence.

    :param text:
    String input

    :param shift:
    The integer for the fixed number of positions to shift the letters

    :param encrypt:
    Boolean value to decide whether ot not the function should encrypt ypur input string

    :return:
    The encrypted or decryted strings

    Example:
    >> cipher("text", 2, encrypt=True)
    output: "vgzv"

    >> cipher("text", 2, encrypt=False)
    output: "rcvr"
    """


    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text