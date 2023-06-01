# File-Manipulation-

##Extract-Text-From-PNG
-> if in a .docx change file to .zip (just rename it) 
-> copy out all the jpgs
-> use "https://github.com/tesseract-ocr/tesseract#installing-tesseract"
Install 
 sudo apt install sudo apt install tesseract-ocr

simple command
tesseract image_file output_file

for loop
```for i in $(ls) do; tesseract $i $i.txt; done```


# Unlocking-PDFs

Set Passowrd Variable
note "The characters <, >, |, &, and ^ are special command shell characters, and they must be preceded by the escape character (^)"
``` 
 set PASSWORD='<password>' 
 echo %PASSWORD%
```

For Loop For Mulitple Files 
```
for /r %f in (SEC*ook*.pdf) do "C:\Program Files\qpdf 11.3.0\bin\qpdf.exe" --password=%PASSWORD% -decrypt "%f" "%~dpnf_unlocked.pdf
```
