# pylint: disable=invalid-name
'''
High level docstring
'''
#Modules
from os import listdir
from os.path import isfile, join
#from wand.image import Image
import ghostscript

#constants
directory_in_str = '/Temp/Documents'
directory_out_str = '/Temp/Images'

#variables
files_in_directory = [f for f in listdir(directory_in_str) if isfile(join(directory_in_str, f))]

def main():
    '''This is the method'''

    for file in files_in_directory: #for each file in list
        input_doc = directory_in_str + '/' + file #set the input path
        print(input_doc)
        output_doc = directory_in_str + '/' + file + '.jpg' #set the output path
        
        args = ["gs", # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r144",
            "-sOutputFile=" + output_doc,
            input_doc]
        
        ghostscript.Ghostscript(*args)
        
        #img = Image(filename=input_doc) #set the input document
        #img.save(filename=output_doc) #set the output image

if __name__ == '__main__':
    main()
