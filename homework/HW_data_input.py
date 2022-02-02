import numpy as np
import csv

with open('HW_data') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=' ')
  for row in csv_reader:
    if len(row) > 0:
      x = [float(item) for item in row]
