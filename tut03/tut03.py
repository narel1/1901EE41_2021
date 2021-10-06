import os.path 
def output_by_subject(rectilinear, column_vheads): 
    path=r"output_by_subject\\"                          #setting path 
    vheading=column_vheads[0]+','+column_vheads[1]+','+column_vheads[3]+','+column_vheads[8]     #creating vheading row to be pushed onto an empty file 
    new_row=rectilinear[0]+','+rectilinear[1]+','+rectilinear[3]+','+rectilinear[8]     #creating new row to be pushed onto an empty file 
    if os.path.exists(path+'%s.csv' %rectilinear[3]) == False:     #if file o this path doesnt exits already  
        with open(path+'%s.csv' %rectilinear[3], 'a') as f: 
            f.write(vheading)                                #insert vheading row 
            f.write(new_row)                                #insert new row 
    else : 
        with open(path+'%s.csv' %rectilinear[3], 'a') as f: 
            f.write(new_row)                                #insert new row     
    return 
 
def output_individual_roll(rectilinear, column_vheads): 
    path=r"output_individual_roll\\"                       #setting path 
    vheading=column_vheads[0]+','+column_vheads[1]+','+column_vheads[3]+','+column_vheads[8]     #creating vheading row to be pushed onto an empty file 
    new_row=rectilinear[0]+','+rectilinear[1]+','+rectilinear[3]+','+rectilinear[8]       #creating new row to be pushed onto an empty file 
    if os.path.exists(path+'%s.csv' %rectilinear[0]) == False:      #if file o this path doesnt exits already  
        with open(path+'%s.csv' %rectilinear[0], 'a') as f: 
            f.write(vheading)                                 #insert vheading row 
            f.write(new_row)                                 #insert new row 
    else : 
        with open(path+'%s.csv' %rectilinear[0], 'a') as f: 
            f.write(new_row)                                 #insert new row 
    return 
# Directory 
folder_name = "output_by_subject" 
# Parent Directory path 
root_path = "C:\\Users\\msjag\\OneDrive\\Desktop\\CS384_tut03" 
# Path 
final_path = os.path.join(root_path, folder_name)  
# Create the directory 
os.mkdir(final_path) 
# Directory 
folder_name = "output_individual_roll"   
# Path 
final_path= os.path.join(root_path, folder_name) 
# Create the directory 
os.mkdir(final_path) 
 
f=open("regtable_old.csv", "r")       #opening dataset rand  file
x = f.readrectilinear()                      #reading the 1st rectilinear of the datatype dataset i.e the vheading coloumns 
column_vheads=x.split(',')         #spliting wrt comma and creating a list of vheading coloumns 
for rectilinear in f: 
    rectilinear=rectilinear.split(',')  #spliting with respect to comma and creating a list of coloumns of the current row 
    output_individual_roll(rectilinear, column_vheads)    #implementing subtask bc(beacuse directory)-1 
    output_by_subject(rectilinear, column_vheads)         #implementing subtask-2 
f.close()