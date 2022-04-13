# sr1,rr,t,lm,bo,rem,sr2,hr,clase
sr1 = sorted([93.80,   91.64,  60.00,  85.76,  48.12])
rr = sorted([25.680,      25.104,      20.000,      23.536,      17.248])
t = sorted([91.840,      91.552,     96.000,     90.768,      97.872])
lm = sorted([16.600,      15.880,      10.000,      13.920,       6.496])
bo = sorted([89.840,      89.552,      95.000,      88.768,      96.248])
rem = sorted([99.60,       98.88,       85.00,       96.92,    72.48])
sr2 = sorted([1.840, 1.552,    7.000,    0.768,    8.248])
hr = sorted([74.20,     72.76,      60.00,      68.84,      53.12])
clase = sorted([3,      3,      1,      3,    0])

def find_median(sorted_list):
    indices = []
    median = 0
    list_size = len(sorted_list)
    #print("Tamaño de la lista=", list_size)

    if list_size % 2 == 0:
        # -1 because index starts from 0
        indices.append(int(list_size / 2) - 1)
        indices.append(int(list_size / 2))

        median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2
        pass
    else:
        indices.append(int(list_size / 2))

        median = sorted_list[indices[0]]
        pass

    return median, indices
    pass

# percentil 25= 1 Cuartil
# percentil 50= 2 Cuartil=Mediana
# percentil 75= 3 Cuartil
# sr1,rr,t,lm,bo,rem,sr2,hr,clase
print("=================================================")
median, median_indices = find_median(sr1)
#print("mediana, median_indices ==>>", median, median_indices)
#("=================================================")
Q1, Q1_indices = find_median(sr1[:median_indices[0]])
#print("Primera Div Vec ==>>", sr1[:median_indices[0]])
#print("Q1 , Q1_indices ==>>", Q1, Q1_indices)
#print("=================================================")

#el 25% es menor a :", Q1
print("sr1-->1er cuartil de datos= ",Q1," percentil 50 = ", median)
# sr1,rr,t,lm,bo,rem,sr2,hr,clase
median, median_indices = find_median(rr)
Q1, Q1_indices = find_median(rr[:median_indices[0]])
print("rr-->1er cuartil de datos= ", Q1, "    percentil 50 = ", median)


median, median_indices = find_median(t)
Q1, Q1_indices = find_median(t[:median_indices[0]])
print("t-->1er cuartil de datos= ",Q1,"    percentil 50 = ", median)
median, median_indices = find_median(lm)
Q1, Q1_indices = find_median(lm[:median_indices[0]])
print("lm-->1er cuartil de datos= ",Q1,"    percentil 50 = ", median)


median, median_indices = find_median(bo)
Q1, Q1_indices = find_median(bo[:median_indices[0]])
print("bo-->1er cuartil de datos= ",Q1,"    percentil 50 = ", median)
median, median_indices = find_median(rem)
Q1, Q1_indices = find_median(rem[:median_indices[0]])
print("rem-->1er cuartil de datos= ",Q1,"    percentil 50 = ", median)


median, median_indices = find_median(sr2)
Q1, Q1_indices = find_median(sr2[:median_indices[0]])
print("sr2-->1er cuartil de datos= ",Q1,"    percentil 50 = ", median)

median, median_indices = find_median(hr)
Q1, Q1_indices = find_median(hr[:median_indices[0]])
print("hr-->1er cuartil de datos= ",Q1,"    percentil 50 = ", median)

median, median_indices = find_median(clase)
Q1, Q1_indices = find_median(clase[:median_indices[0]])
print("clase-->1er cuartil de datos= ",Q1,"    percentil 50 = ", median)

#los resultados de objetivo muestran una media de 3
#y un 1er cuartil de datos=  0.5  dondo a decir que estos niveles son frecuentes


# =============================================================================
# =================================================
# sr1-->1er cuartil de datos=  54.06  percentil 50 =  85.76
# rr-->1er cuartil de datos=  18.624000000000002     percentil 50 =  23.536
# t-->1er cuartil de datos=  91.16     percentil 50 =  91.84
# lm-->1er cuartil de datos=  8.248000000000001     percentil 50 =  13.92
# bo-->1er cuartil de datos=  89.16     percentil 50 =  89.84
# rem-->1er cuartil de datos=  78.74000000000001     percentil 50 =  96.92
# sr2-->1er cuartil de datos=  1.1600000000000001     percentil 50 =  1.84
# hr-->1er cuartil de datos=  56.56     percentil 50 =  68.84
# clase-->1er cuartil de datos=  0.5     percentil 50 =  3
# =============================================================================
