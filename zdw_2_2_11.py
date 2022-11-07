def is_sorted(word_list, alphabet):
    alphabet = list(alphabet)
    try:
        for i in range(0, len(word_list)-1):
            k = 0
            while word_list[i][k] == word_list[i+1][k]:
                k += 1
            if alphabet.index(word_list[i][k]) > alphabet.index(word_list[i+1][k]):
                return False
    except IndexError:
        if len(word_list[i]) > len(word_list[i+1]):
            return False
    return True


print(is_sorted(["hello", "emma"], "hlabcdefgijkmnopqrstuvwxyz"))
print(is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
print(is_sorted(["down", "funny", "carrot", "vote"], "abdefghijklmnopqrstcuvwxyz"))
