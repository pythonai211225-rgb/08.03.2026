# Homework – Lucky Numbers

Write the following Python functions

## Function 1

Create a function:

```python
def get_lucky_numbers(amount: int) -> tuple[int]:
    pass
```

Mission:

* Generate a **tuple of random numbers**
* The tuple should contain **amount numbers**
* Each number must be between **1 and 100**

Example

```python
get_lucky_numbers(3)
```

Possible output

```python
(17, 83, 4)
```

## Function 2

Create a function:

```python
def input_until_lucky(lucky_numbers: tuple) -> int:
    pass
```

Mission:

* The function receives the **tuple of lucky numbers**.
* Ask the user to **input numbers**.
* Continue asking until the user guesses **one of the lucky numbers**.
* When the user guesses correctly, **stop the loop**.
* Return the **number of attempts** the user needed.

Example

Lucky numbers

```python
(17, 83, 4)
```

User inputs

```
10
25
83
```

Output

```
3
```

## 🚀 Bonus (Optional)

Add **try / except**:

* If the user enters an **invalid value** (not a number), ask again
* The program should **not crash**
* Only valid numeric inputs should count as attempts

**Submission email:** [pythonai211225+python16tup@gmail.com](mailto:pythonai211225+python16tup@gmail.com)


