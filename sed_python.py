import os
import sys

with open(sys.argv[1], 'r') as file:
    str_tmp = "ghostgoose"
    data = file.read()
    tmp = sys.argv[2] + ":" + sys.argv[3]
    data = data.replace("100.71.71.71:5000/init-container:latest", tmp)
         

with open(sys.argv[1], 'w') as file:
    file.write( data )
    print(data)
