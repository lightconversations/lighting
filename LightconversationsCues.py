"""
This file converts a Comma separated value spreadsheet of CUES into a text
file that can then be imported to a lighting desk. The original code was created by David Orlando.
Tlaloc Lopez-Watermann added file name choice, export file name choice and cue list select.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

filename = ""
fileout= ""
q_list= ""
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.geometry('300x300')
root.resizable(True,True)
#q_list = Entry(root, width=50)
#q_list.pack()
#q_list.insert(0, "enter the cuelist")
#label = tk.Label(0,text= fileout)
#label.pack(side="bottom")

#select the file to convert.

def select_file():
    global filename
    filetypes = (
    ('text files', '*.csv'),
    ('All files', '*.*'))
    
    filename = fd.askopenfilename(
    title='Open a file',
    initialdir='/',
    filetypes=filetypes)
    
    
#Set the file and location to save to.

def save_file():
        global fileout
        filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*'))
        
        
        fileout = fd.asksaveasfilename(
        title='name to save your text file to for the EOS',
        initialdir='/',
        filetypes=filetypes)
       # Creates label and shows it
        
        
        
#def cue_list_e():
#        listLabel = "Cue List #:" + q_list()
#        myLabel = Label(root, text=listLabel())
 #       myLabel.pack()


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file)

open_button.pack(expand=True)


# open button
save_button = ttk.Button(
    root,
    text='save name and location',
    command=save_file)
save_button.pack(expand=True)


#q_button = ttk.Button(
#   root, 
#    text="enter", 
#    command=cue_list_e)
#q_button.pack(expand=True)

#("Which cue list would you like to add this to? ")
         


CUELIST = input("Which cue list would you like to add this to? ")
CSV=open(str(filename)).readlines()
PATCH = open(fileout,'w')

CUE=['Ident 3:0',"\n",'Clear Cues', "\n",'Manufacturer ETC',"\n","Console Eos","\n",'$CueList'+' '+CUELIST,"\n"]
#print(CSV[0])

TITLES=CSV[0]
TITLES=TITLES.split(',')
CUE_INDEX=TITLES.index("CUE")
UT_INDEX=TITLES.index("UT")
DT_INDEX=TITLES.index("DT")
TEXT_INDEX=TITLES.index("Label")
F_INDEX=TITLES.index("F/H")
B_INDEX=TITLES.index("B")
PT_INDEX=TITLES.index("PT")
NOTE_INDEX=TITLES.index("Note")
SCENE_INDEX=TITLES.index("Scene")

CSV.remove(CSV[0])



for x in CSV:
    line=x.split(',',)
    #print(line)
    #Q number
    if ">" in line[CUE_INDEX]:
        line[CUE_INDEX]=line[CUE_INDEX][2:]
    q_num="Cue "
    q_num+=line[CUE_INDEX]
    q_num+=" 1"
    CUE.append(q_num)
    CUE.append("\n")

    #PT
    if line[PT_INDEX] != '':
        if line[PT_INDEX] != '1':
            print("i lie:",line[PT_INDEX])
            del CUE[CUE.index(q_num,len(CUE)-2)]
        q_pt="Part "
        q_pt+=line[PT_INDEX]
        CUE.append(q_pt)
        CUE.append("\n")

    #UT
    if line[UT_INDEX] != '':
        q_ut="Up "
        q_ut+=line[UT_INDEX]
        CUE.append(q_ut)
        CUE.append("\n")
        q_ut="$$TimeUp "
        q_ut+=line[UT_INDEX]
        q_ut+=" 0 0 1"
        CUE.append(q_ut)
        CUE.append("\n")


    #DT
    if line[DT_INDEX]!= '':
        q_dt="Down "
        q_dt+=line[DT_INDEX]
        CUE.append(q_dt)
        CUE.append("\n")
        q_dt="$$TimeDown "
        q_dt+=line[DT_INDEX]
        q_dt+=" 0 0 1"
        CUE.append(q_dt)
        CUE.append("\n")

    #chans
#    CUE.append("Chan 999 0")
#    CUE.append("\n")

    #f
    if line[F_INDEX] != '':
        f_h=line[F_INDEX]
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
    if line[TEXT_INDEX] != '':
        text_dt="Text "
        text_dt+=line[TEXT_INDEX]
        CUE.append(text_dt)
        CUE.append("\n")

    #Block
    if line[B_INDEX] == 'B':
        q_b='$$Block'
        CUE.append(q_b)
        CUE.append("\n")
    if line[B_INDEX] == 'I':
        q_b='$$IntBlock'
        CUE.append(q_b)
        CUE.append("\n")

    #Note
    if line[NOTE_INDEX] != '':
        text_text='$$CueNotes '
        text_text+=line[NOTE_INDEX]
        CUE.append(text_text)
        CUE.append("\n")

    #scene
    if line[SCENE_INDEX] != '':
        scene_text='$$scenetext '
        scene_text+=line[SCENE_INDEX]
        CUE.append(scene_text)
        CUE.append("\n")

#end append
    CUE.append("\n")
#
CUE.append("EndData")
#
for x in CUE:
    PATCH.write(x)       #writes group to file
    print(x)
PATCH.close()

    
#README FILE
README=open('README.txt','w')
README.write("""
This file converts a Comma separated value spreadsheet of CUES into a text
file that can then be imported to a lighting desk. The original code was created by David Orlando.
Tlaloc Lopez-Watermann added file name choice, export file name choice and cue list select.

