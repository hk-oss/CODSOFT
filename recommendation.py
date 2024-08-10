#recommendation system for books


fic=["All the colour of the dark","Husbands and lovers","sandwich","How to read a book"]
nov=["sherlock holmes","the girl who knew too much","the lord of the rings","beloved"]
scifi=["starwars","Moonstrom","kis Harrison","Fiasco"]
Mys=["That Night","The House of secrets","Then she was gone","Dead of nights"]

def rec(list):
    print(*list,sep="\n")

while True:
    ip=int(input("select book genres in Number:\n1.Fiction\n2.Novel\n3.science fiction\n4.mystery\n"))
    if ip==1:
        rec(fic)
        break
    elif ip==2:
        rec(nov)
        break
    elif ip==3:
        rec(scifi)
        break
    elif ip==4:
        rec(mys)
        break
    else:
        print("invalid option")
        continue
