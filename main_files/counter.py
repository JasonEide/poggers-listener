def foo(lst, word: str) -> int:
    temp = lst[:]
    acc = []
    for i in temp:
        file = open(f'{i}.log', 'r')
        data = file.read()
        acc.append(data.count(word))
    return sum(acc)
