'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, inc=None):
    if inc == None:
        inc = 0
    if inc < len(word):
        if inc + 1 ==  len(word):
            return 0
        elif f"{word[inc]}{word[inc+1]}" == "th":
            return 1 + count_th(word, inc + 2)
        else:
            return 0 + count_th(word, inc + 1)
    else:
        return 0
