#imprimir el mayor numero en una lista
#forma 4

def numeroMasGrande(*nums):
    mayor=max(nums)
    return mayor

print("El numero mas grande: ",(numeroMasGrande(1,45,6,86)))