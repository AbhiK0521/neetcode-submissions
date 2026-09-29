from typing import List

def contains_duplicate(words: List[str]) -> bool:
    set_list = set()
    for i in range(len(words)):
        if words[i] in set_list:
            return True
        set_list.add(words[i])
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
