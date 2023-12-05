class Task1:

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file.readlines()]
        return data

    @staticmethod
    def get_int_chars(s):
        return ''.join(c for c in s if c.isdigit())

    @staticmethod
    def get_first_and_last(s):
        return s[0] + s[-1]

    @staticmethod
    def filter_strings_starting_with_prefix(strings, prefix):
        return [s for s in strings if s.startswith(prefix)]

    @staticmethod
    def get_first_int(s):
        number_dict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        i = 0
        while i < len(s):
            if s[i].isalpha():
                for key in number_dict.keys():
                    if s[i:].startswith(key):
                        return int(number_dict[key])
                else:
                    i += 1
            else:
                return int(s[i])

        return None

    @staticmethod
    def get_int(s):
        number_dict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        first_int = None
        last_int = None

        i = len(s) - 1
        while (i >= 0 and last_int is None):
            if s[i].isalpha():
                for key in number_dict.keys():
                    if s[:i + 1].endswith(key):
                        last_int = int(number_dict[key])
                        break
                else:
                    i -= 1
            else:
                last_int = int(s[i])
                break

        i = 0
        while (i < len(s) and first_int is None):
            if s[i].isalpha():
                for key in number_dict.keys():
                    if s[i:].startswith(key):
                        first_int = int(number_dict[key])
                        break
                else:
                    i += 1
            else:
                first_int = int(s[i])

        return int(str(first_int) + str(last_int))

    class Day1:

        def execute(self):
            print("Day 1")
            data = Task.read_file('day1.txt')
            print(data)
            processed_data = list(map(Task.get_int_chars, data))
            print(processed_data)
            next_data = list(map(Task.get_first_and_last, processed_data))
            print(next_data)
            sum_of_ints = sum(int(i) for i in next_data if i.isdigit())
            print(sum_of_ints)

    class Day1a:

        def execute(self):
            print("Day 1a")
            data = Task.read_file('day1.txt')
            print(data)
            numbers_data = list(map(Task.get_int, data))
            print(numbers_data)
            sum_of_ints = sum(int(i) for i in numbers_data)
            print(sum_of_ints)


