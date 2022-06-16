def flights(*args):
    all_f = []
    dictionary = {}
    for f in args:
        all_f.append(f)
    for i in range(0, len(all_f), 2):
        if all_f[i] == "Finish":
            break
        elif not all_f[i] in dictionary:
            dictionary[all_f[i]] = all_f[i + 1]
        else:
            dictionary[all_f[i]] += all_f[i + 1]
    return dictionary
