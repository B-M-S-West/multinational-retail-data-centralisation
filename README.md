# multinational-retail-data-centralisation

## Table of Contents
1. Project Description
2. Installation Instructions
3. Usage Instructions
4. File Structure
5. License Information

## Project Description
Project to make the sales data of a company more accessible from one centralised location. The first step is to produce a system to store the current company data in a database so that it is accessed from one centralised location and act as a single source for all sales data. The second part is to query the database to get up-to-date metrics for the business.

## Installation Instructions
To install and run this project:

1. Clone the repository or download the files.
2. Make sure you have a 'db_creds.yaml' and 'local_db_creds.yaml' file so that you can access the database
3. Ensure you have Python installed on your machine.
4. Run the script using a Python interpreter.

## Usage Instructions
To use the program:

1. Run the script.

## File Structure
The project has the following structure:

- `__main__.py`: This is the main Python script that you run to run through the program.
- 'data_cleaning.py': This is the Python script that performs the cleaning of the different data.
- 'data_extraction.py': This is the Python script that performs the extraction of the data from the different sources.
- 'database_utils.py': This is the Python script that connects to the database and uploads
- 'db_creds.yaml': This contains the details to access the original database
- 'local_db_creds.yaml': This contains the details to access the database on the local area 

## License Information
This project is licensed under the MIT License. See the LICENSE file for details.