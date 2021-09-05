def read_a_file():
    try:
        input_file = open("Query-1_inp.txt", "r")
        li = []
        inp = input_file.read().split("\n")
        for x in inp:
            y = x.split(' ')
            for z in y:
                li.append(z)
        li = list(set(li))
        li.sort(key=len)
        input_file.close()
        output_file = open("Query-1_out.txt", "w")
        for i in li:
            output_file.write(i + " ")
            output_file.write(str(len(i)) + "\n")
        output_file.close()
    except():
        print("An Error Occurred")


if __name__ == '__main__':
    read_a_file()