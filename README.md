# lighting
Code in service to lighting designers

# Info on LightConversationsCue.py

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
ASCII import empties all the data of the current file and repopulates it ONLY with the data in the .txt file.
A good practice is to use this is to import the ASCII to new (merging) show file in an offline editor, then MERGE the cues to a show on the
console. When merging make sure to MERGE ONLY THE CUES. The reason for doing it this way is so the patch at the theatre is not lost.
!!!!!!!!!!ONLY USE ASCII IMPORT WITH NEW SHOWFILES!!!!!!!!!!!!!!!!
in EOS to import:
-File>Import>USITT ASCII
""")
README.close()
