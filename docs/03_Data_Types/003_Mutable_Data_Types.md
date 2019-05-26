# Mutable Data Types

- Lists
- Dictionaries
- Sets

## Lists

- List is an ordered set of elements enclosed within square brackets.

### Main Differences between Lists and Tumples

- Lists are enclosed in brackets[]while tuples are enclosed within parenthesis()
- Lists are Mutable and tuples are immutable
- Tuples are faster than lists

```python
A = [1, 2, 3.15, 'Education']
print(A)
```

## Dictionaries

### Definitions

- Dictionaries contain key value pairs
- Each key is separated from its value by a colon `(:)`
- The items are separated by comma
- The whole thing is enclosed within curly braces

### Example

- keys: 'Age', 'Name'
- values: 24, 'John'

```python
A = {'Age': 24, 'Name': 'John'}

print(A)
```

## Sets

### Definitions

- A set is an unordered collection of items
- Every element is unique
- A set is created by placing all the items (elements) inside curly braces `{}`, separated by comma

### Example

```python
A = {1, 2, 3, 3}

print(A)
```

Output:

```shell
{1, 2, 3}
```
