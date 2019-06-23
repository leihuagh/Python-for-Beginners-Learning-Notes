# Membership Operator

## `in`

- Evaluates to TRUE if it finds a variable in the specified sequence and FALSE otherwise

## `not in`

- Evaluates to TRUE if it does not finds a variable in the specified sequence and FALSE otherwise

## Examples

```shell
python
list = (4, 5, 6)
print(list)
print(4 not in list)

A = [1, 2, 3, 15, 'Lei']
print('Lei' in A)
print('Lei' not in A)

B = {'Age':55, 'Name':'Lei', 'Jobs': [], 'cities': {}}
print(B['Age'])
print('Age' in B)
print('age' in B)
print(B['age'])
exit()
```
