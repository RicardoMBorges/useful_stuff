import csv

# writen by Ricardo M Borges 03-22-2023

def parse_file(input_file_path, output_file_path, info_to_parse):
    # Open the input and output files
    input_file = open(input_file_path, 'r')
    output_file = open(output_file_path, 'w', newline='')

    # Create a CSV writer object
    csv_writer = csv.writer(output_file)

    # Define the column names for the output CSV file
    csv_columns = ['Name', 'Peptide Mass']
    if 'other' in info_to_parse:
        csv_columns.append('Other Info')
    if 'smiles' in info_to_parse:
        csv_columns.append('SMILES')
    csv_writer.writerow(csv_columns)

    # Parse the input file and extract the required information
    block_data = []
    other_info = []  # Initialize other_info list
    smiles = ''  # Initialize smiles variable
    for line in input_file:
        if line.startswith('NAME='):
            # Store the previous block data
            if block_data:
                block_data.append(smiles)  # Add SMILES to the block data
                csv_writer.writerow(block_data)
                block_data = []
                other_info = []  # Reset other_info list for the next block
                smiles = ''  # Reset smiles variable for the next block
            # Extract the new block data
            name = line.strip().split('=', 1)[1]
        elif line.startswith('PEPMASS='):
            peptide_mass = line.strip().split('=', 1)[1]
        elif line.startswith('SMILES='):
            # Extract the SMILES information
            if 'smiles' in info_to_parse:
                smiles = line.strip().split('=', 1)[1]
        elif line.startswith('BEGIN IONS'):
            # Ignore the start of a new block
            continue
        elif line.startswith('END IONS'):
            # Store the current block data
            block_data.append(name)
            block_data.append(peptide_mass)
            if 'other' in info_to_parse:
                block_data.append(' '.join(other_info))
            if 'smiles' in info_to_parse:
                block_data.append(smiles)
            # Reset the variables for the next block
            name = ''
            peptide_mass = ''
            other_info = []  # Reset other_info list for the next block
        else:
            # Store any other information in the current block
            if 'other' in info_to_parse:
                other_info.append(line.strip())

    # Write the last block data
    if block_data:
        block_data.append(smiles)  # Add SMILES to the last block data
        csv_writer.writerow(block_data)

    # Close the input and output files
    input_file.close()
    output_file.close()