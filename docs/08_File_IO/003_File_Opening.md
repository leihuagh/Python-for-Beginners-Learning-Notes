# File Opening

## Open Function

### Syntax

- You can open file using Python's built-in `open()` function

```python
file_object = open(file_name, [access_mode])
```

### Parameter  Details

- `file_name`: The `file_name` argument is a string value that contains the name of the file that you want to access
- `access_mode`: The `access_mode` determines the mode in which the file has to be opened, i.e., 
  - read
  - write
  - append

### Open Function - Access Mode

- r: This is default mode. Opens a file for reading only
- rb: Opens a file reading only in binary format
- r+: Opens a file for both reading and writing
- rb+: Opens a file for both reading and writing in binary format
- w: Opens a file for writing only.  
  - Overwrites the file if the file exsits.  
  - Creates a new file for writing if the file doesn't exist
- wb: Opens a file for writing only in binary format
  - Overwrites the file if the file exists
  - Create a new file for writing if the file doesn't exist.