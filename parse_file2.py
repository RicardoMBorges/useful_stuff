import csv

# writen by Ricardo M Borges 03-22-2023

# input_file_path = 'GNPS-COLLECTIONS-PESTICIDES-POSITIVE.mgf'
# output_file_path = 'outfile.csv'
# info_to_parse = ['MSLEVEL', 'SOURCE_INSTRUMENT', 'FILENAME', 'IONMODE', 'ORGANISM', 'NAME', 'PI', 'DATACOLLECTOR', 'SMILES', 'INCHI', 'INCHIAUX', 'PUBMED', 'SUBMITUSER', 'LIBRARYQUALITY', 'SCANS']
# parse_file2(input_file_path, output_file_path, info_to_parse)


def parse_file2(input_file_path, output_file_path, info_to_parse):
    # Define the keys to extract from each block of data
    keys = []
    if 'MSLEVEL' in info_to_parse:
        keys.append('MSLEVEL')
    if 'SOURCE_INSTRUMENT' in info_to_parse:
        keys.append('SOURCE_INSTRUMENT')
    if 'FILENAME' in info_to_parse:
        keys.append('FILENAME')
    if 'IONMODE' in info_to_parse:
        keys.append('IONMODE')
    if 'ORGANISM' in info_to_parse:
        keys.append('ORGANISM')
    if 'NAME' in info_to_parse:
        keys.append('NAME')
    if 'PI' in info_to_parse:
        keys.append('PI')
    if 'DATACOLLECTOR' in info_to_parse:
        keys.append('DATACOLLECTOR')
    if 'SMILES' in info_to_parse:
        keys.append('SMILES')
    if 'INCHI' in info_to_parse:
        keys.append('INCHI')
    if 'INCHIAUX' in info_to_parse:
        keys.append('INCHIAUX')
    if 'PUBMED' in info_to_parse:
        keys.append('PUBMED')
    if 'SUBMITUSER' in info_to_parse:
        keys.append('SUBMITUSER')
    if 'LIBRARYQUALITY' in info_to_parse:
        keys.append('LIBRARYQUALITY')
    if 'SPECTRUMID' in info_to_parse:
        keys.append('SPECTRUMID')
    if 'SCANS' in info_to_parse:
        keys.append('SCANS')

    # Open the input and output files
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        # Create a CSV writer object
        csv_writer = csv.DictWriter(output_file, fieldnames=keys)
        csv_writer.writeheader()

        # Parse the input file and extract the required information
        block_data = {}
        in_block = False
        for line in input_file:
            if line.startswith('BEGIN IONS'):
                # Start of a new block
                in_block = True
                block_data = {}
            elif line.startswith('END IONS'):
                # End of the current block, write to CSV
                in_block = False
                csv_writer.writerow(block_data)
            elif in_block:
                # Extract information from the current block
                line = line.strip()
                if '=' in line:
                    key, value = line.split('=', 1)
                    if key in keys:
                        block_data[key] = value