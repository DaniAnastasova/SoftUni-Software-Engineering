n = int(input())

for i in range(1111, 9999, 1):
    if n % (i//1000) == 0:
        if ((i//100)%10) == 0:
            continue
        else:
            if n % ((i // 100) % 10) == 0:
                if ((i // 10) % 10) == 0:
                    continue
                else:
                    if n % ((i // 10) % 10) == 0:
                        if (i % 10) == 0:
                            continue
                        else:
                            if n % (i % 10) == 0:
                                print(i, end=' ')



