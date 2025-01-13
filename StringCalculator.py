#**************The method add is implemented to handle a basic case where the input is either an empty string or a string containing up to two comma-separated numbers**************
# The method add is updated to handle custom delimiters specified in the format //[delimiter]\n[numbers].

# Define the StringCalculator class to implement the `add` method that already support multiple numbers and empty string.
class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        # Return 0 if the input string is empty.
        if not numbers:
            return 0
            
        # The method add is updated to handle custom delimiters specified in the format //[delimiter]\n[numbers].
        if numbers.startswith("//"):
            # Extract the custom delimiter and the remaining numbers.
            delimiter, numbers = numbers[2:].split("\n", 1)
            # Replace the custom delimiter with commas for processing.
            numbers = numbers.replace(delimiter, ",")
            
        # Replace new lines with commas to unify delimiters.
        numbers = numbers.replace("\n", ",")
        
        # Split the string by comma, convert to integers, and return their sum.
        return sum(int(num) for num in numbers.split(",") if num)
