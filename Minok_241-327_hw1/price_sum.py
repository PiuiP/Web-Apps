with open('products.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
    adult_total = 0.0
    pensioner_total = 0.0
    child_total = 0.0
    
    for line in lines[1:]: 
        parts = line.strip().split(',')
        
        if len(parts) >= 4:
            adult_total += float(parts[1].strip())
            pensioner_total += float(parts[2].strip())
            child_total += float(parts[3].strip())

    
    adult_total = round(adult_total, 2)
    pensioner_total = round(pensioner_total, 2)
    child_total = round(child_total, 2)
    
    print(f"{adult_total} {pensioner_total} {child_total}")