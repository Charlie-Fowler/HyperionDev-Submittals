#replace.py
#save sentence as a viarable
#Replace '!' Character to a blank space
#reprint sentence in upper case
#reprint in reverse

sentence_variable = "The!quick!brown!fox!jumps!over!the!lazy!dog"

print(sentence_variable.replace('!',' ')) #removes '!' and replaces with ' '
print(sentence_variable.upper().replace('!',' ')) #retains replacement of !, however prints in CAPS
print(sentence_variable.upper().replace('!',' ')[::-1]) #retains replacement of !, in CAPS but prints backwards.
