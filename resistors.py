def getNumber(n):
    number = n[0]
    i=1
    while n[i]>="." and n[i]<="9":
        if n[i]!=".":
            number = number+n[i]
        i+=1
    return number

def getNumberWithPoint(n):
    number = n[0]
    i=1
    while n[i]>="." and n[i]<="9":
        number = number+n[i]
        i+=1
    return number

def unit_measurement(r):
    i=0
    while i < len(r):
        if r[i]=="m":
            return 10**-3
        elif r[i]=="-":
            return 1
        elif r[i]=="K":
            return 10**3
        elif r[i]=="M":
            return 10**6
        elif r[i]=="G":
            return 10**9
        i+=1
        
def getTolerance(r):
    i=0
    while True:
        if r[i] == " ":
            space = i+1
            break
        i+=1
    t = r[space]
    space+=1
    while space < len(r):
        t = t+r[space]
        space+=1
    return float(t)
        
def signficantFigures(n):
    if n=="0":
        return "Preta"
    elif n=="1":
        return "Marrom"
    elif n=="2":
        return "Vermelha"
    elif n=="3":
        return "Laranja"
    elif n=="4":
        return "Amarela"
    elif n=="5":
        return "Verde"
    elif n=="6":
        return "Azul"
    elif n=="7":
        return "Violeta"
    elif n=="8":
        return "Cinza"
    else:
        return "Branca"

'''def multiply(tam):
    if tam==-3:
        return "Rosa"
    elif tam==-2:
        return "Prata"
    elif tam==-1:
        return "Dourada"
    elif tam==1:
        return "Preta"
    elif tam==2:
        return "Vermelha"
    elif tam==3:
        return "Laranja"
    elif tam==4:
        return "Amarela"
    elif tam==5:
        return "Verde"
    elif tam==6:
        return "Azul"
    elif tam==7:
        return "Violeta"
    elif tam==8:
        return "Cinza"
    elif tam==9:
        return "Branca"'''

def multiply(x,y):
    y=float(y)
    x=float(x)
    if y==round(x*10**-3,10):
        return "Rosa"
    elif y==round(x*10**-2,10):
        return "Prata"
    elif y==round(x*10**-1,10):
        return "Dourada"
    elif y==round(x*10**0,10):
        return "Preta"
    elif y==round(x*10,10):
        return "Marrom"    
    elif y==round(x*10**2,10):
        return "Vermelha"
    elif y==round(x*10**3,10):
        return "Laranja"
    elif y==round(x*10**4,10):
        return "Amarela"
    elif y==round(x*10**5,10):
        return "Verde"
    elif y==round(x*10**6,10):
        return "Azul"
    elif y==round(x*10**7,10):
        return "Violeta"
    elif y==round(x*10**8,10):
        return "Cinza"
    elif y==round(x*10**9,10):
        return "Branca"

def toleranceColor(n):
    if n==20:
        return "Nenhuma"
    elif n==10:
        return "Prata"
    elif n==5:
        return "Dourada"
    elif n==1:
        return "Marrom"
    elif n==2:
        return "Vermelha"
    elif n==0.05:
        return "Laranja"
    elif n==0.02:
        return "Amarela"
    elif n==0.5:
        return "Verde"
    elif n==0.25:
        return "Azul"
    elif n==0.1:
        return "Violeta"
    elif n==0.01:
        return "Cinza"

def devideByTen(n):
    n = str(round(float(n)/10))
    return n

def IEC60062(r):
    codeColors = []
    resistor_value = getNumber(r) #tipo string
    unit = unit_measurement(r) #tipo float
    tolerance_value = getTolerance(r) #tipo float
    past_value_ohms = "False"
    i=0
    
    if float(resistor_value)<10:
        past_value_ohms=resistor_value
        resistor_value = str(int(resistor_value)*10)
        value_ohms=resistor_value
    else:
        if(unit<1):
            value_ohms = str(round(float(getNumberWithPoint(r)) * unit,4)) #transforma o valor do resistor para Ohms
        else:
            if unit!=1:
                value_ohms = str(round(float(getNumberWithPoint(r)) * unit))
            else:
                past_value_ohms = str(round(float(getNumberWithPoint(r)),4))
                value_ohms = str(round(int(getNumber(r)) * unit))
    
    if unit!=1:
        while i < len(resistor_value):
            #if resistor_value!=".":
            codeColors.append(signficantFigures(resistor_value[i]))
            i+=1
    else:
        i=0
        while i<3 and  i<len(value_ohms):
            codeColors.append(signficantFigures(value_ohms[i]))
            i+=1

    while len(resistor_value) > 3:
        resistor_value = devideByTen(resistor_value)
    
    if past_value_ohms=="False":
        codeColors.append(multiply(resistor_value, value_ohms))
    else:
        codeColors.append(multiply(resistor_value, past_value_ohms))
    
    codeColors.append(toleranceColor(tolerance_value))
    
    '''print(f"Unidade: {unit}")
    print(f"Resistor: {resistor_value}")
    print(f"Tolerancia: {tolerance_value}")
    print(f"Resistor (Ohms): {value_ohms}")'''
    return codeColors

print(IEC60062('22000000- 5'))
print(IEC60062('1- 10'))
print(IEC60062('2.70M- 0.01'))
print(IEC60062('130M 0.02'))
print(IEC60062('2.26K 0.05'))
print(IEC60062('2.7M 1'))
print(IEC60062('2260- 0.02'))