from english_words import get_english_words_set
words_set = get_english_words_set(['web2'], lower=True)

fives = [word for word in words_set if len(word) == 5]

# print(len(fives))

def no_repeat(word):
    for ch in word:
        if word.count(ch) != 1:
            return False
    return True

no_repeats = [word for word in fives if no_repeat(word)]

# print(len(no_repeats))

def char_count(wordlist):
    alphs = {}
    for word in wordlist:
        for ch in word:
            if ch not in alphs:
                alphs[ch] = 1
            else:
                alphs[ch] += 1
    return alphs

counts = char_count(fives)

def sum_appear(word):
    summ = 0
    for ch in word:
        summ += counts[ch]
    return summ

max_chances = sorted(no_repeats, key = lambda x: sum_appear(x), reverse = True)

print(max_chances.index('adieu'), sum_appear('adieu'), len(max_chances))
print(max_chances)
