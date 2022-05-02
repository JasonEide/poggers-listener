def foo(lst: list, word: str) -> int:
    """ Precondition: Streamer must be live on twitch
    """
    temp = lst[:]
    acc = []
    for i in temp:
        # finds word
        file = open(f'{i}.log', 'r')
        data = file.read()
        acc.append(data.count(word))
        file.close()
        # rewrites file
        file = open(f'{i}.log', 'w')
        file.write('')
        file.close()
    return sum(acc)
