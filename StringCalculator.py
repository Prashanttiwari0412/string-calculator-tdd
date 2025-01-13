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
        
        # Convert the input numbers to a list of integers.
        nums = [int(num) for num in numbers.split(",") if num]
        
        # Identify all negative numbers in the list.
        negatives = [num for num in nums if num < 0]
        
        # If there are negative numbers, raise an exception with their list.
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
            
        # Return the sum of all valid numbers.
        return sum(nums)
