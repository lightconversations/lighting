# lighting
Code in service to lighting designers

# Info on LightConversationsCue.py

This file converts a Comma separated value spreadsheet of CUES into a text
file that can then be imported to a lighting desk. The original code was created by David Orlando.

Tlaloc Lopez-Watermann added file name choice, export file name choice and cue list select.

Please use the following label headers for you CSV file:
<br />CUE for the cue number
<br />UT for the Up Time
<br />DT for the Down Time
<br />Label for the cue label
<br />F/H for follow hang
<br />B for block cues. Must be a capital B to work
<br />PT for part
<br />Note for the notes
<br />Scene for scenes
please know that scenes are associated with cues and should not have their own row'.

!!!!!!!!!!ONLY USE ASCII IMPORT WITH NEW SHOWFILES!!!!!!!!!!!!!!!!
ASCII import empties all the data of the current file and repopulates it ONLY with the data in the .txt file.
A good practice is to use this is to import the ASCII to new (merging) show file in an offline editor, making it possible to MERGE the cues to a show on a console with a patch, macros, other cue lists etc. When merging make sure to MERGE ONLY THE CUES. The reason for doing it this way is so the patch at the theatre is not lost. When running the LightConversationsCues.py you will be able to choose the cue list number. This number will follow the merge into your show file.
!!!!!!!!!!ONLY USE ASCII IMPORT WITH NEW SHOWFILES!!!!!!!!!!!!!!!!

In EOS to import use -File>Import>USITT ASCII
