import re
import os
import shutil 





os.system('cls')

def regex_renamer():
   
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webchapters_num = int(input("Enter the number of the web chapters that you wish to rename. 1/2/3: "))
    s_padding = int(input("Enter the Season Number Padding: "))
    e_padding = int(input("Enter the Episode Number Padding: "))
    name_of_chapters = ""
    if webchapters_num==1:
        name_of_chapters = "Breaking Bad"
    elif webchapters_num ==2:
        name_of_chapters="Game of Thrones"
    else:
        name_of_chapters ="Lucifer"
       
    if name_of_chapters=='Breaking Bad':
        files_chapters= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_chapters)
        for chapters in files_chapters:
            chapters_sub= re.split(' ',chapters)
            info_chapters=re.split('[se]',chapters_sub[2])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_chapters+"\\"+chapters,newpath+"\\corrected_srt\\Breaking Bad\\Breaking Bad - Season "+str('{:' + '0' + '>' + str(s_padding) + '}').format(info_chapters[1])+" Episode "+str('{:' + '0' + '>' + str(e_padding) + '}').format(info_chapters[2])+"."+re.split('\.',chapters_sub[3])[3]) 
    
    elif name_of_chapters=='Game of Thrones':
        files_chapters= os.listdir(os.getcwd()+"\\wrong_srt\\"+name_of_chapters)
        for chapters in files_chapters:
            chapters_main= re.split('.WEB',chapters)
            chapters_sub=re.split("-",chapters_main[0])
            info_chapters=re.split('[x]',chapters_sub[1])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+name_of_chapters+"\\"+chapters,newpath+"\\corrected_srt\\Game of Thrones\\Game of Thrones - Season "+str('{:' + '0' + '>' + str(s_padding) + '}').format(info_chapters[0].strip())+" Episode "+str('{:' + '0' + '>' + str(e_padding) + '}').format(info_chapters[1])+"-"+chapters_sub[2]+"."+re.split('\.',chapters_main[1])[4])          