import csv
import os
from collections import defaultdict

def process_files(input_folder, output_folder):
    """
    Process files in the input folder and generate a CSV file containing salary information in the output folder.
    
    Args:
        input_folder (str): Path to the folder containing input files.
        output_folder (str): Path to the folder where the output CSV file will be generated.
    """
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        salaries = defaultdict(list)

        # Iterate through input files
        print("Processing input files...")
        for filename in os.listdir(input_folder):
            if filename.endswith(".dat"):
                file_path = os.path.join(input_folder, filename)
                print("Processing:", file_path)
                with open(file_path, 'r') as file:
                    for line in file:
                        line = line.replace(";", " ")
                        parts = line.strip().split()

                        if len(parts) >= 8:
                            id_num = parts[0]
                            first_name = parts[1]
                            last_name = parts[2]

                            email = parts[3]
                            if "@" not in parts[3]:
                                last_name += " " + email
                                email = parts[4]
                            else:
                                job_title = ' '.join(parts[4:-2])

                            basic_salary = float(parts[-2])
                            allowances = float(parts[-1])
                            gross_salary = basic_salary + allowances
                            salaries[id_num].append({'ID': id_num, 'First Name': first_name, 'Last Name': last_name,
                                                    'Email': email, 'Job Title': job_title, 'Basic Salary': basic_salary,
                                                    'Allowances': allowances, 'Gross Salary': gross_salary})

        # Merge salary data from all files
        all_salaries = [salary for sublist in salaries.values() for salary in sublist]

        # Sort by gross salary
        sorted_salaries = sorted(all_salaries, key=lambda x: x['Gross Salary'], reverse=True)

        # Calculate second highest gross salary and average gross salary
        second_highest_salary = sorted_salaries[1]['Gross Salary'] if len(sorted_salaries) > 1 else 0
        total_gross_salary = sum(salary['Gross Salary'] for salary in sorted_salaries)
        average_salary = total_gross_salary / len(sorted_salaries) if sorted_salaries else 0

        # Write data to CSV file
        output_file = os.path.join(output_folder, "output.csv")
        print("Writing to CSV file...")
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['ID', 'First Name', 'Last Name', 'Email', 'Job Title', 'Basic Salary', 'Allowances', 'Gross Salary']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for salary_info in sorted_salaries:
                writer.writerow(salary_info)

            writer.writerow({})  # Empty row
            writer.writerow({'ID': 'Second Highest Salary:', 'First Name': second_highest_salary})
            writer.writerow({'ID': 'Average Salary:', 'First Name': average_salary})
        print("Output CSV file has been generated successfully.")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    try:
        current_directory = os.getcwd()
        output_folder = os.path.join(current_directory, "output_files")
        input_folder = current_directory
        print("Current Directory:", current_directory)
        print("Output Folder:", output_folder)
        process_files(input_folder, output_folder)
        print("Processing completed successfully.")
    except Exception as e:
        print("An error occurred:", str(e))
