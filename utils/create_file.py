def create_file(content, filename):
    file = open(filename, "w")
    file.write(content)
    file.close()
