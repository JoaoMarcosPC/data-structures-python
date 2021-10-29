# Entrada: array com elementos em qualquer ordem
# Saida: array com elementos ordenados de forma crescente

from heap import BinaryHeap


def heap_sort(a):
    hp = BinaryHeap(a[0])

    for i in range(1, len(a)):
        hp.addHeap(a[i])

    while hp.n > 1:
        tmp = hp.heap[0]
        hp.heap[0] = hp.heap[hp.n - 1]
        hp.heap[hp.n - 1] = tmp

        hp.n = hp.n - 1

        hp.trickle_down(0)

    hp.heap.reverse()
    return hp.heap

# Tempo -> O(n log n)


if __name__ == '__main__':

    a = [4, 9, 8, 17, 26, 50, 16, 19, 69, 32, 93, 55, 6]

    sorted_a = heap_sort(a)

    print(sorted_a)
