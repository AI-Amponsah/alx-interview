# 0x07-rotate_2d_matrix

This project is the eighth of many to test readiness for technical interviews.

## File Descriptions
### Mandatory
1. [0-rotate_2d_matrix.py](./0-rotate_2d_matrix.py) - a script that given an `n` x `n` 2D matrix, rotates it 90 degrees clockwise
   - Prototype: `def rotate_2d_matrix(matrix):`
   - The matrix must be edited in-place.
   - Assume the matrix will have 2 dimensions and will not be empty.

   **Execution Example**
   ```
   Niyi@ubuntu$ cat main_0.py
   #!/usr/bin/python3
   """
   Test 0x07 - Rotate 2D Matrix
   """
   rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

   if __name__ == "__main__":
       matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

    Niyi@ubuntu$
    Niyi@ubuntu$ ./main_0.py
    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]
    Niyi@ubuntu$
   ```


