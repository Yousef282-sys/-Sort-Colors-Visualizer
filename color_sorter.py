class ColorSorter:
    def sort(self, n, inputs_list):
        """
        Adapted from the original read_and_sort to work with an API.
        Accepts n (int) and inputs_list (list of strings/ints).
        """
        try:
            # Check count
            # In your original code: if len(inputs) != n: print("sorry")
            if len(inputs_list) != n:
                return "sorry"

            arr = []

            # Validate and convert
            for value in inputs_list:
                try:
                    num = int(value)
                except ValueError:
                    return "sorry"
                
                if num not in (0, 1, 2):
                    return "sorry"
                arr.append(num)

            # Bubble Sort (As requested)
            # This is O(n^2), effectively sorting the array in place
            for i in range(len(arr) - 1):
                for j in range(len(arr) - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # Output
            return " ".join(map(str, arr))

        except Exception as ex:
            return f"Message: {ex}"