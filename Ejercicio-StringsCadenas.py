my_string = """ 
Este es un product muy defectuoso, excelente, horrible 
"""

positive_words = ["bueno", "excelente", "maravilloso"]
negative_words = ["defectuoso", "malo", "horrible"]

score = 0

for positive_word in positive_words:
    score = score + my_string.count(positive_word)

for negative_word in negative_words:
    score = score - my_string.count(negative_word)

if score == 0:
    result = "Neutro"
if score > 0:
    result = "Positivo"
if score < 0:
    result = "Negativo"

print("Analizador de sentimientos\n")
print("my_string: {}\nscore: {} \nresultado: {}".format(my_string, score, result))
