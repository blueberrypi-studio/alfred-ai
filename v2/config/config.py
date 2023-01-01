import configparser


class Config():
    # Method to read config file settings
    def read_config():
        config = configparser.ConfigParser()
        config.read('config/configurations.ini')
        return config

    def print_config():
        # PRINT FILE CONTENT
        read_file = open("config/configurations.ini", "r")
        content = read_file.read()
        print("Content of the config file are:\n")
        print(content)
        read_file.flush()
        read_file.close()