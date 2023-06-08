import sys

if (len(sys.argv) > 1):
    string = sys.argv[1]
    words = string.split()
    for word in words:
        print(word[0], end='')

print()