c=0
k=1
while c < k:
    n=11
    text=""
    m=int(input ("toxeri qanak@ =" ))
    for i in range(n):
        for j in range(n):
            if i<=m-1 or  i>=n-m:
                text+="*"
            elif j<=m-1 or j>=n-m:
                text+="*"
            else:
                text+="0"
        text+="\n"
        
    print(text)
