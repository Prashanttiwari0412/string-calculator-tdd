# String Calculator - TDD Kata Approach

This repository contains a solution for the **String Calculator** problem, implemented using **Test-Driven Development (TDD)** principles. The solution evolves step-by-step, with each feature being developed incrementally and backed by corresponding test cases.

### Features Implemented:
1. **Handling Empty String**: The `add` method returns 0 when the input is an empty string.
2. **Single and Multiple Numbers**: The `add` method handles both single and multiple comma-separated numbers.
3. **New Line as a Delimiter**: The `add` method can process numbers separated by new lines (`\n`), in addition to commas.
4. **Custom Delimiters**: The `add` method supports user-defined delimiters provided at the start of the input.
5. **Negative Numbers Handling**: The method raises a `ValueError` if negative numbers are encountered, with a detailed message listing all negative numbers.

### TDD Process:
- **Test-Driven Development (TDD)** was followed throughout the development process. The code was written incrementally, with tests created before implementation to ensure the correctness of each feature.
- Each commit in the repository represents a step in the development process, showcasing how the solution evolved.

### Usage:
1. Clone the repository.
2. Run the tests using `unittest` to verify the functionality:
   ```bash
   python -m unittest discover
   ```

### Commit History:
- The commits show the evolution of the code, starting from the first failing test to the final implementation. Each commit is accompanied by a meaningful message reflecting the step taken.
