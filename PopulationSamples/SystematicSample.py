from Random.WithSeed import WithSeed


class SystematicSampling():
    @staticmethod

    def systematicSampling(lst):
        size = len(lst)
        num = round((RandomWithSeed.randomInt(size, 2, size))/4)

        if num == 1:
            num = 3

        lst2 = []
        temp = num - 1

        while temp <= size-1:
            value = lst[temp]
            lst2.append(value)
            temp+= num

        return lst2