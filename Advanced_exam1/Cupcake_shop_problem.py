def stock_availability(*args):
    from collections import deque
    all = deque([*args[0]])
    if args[1] == "delivery":
        for i in range(2, len(args)):
            all.append(args[i])
        return list(all)
    if args[1] == "sell":
        if not len(args) == 2:
            if isinstance(args[2], int):
                for _ in range(args[2]):
                    all.popleft()
                return list(all)
            elif isinstance(args[2], str):
                for i in range(2, len(args)):
                    if args[i] in all:
                        while args[i] in all:
                            all.remove(args[i])
                    return list(all)
        else:
            all.popleft()
            return list(all)



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
