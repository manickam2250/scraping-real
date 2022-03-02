import os
from os import walk
i=1
for root,dir,files in walk("/home/manikam/projects"):

    print(i,")-->",root,"--------->",dir,"------>",files)
    i+=1
    print("=========================================================================================================")

    # for j in files:
    

      
    #        if j[-1:-4:-1] == "txt":

    #            print(i,")-->",j)

             
    #         #   with open (f"{root}/{j}","r") as file1:
    #         #       data1=file1.read()
    #         #       print("data1 info ---->",data1)
    #         #       break
   