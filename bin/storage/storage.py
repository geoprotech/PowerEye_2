class Storage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Storage, cls).__new__(cls)
            cls._instance.data = {}  # Initialize an empty dictionary to store data
        return cls._instance

    def set_data(self, key, value):
        print(f"set_data {key=} {value=}")
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)
