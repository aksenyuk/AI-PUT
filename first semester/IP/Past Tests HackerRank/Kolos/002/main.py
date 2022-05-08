word = input().lower()

if word == word[::-1]:
    print("YES")
    exit()

for i in range(len(word)):
    new_word = word[0:i] + word[i+1:]
    if new_word == new_word[::-1]:
        print("YES")
        exit()

    for j in range(len(new_word)):
        next_word = new_word[0:j]+new_word[j+1:]
        if next_word == next_word[::-1]:
            print("YES")
            exit()
print("NO")
