# Python Average Calculation Bug

This repository demonstrates a common error in Python when calculating the average of a list of numbers: the `ZeroDivisionError` that occurs when trying to divide by zero if the input list is empty.

## Bug
The original code lacks error handling for empty input lists.

## Solution
The solution adds a check for an empty input list and returns 0 in that case.