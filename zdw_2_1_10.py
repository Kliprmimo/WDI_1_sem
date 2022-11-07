import random


def subsequence(num, high, low):
    rand_list = []
    longest_list = []

    for x in range(0, num):
        rand_list.append(random.randint(low, high))

    for dif in range(-high, high + 1):
        temp_list = []
        for numb in range(0, (num - 1)):

            if rand_list[numb] == (rand_list[numb + 1] + dif):
                if not temp_list:
                    temp_list.append(rand_list[numb])
                temp_list.append(rand_list[numb + 1])
            else:
                if len(temp_list) >= len(longest_list):
                    longest_list = temp_list
                temp_list = []

    return rand_list, longest_list, sum(longest_list)


a, b, c = subsequence(20, 10, 0)
print(f'dla losowej listy {a} najdłóższym spójnym podciągiem jest {b}, i jego suma wynosi: {c}')
