import json
import math
class EE:
    def __init__(self, arg):
        self.arg = arg
    def single_trf(self):
        argument = self.arg[:]      
        IP1 = 0            #float(argument[4])*float(argument[1])
        IP2 = float(argument[10])*float(argument[1])
        IP3 = float(argument[16])*float(argument[1])
        IP4 = float(argument[22])*float(argument[1])
        IP5 = float(argument[28])*float(argument[1])
        OP1 = 0               #float(argument[7])*float(argument[1])
        OP2 = float(argument[13])*float(argument[1])
        OP3 = float(argument[19])*float(argument[1])
        OP4 = float(argument[25])*float(argument[1])
        OP5 = float(argument[31])*float(argument[1])
        E1 =  0                     # (OP1/IP1)*100
        E2 = round((OP2/IP2)*100,2)
        E3 = round((OP3/IP3)*100,2)
        E4 = round((OP4/IP4)*100,2)
        E5 = round((OP5/IP5)*100,2)
        R1 = 0
        R2 = round(((float(argument[5])-float(argument[11]))/float(argument[5])*100),2)
        R3 = round(((float(argument[5])-float(argument[17]))/float(argument[5])*100),2)
        R4 = round(((float(argument[5])-float(argument[23]))/float(argument[5])*100),2)
        R5 = round(((float(argument[5])-float(argument[29]))/float(argument[5])*100),2)
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn.","Efficiency E1":"Zero at no load","Efficiency E2":str(E2)+"%","Efficiency E3":str(E3)+"%","Efficiency E4":str(E4)+"%","Efficiency E5":str(E5)+"%","Regulation R1":"zero at no load","Regulation R2":str(R2)+"%","Regulation R3":str(R3)+"%","Regulation R4":str(R4)+"%","Regulation R5":str(R5)+"%"}]}))

    def INDUCTION(self):
        argument = self.arg[0:]
        #Torque
        T1 = 9.81*0.143* abs(float(argument[4])-float(argument[5]))  
        T2 = 9.81*0.143* abs(float(argument[10])-float(argument[11]))
        T3 = 9.81*0.143* abs(float(argument[16])-float(argument[17]))
        T4 = 9.81*0.143* abs(float(argument[22])-float(argument[23]))
        T5 = 9.81*0.143* abs(float(argument[28])-float(argument[29]))
                      
        #input
        IP1 = float(argument[6]) * float(argument[1])
        IP2 = float(argument[12]) * float(argument[1])
        IP3 = float(argument[18]) * float(argument[1])
        IP4 = float(argument[24]) * float(argument[1])
        IP5 = float(argument[30]) * float(argument[1])

            #output
        OP1 = (2*math.pi*float(argument[7])*T1)/60
        OP2 = (2*math.pi*float(argument[13])*T2)/60
        OP3 = (2*math.pi*float(argument[19])*T3)/60
        OP4 = (2*math.pi*float(argument[25])*T4)/60
        OP5 = (2*math.pi*float(argument[31])*T5)/60

        #Eff
        E1 = round((OP1/IP1)*100,2)
        E2 = round((OP2/IP2)*100,2)
        E3 = round((OP3/IP3)*100,2)
        E4 = round((OP4/IP4)*100,2)
        E5 = round((OP5/IP5)*100,2)

        Ns = 1500
        slip1 = round(((Ns - float(argument[7]))/Ns)*100,2)
        slip2 = round(((Ns - float(argument[13]))/Ns)*100,2)
        slip3 = round(((Ns - float(argument[19]))/Ns)*100,2)
        slip4 = round(((Ns - float(argument[25]))/Ns)*100,2)
        slip5 = round(((Ns - float(argument[31]))/Ns)*100,2)
        print(json.dumps({"answer":[{"result":"Thus the efficiency and slip of a motor is determined by conducting test.","Efficiency E1":str(E1),"Efficiency E2":str(E2)+"%","Efficiency E3":str(E3)+"%","Efficiency E4":str(E4)+"%","Efficiency E5":str(E5)+"%","Regulation R1":str(E1),"Regulation R2":str(slip2)+"%","Regulation R3":str(slip3)+"%","Regulation R4":str(slip4)+"%","Regulation R5":str(slip5)+"%"}]}))
        
    def wattmeter(self):
        argument = self.arg[0:]
        def P1(x,y):return(x+y)
        def P2(x,y):return(x-y)
        def pi(x,y):return(math.atan(1.732*(x/y)))
        def pf(x):return(math.cos(x))*10

        PP1=P1(float(argument[4]),float(argument[6]))
        PP2=P1(float(argument[10]),float(argument[12]))
        PP3=P1(float(argument[16]),float(argument[18]))
        PP4=P1(float(argument[22]),float(argument[24]))
        PP5=P1(float(argument[28]),float(argument[30]))
        PP6=P1(float(argument[34]),float(argument[36]))
        PP7=P1(float(argument[40]),float(argument[42]))
        PM1=P2(float(argument[4]),float(argument[6]))
        PM2=P2(float(argument[10]),float(argument[12]))
        PM3=P2(float(argument[16]),float(argument[18]))
        PM4=P2(float(argument[22]),float(argument[24]))
        PM5=P2(float(argument[28]),float(argument[30]))
        PM6=P2(float(argument[34]),float(argument[36]))
        PM7=P2(float(argument[40]),float(argument[42]))
        A1=round((math.degrees(pi(PM1,PP1))),2)
        A2=round((math.degrees(pi(PM2,PP2))),2)
        A3=round((math.degrees(pi(PM3,PP3))),2)
        A4=round((math.degrees(pi(PM4,PP4))),2)
        A5=round((math.degrees(pi(PM5,PP5))),2)
        A6=round((math.degrees(pi(PM6,PP6))),2)
        A7=round((math.degrees(pi(PM7,PP7))),2)
        C1=round((math.radians(pf(A1))),3)
        C2=round((math.radians(pf(A2))),3)
        C3=round((math.radians(pf(A3))),3)
        C4=round((math.radians(pf(A4))),3)
        C5=round((math.radians(pf(A5))),3)
        C6=round((math.radians(pf(A6))),3)
        C7=round((math.radians(pf(A7))),3)
        print(json.dumps({"Mean":[{"To measure power and power factor of a 3 phase induction motor by using two wattmeters":str(),"Power (W1+W2) Watts":str(PP1)+", "+str(PP2)+
        ", "+str(PP3)+", "+str(PP4)+", "+str(PP5)+", "+str(PP6)+", "
        +str(PP7),"Power (W1-W2) Watts":str(PM1)+", "+str(PM2)+", "+str(PM3)+", "
        +str(PM4)+", "+str(PM5)+", "+str(PM6)+", "+str(PM7),"Phase angle(ϕ)":str(A1)+", "+str(A2)+", "+str(A3)+", "+str(A4)+", "+str(A5)+", "+str(A6)+", "+str(A7),"Power factor(cosϕ)":str(C1)+", "+str(C2)+", "+str(C3)+", "+str(C4)+", "+str(C5)+", "+str(C6)+", "+str(C7)}]}))

    def emf(self):
        argument = self.arg[:]
        Zs = round(float(argument[1])/float(argument[2]),2)
        Xs=round(math.sqrt((Zs**2)-(2.3**2)),2)
        IaRa = round( float(argument[14])*2.3,2)
        IaXl = round(Xs*float(argument[14]),2)
        def θ(x):return(math.degrees(math.acos(x)))
        def E(x,y):return(math.sqrt((float(argument[15])*x+IaRa)**2 +(float(argument[15])*(math.sin(math.radians(y)))+IaXl)**2))
        def LE(x,y):return(math.sqrt((float(argument[15])*x+IaRa)**2 +(float(argument[15])*(math.sin(math.radians(y)))-IaXl)**2))
        def R(x):return(x- float(argument[15]))/float(argument[15])*100
        θ1=round(θ(float(argument[16])),2)
        θ2=round(θ(float(argument[17])),2)
        θ3=round(θ(float(argument[18])),2)
        θ4=round(θ(float(argument[19])),2)
        θ5=round(θ(float(argument[20])),2)
        E1=round(E(float(argument[16]),θ1),2)
        E2=round(E(float(argument[17]),θ2),2)
        E3=round(E(float(argument[18]),θ3),2)
        E4=round(E(float(argument[19]),θ4),2)
        E5=round(E(float(argument[20]),θ5),2)
        L1=round(LE(float(argument[16]),θ1),2)
        L2=round(LE(float(argument[17]),θ2),2)
        L3=round(LE(float(argument[18]),θ3),2)
        L4=round(LE(float(argument[19]),θ4),2)
        L5=round(LE(float(argument[20]),θ5),2)
        R1=round(R(E1),2)
        R2=round(R(E2),2)
        R3=round(R(E3),2)
        R4=round(R(E4),2)
        R5=round(R(E5),2)
        R6=round(R(L1),2)
        R7=round(R(L2),2)
        R8=round(R(L3),2)
        R9=round(R(L4),2)
        R10=round(R(L5),2)

        print(json.dumps({"Mean":[{"The regulation of three phase alternator by EMF and MMF method is determined":str(),"Zs":str(Zs),"Xs":str(Xs)+"Ω","IaRa":str(IaRa),"IaXl":str(IaXl)+" Ω","θ":str(θ1)+", "+str(θ2)+", "+str(θ3)+", "+str(θ4)+", "+str(θ5),"% Lagging Ef":str(E1)+" %, "+str(E2)+" %, "+str(E3)+" %, "+str(E4)+" %, "+str(E5)+" %","Lagging Rgulation":str(R1)+", "+str(R2)+" , "+str(R3)+", "+str(R4)+" %, "+str(R5),"Leading Ef":str(L1)+" %, "+str(L2)+" %, "+str(L3)+" %, "+str(L4)+" %, "+str(L5)+" %","Leading regulation":str(R6)+", "+str(R7)+" %, "+str(R8)+", "+str(R9)+" %, "+str(R10)}]}))

