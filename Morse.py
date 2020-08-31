morse_letters = {
    ' ': ' ',
    ',': ',',
    '.': '. ',
    'A': ' •- ',
    'B': ' -••• ',
    'C': ' -•-• ',
    'D': ' -•• ',
    'E': ' • ',
    'F': ' ••-• ',
    'G': ' --• ',
    'H': ' •••• ',
    'I': ' •• ',
    'J': ' •--- ',
    'K': ' -•- ',
    'L': ' •-••',
    'M': ' -- ',
    'N': ' -• ',
    'O': ' --- ',
    'P': ' •--• ',
    'Q': ' --•- ',
    'R': ' •-• ',
    'S': ' ••• ',
    'T': ' - ',
    'U': ' ••- ',
    'V': ' •••- ',
    'W': ' •-- ',
    'X': ' -••- ',
    'Y': ' -•-- ',
    'Z': ' --•• '
}

word = input('Enter a word: ').upper()
word = list(word)
start = 0

while start < len(word):
    print(morse_letters[word[start]], end=' ')
    start += 1