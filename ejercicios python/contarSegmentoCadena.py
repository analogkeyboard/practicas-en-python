def contarSegmentoCadena(segm,cad):
    cont=0
    print("cadena: ",cad)
    for x in cad:
        if x==segm:
            cont+=1
    print("letra:",segm,"=",cont)

contarSegmentoCadena("a","taagggfhgfjnia")
contarSegmentoCadena("g","taagggfhgfjnia")
contarSegmentoCadena("f","taagggfhgfjnia")
