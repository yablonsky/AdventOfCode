def count_arrangements(adapters):
    def dfs_count(adapter, i=0, cache={}):
        if adapter == adapters[-1]:
            return 1

        if adapter not in cache:
            compat_adapters = [a for a in adapters[i+1:i+4] if a - adapter <= 3]
            cache[adapter] = sum(dfs_count(ca, i + j) for j, ca in enumerate(compat_adapters, 1))

        return cache[adapter]

    return dfs_count(adapters[0])


def adapter_arrangements(raw_data):
    adapters = [0] + sorted(int(x) for x in raw_data)
    adapters += [adapters[-1] + 3]

    return count_arrangements(adapters)


assert adapter_arrangements(open('input-10.txt')) == 2314037239808
