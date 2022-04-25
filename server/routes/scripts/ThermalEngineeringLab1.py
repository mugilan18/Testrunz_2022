import json
import math

class TE1:
    def __init__(self, arg):
        self.arg = arg
    def REDWOOD(self):
        argument = self.arg[0:]
        A = float(argument[1])
        B = float(argument[2])
        pr=float(argument[3])
        V1 = (A*float(argument[5])) +(B/ float(argument[5]))
        V2 = (A*float(argument[7])) +(B/ float(argument[7]))
        V3 = (A*float(argument[9])) +(B/ float(argument[9]))
        V4 = (A*float(argument[11])) +(B/ float(argument[11]))
        V5 = (A*float(argument[13])) +(B/ float(argument[13]))
        V = (V1+V2+V3+V4+V5)/5
        U1 = (float(argument[15])*pr)
        U2 = (float(argument[17])*pr)
        U3 = (float(argument[19])*pr)
        U4 = (float(argument[21])*pr)
        U5 = (float(argument[23])*pr)
        U = (U1+U2+U3+U4+U5)/5
        print(json.dumps({"ans":[{"Result":"Thus dynamic and kinematic viscosity at given oil at different temperature were determined."}],"Normality":[{"Kinematic viscosity" : str(V)+ " Ns/m2"}], "Nrmality":[{"Absolute Viscosity" : str(U) + " Ns/m2"}]}))
    def CLEVELAND(self):
        argument = self.arg[0:]
        O = str(argument[1])
        F = float(argument[2])
        P =float(argument[3])
        #print(argument)
        print(json.dumps({"answer":[{"Result":"Thus the sample flask & fire point is determined"}], "Normality":[{"Oil sample" : str(O)}], "mality":[{"Flash Point" : str(F)}],"lity":[{"Fire Point" : str(P)}]}))
    def Fire_Point(self):
        argument = self.arg[0:]
        A = float(argument[1])
        B = float(argument[2])
        c =float(argument[3])
        print(json.dumps({"Normality":[{"Oil Sample" : str(A)}], "bnormality":[{"Flash Point" : str(B)}], "Amount":[{"Fire Point":str(C)}]}))

    def Junkers(self):
        argument = self.arg[0:]
        Mw =float(argument[1])
        Cpw=float(argument[2])
        T1 =float(argument[3])
        T2 =float(argument[4])
        Vg =float(argument[5])
        Hcv = (Mw*Cpw*(T2-T1))/Vg
        print(json.dumps({"Normality":[{"Thus the calorific value of fuel was determined by using the junker calorimeter. Thus the value is" : str(Hcv)}]}))

    def BOMB(self):
        argument = self.arg[0:]
        T1 =float(argument[1])
        T2 =float(argument[2])
        Ot = T2-T1
        Maxt=float(argument[3])
        Mint=float(argument[4])
        T=float(argument[5])
        R=(Maxt-Mint)/T
        Tm=float(argument[6])
        C=(R/2)*Tm
        #Rt=float(argument[7])
        dt=Ot+C
        mf=float(argument[7])
        Mw=2
        Cpw=4.18
        Mc=0.69
        Hcv=(Mw+Mc)*Cpw*(dt/mf)
        print(json.dumps({"Normality":[{"Thus the calorific value of fuel was determined by using the bomb calorimeter. Thus the value is" : str(Hcv)}]}))
    def COMPRESSOR(self):
        argument = self.arg[0:]
        h1=(1000/1.165)*(float(argument[2])-float(argument[3]))
        h2=(1000/1.165)*(float(argument[10])-float(argument[11]))
        h3=(1000/1.165)*(float(argument[18])-float(argument[19]))
        h4=(1000/1.165)*(float(argument[26])-float(argument[27]))
        #Actual discharge
        h=(h1+h2+h3+h4)/4
        cd=0.68
        d0=12*10**-3
        a0=math.pi*(d0**2)
        Vc= cd*a0*math.sqrt(2*9.81*h)
        D=79*10**-3
        A=math.pi*(D**2)
        L=80*10**-3
        N=(float(argument[6])+float(argument[14])+float(argument[22])+float(argument[30]))/4
        #theoratical disacharge
        Vt= (A*L*N)/60
        Vc=0.035
        E=Vc/Vt
        #input power
        I=(3600/180)*(5/300)
        pc=1.165
        p0=8621
        O=(pc*Vc*p0*9.81)/1000
        F=O/I
        print(json.dumps({"Amount":[{"Result":"Thus the performace test on reciprocating air compressor is conducted and the graph is drawn."}],"Normality":[{"Vact" : str(Vc)}], "Nrmality":[{"Vtheo" : str(Vt)}], "mality":[{"Volumetric efficiency" : str(E)}], "lity":[{"Efficiency" : str(F)}]}))
    def NATURAL(self):
        argument = self.arg[0:]
        Qs1 = (float(argument[1])) *(float(argument[2]))
        Qs2 = (float(argument[9])) *(float(argument[10]))
        Qs3 = (float(argument[17])) *(float(argument[18]))
        Qs4 = (float(argument[25])) *(float(argument[26]))
        Qs5 = (float(argument[33])) *(float(argument[34]))
        Ts1 =(float(argument[3])+float(argument[4])+float(argument[5])+float(argument[6])+float(argument[7])+float(argument[8]))/6
        Ts2 =(float(argument[11])+float(argument[12])+float(argument[13])+float(argument[14])+float(argument[15])+float(argument[16]))/6
        Ts3 =(float(argument[19])+float(argument[20])+float(argument[21])+float(argument[22])+float(argument[23])+float(argument[24]))/6
        Ts4 =(float(argument[27])+float(argument[28])+float(argument[29])+float(argument[30])+float(argument[31])+float(argument[32]))/6
        Ts5 =(float(argument[35])+float(argument[36])+float(argument[37])+float(argument[38])+float(argument[39])+float(argument[40]))/6
        D = 0.038
        L = 0.8
        As = math.pi*D**2*L
        Ta = 30
        T1 = Ts1 - Ta
        T2 = Ts2 - Ta
        T3 = Ts3 - Ta
        T4 = Ts4 - Ta
        T5 = Ts5 - Ta
        T =(T1+T2+T3+T4+T5)/5
        H1 = Qs1/(As*T1)
        H2 = Qs2/(As*T2)
        H3 = Qs3/(As*T3)
        H4 = Qs4/(As*T4)
        H5 = Qs5/(As*T5)
        H = (H1+H2+H3+H4+H5)/5
        Tf1 = (Ts1+Ta)/2
        Tf2 = (Ts2+Ta)/2
        Tf3 = (Ts3+Ta)/2
        Tf4 = (Ts4+Ta)/2
        Tf5 = (Ts5+Ta)/2
        B1 = 1/(Tf1+273)
        B2 = 1/(Tf2+273)
        B3 = 1/(Tf3+273)
        B4 = 1/(Tf4+273)
        B5 = 1/(Tf5+273)
        B = (B1+B2+B3+B4+B5)/5
        g = 9.81
        Gama = 16.96*10**-6
        G =(g*L**3*B*T)/Gama**2
        Cp = 1005
        U=19.26*10**-6
        K = 0.02756
        Pr = (Cp*U)/K
        Nu = (0.59*(Pr)**0.25)
        Htheo = (Nu*K)/L
        print(json.dumps({"Amount":[{"Result":"The surface heat transfer wett of a vertical tube losing water by natural convection is"}],"Normality":[{"Experimental effeiciency" : str(Nu)}], "Nrmality":[{"Theoratical efficiency" : str(Htheo)}]}))
    def Forced(self):
        argument = self.arg[0:]
        Qs1 = (float(argument[1])) *(float(argument[2]))
        Qs2 = (float(argument[10])) *(float(argument[11]))
        Qs3 = (float(argument[19])) *(float(argument[20]))
        Qs4 = (float(argument[28])) *(float(argument[29]))
        Qs5 = (float(argument[37])) *(float(argument[38]))
        Ts1 =(float(argument[5])+float(argument[6])+float(argument[7])+float(argument[8])+float(argument[9]))/5
        Ts2 =(float(argument[14])+float(argument[15])+float(argument[16])+float(argument[17])+float(argument[18]))/5
        Ts3 =(float(argument[23])+float(argument[24])+float(argument[25])+float(argument[26])+float(argument[27]))/5
        Ts4 =(float(argument[32])+float(argument[33])+float(argument[34])+float(argument[35])+float(argument[36]))/5
        Ts5 =(float(argument[41])+float(argument[42])+float(argument[43])+float(argument[44])+float(argument[45]))/5
        D = 50*10**-3
        L= 400*10**-3
        As = math.pi*D**2*L
        Ta = 32
        T1 = Ts1 - Ta
        T2 = Ts2 - Ta
        T3 = Ts3 - Ta
        T4 = Ts4 - Ta
        T5 = Ts5 - Ta
        T =(T1+T2+T3+T4+T5)/5
        H1 = Qs1/(As*T1)
        H2 = Qs2/(As*T2)
        H3 = Qs3/(As*T3)
        H4 = Qs4/(As*T4)
        H5 = Qs5/(As*T5)
        H = (H1+H2+H3+H4+H5)/5
        d0=10*10**-3
        A0=(math.pi/4)*d0**2
        h1 = (float(argument[3])) -(float(argument[4]))
        h2 = (float(argument[12])) -(float(argument[13]))
        h3 = (float(argument[21])) -(float(argument[22]))
        h4 = (float(argument[30])) -(float(argument[31]))
        h5 = (float(argument[39])) -(float(argument[40]))
        h = (h1+h2+h3+h4+h5)/5
        Q=0.68*A0*(math.sqrt(2*9.81*h*(1000/1.16)))
        A=(math.pi/4)*D**2
        V=Q/A
        Re =2208.13
        pr = 0.69
        Nu=0.023*(Re**0.8)*(pr**0.3)
        K = 0.02756
        Etheo =(Nu*K)/D
        print(json.dumps({"Amount":[{"Result":"Thus the heat transfer wett by forced convertioon was determined by using fourced convection apparatus"}],"Normality":[{"Experimental effeiciency" : str(Nu)}], "Nrmality":[{"Theoratical efficiency" : str(Etheo)}]}))
    def Pin_Fin(self):
        argument = self.arg[0:]
        Qs1 = (float(argument[1])) *(float(argument[2]))
        Qs2 = (float(argument[10])) *(float(argument[11]))
        Qs3 = (float(argument[19])) *(float(argument[20]))
        Qs4 = (float(argument[28])) *(float(argument[29]))
        Qs5 = (float(argument[37])) *(float(argument[38]))
        Qact =(Qs1+Qs2+Qs3+Qs4+Qs5)/5
        Ts1 =(float(argument[5])+float(argument[6])+float(argument[7])+float(argument[8]))/4
        Ts2 =(float(argument[14])+float(argument[15])+float(argument[16])+float(argument[17]))/4
        Ts3 =(float(argument[23])+float(argument[24])+float(argument[25])+float(argument[26]))/4
        Ts4 =(float(argument[32])+float(argument[33])+float(argument[34])+float(argument[35]))/4
        Ts5 =(float(argument[41])+float(argument[42])+float(argument[43])+float(argument[44]))/4
        Ts=(Ts1+Ts2+Ts3+Ts4+Ts5)/5
        As = math.pi*D**2*L
        Ta = 32
        T1 = Ts1 - Ta
        T2 = Ts2 - Ta
        T3 = Ts3 - Ta
        T4 = Ts4 - Ta
        T5 = Ts5 - Ta
        T =(T1+T2+T3+T4+T5)/5
        H1 = Qs1/(As*T1)
        H2 = Qs2/(As*T2)
        H3 = Qs3/(As*T3)
        H4 = Qs4/(As*T4)
        H5 = Qs5/(As*T5)
        H = (H1+H2+H3+H4+H5)/5
        Tf =(Ts+Ta)/2
        A0=(math.pi/4)*d0**2
        h1 = (float(argument[3])) -(float(argument[4]))
        h2 = (float(argument[12])) -(float(argument[13]))
        h3 = (float(argument[21])) -(float(argument[22]))
        h4 = (float(argument[30])) -(float(argument[31]))
        h5 = (float(argument[39])) -(float(argument[40]))
        h = (h1+h2+h3+h4+h5)/5
        Q=Cd*A0*(math.sqrt*2*g*h*(pw/pe))
        A=(math.pi/4)*D**2
        V=Q/A
        Re = (V*d0)/Gama
        Nu=0.023*(Re**0.8)*(Pr**0.3)
        Etheo =(Nu*K)/d0
        print(json.dumps({"Amount":[{"Result:The experiment was conducted & the result were found as pin fin efficiency"}],"Normality":[{"Experimental effeiciency" : str(Nu)}], "Nrmality":[{"Theoratical efficiency" : str(Etheo)}]}))


