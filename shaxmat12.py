figur=[["♜","♞","♝","♛","♚","♝","♞","♜"],
       ["♟","♟","♟","♟","♟","♟","♟","♟"],
       [" "," "," "," "," "," "," "," "," ",],
       [" "," "," "," "," "," "," "," "," ",],
       [" "," "," "," "," "," "," "," "," ",],
       [" "," "," "," "," "," "," "," "," ",],
       ["♙","♙","♙","♙","♙","♙","♙","♙"],
       ["♖","♘","♗","♕","♔","♗","♘","♖"]]
##if figur=="♜":
 #   print("jan")
#tiv=0

def sev(n1,n2,m1,m2):
    if ord(figur[n1][n2])>9811 and ord(figur [n1][n2])<9818:
        print("spitak")
    if ord(figur [m1][m2])>9818 and ord(figur [m1][m2])<9824:
        print("sev")

def qaylkatarel(xn1,xn2,xm1,xm2):
    #print(xn1,xn2,xm1,xm2)
    figur[xm1][xm2]=figur[xn1][xn2]
    figur[xn1][xn2]=" "

qayler=""
def qaylara():
    global qayler
    #n1=int (input("mutqagreq texapoxvox figuri i= "))
    #n2=int (input("mutqagreq texapoxvox figuri j= "))
    #m1=int (input("mutqagreq figuri uxutyun@ i= "))
    #m2=int(input("mutqagreq figuri uxutyun@ j= "))
    
    qayl=input("mutqagreq qayl@")
    qayler+=qayl
    n2text=qayl[0]
    n1text=qayl[1]
    m2text=qayl[3]
    m1text=qayl[4]
    #print(n1text,n2text,m1text,m2text)

    n1=ord(n1text)-49
    n2=ord(n2text)-65
    m1=ord(m1text)-49
    m2=ord(m2text)-65
    #print(n1,n2,m1,m2)
    #sev(n1,n2,m1,m2)
    tiv=0
    
    figur[m1][m2]=figur[n1][n2]
    figur[n1][n2]=" "
    nkarel()
    print(qayler)
    if ord (figur[m1][m2])==9820:
        for i in range(len(figur)):
            if figur[i][i-i]==" ":
                pass
            else :
                print(figur [i][i-i])
            for j in range(len(figur)):
                pass
                #print(figur[i])

    
def nkarel():
    board=""
    for i in range(len(figur)):
        for j in range(len(figur)):
            board+=figur[i][j]+"\t"
        board+="\n"
    print(board)    
    
nkarel()
#qayler=""
k=10
i=0
while i<k:
    qaylara()
    nkarel()
    if figur=="♜":
        print("jan")
    #print(figur[m1][m2])    
    
    
    
    
    
