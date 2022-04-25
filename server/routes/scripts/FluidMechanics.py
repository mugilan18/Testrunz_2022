import json
import math as m
import re

class FML:
    def __init__(self, arg):
        self.arg = arg

    def Through_Pipe(self):
        argument = self.arg[0:]
        def X(a,b):return((a-b)/100)
        d1 = float(argument[1])
        d2 = float(argument[2])
        A = float(argument[3])
        h = float(argument[4])
        Sm=float(argument[5])
        Sw=float(argument[6])
        g=float(argument[7])
        Kine=float(argument[8])
        l= float(argument[9])
        A1= int(0.785*(d1**2))
        def Hf(a):return((a*((Sm-Sw)/Sw)))
        def Q(a):return((A*h)/a*10000)
        def RE(a):return(((a*2)/(0.89))*10**6)
        X1 = X(float(argument[10]),float(argument[11]))
        X2 = X(float(argument[13]),float(argument[14]))
        X3 = X(float(argument[16]),float(argument[17]))
        Hf1=Hf(X1)
        Hf2=Hf(X2)
        Hf3=Hf(X3)
        Qact1 =round(Q(float(argument[12])),2)
        Qact2 =round(Q(float(argument[15])),2)
        Qact3 =round(Q(float(argument[18])),2)
        V1 = round((Qact1/A1),4)
        V2 = round((Qact2/A1),3)
        V3 = round((Qact3/A1),3)
        Velocity1=(V1**2)*10000
        Velocity2=(V2**2)*10000
        Velocity3=(V3**2)*10000
        F1 = round(((2*g*d1*Hf1)/(l*(Velocity1))),3)
        F2 = round(((2*g*d1*Hf2)/(l*(Velocity2))),3)
        F3 = round(((2*g*d1*Hf3)/(l*(Velocity3))),3)
        Re1= round(RE(V1),2)
        Re2=round(RE(V2),2)
        Re3=round(RE(V3),2)
        print(json.dumps({"pipe":[{"The coefficient of friction of given pipe is" : str(),"Darcy's friction factor":str(),"F1=":str(F1), "F2=":str(F2),"F3=":str(F3),"Reynold's Number(Re)":str(),"Re1=":str(Re1), "Re2=":str(Re2),"Re3=":str(Re3)}]}))

    def Venturimeter(self):
        argument = self.arg[0:]
        def H(x,y):return(x-y)*0.126
        A= round(float(argument[4])*float(argument[5]),3)
        r= float(argument[3])*0.01
        def AD(x):return((A*r)/x)/0.0001
        def TD(x):return(((A1*A2)/(m.sqrt((A1**2)-(A2**2))))*(2*(m.sqrt(19.62*x))))
        def CD(x,y):return(x/y)
        A1=round((0.785*(float(argument[1])**2))/0.0001,3)
        A2=round((0.785*(float(argument[2])**2))/0.0001,3)
        H1=round(H(float(argument[6]),float(argument[7])),3)
        H2=round(H(float(argument[9]),float(argument[10])),3)
        H3=round(H(float(argument[12]),float(argument[13])),3)
        H4=round(H(float(argument[15]),float(argument[16])),3)
        AD1=round(AD(float(argument[8])),3)
        AD2=round(AD(float(argument[11])),3)
        AD3=round(AD(float(argument[14])),3)
        AD4=round(AD(float(argument[17])),3)
        TD1= round(TD(H1),3)
        TD2= round(TD(H2),3)
        TD3= round(TD(H3),3)
        TD4= round(TD(H4),3)
        cd1= round(CD(AD1,TD1),3)
        cd2= round(CD(AD2,TD2),3)
        cd3= round(CD(AD3,TD3),3)
        cd4= round(CD(AD4,TD4),3)
        print(json.dumps({"Ven":[{"The coefficient of the discharge of given Venturi metre is determined" : str(),"Area of measuring tank(A)":str(A)+"m2","Rise of water in collecting tank(R)":str(r)+"m","Venturi Head":str(H1)+" cm of Hg, "+str(H2)+" cm of Hg, "+str(H3)+" cm of Hg, "+str(H4)+" cm of Hg","Actual discharge(Qa)":str(AD1)+" x10^-4, "+str(AD2)+" x10^-4, "+str(AD3)+" x10^-4, "+str(AD4)+" x10^-4","A1":str(A1),"A2":str(A2),"Theoritical discharge(Qth)":str(TD1)+" m3/sec, "+str(TD2)+" m3/sec, "+str(TD3)+" m3/sec, "+str(TD4)+" m3/sec","Co-efficient (Cd)":str(cd1)+", "+str(cd2)+", "+str(cd3)+", "+str(cd4)}]}))
    
    def Jet(self):
        argument = self.arg[0:]
        #print(argument)got output
        A = float(argument[3])
        h = float(argument[6])
        a= (m.pi/4)*float(argument[1])**2
        Qact1 =(A*h)/(float(argument[8]))
        Qact2 =(A*h)/(float(argument[10]))
        Qact3 =(A*h)/(float(argument[12]))
        Qact4 =(A*h)/(float(argument[14]))
        Qact5 =(A*h)/(float(argument[16]))
        V1 = Qact1/a
        V2 = Qact1/a
        V3 = Qact1/a
        V4 = Qact1/a
        V5 = Qact1/a
        F1 = 1000*a*V1**2
        F2 = 1000*a*V2**2
        F3 = 1000*a*V3**2
        F4 = 1000*a*V4**2
        F5 = 1000*a*V5**2   
        E1 = (((float(argument[9])*10**4*float(argument[4])) /(F1*float(argument[5])))*100)            
        E2 = (((float(argument[11])*10**4*float(argument[4])) /(F2*float(argument[5])))*100)
        E3 = (((float(argument[13])*10**4*float(argument[4])) /(F3*float(argument[5])))*100)
        E4 = (((float(argument[15])*10**4*float(argument[4])) /(F4*float(argument[5])))*100)
        E5 = (((float(argument[17])*10**4*float(argument[4])) /(F5*float(argument[5])))*100)
        E = (E1+E2+E3+E4+E5)/5
        print(json.dumps({"Jet":[{"The efficiency of the jet is determined by the method of impact of Jet on curved vanes is " : str(E) }]}))

    def Centrifugal(self):
        argument = self.arg[0:]
        A =float(argument[22])
        g= float(argument[23])
        E= float(argument[24])
        C= float(argument[25])
        def HS(x):
            return((x*g)/g)
        def HD(x):
            return((x*g*10)/g)
        def Q(x,y):
            return((A*x)/y)
        def TH(x,y):
            return(x+y)
        def Input(x):
            return((90000*E)/(C*x))
        def output(x,y):
            return(g*x*y)
        def eff(x,y):
            return(x/y)*100
        Hs1= HS(float(argument[2]))
        Hs2= HS(float(argument[9]))
        Hs3= HS(float(argument[16]))
        Hd1= HD(float(argument[3]))
        Hd2= HD(float(argument[10]))
        Hd3= HD(float(argument[17]))
        Q1= Q(float(argument[5]),float(argument[6]))
        Q2= Q(float(argument[12]), float(argument[13]))
        Q3= Q(float(argument[19]), float(argument[20]))
        TH1=TH(Hs1,Hd1)
        TH2= TH(Hs2,Hd2)
        TH3= TH(Hs3,Hd3)
        I1=round(Input(float(argument[7])),3)
        I2= round(Input(float(argument[14])),3)
        I3= round(Input(float(argument[21])),3)
        O1= round((output((Q1),(TH1))),4)
        O2= round((output((Q2),(TH2))),4)
        O3= round((output((Q3),(TH3))),4) 
        Eff1= round((O1/I1)*100,4)
        Eff2= round(eff(O2,I2),4)
        Eff3=round(eff(O3,I3),4)
        print(json.dumps({"Centrifugal":[{"The performance characteristics of centrifugal pump was studied and the efficiency is calculated from the graph." : str(),"Efficiency_1":str(Eff1),"Efficiency_2":str(Eff2),"Efficiency_3":str(Eff3) }]}))

    def Submersible(self):
        argument = self.arg[0:]
        #print(argument)got output
        N = float(argument[1])
        A=float(argument[2])
        EMC =float(argument[3])
        x= float(argument[4])
        Nmotor= float(argument[5])
        def Q(x):
            return((0.1098/x)*1000)
        def Input(x):
            return((17100000)/(EMC*x))
        def TH(a):return((a*10)+x)
        def output(x,y):
            return(9810*x*y)/1000
        def Eff(x,y):return(x/y)*100
        H1 = TH(float(argument[6]))
        H2= TH(float(argument[10]))
        H3= TH(float(argument[14]))
        H4= TH(float(argument[18]))

        Qact1 =round(Q(float(argument[8])),2)
        Qact2 =round(Q(float(argument[12])),2)
        Qact3 =round(Q(float(argument[16])),2)
        Qact4=round(Q(float(argument[20])),2)
        I1 = round(Input(float(argument[9])),2)
        I2 = round(Input(float(argument[13])),2)
        I3 = round(Input(float(argument[17])),2)
        I4 = round(Input(float(argument[21])),2)
        O1=round(output(Qact1,H1),2)
        O2=round(output(Qact2,H2),2)
        O3=round(output(Qact3,H3),2)
        O4=round(output(Qact4,H4),2)
        E1=round(Eff(O1,I1),2)
        E2=round(Eff(O2,I2),2)
        E3=round(Eff(O3,I3),2)
        E4=round(Eff(O4,I4),2)

        print(json.dumps({"Submersible":[{"The efficiency of the Submersible is " : str(),"Efficiency of the pump(ηmotor)_1":str(E1)+"%","Efficiency of the pump(ηmotor)_2":str(E2)+"%","Efficiency of the pump(ηmotor)_3":str(E3)+"%" }]}))

    def Test_Reciprocating(self):
        argument = self.arg[0:]
        Z =float(argument[1])
        A= float(argument[2])
        h =float(argument[3])
        Nc=float(argument[4])
        K= float(argument[5])
        Sg=float(argument[6])
        g=float(argument[7])
        def suction(x):
            return((x*13.6-1)/1000)
        def delivery(y):
            return((y*10**4)/10000)
        def TH(x,y):return(x+y+Z)
        def discharge(x):
            return(A*h)/x
        def input(x):
            return(Nc*3600*1000)/(x*K)
        def output(x,y):
            return(Sg*g*x*y)*10
        def E(x,y):return(x/y)*100
        Hs1= suction(float(argument[8]))
        Hs2= suction(float(argument[13]))
        Hs3= suction(float(argument[18]))
        Hd1= delivery(float(argument[9]))
        Hd2= delivery(float(argument[14]))
        Hd3= delivery(float(argument[19]))
        H1=round(TH(Hs1,Hd1),2)
        H2=round(TH(Hs2,Hd2),2)
        H3=round(TH(Hs3,Hd3),2)
        Qact1 = round(discharge(float(argument[11])),7)
        Qact2=round(discharge(float(argument[16])),7)
        Qact3= round(discharge(float(argument[21])),7)
        
        I1=round(input(float(argument[12])),2)
        I2=round(input(float(argument[17])),2)
        I3=round(input(float(argument[22])),2)
        O1= round(output(H1,Qact1),2)
        O2= round(output(H2,Qact2),2)
        O3= round(output(H3,Qact3),2)
        Eff1= round(E(O1,I1),3)
        Eff2= round(E(O2,I2),3)
        Eff3= round(E(O3,I3),3)
        print(json.dumps({"RP":[{"Thus the performance characteristics of the reciprocating pump was studied, the maximum h is calculated from the graph":str(),"Efficiency of reciprocting_1":str(Eff1)+"%","Efficiency of reciprocting_2":str(Eff2)+"%","Efficiency of reciprocting_3":str(Eff3)+"%"}]}))
        
        

    def Orifice(self):
        argument = self.arg[0:]
        A= float(argument[1])
        g=float(argument[2])
        d=float(argument[3])
        D= float(argument[4])
        def H(x):
            return(12600*x*10**-3)/1000
        def Hg(x,y):
            return(x-y)
        def act(a):
            return(((A*1000)/(1000*a)))
        a1=round(0.785*(D**2)/100,2)
        a2=round(0.785*(d**2)/100,2)
        Hg1=Hg(float(argument[7]), float(argument[8]))
        Hg2=Hg(float(argument[11]), float(argument[12]))
        Hg3=Hg(float(argument[15]),float(argument[16]))   
        h1=round(H (Hg1),2)
        h2=round(H (Hg2),2)
        h3=round(H (Hg3),2)
        X1= a1*(m.sqrt(2*g*h1))  
        Y1= m.sqrt(((a1**2)-(a2**2)))
        X2= a1*(m.sqrt(2*g*h2))
        X3= a1*(m.sqrt(2*g*h3))
        Qth1=round(X1/Y1,3)
        Qth2=round(X2/Y1,3)
        Qth3= round(X3/Y1,3)
        Qact1=round(act(float(argument[6])/1000),3)
        Qact2=round(act(float(argument[10]))*1000,6)
        Qact3=round(act(float(argument[14]))/100 ,6) 
        Ce1=round((Qact1/Qth1),2)
        Ce2=round((Qact2/Qth2),2)
        Ce3=round((Qact3/Qth3),6)
        print(json.dumps({"Orifice":[{"Theoritical discharge Qth1" : str(Qth1)+"X10^-4 m3/sec","Theoritical discharge Qth2" : str(Qth2)+"X10^-4 m3/sec","Theoritical discharge Qth3" : str(Qth3)+"X10^-4 m3/sec","Actual discharge Qact1":str(Qact1)+"X10^-4 m3/sec","Actual discharge Qact2":str(Qact2)+"X10^-4 m3/sec","Actual discharge Qact3":str(Qact3)+"X10^-4 m3/sec","Co-efficient of discharge Cd_1":str(Ce1)+"X10^-4","Co-efficient of discharge Cd_2":str(Ce2)+"X10^-4","Co-efficient of discharge Cd_3":str(Ce3)+"X10^-4"}]}))

    
    def Minor_Loss(self):
        argument = self.arg[0:]
        dp=float(argument[1])
        de=float(argument[2])
        db= float(argument[3])
        
        def Q(x):
            return((A*0.1)/x)
        def he():
            return(0.5*(VE1**2))/2*Sm
        A=(1.785*d1)
        #print(json.dumps({"MO":[{"Loss of head due to expansion " : str(K) }]}))
        
        td1 = float(argument[5])
        td2 = float(argument[6])
        th = float(argument[7])
        tA = float(argument[8])
        ta1= (m.pi/4)*td1**2
        ta2= (m.pi/4)*td2**2
        tH1 = float(argument[26])- float(argument[27])
        tH2 = float(argument[29])- float(argument[30])
        tH3 = float(argument[32])- float(argument[33])
        tH4 = float(argument[35])- float(argument[36])
        tQact1 =(tA*th)/(2*float(argument[28]))
        tQact2 =(tA*th)/(2*float(argument[31]))
        tQact3 =(tA*th)/(2*float(argument[34]))
        tQact4 =(tA*th)/(2*float(argument[37]))
        tV11 = (tQact1/ta1)
        tV12 = (tQact2/ta1)
        tV13 = (tQact3/ta1)
        tV14 = (tQact4/ta1)
        tV21 = (tQact1/ta2)
        tV22 = (tQact2/ta2)
        tV23 = (tQact3/ta2)
        tV24 = (tQact4/ta2)
        tK = (((2*9.81*tH1*10**-2)/(tV11-tV21)**2)+((2*9.81*tH2*10**-2)/(tV12-tV22)**2)+((2*9.81*tH3*10**-2)/(tV13-tV23)**2)+((2*9.81*tH4*10**-2)/(tV14-tV24)**2))/4
        #print(json.dumps({"ML":[{"Loss of head due to Contraction " : str(tK) }]}))
