#imprimir el mayor numero en una lista
#forma 3

def numeroMasGrande(*nums):
    mayor=nums[0]

    for n in nums:
        if n>mayor:
            mayor=n

    print("numero mas grande: ",mayor)

numeroMasGrande(56,34,5,6)
            