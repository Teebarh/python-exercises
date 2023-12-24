rivers = {
    'Nile':"Egypt",
    'Amazon':'Brazil',
    'Zaire':'Congo'
}

for k,v in rivers.items():
    print(f"The {k} runs through {v}.")
    
for k in rivers.keys():
    print(k)
    
for v in rivers.values():
    print(v)