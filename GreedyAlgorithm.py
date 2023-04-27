options = [{'name': 'Option 1', 'cost': 4000, 'roi': 0.4},    
           {'name': 'Option 2', 'cost': 2000, 'roi': 0.6},    
           {'name': 'Option 3', 'cost': 10000, 'roi': 0.8},    
           {'name': 'Option 4', 'cost': 4000, 'roi': 1.0},    
           {'name': 'Option 5', 'cost': 5000, 'roi': 1.2},   
           {'name': 'Option 6', 'cost': 6000, 'roi': 1.4},   
           {'name': 'Option 7', 'cost': 7000, 'roi': 1.6},   
           {'name': 'Option 8', 'cost': 8000, 'roi': 1.8},   
           {'name': 'Option 9', 'cost': 1000, 'roi': 2.0},  
           {'name': 'Option 10', 'cost': 10000, 'roi': 2.2},]

total_budget = 20000
options_sorted = sorted(options, key=lambda x: x['roi'] / x['cost'], reverse=True)
total_cost = 0
total_roi = 0
chosen_options = []

for option in options_sorted:
    if total_cost + option['cost'] <= total_budget:
        total_cost += option['cost']
        total_roi += option['roi']
        chosen_options.append(option)
    else:
        break

print("Chosen options:")
for option in chosen_options:
    print(option['name'])

print("Total cost:", total_cost)
print("Total ROI:", total_roi)