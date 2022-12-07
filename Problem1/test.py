import LRU

if __name__ == "__main__":
    our_cache = LRU.LRU(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print(our_cache.get(1))
    print(our_cache.get(2))
    print(our_cache.get(9))

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
