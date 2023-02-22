def main():
    try:
        configuration = open('config.txt')
    except (FileNotFoundError, IsADirectoryError):
        print("Couldn't find the config.txt file!")

main()