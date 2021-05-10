def read_text_file(filename):
    records = []
    infile = open(filename, 'r')
    for line in infile:
        records.append(line.strip())
    infile.close()
    print('<<', filename)
    return records

def read_binary_file(filename):
    records = []
    infile = open(filename, 'rb')
    record = infile.read(32).decode('ascii')
    while record:
        records.append(record.strip())
        record = infile.read(32).decode('ascii')
    infile.close()
    print('<<', filename)
    return records

def write_text_file(records, filename):
    outfile = open(filename, 'w')
    for record in records:
        outfile.write('%s\n' % record)
    outfile.close()
    print('>>', filename)

def write_binary_file(records, filename):
    outfile = open(filename, 'wb')
    for record in records:
        outfile.write(bytes(record.ljust(32), 'ascii'))
    outfile.close()
    print('>>', filename)
