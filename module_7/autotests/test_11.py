


def sequence_buttons(string):
    latin = (".",",","?","!",":","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ")
    nums = ("1","11","111","1111","11111","2","22","222","3","33","333","4","44","444","5","55","555","6","66","666","7","77","777","7777","8","88","888","9","99","999","9999","0")

    trans_dict = {}
    for c, l in zip(latin, nums):
        trans_dict[ord(c)] = l
        trans_dict[ord(c.upper())] = l.upper()
    return string.translate(trans_dict)


print(sequence_buttons("Hello, World!"))