For a tutorial on how to best utilize this code please see this video on YouTube. https://www.youtube.com/watch?v=ApFyayLdHcA

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
ASCII import empties all the data of the current file and repopulates it ONLY with the data in the .txt file.
A good practice is to use this is to import the ASCII to new (merging) show file in an offline editor, then MERGE the cues to a show on the
console. When merging make sure to MERGE ONLY THE CUES. The reason for doing it this way is so the patch at the theatre is not lost.
!!!!!!!!!!ONLY USE ASCII IMPORT WITH NEW SHOWFILES!!!!!!!!!!!!!!!!


in EOS to import:
-File>Import>USITT ASCII
""")
README.close()


#!!!!EOS ASCII COMMANDS FOR REFERENCE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#! Cues
#! $CueList n      All subsequent cues are in cuelist n
#!                 Cue lists can have a TEXT secondary and the following flags:
#! $$IntensityMaster
#! $$Independent
#! $$HTP           HTP
#! $$Assert        Assert
#! $$SoloMode      Solo Mode
#! $$Master        Slider mode, see comment, default=Master
#! $$BackFrom1st   see comment
#! $$GoFromLast    see comment
#! $$Stomp         see comment
#! $$Exclude       see comment
#! $$Control       number, fader mode, min, max, buttons 1-3 id/arg
#! $Cue:           All cues not in the first cue list and those
#!                 with more than one digit after the decimal point
#! $$Text          Cue/Part label
#! $$Assert        Assert
#! $$Block         Block
#! $$IntBlock      IntBlocK
#! The following cue times use this format:  Fade time, Delay time,
#!                 Use default fadetime (1=true, 0=false, M=manual),
#!                 Use default delay time (1=true, 0=false)
#! $$TimeUp        Up times
#! $$TimeDown      Down times
#! $$TimePosition  Focus times
#! $$TimeColor     Color times
#! $$TimeGraphic   Beam times
#! $$Rate          Rate (100 = normal)
#! $$Follow        Auto-follow time counting from previous cue start
#! $$Hang          Auto-follow time counting from previous cue completion
#! $$Action        Stop/Execute, Target
#! $$Action        UDP/MIDI, String
#! $$Curve         Curve (0.01 .. 9999.99)
#! $$Link list/cue Link to or from a cue not in the first list or to
#!                 one with more than one digit after the decimal point
#! $$CueNotes      Cue Notes
#! $$SceneText     Scene Text
#! $$SceneEnd      Scene End flag
#!
#! $$ChanMove      Intensity moves
#! Chan            Tracked levels
