# ✨ Desafio 100 Dias de Código - Dia 8/100 💻

# Hogwarts House Sorting Quiz

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


q1 = int(input('''[Q1] Do you like Dawn or Dusk?

    [1] Dawn
    [2] Dusk
    
    '''))

if q1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong input")  

q2 = int (input('''[Q2] When I’m dead, I want people to remember me as:

    [1] The Good
    [2] The Great
    [3] The Wise
    [4] The Bold
           
    '''))

if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print("Wrong input")        

q3 = int(input("""[Q3] Which kind of instrument most pleases your ear?

    [1] The violin
    [2] The trumpet
    [3] The piano
    [4] The drum
           
    """))

if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:          
  print("Wrong input")  


print("🦁 Gryffindor", gryffindor)
print("🦅 Ravenclaw", ravenclaw)  
print("🦡 Hufflepuff", hufflepuff)  
print("🐍 Slytherin", slytherin)

max_score = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print("\nYour house is:")
if gryffindor == max_score:
    print("🦁 Gryffindor")
if ravenclaw == max_score:
    print("🦅 Ravenclaw")
if hufflepuff == max_score:
    print("🦡 Hufflepuff")
if slytherin == max_score:
    print("🐍 Slytherin")