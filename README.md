Pcrawl is a python tool that crawl list of urls and extract parameteres from it.

## usage ##
- python3 Param.py -h

usage: Param.py [-h] -f INPUT_FILE -o OUTPUT_FILE [-t THREADS]

Crawl URLs and extract parameters

options:
  -h, --help            show this help message and exit
  -f INPUT_FILE, --input_file INPUT_FILE
                        Path to the file containing URLs
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to the output file
  -t THREADS, --threads THREADS
                        Number of threads to use for crawling URLs
                       
- -f : for input file(endpoints file)
- -o : for output file(file contain tool result)
- -t : for control threading (defult is 1)

## install ##

- git clone https://github.com/Mostafa-Elguerdawi/Pcrawl
- cd Pcrawl/Pcrawl
- pip3 install requirements.txt OR sudo xargs -a requirements.txt sudo apt-get install -y
- python3 Param.py -f endpoints.txt -o result.txt -t 2
