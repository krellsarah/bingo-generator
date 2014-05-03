bingo-generator
===============

This is a script to create nicely formatted bingo sheets for buzzword bingo. Bingo sheet are outputted in pdf format. 

Setup
-----

In order to use this script, you must make sure you have the wkhtmltopdf library installed. 

On a debian based system:
```
sudo apt-get install wkhtmltopdf
```

After that, you should be able to run the bingo.py script found in the src folder. 

Syntax
------

The most basic syntax for bingo-generator is
```
python bingo.py -i input_file -o output_file
```

The input_file is a text file containing the words you would like to use in the bingo squares, with one word per line. An example file can be found in the example folder. 

The output_file is the file you would like the bingo card to be written to. The bingo card will be a pdf. 

You can also specify different header letters other than BINGO using the -t flag:

```
python bingo.py -i input_file -o output_file -t TESTO
```

would make the letters T E S T O the headers for the bingo columns.

The other option available is the -f flag which allows you to change the free space text to whatever you want it to be. 

```
python bingo.py -i input_file -o output_file -f "The Most Free Space Ever"
```
would make the free space text "The Most Free Space Ever"
