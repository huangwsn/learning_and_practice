# PDF.P166
args = [
    "Dog", 
    "Cat",
    "Cow",    
]
print(*args)

# PDF.P167
print("Dog", "Cat", "Cow", sep="-")
kwarsForPrint = {"sep": "-"}
print("Dog", "Cat", "Cow", **kwarsForPrint)

# PDF.P167
# using * to create variadic functions

