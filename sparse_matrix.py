#!/usr/bin/python3
"""Script that reads a sparse matrix and performs operations on it"""

import os

class SparseMatrix:
    def __init__(self, filepath=None):
        self.numrows = 0
        self.numcols = 0
        self.matrix = {}
        self.filepath = filepath

        if self.filepath:
            self.read_matrix()

    def read_matrix(self):
        """Reads a sparse matrix from the file and loads it into memory."""
        try:
            with open(self.filepath, 'r') as f:
                lines = f.readlines()
                first_line = lines[0].strip().split('=')
                second_line = lines[1].strip().split('=')

                if len(first_line) != 2 or len(second_line) != 2:
                    raise ValueError("Input file has wrong format")

                self.numrows = int(first_line[1])
                self.numcols = int(second_line[1])
                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Input file has wrong format")
                    row, col, value = line[1:-1].split(',')
                    row, col, value = int(row), int(col), float(value)
                    if value != 0:
                        self.matrix[(row, col)] = value

            print(f"Matrix loaded with dimensions {self.numrows}x{self.numcols}.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except FileNotFoundError:
            print(f"Error: The file '{self.filepath}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        savedir = os.path.join(os.getcwd(), 'sample_results')
        if not os.path.exists(savedir):
            try:
                os.makedirs(savedir)
                print(f"Directory '{savedir}' created.")
            except Exception as e:
                print(f"Error creating directory '{savedir}': {e}")
                exit()

        save = os.path.basename(self.filepath) + "_results.txt"
        save_file = os.path.join(savedir, save)

        with open(save_file, "w") as f2:
            f2.write(f"numrows={self.numrows}\n")
            f2.write(f"numcols={self.numcols}\n")
            for key, value in self.matrix.items():
                f2.write(f"({key[0]},{key[1]},{value})\n")

    def add(self, other):
        """Add another sparse matrix to this one."""
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result_matrix = SparseMatrix()
        result_matrix.numrows = self.numrows
        result_matrix.numcols = self.numcols

        for key, value in self.matrix.items():
            result_matrix.matrix[key] = value

        for key, value in other.matrix.items():
            if key in result_matrix.matrix:
                result_matrix.matrix[key] += value
            else:
                result_matrix.matrix[key] = value

        return result_matrix

    def subtract(self, other):
        """Subtract another sparse matrix from this one."""
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        result_matrix = SparseMatrix()
        result_matrix.numrows = self.numrows
        result_matrix.numcols = self.numcols

        for key, value in self.matrix.items():
            result_matrix.matrix[key] = value

        for key, value in other.matrix.items():
            if key in result_matrix.matrix:
                result_matrix.matrix[key] -= value
            else:
                result_matrix.matrix[key] = -value

        return result_matrix

    def multiply(self, other):
        """Multiply this sparse matrix by another."""
        if self.numcols != other.numrows:
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix for multiplication.")
        
        result_matrix = SparseMatrix()
        result_matrix.numrows = self.numrows
        result_matrix.numcols = other.numcols

        for (i, j), value in self.matrix.items():
            for (k, l), other_value in other.matrix.items():
                if j == k:
                    if (i, l) in result_matrix.matrix:
                        result_matrix.matrix[(i, l)] += value * other_value
                    else:
                        result_matrix.matrix[(i, l)] = value * other_value

    def print_matrix(self):
        """Prints the sparse matrix."""
        print(f"Sparse Matrix: {self.numrows}x{self.numcols}")
        for key, value in self.matrix.items():
            print(f"({key[0]}, {key[1]}, {value})")

if __name__ == "__main__":
    input_dir = os.path.join(os.getcwd(), "sample_inputs")
    filename = input("Please enter the filename (with extension): ")
    filepath = os.path.join(input_dir, filename)

    if not os.path.isfile(filepath):
        print(f"File '{filename}' doesn't exist in '{input_dir}'. Exiting.")
        exit()

    matrix1 = SparseMatrix(filepath)

    while True:
        print("\nSelect an operation to perform:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '4':
            print("Exiting the program.")
            break

        second_filename = input("Please enter the second filename (with extension) for the second matrix: ")
        second_filepath = os.path.join(input_dir, second_filename)

        if not os.path.isfile(second_filepath):
            print(f"File '{second_filename}' doesn't exist in '{input_dir}'. Exiting.")
            exit()

        matrix2 = SparseMatrix(second_filepath)

        if choice == '1':
            result = matrix1.add(matrix2)
            print("the outcome is:")
            result.print_matrix()
        elif choice == '2':
            result = matrix1.subtract(matrix2)
            print("the outcome is:")
            result.print_matrix()
        elif choice == '3':
            print("the outcome is:")
            result = matrix1.multiply(matrix2)
            result.print_matrix()
        else:
            print("Invalid choice. Please enter a valid option.")
