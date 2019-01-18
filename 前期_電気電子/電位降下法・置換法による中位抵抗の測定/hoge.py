for i in range(12):
    print("="+"D"+str(i+2)+"-f2")

"""
I:"B"+str(i+2)
V:"C"+str(i+2)
R:"D"+str(i+2)
    "="+"C"+str(i+2)+"/B"+str(i+2)
rv:"E2"
ra:"F2"
Rxa:"G"+str(i+2)
Rxb:"G"+str(i+2)
R-Rx':"I"+str(i+2)
    "=D"+str(i+2)+"-G"+str(i+2)
ε:"J"+str(i+2)
    "=ROUND("+"I"+str(i+2)+"/"+"G"+str(i+2)+"*100,-INT(LOG10("+"I"+str(i+2)+"/"+"G"+str(i+2)+"*100"+"))+2)"
"""

# "=ROUND(C"+str(i+2)+"/((B"+str(i+2)+"*10^3)-(C"+str(i+2)+"/E2)),-INT(LOG10(C"+str(i+2)+"/((B"+str(i+2)+"*10^3)-(C"+str(i+2)+"/E2))))+2)"

# "C"+str(i+2)+"/((B"+str(i+2)+"*10^3)-(C"+str(i+2)+"/E2))"

# # V/(I*10^3-(V/rv))