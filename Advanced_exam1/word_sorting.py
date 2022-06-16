def words_sorting(*args):
    all = {}
    prin = []
    a = 0
    sum_of_all = 0
    is_even = True
    for arg in args:
        value = [ord(i) for i in arg]
        for i in value:
            a += i
            sum_of_all += i
        all[arg] = a
        a = 0

    if a % 2 == 1:
        is_even = False

    if not is_even:
        all = dict(sorted(all.items(),
                          key=lambda item: item[0],
                          reverse=False))
    else:
        all = dict(sorted(all.items(),
                          key=lambda item: item[0],
                          reverse=True))
    for key, value in all.items():
        prin.append(f"{key} - {value}")
    return "\n".join(prin)