from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here

    baseValue = type(elements)
    print(baseValue)

    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 2, 1]))