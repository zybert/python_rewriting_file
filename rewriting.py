def rewriting_file(source_file, target_file):
    with open(source_file, 'r') as source_file:
        with open(target_file, 'r+') as target_file:
            for line in source_file:
                if line != "\n":
                    target_file.write(line)


rewriting_file('fileOne.txt', 'fileTwo.txt')
