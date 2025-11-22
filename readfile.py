import os





def get_urls_files(directory):
    urls = []
    name_files = []
    for root, dirs, files in os.walk(directory):
        if ".git" not in  root:
            for file in files:
                urls.append(os.path.join(root, file))
                name_files.append(file)
    return urls, name_files


class Read:
    def __init__(self, directory: str):
        """
        Read url file

        Args:
            directory (str): url file.
        """
        try:
            self.directory = directory
            self.urls, self.name_files = get_urls_files(directory)
            self.data_all = {}
        except Exception as e:
            print(f'Error: {e}')

