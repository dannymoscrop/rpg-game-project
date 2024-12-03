Village
print (story section: village)
    print ("I open locks yet hold no teeth,
Silent I stand, with secrets beneath.
Though I am small, I hold great might,
To open doors and grant you sight.
What am I?")
input
    if answer is "key" "hp" = "hp"+1 and send to "swamp"
    else send to "forest""

forest
print (story section: forest)
"hp" = "hp"-2
send to "the cave"
