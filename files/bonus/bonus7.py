filenames = ["1.doc.txt","2.report.txt","3.presentation.txt"]

filenames = [filename.replace('.','-') for filename in filenames]
print(filenames)