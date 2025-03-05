from typing import List


class ListExercise:
    @staticmethod
    def replace(input_list: List[int]) -> List[int]:
        if not input_list:
            return input_list

        # Function to search max of list
        def find_max(input_list: List[int], index: int = 0, current_max: int = None) -> int:
            if index == len(input_list):  # When list is at the end
                return current_max
            else:
                # If element is larger
                new_max = (
                    max(current_max, input_list[index])
                    if current_max is not None
                    else input_list[index]
                )
                return find_max(input_list, index + 1, new_max)

        max_value = find_max(input_list)

        # Replace all positive numbers with max value
        return [max_value if x > 0 else x for x in input_list]

    @staticmethod
    def search(input_list: List[int], query: int) -> int:
        def binary_search(input_list: List[int], left: int, right: int, query: int) -> int:
            if left > right:
                return -1  # If the element is not found

            mid = (left + right) // 2  # Find the middle of the list

            if input_list[mid] == query:
                return mid  # If the element is found, return the index
            elif input_list[mid] < query:
                return binary_search(
                    input_list, mid + 1, right, query
                )  # Searching in the right part
            else:
                return binary_search(input_list, left, mid - 1, query)  # Searching in the left part

        return binary_search(input_list, 0, len(input_list) - 1, query)
