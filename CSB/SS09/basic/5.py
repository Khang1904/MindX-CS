dictionary = {"cat": "mèo", "dog": "chó", "fish": "cá"}

word = input("Enter a word: ")

print(dictionary[word] if word in dictionary else "Word not found")
