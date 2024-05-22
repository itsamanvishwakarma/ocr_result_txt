## how to use the surya-ocr package & get the text from the results.json file to a text file

All you need to do is to install the surya package using pip:

```
pip install surya-ocr
```

and then use the following command to run the OCR on the image and the results will be saved in the results/surya/{filename}/results.json:

```
surya_ocr samplefile.pdf --langs hi,en
```

where samplefile.pdf is the file you want to run OCR on and hi,en are the languages you want to run OCR on. You can run surya_ocr form anywhere form the computer as it installs throughout the system.

after that you can use the following command to get the text from the results.json file:

```
python ocr_text.py
```

and now you will get the text from the results.json file to a text file.
