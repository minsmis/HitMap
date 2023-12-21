import os

import mat73
import seaborn as sns


def make_toydata():
    # This function is for import toy datasets from seaborn flights.

    flights = sns.load_dataset('flights')
    toy_data = flights.pivot(index='month', columns='year', values='passengers')
    return toy_data


def get_file_extension(path):
    # Get file extension
    split_extension = os.path.splitext(path)

    # Extract only extension type
    extension = split_extension[-1][1:]
    return extension


def import_data(data_path, import_variables):
    # This import data from matlab data file.
    # 'data_path' [str]: Path for data.
    # 'import_variables' [list]: Variables in the data to import.

    # Output
    data = {}

    # Get file extension
    extension = get_file_extension(data_path)

    # For matlab data
    if extension == 'mat':
        # Load .mat data
        mat_data = mat73.loadmat(data_path)

        # Get variables to import
        for variable in import_variables:
            data[variable] = mat_data[variable]
    return data
