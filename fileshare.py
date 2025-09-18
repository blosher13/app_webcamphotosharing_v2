import Client

class FileShare:
    def __init__(self, filepath, api_key = 'AViVqqp7sumSQWWEdrl6hf9z') -> None:
        self.filepath = filepath
        self.api_key = api_key
    
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath = self.filepath)
        return new_filelink