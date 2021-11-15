# Re'trie'val
# Trie é uma estrutura que ocupa bastante espaço na memória
# Em contrapartida é uma estrutura bastante eficiente, competindo em certos casos com a estrutura Hash

# TAD R-wayTrie
# R = 26

class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = [None] * 26


class Trie():
    def __init__(self, node):
        self.root = node

    def get(key):
        x = self._get(self.root, key, 0)

        if x == None:
            return None

        return x.data

    def _get(x, key, d):
        if x == None:
            return None

        if d == len(key):
            return x

        c = key[d]
        return self._get(x.next[c], key, d + 1)

    def put(key, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(x, key, val, d):
        if x == None:
            x = Node(val)

        if d == len(key):
            x.data = val
            return x

        c = key[d]
        x.next[c] = self._put(x.next[c], key, val, d + 1)
        return x

    def delete(key):
        self.root = self._delete(self.root, key, 0)

    def _delete(x, key, d):
        if x == None:
            return None

        if d == len(key):
            x.data = None
        else:
            c = key[d]
            x.next[c] = self._delete(x.next[c], key, d + 1)

        if x.data != None:
            return x

        c = 0
        for c in range(25):
            if x.next[c] != None:
                return x

        return x


# Análise de tempo de complexidade:
# Busca -> Ω(L) e O(log N na base R)
