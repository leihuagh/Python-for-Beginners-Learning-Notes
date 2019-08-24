# Command Line Parameters

- It is possible to pass arguments to Python programs when they are executed
- The brackets which follow main are used for this purpose
- `.argv` refers to the number of arguments passed, and `argv[]` is a pointer array which points to each argument which is passed to main
- The Python `sys` module provides access to any command-line arguments via the `sys.argv`. This serves two purposes:
  - `sys.argv` is the list of command-line arguments
  - len(sys.argv) is the number of command-line arguments