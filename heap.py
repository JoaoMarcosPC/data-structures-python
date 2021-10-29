# Estruturas em fomato de árvore que permite estabelecer prioridades no acesso aos elementos armazenados
# As Chaves nos nós indicam a prioridade do item que está armazenado

# Fila de prioridade -> o item com menor chave é o primeiro a ser retirado/processado

# Binary Heap - baseado em árvores binárias

# root = 0
# left(i) = 2i + 1 | right(i) = 2i + 2 | parent(i) = floor((i-1) / 2)

# O valor de um filho nunca será menor que o valor de um pai

import math


class BinaryHeap:
    def __init__(self, i):
        self.heap = [i]
        self.n = 1

    def left(self, i):
        return (2 * i) + 1

    def right(self, i):
        return (2 * i) + 2

    def parent(self, i):
        return math.floor((i - 1) / 2)

    def addHeap(self, i):
        self.heap.append(i)
        self.n = self.n + 1
        self.bubble_up(self.n - 1)
        return True

    def removeHeap(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.n - 1]
        self.heap.pop()
        self.n = self.n - 1

        self.trickle_down(0)
        return x

    def bubble_up(self, i):
        p = self.parent(i)

        while i > 0 and self.heap[i] < self.heap[p]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[p]
            self.heap[p] = tmp

            i = p
            p = self.parent(i)

    def trickle_down(self, i):
        # A chave é comparado continuamente
        # com ambos os filhos; se ela for menor
        # entre os 3 valores, encerra
        while i >= 0:
            j = -1

            # Esse trecho basicamente descobre qual
            # o menor elemento entre i e seus filhos
            r = self.right(i)
            if r < self.n and self.heap[r] < self.heap[i]:
                l = self.left(i)
                if self.heap[l] < self.heap[r]:
                    j = l
                else:
                    j = r
            else:
                l = self.left(i)
                if l < self.n and self.heap[l] < self.heap[i]:
                    j = l
            # Flag j é testada para efetuar troca
            # com o menor dos valores ou para encerrar
            # o processo de reposicionamento
            if j >= 0:
                tmp = self.heap[j]
                self.heap[j] = self.heap[i]
                self.heap[i] = tmp

            i = j

# Tempo de AddHeap -> Ω(1) e O(log n)
# Tempo de RemoveHeap -> Θ(log n)


if __name__ == '__main__':
    bh = BinaryHeap(4)

    bh.addHeap(9)
    bh.addHeap(8)
    bh.addHeap(17)
    bh.addHeap(26)
    bh.addHeap(50)
    bh.addHeap(16)
    bh.addHeap(19)
    bh.addHeap(69)
    bh.addHeap(32)
    bh.addHeap(93)
    bh.addHeap(55)
    bh.addHeap(6)

    print(bh.removeHeap())

    print(bh.heap)
