# Import libraries
import csv
import os
import json

# Console log print color
class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

def main():
# Path user prompt
    def PathPrompt():
        c1 = 0
        while c1 == 0:
            try:
                InPath = input(bcolors.HEADER + f'\nEnter directory path where file is located:\n' + bcolors.ENDC)
                os.chdir(InPath)#move to path
                print(bcolors.OKCYAN + '\nlocating path...')
            except FileNotFoundError:
                print(bcolors.OKCYAN + '\nlocating path...')
                print(bcolors.WARNING + "    Warning: Path not found. Please try again." + bcolors.ENDC)
            except:
                print(bcolors.OKCYAN + '\nlocating path...')
                print(bcolors.WARNING + "    Warning: Something went wrong. Please try again." + bcolors.ENDC)
            else:
                c1 = 1
                print(bcolors.OKCYAN + 'path found')
                print(bcolors.OKGREEN + 'You have selected: ' + bcolors.UNDERLINE + InPath + bcolors.ENDC)
        else: 
            pass

# File name user prompt
    def FilenamePrompt():
        global csvFile
        c2 = 0
        while c2 == 0:
            try:
                InFile = input(bcolors.HEADER + '''\nPlease enter CSV file name that you'd like to convert into JSON:\n''' + bcolors.ENDC)
                csvFile = csv.DictReader(open(f'{InFile}')) #open and convert CSV into dictionary 
                print(bcolors.OKCYAN + '\nlocating file...')
            except FileNotFoundError:
                print(bcolors.OKCYAN + '\nlocating file...')
                print(bcolors.WARNING + '''    Warning: File not found. Please try again.\n    (Don't forget extenstion ".csv")''' + bcolors.ENDC)
            except:
                print(bcolors.OKCYAN + '\nlocating file...')
                print(bcolors.WARNING + "    Warning: Something went wrong. Please try again." + bcolors.ENDC)
            else:
                c2 = 1
                print(bcolors.OKCYAN + 'file found: preparing file for conversion...')
                print(bcolors.OKGREEN + 'You have selected: ' + bcolors.UNDERLINE + InFile + bcolors.ENDC)
        else: 
            pass

# File converter CSV -> JSON
    def Transformer():
        # Clear file if it exists
        f = open("jsonFile.json", "w")
        f.write('')
        print(bcolors.OKCYAN + 'creating JSON file...')

        # Set file handling to function to "append" to allow string input
        f = open("jsonFile.json", "a")
        f.write('[') 
        print(bcolors.OKCYAN + 'writing JSON file...')

        # Write JSON file in a its correct structure
        for row in csvFile:
            f.write(json.dumps(row))
            f.write(',')
        print(bcolors.OKCYAN + 'converting CSV into JSON...')
        

        # Set file handling function to "read and write binary" to allow the use of seek() and truncate() 
        f = open('jsonFile.json', 'rb+') 
        f.seek(-1, 2) 
        f.truncate() #delete last comma

        # Set file handling function to "append" to allow string input
        f = open("jsonFile.json", "a")
        f.write(']')
        print(bcolors.OKBLUE + 'DONE' + bcolors.ENDC)

    PathPrompt()
    FilenamePrompt()
    Transformer()

main()