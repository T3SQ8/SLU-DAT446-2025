def matrix_multiply(A, B):
    A_rows = len(A) 
    B_rows = len(B)
    C = []
    if A_rows > 0 and B_rows > 0:
        A_cols = len(A[0])
        B_cols = len(B[0])

        # NOTE Raden nedan kan vara svår att förstå, stycket efter gör samma sak på ett enklare
        # sätt. Om du vill förstå hur det fungerar kan du kolla denna 2 min video:
        # https://youtu.be/l8mWvDUwOt4  

        # C = [[0 for _ in range(B_cols)] for _ in range(A_rows)] # skapar en matris av rätt storlek


        # Skapa nollmatris av rätt dimentioner
        C = []
        for _ in range(A_rows):
            row = []
            for _ in range(B_cols):
                row.append(0)
            C.append(row)


        # NOTE Lägg märke till att koden nedan adderar "in place" via += till elementen i C, som i
        # början är noll. Detta gör vi eftersom varje element ska vara summan av flera produkter.

        for i in range(A_rows): # rader i A
            for j in range(B_cols): # kolonner i B
                for k in range(A_cols): # kolumn i A, rad i B
                    C[i][j] += A[i][k] * B[k][j] # dot produkt
    return C



A = [[1, 2],
     [3, 4]]

B = [[2, 0],
     [1, 3]]



print(matrix_multiply(A, B))
