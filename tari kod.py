aybuben="ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՓՔևՕՖ"
text="Մեսրոպ Մաշտոցը, դժվարությամբ դարձի բերելով Գողթն գավառի ժողովրդին, հասկանում է, որ երկրում տիրապետող կրոնական-պաշտամունքային լեզուներով՝ հունարենով և ասորերենով հնարավոր չէ ժողովրդի մեջ տարածել քրիստոնեությունը. չնայած արդեն 100 տարի էր անցել քրիստոնեության ընդունումից, ժողովրդի մեծ մասը դեռ պահպանում էր հեթանոսական կրոնն ու սովորույթները։ Մաշտոցը հասկանում է, որ քրիստոնեության դիրքերը հնարավոր է ամրապնդել միայն այն դեպքում, երբ եկեղեցական արարողակարգը տարվի մայրենի լեզվով՝ հայերենով, իսկ դրա համար անհրաժեշտ էր սեփական գրերի ստեղծումը։ Իր մտքերով նա կիսվում է Սահակ Պարթևի հետ, և պարզվում է, որ կաթողիկոսը նույնպես այդպես է կարծում։ Նրանք գումարում են ընդհանրական ժողով, որը միահամուռ հավանություն է տալիս հայերենի այբուբեն ստեղծելու նրանց ծրագրին։ Քաջալերելով նրանց ծրագիրը՝ Վռամշապուհ թագավորը ասում է, որ Դանիել անունով մի ասորի եպիսկոպոս «հանկարծ գտել է» հայոց լեզվի նշանագրերը։ Այդ նշանագրերը հայագիտության մեջ հայտնի են Դանիելյան գրեր անունով։ Ոգևորված դրանով՝ Մաշտոցը սկսում է սովորեցնել այդ նշանագրերը հայ իշխաններին, բայց շուտով պարզվում է, որ դրանք թերի են և չեն համապատասխանում հայերենի հարուստ հնչյունային համակարգին։ Այդ պատճառով էլ նա ձեռնամուխ է լինում հայոց գրերի ստեղծմանը։"
t=text.upper()
et=len(t)
qanak=0
tar=""
tver=[]
for i in range (len(aybuben)):
    tar=aybuben[i]
    qanak=0
    for j in range(et):
        if t[j]==tar:
            qanak+=1
    print(tar,qanak,qanak*"*")        
    #tver.append(qanak)
tver.sort()
for k in tver:
    print(chr(k),k,"=",k*"!")
print(tar,tver)
    #print(tar,qanak,qanak*"*")

