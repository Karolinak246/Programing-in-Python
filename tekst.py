################################
# 7.12.2020
# Kopczak Karolina
# Programowanie w jezyku Python
# Zadania: TEKST
################################

#!/usr/bin/env python3

path = "/home/pi/Documents/Python"

### TASK 1 ###
def delete_words():
	selected_text = open("Texts/Before_removing.txt").read().split(sep=' ')
	words_to_delete = ["sie", "i", "oraz", "nigdy", "dlaczego"]
	finished_text = open("Texts/After_removing.txt", "a")
	for f in selected_text:
		if f in words_to_delete:
			selected_text.remove(f)
	finished_text.write(' '.join(selected_text))
	finished_text.close()

delete_words()

### TASK 2 ###
def replace_words():
	selected_text = open("Texts/Before_replacing.txt").read().split(sep = ' ')
	repl_words = {"i" : "oraz","oraz" : "i","nigdy" : "prawie nigdy", "dlaczego": "czemu"}
	finished_text = open("Texts/After_replacing.txt", "a")
	for f in range (len(selected_text)):
		if selected_text[f] in repl_words.keys():
			selected_text[f]  = repl_words[selected_text[f]]
	finished_text.write(' '.join(selected_text))
	finished_text.close()

replace_words()
