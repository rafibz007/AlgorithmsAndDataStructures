from random import randint, shuffle

def comp(word, max_len, position):
    if len(word)+position < max_len: return " "
    else: return word[max_len - position - 1]

def insertion_sort(A, comp, position, max_len):
    for i in range(1, len(A)):
        j = i
        current = A[i]
        while j-1 >= 0 and ord(comp(A[j - 1], max_len, position)) > ord(comp(current, max_len, position)):
            A[j] = A[j-1]
        A[j] = current

def bucket_sort(list_of_words, position, max_len):
    buckets = [ [] for _ in range(224) ] #liczba znakow uzytkowych w ascii

    for i in range(len(list_of_words)):
        buckets[ ord( comp( list_of_words[i], max_len, position ) )-32 ].append(list_of_words[i])

    w_index = 0
    for bucket in buckets:
        insertion_sort(bucket, comp, position, max_len)
        for i in range(len(bucket)):
            list_of_words[w_index] = bucket[i]
            w_index += 1


def radix_sort(list_of_words):
    max_len = 0
    for word in list_of_words: max_len = max(max_len, len(word))
    for position in range(max_len): bucket_sort(list_of_words, position, max_len)



#
# string = "ABCDEFGH"
# print(comp(string, len(string), 0))
# print(ord(" "))
n = 10
T = []
for _ in range(n):
    word = ""
    for i in range(randint(1, 10)): word += chr(randint(65, 90))
    T.append(word)

print(T)
radix_sort(T)
print(T)
