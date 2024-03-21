# File Processor README

## Overview

The File Processor project is a practical coding challenge for back-end development. The goal of this task is to design and develop a program that reads data from multiple files located in a particular folder, processes the data, and generates an output CSV file with specific details. The output CSV file should contain a footer with details of the 2nd highest salary and the average salary.

## Features

- Reads data from multiple input files in a specified folder.
- Processes the data and generates a CSV output file with the required details.
- Includes a footer in the output CSV file with the 2nd highest salary and average salary.
- Handles errors gracefully and provides informative error messages.

## Requirements

- Python 3.x
- Libraries: `csv`, `os`

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/s-killer/-File-Processor-Assignment
   ```

2. Navigate to the project directory:

   ```bash
   cd file-processor
   ```

3. Ensure you have Python 3.x installed on your machine.

## Usage

1. Place input data files in the project directory.
2. Run the `file_processor.py` script to process the files and generate output:

   ```bash
   python file_processor.py
   ```

3. The generated output file will be saved in the `output_files/` directory.

## File Structure

- `input_files/`: Directory containing input data files.
- `output_files/`: Directory for storing generated output files.
- `expected_output/`: Directory containing the expected result CSV file.
- `file_processor.py`: Main script for processing files and generating output.
- `.gitignore`: Specifies files and directories to ignore in version control.
- `README.md`: Documentation providing an overview of the project, setup instructions, usage guidelines, etc.

## Example Output

An example output CSV file (`expected_output/expected_result.csv`) is provided to demonstrate the expected format and content of the output file.

## Author

Keval Thakkar

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

The project structure and README template were inspired by various open-source projects and best practices in software development.
