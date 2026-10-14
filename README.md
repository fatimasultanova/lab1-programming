In the imperative solution, I wrote step-by-step instructions using traditional for loops and if statements. I had to manually manage state, check each condition, and update list variables myself.

In contrast, the functional solution used built-in functions like filter(), map(), and reduce() to transform the data as a clean pipeline. Instead of writing loops, I simply told Python what to extract or transform using lambda expressions.

Overall, the imperative approach felt very direct and easy to debug line by line, but it required more boiler-plate code. The functional approach was significantly shorter, cleaner, and avoided changing data directly, making it better for reusable code.

- Detailed explanation

The main objective is to demonstrate how to handle the same dataset using different programming paradigms: imperative programming, functional programming, and higher-order functions.

Task 1: Imperative Style

What was done:
Traditional loops and conditional statements were used to validate raw student scores, extract passing students, and count performance categories.

Why it was used:
The imperative style provides clear, step-by-step control flow over the data.

How it works:
- A "for" loop iterates through each student dictionary in the list.
- An "if" condition checks if the score falls outside the valid 0-100 range and uses "continue" to skip invalid data (like the 120 score entry).
- Subsequent conditions check if the student passed (score >= 51) and append their name to a "passed_students" list.
- Other conditions increment the respective count inside a "categories" dictionary based on the score range.

Task 2: Functional Style

What was done:
Built-in Python functions—specifically "filter", "map", and "reduce" - were used to process the student data in a declarative.

Why it was used:
Functional programming helps avoid side effects and mutable state. By treating operations as data pipelines, the code becomes more concise and focuses heavily on what transformation to perform rather than how to loop through elements manually.

How it works:
- "filter()": Combined with a "lambda" function, it extracts only the valid student records where scores are between 51 and 100.
- "map()": Transforms the filtered student dictionaries into formatted text strings showing "Name: Score".
- "reduce()": Imports from the "functools" module to accumulate and sum up all passing scores, which are then divided by the total count to compute the final average score safely.

Task 3: Higher-Order Functions and Callbacks

What was done:
A custom higher-order function was created to accept callback functions, enabling safe and reusable data modifications without altering the original dataset.

Why it was used:
In software development, maintaining data immutability prevents unintended bugs caused by shared state mutations. Higher-order functions allow developers to pass logic (like custom bonus calculation or scaling rules) as arguments, making the codebase highly flexible and modular.

How it works:
- "copy.deepcopy()": Creates a fully independent recursive clone of the original student list, ensuring the source data remains entirely untouched.
- "apply_to_scores()": Acts as a higher-order function that takes the copied list and a callback function, iterates through the elements, and applies the callback to every score.
- Callbacks: A regular function ("add_bonus") adds 5 points while capping the maximum at 100 using "min()", and a "lambda" function scales down scores into a 0-10 format.