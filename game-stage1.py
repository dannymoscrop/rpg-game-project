import textwrap

def printtext(text):
  wrapped_text = textwrap.wrap(text, width=50)
  for line in wrapped_text:
    print(line)

text = "Stage 1: The Royal Audience"
printtext(text)
text = "You stand in the grand throne room of Castle Denethor. \
King Denethor, frail and aged, sits on his ornate throne, his crown slightly askew. He looks at you with weary but hopeful eyes. \
King Denethor: We need a hero to face the unknown and save Denethor. Will you take up this burden?" 

"1. Agree to Help"
"2. Refuse"
printtext(text)

