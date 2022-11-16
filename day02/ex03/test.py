from csvreader import CsvReader

if __name__ == "__main__":

    with CsvReader('good.csv', sep=',', header=True, skip_top=1, skip_bottom=0) as file:
        if file == None:
           print("File is corrupted")
           exit(1)
        data = file.getdata()
        header = file.getheader()
        print(header)
        for line in data :
            print(line)

    print(' ------------------------------ \n')

    with CsvReader('bad.csv', sep=',', header=True, skip_top=1, skip_bottom=0) as file:
        if file == None:
           print("File is corrupted")
           exit(1)
        data = file.getdata()
        header = file.getheader()
        print(header)
        for line in data :
            print(line)
        