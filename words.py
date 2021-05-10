#!/usr/bin/env python3

from file_module import *

records = read_text_file('/usr/dict/words')
write_binary_file(records, 'words.bin')
records = read_binary_file('words.bin')
write_text_file(records, 'words.txt')
