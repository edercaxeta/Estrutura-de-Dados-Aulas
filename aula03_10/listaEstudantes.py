estudantes = { "Eder":{"Idade":20,"Telefone":"61995587078","Nota":9.5},   
              "Maria":{"Idade":15,"Telefone":"61993589615","Nota":6.5},   
              "Carlos":{"Idade":22,"Telefone":"61996356789","Nota":9.0},   
              "Ana":{"Idade":20,"Telefone":"61996633668","Nota":7.6},   
              "Rafael":{"Idade":20,"Telefone":"61999863659","Nota":6.7}}   


print("Eder" + str(estudantes["Eder"]))
print()

estudantes["Marcos"] = {"Idade":22,"Telefone":"61996356789","Nota":10}  ##add no mapa
del estudantes["Rafael"]    ##deletendo no mapa

for aluno, info in estudantes.items():
    print(f"{aluno} - Idade: {info['Idade']}, - Telefone {info['Telefone']}, - Nota: {info['Nota']}")


somaNota=0
for aluno in estudantes.values():
    somaNota += aluno['Nota']   

print(f"A soma das notas é {somaNota}")

media = somaNota/len(estudantes)

print(f"A media da turma é: {media}")