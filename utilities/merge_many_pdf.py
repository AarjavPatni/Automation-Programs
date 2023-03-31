import sys
import PyPDF4
from pathlib import Path

pdfs = sys.argv
 
# Call the PdfFileMerger
mergedObject = PyPDF4.PdfFileMerger()
disclaimer = """
\033[1mDISCLAIMER:\033[0m
1. Make sure all files to be merged, are named in the format (common_name)(number).
2. Appended number must start with 1.
3. All the files to be merged must be placed in the destination folder.
4. Desired name of the merged file must \033[1mNOT\033[0m include \".pdf\"
"""
print(disclaimer)

f_name = input("Enter the desired name of the merged file: ")

for fileNumber in pdfs:
    mergedObject.append(PyPDF4.PdfFileReader(str(Path().absolute()) + "\\" + com_name + "(" + str(fileNumber) + ")" + '.pdf', 'rb'))

mergedObject.write(f_name + ".pdf")
print("Voila!")