#Chad Johnson 1323504 LAB: Word frequencies
input_words = input().split()
for word in input_words:
    frequency = 0
    for w in input_words:
        if w == word:
            frequency += 1
    print(word, frequency)
