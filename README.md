# Sparse Matrix Operations

This Python program reads a sparse matrix from a file and allows users to perform basic matrix operations such as addition, subtraction, and multiplication on two sparse matrices. The matrices are stored efficiently in a dictionary (using dictionary of keys format) to handle the sparsity, avoiding storing zero values.

## Features
- **Addition**: Add two matrices of the same dimensions.
- **Subtraction**: Subtract one matrix from another, provided they have the same dimensions.
- **Multiplication**: Multiply two matrices if the number of columns in the first matrix matches the number of rows in the second matrix.
- The program ensures proper validation of matrix dimensions before performing operations.

## File Structure

```
.
├── sample_inputs/                # Directory for input files
│   ├── easy_sample_01_2.txt      # Example sparse matrix input
│   └── easy_sample_01_3.txt      # Another example sparse matrix input
├── sample_results/               # Directory where results are saved
├── sparse_matrix.py              # Main program file
└── README.md                     # This file
```

## How to Use the Program

### Input File Format
The input files should follow a specific format to represent the sparse matrix. The first two lines of the file specify the number of rows and columns, and the subsequent lines provide the non-zero entries of the matrix in the format `(row, column, value)`.

Example input file (`easy_sample_01_2.txt`):
```
numrows=3
numcols=3
(0,1,5.0)
(2,2,3.0)
```

### Running the Program
1. Ensure that the input files are placed in a directory named `sample_inputs` in the same folder as the script.
2. Run the program using Python 3:
   ```bash
   python3 sparse_matrix.py
   ```

3. The program will prompt you to enter the filename of the first matrix (which should be in `sample_inputs`), then it will load the matrix and display its dimensions.

4. Next, it will ask you to choose an operation:
   - **1**: Addition
   - **2**: Subtraction
   - **3**: Multiplication
   - **4**: Exit

5. If you choose any of the operations (1, 2, or 3), the program will prompt you to enter the filename of a second matrix. The second matrix file should also be in the `sample_inputs` directory.

6. Once both matrices are loaded, the selected operation is performed, and the result is displayed. The program also saves the result in the `sample_results` directory as a new text file.

### Output File Format
After performing the operations, the result is saved in the `sample_results` directory. The result file format is similar to the input file, with non-zero elements being saved.

### Example Workflow
```bash
Please enter the filename (with extension): easy_sample_01_2.txt
File 'easy_sample_01_2.txt' is found in sample_inputs.
Matrix loaded with dimensions 3x3.

Select an operation to perform:
1: Addition
2: Subtraction
3: Multiplication
4: Exit
Enter your choice (1/2/3/4): 1
Please enter the second filename (with extension) for the second matrix: easy_sample_01_3.txt
File 'easy_sample_01_3.txt' is found in sample_inputs.
Matrix loaded with dimensions 3x3.

Resultant matrix after addition:
{(0, 1): 5.0, (2, 2): 3.0, (0, 2): 4.0}
```

The result will be saved as `easy_sample_01_2_results.txt` inside the `sample_results` directory.

## Notes
- Ensure that the matrices you want to add or subtract have the same dimensions (number of rows and columns).
- Ensure that the number of columns in the first matrix matches the number of rows in the second matrix for matrix multiplication.
- The program handles sparse matrices by storing only non-zero elements.
