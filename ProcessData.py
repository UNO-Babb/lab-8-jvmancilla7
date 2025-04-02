#ProcessData.py
#Name: Juan V Mancilla Vargas
#Date:4/2/2025
#Assignment: Student List

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:

    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data [6]
    year = data [5]

    student_id = makeID(first, last, idNum)
    major =  major.replace(" ", " ")
    major_abbr = ""
    for i in range (3):
      if i < len(major):
        major_abbr = major_abbr + major[i]

    year_abbr = ""

    if year == "Freshman":
      year_abbr = "FR"
    elif year == "Sophomore":
      year_abbr = "SO"
    elif year == "Junior":
      year_abbr = "Jr"
    elif year == "Senior":
      year_abbr = "SR"
    else:
      year_abbr = "NONE"

    major_year = major + "-" + year_abbr

    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)
   


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()
  
def makeID(first, last, idNum):
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "x"

  id = first[0] + last + idNum[idLen- 3: ]

  return id
if __name__ == '__main__':
  main()
