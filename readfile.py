import os





def get_urls_files(directory):
    urls = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            urls.append(os.path.join(root, file))
    return urls


class Read:
    def __init__(self, directory: str):
        """
        Read url file

        Args:
            directory (str): url file.
        """
        try:
            self.directory = directory
            self.urls = get_urls_files(directory)
            self.data_all = {}
        except Exception as e:
            print(f'Error: {e}')

