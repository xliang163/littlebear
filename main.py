# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    print(f'Hello, {name}')


if __name__ == '__main__':
    #print_hi('world')
    print(list(range(11, 1, -2)))

    num_l = [1, 2, 3, 4, 5, 6]
    sum = 0

    for i in range(0, 6, 1):
        sum = sum + num_l[i]
        print(num_l[i])
        if sum == 6:
            break
    average = sum/len(num_l)
    print(average)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
