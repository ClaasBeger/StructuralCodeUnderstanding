lines = Queue(1)
count = Queue(1)

def read(file):
    try:
        for line in file:
            lines.put(line)
    finally:
        lines.put(None)
    print(count.get())

def write(file):
    n = 0
    while 1:
        line = lines.get()
        if line is None:
            break
        file.write(line)
        n += 1
    count.put(n)

if __name__ == "__main__":
    input_file = io.StringIO("First line\nSecond line\nThird line\nFourth line\nFirst line\nSecond line\nThird line\nFourth line\nFirst line\nSecond line\nThird line\nFourth line\n")
    output_file = io.StringIO()
    reader = Thread(target=read, args=(input_file,))
    writer = Thread(target=write, args=(output_file,))
    reader.start() #START

    writer.start()
    reader.join()
    writer.join() #END

    print(output_file.getvalue())