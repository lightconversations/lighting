"""
This file converts a Comma separated value spreadsheet of CUES into a text
file that can then be imported to a lighting desk. The original code was created by David Orlando.
Tlaloc Lopez-Watermann added file name choice, export file name choice and cue list select.
"""




name = raw_input("What's the csv filename that you want to convert to Eos_ASCII?--this should be a .csv file-- ")
nameout = raw_input("What should your new filename be?--This should be a .txt file-- ")
cuelist = raw_input("Which cue list would you like to add this to? ")


CSV=open(name).readlines()


patch=open(nameout,'w') #Export file
CUE=['Ident 3:0',"\n",'Clear Cues', "\n",'Manufacturer ETC',"\n","Console Eos","\n",'$CueList'+' '+cuelist, "\n"]

#print(CSV[0])

titles=CSV[0]
titles=titles.split(',')

cue_index=titles.index("CUE")
ut_index=titles.index("UT")
dt_index=titles.index("DT")
text_index=titles.index("Label")
f_index=titles.index("F/H")
b_index=titles.index("B")
pt_index=titles.index("PT")
note_index=titles.index("Note")
scene_index=titles.index("Scene")

CSV.remove(CSV[0])
 


for x in CSV:
    line=x.split(',',)
    #print(line)
    #Q number
    if ">" in line[cue_index]:
        line[cue_index]=line[cue_index][2:]
    q_num="Cue "
    q_num+=line[cue_index]
    q_num+=" 1"
    CUE.append(q_num)
    CUE.append("\n")
    
    #PT
    if line[pt_index] != '':
        if line[pt_index] != '1':
            print("i lie:",line[pt_index])
            del CUE[CUE.index(q_num,len(CUE)-2)]
        q_pt="Part "
        q_pt+=line[pt_index]
        CUE.append(q_pt)
        CUE.append("\n")
    
    #UT
    if line[ut_index] != '':
        q_ut="Up "
        q_ut+=line[ut_index]
        CUE.append(q_ut)
        CUE.append("\n")
        q_ut="$$TimeUp "
        q_ut+=line[ut_index]
        q_ut+=" 0 0 1"
        CUE.append(q_ut)
        CUE.append("\n")
    
    
    #DT
    if line[dt_index]!= '':
        q_dt="Down "
        q_dt+=line[dt_index]
        CUE.append(q_dt)
        CUE.append("\n")
        q_dt="$$TimeDown "
        q_dt+=line[dt_index]
        q_dt+=" 0 0 1"
        CUE.append(q_dt)
        CUE.append("\n")
    
    #chans
#    CUE.append("Chan 999 0")
#    CUE.append("\n")
    
    #f
    if line[f_index] != '':
        f_h=line[f_index]
        if f_h[0] == 'F':
            q_f="Followon "
            q_f+=f_h[1:]
            CUE.append(q_f)
            CUE.append("\n")
        if f_h[0] == 'H':
            q_f="$$Hang "
            q_f+=f_h[1:]
            CUE.append(q_f)
            CUE.append("\n")
    
    #text
    if line[text_index] != '':
        text_dt="Text "
        text_dt+=line[text_index]
        CUE.append(text_dt)
        CUE.append("\n")
    
    #Block
    if line[b_index] == 'B':
        q_b='$$Block'
        CUE.append(q_b)
        CUE.append("\n")
    
    #Note
    if line[note_index] != '':
        text_text='$$CueNotes '
        text_text+=line[note_index]
        CUE.append(text_text)
        CUE.append("\n")
    
    #scene
    if line[scene_index] != '':
        scene_text='$$scenetext '
        scene_text+=line[scene_index]
        CUE.append(scene_text)
        CUE.append("\n")
    
    
    CUE.append("\n")
#
CUE.append("EndData")
#
for x in CUE:
    patch.write(x)       #writes group to file
    print(x)
patch.close()
 
 
 
 
 
 


#README FILE
README=open('README.txt','w')
README.write("""
This file converts a Comma separated value spreadsheet of CUES into a text
file that can then be imported to a lighting desk. The original code was created by David Orlando.
Tlaloc Lopez-Watermann added file name choice, export file name choice and cue list select.

Please use the following label headers for you CSV file:
CUE for the cue number
UT for the Up Time
DT for the Down Time
Label for the cue label
F/H for follow hang
B for block cues. Must be a capital B to work
PT for part
Note for the notes
Scene for scenes
'please know that scenes are associated with cues and should not have their own row'.

!!!!!!!!!!ONLY USE ASCII IMPORT WITH NEW SHOWFILES!!!!!!!!!!!!!!!!

ASCII import empties all the data of the current file and repopulates it ONLY with the data in the .txt file

!!!!!!!!!!ONLY USE ASCII IMPORT WITH NEW SHOWFILES!!!!!!!!!!!!!!!!


the only information contained here is group information

in EOS, this import will also create presets with identical information as the groups with all channels at 100%

in EOS to import:
-File>Import>USITT ASCII
""")
README.close()
     