#3
        Td1 = float(argument[9])
        TA = float(argument[12])
        Th = float(argument[11])
        Ta1= (m.pi/4)*Td1**2
        TH1 = float(argument[38])- float(argument[39])
        TH2 = float(argument[41])- float(argument[42])
        TH3 = float(argument[44])- float(argument[45])
        TH4 = float(argument[47])- float(argument[48])
        TQact1 =(TA*Th)/(2*float(argument[40]))
        TQact2 =(TA*Th)/(2*float(argument[43]))
        TQact3 =(TA*Th)/(2*float(argument[46]))
        TQact4 =(TA*Th)/(2*float(argument[49]))
        TV11 = (TQact1/Ta1)
        TV12 = (TQact2/Ta1)
        TV13 = (TQact3/Ta1)
        TV14 = (TQact4/Ta1)
        TK = (((2*9.81*TH1*10**-2)/(TV11)**2)+((2*9.81*TH2*10**-2)/(TV12)**2)+((2*9.81*TH3*10**-2)/(TV13)**2)+((2*9.81*TH4*10**-2)/(TV14)**2))/4
        #print(json.dumps({"MH":[{"Loss of head due to elbow " : str(TK) }]}))
#4
        T1d1 = float(argument[13])
        T1A = float(argument[16])
        T1h = float(argument[15])
        T1a1= (m.pi/4)*T1d1**2
        T1H1 = float(argument[50])- float(argument[51])
        T1H2 = float(argument[53])- float(argument[51])
        T1H3 = float(argument[56])- float(argument[57])
        T1Qact1 =(T1A*T1h)/(2*float(argument[52]))
        T1Qact2 =(T1A*T1h)/(2*float(argument[55]))
        T1Qact3 =(T1A*T1h)/(2*float(argument[58]))
        T1V11 = (T1Qact1/T1a1)
        T1V12 = (T1Qact2/T1a1)
        T1V13 = (T1Qact3/T1a1)
        T1K = (((2*9.81*T1H1*10**-2)/(T1V11)**2)+((2*9.81*T1H2*10**-2)/(T1V12)**2)+((2*9.81*T1H3*10**-2)/(T1V13)**2))/3
        #print(json.dumps({"MD":[{"Loss due to bend " : str(T1K) }]}))
        print(json.dumps({"length":[{"Loss of head due to expansion " : str(K),"Loss of head due to Contraction " : str(tK)}], "breadth":[{"Loss of head due to elbow " : str(TK), "Loss due to bend " : str(T1K) }] }))

    def pelton(self):
        argument = self.arg[0:]
        def P(x,y):return(x-y)
        def Q(x):return(3.251*(m.sqrt(x*10)))
        def IP(x,y):return(9.81*x*y)/100
        def OP(x):return(7084.782*x)/60000
        def E(x,y):return(x/y)*100
        h1=round(P(float(argument[3]),float(argument[4])),2)
        h2=round(P(float(argument[9]),float(argument[10])),2)
        h3=round(P(float(argument[15]),float(argument[16])),2)
        h4=round(P(float(argument[21]),float(argument[22])),2)
        h5=round(P(float(argument[27]),float(argument[28])),2)
        T1=round(P(float(argument[5]),float(argument[6])),2)
        T2=round(P(float(argument[11]),float(argument[12])),2)
        T3=round(P(float(argument[17]),float(argument[18])),2)
        T4=round(P(float(argument[23]),float(argument[24])),2)
        T5=round(P(float(argument[29]),float(argument[30])),2)
        q1=round(Q(h1),2)
        q2=round(Q(h2),2)
        q3=round(Q(h3),2)
        q4=round(Q(h4),2)
        q5=round(Q(h5),2)
        IP1=round(IP(q1,float(argument[2])),3)
        IP2=round(IP(q2,float(argument[8])),3)
        IP3=round(IP(q3,float(argument[14])),3)
        IP4=round(IP(q4,float(argument[20])),3)
        IP5=round(IP(q5,float(argument[26])),3)
        OP1=round(OP(T1),3)
        OP2=round(OP(T2),3)
        OP3=round(OP(T3),3)
        OP4=round(OP(T4),3)
        OP5=round(OP(T5),3)
        E1=round(E(OP1,IP1),3)
        E2=round(E(OP2,IP2),3)
        E3=round(E(OP3,IP3),3)
        E4=round(E(OP4,IP4),3)
        E5=round(E(OP5,IP5),3)
        print(json.dumps({"Software":[{"Conduct the load test on the given Pelton wheel turbine by keeping constant gate opening and variable speed and to draw the characteristics curve":str(),"Pressure gauge reading(h)":str(h1)+", "+str(h2)+", "+str(h3)+", "+str(h4)+", "+str(h5),"Net break weight(W)":str(T1)+", "+str(T2)+", "+str(T3)+", "+str(T4)+", "+str(T5),"Discharge (Q) m3/sec":str(q1)+", "+str(q2)+", "+str(q3)+", "+str(q4)+", "+str(q5),"Input power":str(IP1)+", "+str(IP2)+", "+str(IP3)+", "+str(IP4)+", "+str(IP5),"Output power":str(OP1)+", "+str(OP2)+", "+str(OP3)+", "+str(OP4)+", "+str(OP5),"Efficiency":str(E1)+"%, "+str(E2)+"%, "+str(E3)+"%, "+str(E4)+"%, "+str(E5)+"%"}]}))
    def Reciprocating(self):
        argument = self.arg[0:]
        def TH(x,y):return(x+y)
        def Q(x,y):return((x*5)/y)/100
        def IP(x):return(5.625/x)
        def OP(X,Y):return(9.81*X*Y)/10000
        def E(x,y):return(y/x)*100
        hs1=float(argument[2])*0.0126
        hs2=float(argument[7])*0.0126
        hs3=float(argument[12])*0.0126
        hs4=float(argument[17])*0.0126
        hd1=float(argument[3])*10
        hd2=float(argument[8])*10
        hd3=float(argument[13])*10
        hd4=float(argument[18])*10
        TH1=round(TH(hs1,hd1),2)
        TH2=round(TH(hs2,hd2),2)
        TH3=round(TH(hs3,hd3),2)
        TH4=round(TH(hs4,hd4),2)
        Q1=round(Q(float(argument[1]),float(argument[4])),3)
        Q2=round(Q(float(argument[6]),float(argument[9])),3)
        Q3=round(Q(float(argument[11]),float(argument[14])),3)
        Q4=round(Q(float(argument[16]),float(argument[19])),3)
        IP1=round(IP(float(argument[5])),3)
        IP2=round(IP(float(argument[10])),3)
        IP3=round(IP(float(argument[15])),3)
        IP4=round(IP(float(argument[20])),3)
        OP1=round(OP(TH1,Q1),3)
        OP2=round(OP(TH2,Q2),3)
        OP3=round(OP(TH3,Q3),3)
        OP4=round(OP(TH4,Q4),3)
        E1=round(E(IP1,OP1),3)
        E2=round(E(IP2,OP2),3)
        E3=round(E(IP3,OP3),3)
        E4=round(E(IP4,OP4),3)
        print(json.dumps({"Software":[{"Studied the characteristics of the reciprocating pump and determine the efficiency of the pump":str(),"Total head":str(TH1)+", "+str(TH2)+", "+str(TH3)+", "+str(TH4),"Discharge in Kg Km2 x 10^-4":str(Q1)+" X 10^4, "+str(Q2)+" X 10^4"+str(Q3)+" X 10^4"+str(Q4)+" x10^-4","Input power":
        str(IP1)+", "+str(IP2)+", "+str(IP3)+", "+str(IP4),"Output Power":str(OP1)+", "+str(OP2)+", "+str(OP3)+", "+str(OP4),"Efficiency":str(E1)+" %, "+str(E2)+" %, "+str(E3)+" %, "+str(E4)+" %"}]}))