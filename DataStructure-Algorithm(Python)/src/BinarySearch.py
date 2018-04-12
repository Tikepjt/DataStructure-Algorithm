# Python3

def binary_search(list, item):
    # 배열 전체길이 설정

    low = 0
    high = len(list) - 1

    # 가운데 있는 원소를 확인

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        # 아이템을 찾음

        if guess == item:
            return mid

        # 추측한 숫자가 너무큼

        if guess > item:
            high = mid - 1

        # 추측한 숫자가 너무작음

        else:
            low = mid + 1

    # 아이템이 리스트에 없음
    return None


# 확인할 리스트

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None
