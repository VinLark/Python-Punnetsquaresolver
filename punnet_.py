square = [[], [], [], []]
           
dominant = "B"
recessive = dominant.lower()

dom_phenotype = "Red"
recessive_phenotype = "Green"

first = [dominant, recessive]
bottom = [dominant, recessive]

top_left = square[0]
top_right = square[1]
bottom_left = square[2]
bottom_right = square[3]

top_left.insert(0, first[0])
bottom_left.insert(0, first[0])

top_right.insert(0, first[0])
bottom_right.insert(0, first[1])

top_left.insert(0, bottom[0])
top_right.insert(0, bottom[0])

bottom_left.insert(0, bottom[1])
bottom_right.insert(0, bottom[1])

val = 0
for item in square:
    square[val] = sorted(item)
    val = int(val) + 1


def geno_match():
    dom = 0
    rec = 0
    het = 0 
    
    for i in range(len(square)):
      list = square[i]
      geno = str(list[0]) + str(list[1])
      
      if geno == (dominant + dominant):
        dom = int(dom) + 1
      elif geno == (dominant + recessive):
        het = int(het) + 1
      elif geno == (recessive + recessive):
        rec = int(rec) + 1
    
    return dom, rec, het

dom, rec, het = geno_match()

dom_max = int(dom) * 25
rec_max = int(rec) * 25
het_max = int(het) * 25

print("Punnet Square:\n[" + str(square[0][0]) + str(square[0][1]) + ", " + str(square[1][0]) + str(square[1][1]) + "]\n[" + str(square[2][0]) + str(square[2][1]) + ", " + str(square[3][0]) + str(square[3][1]) + "]\n")

print("Genotypes:\n" + (dominant + dominant) + ": " + str(dom_max) + "%\n" + (dominant + recessive) + ": " + str(het_max) + "%\n" + (recessive + recessive) + ": " + str(rec_max) + "%\n")

print("Phenotypes:\n" + dom_phenotype + ": " + (str(int(dom_max) + int(het_max))) + "%\n" + recessive_phenotype + ": " + (str(rec_max)) + "%")