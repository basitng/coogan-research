import pickle
import os


class PickleData:
    def __init__(self, filename):
        self.filename = filename

    def store_pickle_data(self, data):
        pickle_filename = f'{self.filename}.pickle'
        with open(pickle_filename, 'wb') as file:
            pickle.dump(data, file)

        return {'status': 'completed'}

    def retrieve_data(self):
        pickle_filename = f'{self.filename}.pickle'
        if not os.path.exists(pickle_filename):
            print(f'Error: File "{pickle_filename}" does not exist.')
            return None

        try:
            with open(pickle_filename, 'rb') as file:
                retrieved_data = pickle.load(file)
                print(retrieved_data)
                return retrieved_data
        except pickle.UnpicklingError as e:
            print(
                f'Error: Failed to retrieve data from "{pickle_filename}". {str(e)}')
            return None
