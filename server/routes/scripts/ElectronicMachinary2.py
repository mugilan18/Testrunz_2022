import json
import math
class EM2:
    def __init__(self, arg):
        self.arg = arg
        
    def NO_LOAD_AND_BLOCKED(self):
        argument = self.arg[0:]
        W11 = (float(argument[3])+float(argument[4]))*2
        W12 = (float(argument[8])+float(argument[9]))*2
        W13 = (float(argument[13])+float(argument[14]))*2
        W1 = (W11+W12+W13)/3
        W21 = (float(argument[18])+float(argument[19]))*2
        W22 = (float(argument[23])+float(argument[24]))*2
        W23 = (float(argument[28])+float(argument[29]))*2
        W2 = (W21+W22+W23)/3
        print(json.dumps({"Test":[{"The  No load test induction motor" : str(W1)}], "Test":[{"The Blocked rotor test induction motor" : str(W2)}]}))
        
    def SLIP_RING_INDUCTION_MOTOR (self):
        argument = self.arg[0:]
        def IP(x,y):return(x+y)
        def W(x,y):return(x-y)
        def T(x,y):return(9.81*x*y)
        def OP(x,y):return(6.28*x*y)/60
        def Eff(x,y):return(x/y)
        P1=round(IP(float(argument[4]),float(argument[5])),2)
        P2=round(IP(float(argument[11]),float(argument[12])),2)
        P3=round(IP(float(argument[18]),float(argument[19])),2)
        W1=round(W(float(argument[6]),float(argument[7])))
        W2=round(W(float(argument[13]),float(argument[14])))
        W3=round(W(float(argument[20]),float(argument[21])))
        T1=round(T(W1,float(argument[1])),2)
        T2=round(T(W2,float(argument[1])),2)
        T3=round(T(W3,float(argument[1])),2)
        OP1=round(OP(float(argument[8]),T1),2)
        OP2=round(OP(float(argument[15]),T2),2)
        OP3=round(OP(float(argument[22]),T3),2)
        E1=round(Eff(OP1,P1),2)
        E2=round(Eff(OP2,P2),2)
        E3=round(Eff(OP3,P3),2)
        print(json.dumps({"Mean":[{"The Slip Ring induction motor observed as" : str(),"Input power":str(P1)+", "+str(P2)+", "+str(P3),"W":str(W1)+", "+str(W2)+", "+str(W3),"Torque":str(T1)+", "+str(T2)+", "+str(T3),"Output Power":str(OP1)+", "+str(OP2)+", "+str(OP3),"Efficiency":str(E1)+" %, "+str(E2)+" %, "+str(E3)+" %"}]}))

        
    def V_AND_INVERTED_V(self):
        argument = self.arg[0:]
        
        def pf1(x,y,z):return((x*8)/(1.732*y*z*2))
        def pf2(x,y,z):return((x)/(1.732*y*z*2))
            
        # PF1=pf1(float(argument[5]),float(argument[1]),float(argument[2]))
        PF2=round(pf1(float(argument[10]),float(argument[6]),float(argument[7])),2)
        PF3=round(pf1(float(argument[15]),float(argument[11]),float(argument[12])),2)
        PF4=round(pf1(float(argument[20]),float(argument[16]),float(argument[17])),2)
        PF5=round(pf1(float(argument[25]),float(argument[21]),float(argument[22])),2)
        PF6=round(pf2(float(argument[29]),float(argument[26]),float(argument[27])),2)
        PF7=round(pf2(float(argument[34]),float(argument[31]),float(argument[32])),2)
        PF8=round(pf2(float(argument[39]),float(argument[36]),float(argument[37])),2)

        print(json.dumps({"Software":[{"The  ‘V’ AND ‘INVERTED V’ CURVES OF SYNCHRONOUS  MOTOR is completed sucessfully":str(), "Power factor":str()+", "+str(PF2)+", "+str(PF3)+", "+str(PF4)+", "+str(PF5)+", "+str(PF6)+", "+str(PF7)}]}))
        
        
    def SINGLE_PHASE_INDUCTION(self):
        argument = self.arg[0:]
        def T(x,y,z):return(9.81*x*(y-z))
        def Po(x,y):return(6.28*x*y)/60
        def PF(x,y,z):return(x/(y*z))
        def Eff(x,y):return(x/y)*100
        def slip(y):return((1500-y)/1500)
        T1=round(T(float(argument[1]),float(argument[4]),float(argument[5])),1)
        T2=round(T(float(argument[1]),float(argument[10]),float(argument[11])),1)
        T3=round(T(float(argument[1]),float(argument[16]),float(argument[17])),1)
        T4=round(T(float(argument[1]),float(argument[22]),float(argument[23])),1)
        T5=round(T(float(argument[1]),float(argument[28]),float(argument[29])),1)
        PO1=round(Po(float(argument[7]),T1),2)
        PO2=round(Po(float(argument[13]),T2),2)
        PO3=round(Po(float(argument[19]),T3),2)
        PO4=round(Po(float(argument[25]),T4),2)
        PO5=round(Po(float(argument[31]),T5),2)  
        n1=round(Eff(PO1,float(argument[6])),2)
        n2=round(Eff(PO2,float(argument[12])),2)
        n3=round(Eff(PO3,float(argument[18])),2)
        n4=round(Eff(PO4,float(argument[24])),2)
        n5=round(Eff(PO5,float(argument[30])),2)
        s1=round(slip(float(argument[7])),2)
        s2=round(slip(float(argument[13])),2)
        s3=round(slip(float(argument[19])),2)
        s4=round(slip(float(argument[25])),2)
        s5=round(slip(float(argument[31])),2)
        pf1=round(PF(PO1,float(argument[2]),float(argument[3])),3)
        pf2=round(PF(PO2,float(argument[8]),float(argument[9])),3)
        pf3=round(PF(PO3,float(argument[14]),float(argument[15])),3)
        pf4=round(PF(PO4,float(argument[20]),float(argument[21])),3)
        pf5=round(PF(PO5,float(argument[26]),float(argument[27])),3)
        print(json.dumps({"Mean":[{"The the direct load test on the given single phase induction motor and to  determine and plot its performance characteristics" : str()}] , "Mean":[{"Torque" : str(T1)+"Nm, "+str(T2)+"Nm, "+str(T3)+"Nm, "+str(T4)+"Nm, "+str(T5)+"Nm","Output Power":str(PO1)+" Watts, "+str(PO2)+" Watts, "+str(PO3)+" Watts, "+str(PO4)+" Watts, "+str(PO5)+" Watts","Efficiency":str(n1)+" %, "+str(n2)+" %, "+str(n3)+" %, "+str(n4)+" %, "
        +str(n5)+" %","Slip":str(s1)+", "+str(s2)+", "+str(s3)+", "+str(s4)+", "+str(s5),"Power factor(COS φ)":str(pf1)+", "+str(pf2)+", "+str(pf3)+", "+str(pf4)+", "+str(pf5)}]}))
        
        
    def Direct_and_Quadrature_axis(self):
        argument = self.arg[0:]
        xd1 = round(float(argument[1])/float(argument[4]),2)
        xd2 = round(float(argument[5])/float(argument[8]),2)
        xd3 = round(float(argument[9])/float(argument[12]),2)
        xq1 = round(float(argument[2])/float(argument[3]),2)
        xq2= round(float(argument[6])/float(argument[7]),2)
        xq3= round(float(argument[10])/float(argument[11]),2)
        print(json.dumps({"Mean":[{"The determine the direct axis reactance Xd and quadrature axis reactance Xq by  conducting a slip test on a salient pole synchronous machine is determined":str(),"The direct axis reactance Xd is" : str(xd1)+", "+str(xd2)+", "+str(xd3),"The Quadrature axis reactance Xq is":str(xq1)+", "+str(xq2)+", "+str(xq3)}]}))
          
    def Three_phase(self):
        argument = self.arg[0:]
        #Torque
        T1 = 9.81*((float(argument[3])-float(argument[4]))+2)*0.0986
        T2 = 9.81*((float(argument[10])-float(argument[11]))+2)*0.0986
        T3 = 9.81*((float(argument[17])-float(argument[18]))+2)*0.0986
        T4 = 9.81*((float(argument[24])-float(argument[25]))+2)*0.0986
        T5 = 9.81*((float(argument[31])-float(argument[32]))+2)*0.0986
                      
        #input
        IP1 = float(argument[5]) * float(argument[6])
        IP2 = float(argument[12]) * float(argument[13])
        IP3 = float(argument[19]) * float(argument[20])
        IP4 = float(argument[26]) * float(argument[27])
        IP5 = float(argument[33]) * float(argument[34])

            #output
        OP1 = (2*math.pi*float(argument[7])*T1)/60
        OP2 = (2*math.pi*float(argument[14])*T2)/60
        OP3 = (2*math.pi*float(argument[21])*T3)/60
        OP4 = (2*math.pi*float(argument[28])*T4)/60
        OP5 = (2*math.pi*float(argument[35])*T5)/60

        #Eff
        Eff1 = (OP1/IP1)*100
        Eff2 = (OP2/IP2)*100
        Eff3 = (OP3/IP3)*100
        Eff4 = (OP4/IP4)*100
        Eff5 = (OP5/IP5)*100
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5)/5

        Ns = 1500
        Reg1 = ((Ns - float(argument[7]))/Ns)*100
        Reg2 = ((Ns - float(argument[14]))/Ns)*100
        Reg3 = ((Ns - float(argument[21]))/Ns)*100
        Reg4 = ((Ns - float(argument[28]))/Ns)*100
        Reg5 = ((Ns - float(argument[35]))/Ns)*100
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5)/5
        print(json.dumps({"Mean":[{"The efficiency of three induction motor is" : str(Eff)}] , "Mean":[{"The Regularity is" : str(Reg)}]}))
 
    def LCT(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The LCT is completed sucessfully"}]}))
        
        
    def DM(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The DM completed sucessfully"}]}))
        
        
    def FREQUENCY_SYNTHESIZER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The FREQUENCY SYNTHESIZER is completed sucessfully"}]}))

    def ASK(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The ASK is completed sucessfully"}]}))
        
        
    def BPSK(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The BPSK completed sucessfully"}]}))
        
        
    def FSK(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The FSK is completed sucessfully"}]}))