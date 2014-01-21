
final_str=""
input_str=""
Done = False
while not(Done) :
    input_str=raw_input("Enter a word (. | or ? to end): ")
    final_str+=(input_str+" ")
    if input_str in ('.','!','?'):
        Done = True
        break

print final_str