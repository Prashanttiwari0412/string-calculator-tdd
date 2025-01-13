# **************The method add is implemented to handle a basic case where the input is either an empty string or a string containing up to two comma-separated numbers**************

# Define the StringCalculator class to implement the `add` method that already support multiple numbers and empty string.
class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        # Return 0 if the input string is empty.
        if not numbers:
            return 0
        # Split the string by comma, convert to integers, and return their sum.
        return sum(int(num) for num in numbers.split(",") if num)
