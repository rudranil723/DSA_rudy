def tower(n, form_rod, to_rod, aux_rod):
    if n == 0:
        return 
    tower (n-1, form_rod, aux_rod,to_rod)
    print("move disk", n,"form rod", form_rod, " to rod ",to_rod)

    tower(n-1,aux_rod, to_rod, form_rod)
    
n=4
tower(n,'A',"B","C")