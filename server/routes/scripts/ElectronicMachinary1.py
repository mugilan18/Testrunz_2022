import json
import math
class EM1:
    def __init__(self, arg):
        self.arg = arg
    def DC_SHUNT_MOTOR(self):
        argument = self.arg[:]
        def S(X,Y):return(Y-X)
        def Torque(x):return(x*1.015)
        def output(x,y):return((6.28*x*y)/60)
        def Input(x,y):return(x*y)
        def Reg(x,y):return(x/y)*100
        S1=S(float(argument[3]),float(argument[4]))
        S2=S(float(argument[8]),float(argument[9]))
        S3=S(float(argument[13]),float(argument[14]))
        S4=S(float(argument[18]),float(argument[19]))
        S5=S(float(argument[23]),float(argument[24]))
        T1=round(Torque(S1),2)
        T2=round(Torque(S2),2)
        T3=round(Torque(S3),2)
        T4=round(Torque(S4),2)
        T5=round(Torque(S5),2)
        IP1=round(Input(float(argument[1]),float(argument[2])),2)
        IP2=round(Input(float(argument[6]),float(argument[7])),2)
        IP3=round(Input(float(argument[11]),float(argument[12])),2)
        IP4=round(Input(float(argument[16]),float(argument[17])),2)
        IP5=round(Input(float(argument[21]),float(argument[22])),2)
        OP1=round(output(float(argument[5]),T1),2)
        OP2=round(output(float(argument[10]),T2),2)
        OP3=round(output(float(argument[15]),T3),2)
        OP4=round(output(float(argument[20]),T4),2)
        OP5=round(output(float(argument[25]),T5),2)
        R1=round((Reg(OP1,IP1)),3)
        R2=round((Reg(OP2,IP2)),3)
        R3=round((Reg(OP3,IP3)),3)
        R4=round((Reg(OP4,IP4)),3)
        R5=round((Reg(OP5,IP5)),3)
        print(json.dumps({"Impact":[{"Thus load test on DC shunt motor is conducted and its efficiency is determined":str(),"Torque(T)":str(T1)+", "+str(T2)+", "+str(T3)+", "+str(T4)+", "+str(T5),"Input Power":str(IP1)+", "+str(IP2)+", "+str(IP3)+", "+str(IP4)+", "+str(IP5),"Output Power":str(OP1)+", "+str(OP2)+", "+str(OP3)+", "+str(OP4)+", "+str(OP5),"Regulation(%)":str(R1)+" % ,"+str(R2)+" % ,"+str(R3)+" % ,"+str(R4)+" % ,"+str(R5)+" %"}]}))

    def DC_SERIES_MOTOR(self):
        argument = self.arg[:]
        def S(X,Y):return(Y-X)
        def Torque(x):return(x*1.015)
        def output(x,y):return((6.28*x*y)/60)
        def Input(x,y):return(x*y)
        def Reg(x,y):return(x/y)*100
        S1=S(float(argument[3]),float(argument[4]))
        S2=S(float(argument[8]),float(argument[9]))
        S3=S(float(argument[13]),float(argument[14]))
        S4=S(float(argument[18]),float(argument[19]))
        S5=S(float(argument[23]),float(argument[24]))
        T1=round(Torque(S1),2)
        T2=round(Torque(S2),2)
        T3=round(Torque(S3),2)
        T4=round(Torque(S4),2)
        T5=round(Torque(S5),2)
        IP1=round(Input(float(argument[1]),float(argument[2])),2)
        IP2=round(Input(float(argument[6]),float(argument[7])),2)
        IP3=round(Input(float(argument[11]),float(argument[12])),2)
        IP4=round(Input(float(argument[16]),float(argument[17])),2)
        IP5=round(Input(float(argument[21]),float(argument[22])),2)
        OP1=round(output(float(argument[5]),T1),2)
        OP2=round(output(float(argument[10]),T2),2)
        OP3=round(output(float(argument[15]),T3),2)
        OP4=round(output(float(argument[20]),T4),2)
        OP5=round(output(float(argument[25]),T5),2)
        R1=round((Reg(OP1,IP1)),3)
        R2=round((Reg(OP2,IP2)),3)
        R3=round((Reg(OP3,IP3)),3)
        R4=round((Reg(OP4,IP4)),3)
        R5=round((Reg(OP5,IP5)),3)

        print(json.dumps({"Impact":[{"Thus load test on DC series motor is conducted and its efficiency is determined":str(),"Torque(T)":str(T1)+", "+str(T2)+", "+str(T3)+", "+str(T4)+", "+str(T5),"Input Power":str(IP1)+", "+str(IP2)+", "+str(IP3)+", "+str(IP4)+", "+str(IP5),"Output Power":str(OP1)+", "+str(OP2)+", "+str(OP3)+", "+str(OP4)+", "+str(OP5),"Regulation(%)":str(R1)+" % ,"+str(R2)+" % ,"+str(R3)+" % ,"+str(R4)+" % ,"+str(R5)+" %"}]}))
    def DC_COMPOUND_MOTOR(self):
        argument = self.arg[:]
        def S(X,Y):return(Y-X)
        def Torque(x):return(x*1.015)
        def output(x,y):return((6.28*x*y)/60)
        def Input(x,y):return(x*y)
        def Reg(x,y):return(x/y)*100
        S1=S(float(argument[3]),float(argument[4]))
        S2=S(float(argument[8]),float(argument[9]))
        S3=S(float(argument[13]),float(argument[14]))
        S4=S(float(argument[18]),float(argument[19]))
        S5=S(float(argument[23]),float(argument[24]))
        T1=round(Torque(S1),2)
        T2=round(Torque(S2),2)
        T3=round(Torque(S3),2)
        T4=round(Torque(S4),2)
        T5=round(Torque(S5),2)
        IP1=round(Input(float(argument[1]),float(argument[2])),2)
        IP2=round(Input(float(argument[6]),float(argument[7])),2)
        IP3=round(Input(float(argument[11]),float(argument[12])),2)
        IP4=round(Input(float(argument[16]),float(argument[17])),2)
        IP5=round(Input(float(argument[21]),float(argument[22])),2)
        OP1=round(output(float(argument[5]),T1),2)
        OP2=round(output(float(argument[10]),T2),2)
        OP3=round(output(float(argument[15]),T3),2)
        OP4=round(output(float(argument[20]),T4),2)
        OP5=round(output(float(argument[25]),T5),2)
        R1=round((Reg(OP1,IP1)),3)
        R2=round((Reg(OP2,IP2)),3)
        R3=round((Reg(OP3,IP3)),3)
        R4=round((Reg(OP4,IP4)),3)
        R5=round((Reg(OP5,IP5)),3)

        print(json.dumps({"Impact":[{"Thus load test on DC compound motor is conducted and its efficiency is determined":str(),"Torque(T)":str(T1)+", "+str(T2)+", "+str(T3)+", "+str(T4)+", "+str(T5),"Input Power":str(IP1)+", "+str(IP2)+", "+str(IP3)+", "+str(IP4)+", "+str(IP5),"Output Power":str(OP1)+", "+str(OP2)+", "+str(OP3)+", "+str(OP4)+", "+str(OP5),"Regulation(%)":str(R1)+" % ,"+str(R2)+" % ,"+str(R3)+" % ,"+str(R4)+" % ,"+str(R5)+" %"}]}))
    def SELF(self):
        print(json.dumps({"answer":[{"result":"Thus open circuit characteristics of self excited DC shunt generator are obtained and its critical resistance is determined."}]}))
    def SEPARATELY(self):
        print(json.dumps({"answer":[{"result":"Thus open circuit characteristics of separately excited DC shunt generators are obtained."}]}))
    def Load_Separately(self):
        argument = self.arg[:]
        R1 = float(argument[1])/float(argument[2])
        R2 = float(argument[3])/float(argument[4])
        R3 = float(argument[5])/float(argument[6])
        R4 = float(argument[7])/float(argument[8])
        I1 = float(argument[9])+float(argument[10])
        I2 = float(argument[12])+float(argument[13])
        I3 = float(argument[15])+float(argument[16])
        I4 = float(argument[18])+float(argument[19])
        Rmean=round((R1+R2+R3+R4)/4,2)
        F1 = round(float(argument[11])+(I1*Rmean),2)
        F2 = round(float(argument[14])+(I2*Rmean),2)
        F3 = round(float(argument[17])+(I3*Rmean),2)
        F4 = round(float(argument[20])+(I4*Rmean),2)
        print(json.dumps({"Impact":[{"Thus load characteristics of separately excited DC shunt generator is obtained- Mean value of Ra":str(Rmean), "Actually Generated Voltage_1": str(F1),"Actually Generated Voltage_2": str(F2),"Actually Generated Voltage_3": str(F3), "Actually Generated Voltage_4": str(F4)}]}))
    def Load_Self(self):
        argument = self.arg[:]
        def IA(x,y):return(x+y)
        def IR(X,Y):return(X*Y)
        def Eg(x,y):return(x+y)
        I1=round(IA(float(argument[2]),float(argument[3])),2)
        I2=round(IA(float(argument[5]),float(argument[6])),2)
        I3=round(IA(float(argument[8]),float(argument[9])),2)
        I4=round(IA(float(argument[11]),float(argument[12])),2)
        IR1=round(IR(float(argument[1]),I1),2)
        IR2=round(IR(float(argument[1]),I2),2)
        IR3=round(IR(float(argument[1]),I3),2)
        IR4=round(IR(float(argument[1]),I4),2)
        eg1=round(Eg(float(argument[4]),IR1),2)
        eg2=round(Eg(float(argument[7]),IR2),2)
        eg3=round(Eg(float(argument[10]),IR3),2)
        eg4=round(Eg(float(argument[13]),IR4),2)
        print(json.dumps({"Impact":[{"Thus load characteristics of separately excited DC shunt generator is obtained":" ","Armature current(Ia)":str(I1)+", "+str(I2)+", "+str(I3)+", "+str(I4)+" (Amps) ","Generated emf in Volts (Eg)": str(eg1)+", "+str(eg2)+", "+str(eg3)+", "+str(eg4)}]}))
    def Hopkin(self):
        argument = self.arg[:]
        def Ra(x,y):return(x/y)
        def Cl(x,y,z):return((x+y)**2)*z
        def R(x,y,z):return(x/((y+z)/2))
        def Fl(x,y):return(x*y)
        def Sl(a,b,c,d):return(((a*b)-c+d)/2)
        def Tl(a,b,c,d):return(a+(b*c)+d)
        def Input(a,b,c,d):return((a+b+c)*d)
        def Eff(x,y):return(((y-x)/x)*100)
        def copper(x,y):return((x**2)*y)
        Ra1=Ra(float(argument[22]),float(argument[23]))
        Ra2=Ra(float(argument[24]),float(argument[25]))
        Ra3=Ra(float(argument[26]),float(argument[27]))
        Ra4=Ra(float(argument[28]),float(argument[29]))
        Ra5=Ra(float(argument[30]),float(argument[31]))
        RA=round((Ra1+Ra2+Ra3+Ra4+Ra5)/5,2)
        R1=round(R(float(argument[1]),float(argument[2]),float(argument[3])),2)
        R2=round(R(float(argument[5]),float(argument[6]),float(argument[7])),2)
        R3=round(R(float(argument[9]),float(argument[10]),float(argument[11])),2)
        r1=round((float(argument[3])**2)*R1)
        r2=round((float(argument[7])**2)*R2)
        r3=round((float(argument[11])**2)*R3)
        CL1=round(Cl(float(argument[2]),float(argument[3]),R1),2)
        CL2=round(Cl(float(argument[6]),float(argument[7]),R2),2)
        CL3=round(Cl(float(argument[10]),float(argument[11]),R3),2)
        Fl1=round(Fl(float(argument[1]),float(argument[4])),2)
        Fl2=round(Fl(float(argument[5]),float(argument[8])),2)
        Fl3=round(Fl(float(argument[9]),float(argument[12])),2)
        Sl1=round(Sl(float(argument[1]),float(argument[2]),CL1,r1))
        Sl2=round(Sl(float(argument[5]),float(argument[6]),CL2,r2))
        Sl3=round(Sl(float(argument[9]),float(argument[10]),CL3,r3))
        I1=round(Input(float(argument[2]),float(argument[3]),float(argument[4]),float(argument[1])),2)
        I2=round(Input(float(argument[6]),float(argument[7]),float(argument[8]),float(argument[5])),2)
        I3=round(Input(float(argument[10]),float(argument[11]),float(argument[12]),float(argument[9])),2)
        TL1=round(Tl(CL1,float(argument[1]),float(argument[4]),Sl1),2)
        TL2=round(Tl(CL2,float(argument[5]),float(argument[8]),Sl2),2)
        TL3=round(Tl(CL3,float(argument[9]),float(argument[12]),Sl3),2)
        E1=round(Eff(I1,TL1),2)
        E2=round(Eff(I2,TL2),2)
        E3=round(Eff(I3,TL3),2)
        Output1=round(Fl(float(argument[13]),float(argument[15])),2)
        Output2=round(Fl(float(argument[16]),float(argument[18])),2)
        Output3=round(Fl(float(argument[19]),float(argument[21])),2)
        Copper1=round(copper(float(argument[15]),RA),2)
        Copper2=round(copper(float(argument[18]),RA),2)
        Copper3=round(copper(float(argument[21]),RA),2)
        Stray1=round(((((float(argument[13])*float(argument[14]))-((float(argument[14])+float(argument[15]))**2))*RA)+Copper1)/2,2)
        Stray2=round(((((float(argument[16])*float(argument[17]))-((float(argument[17])+float(argument[18]))**2))*RA)+Copper2)/2,2)
        Stray3=round(((((float(argument[19])*float(argument[20]))-((float(argument[20])+float(argument[21]))**2))*RA)+Copper3)/2,2)
        Total1=round((Copper1+Output1+Stray1),2)
        Total2=round((Copper2+Output2+Stray2),2)
        Total3=round((Copper3+Output3+Stray3),2)
        Efficiency1=round((Output1/(Output1+Total1))*100,2)
        Efficiency2=round((Output2/(Output2+Total2))*100,2)
        Efficiency3=round((Output3/(Output3+Total3))*100,2)
        print(json.dumps({"answer":[{"The Hopkinson’s test on a pair of identical DC machines to pre-determine the efficiency of the machine as generator and as motor":"For Motor" ,"Armature Resistance(Ra)" :str(RA),"Copper Loss:":str(CL1)+", "+str(CL2)+", "+str(CL3)+", ","Fluid loss":str(Fl1)+", "+str(Fl2)+", "+str(Fl3),"Stray loss":str(Sl1)+", "+str(Sl2)+", "+str(Sl3),"Input Power":str(I1)+", "+str(I2)+", "+str(I3),"Total loss":str(TL1)+", "+str(TL2)+", "+str(TL3),"Efficiency":str(E1)+"% ,"+str(E2)+"% ,"+str(E3)+"% ",
        "For generator":str(),"Copper losses":str(Copper1)+", "+str(Copper2)+", "+str(Copper3),"Output Power":str(Output1)+", "+str(Output2)+", "+str(Output3),"Stray losses":str(Stray1)+", "+str(Stray2)+", "+str(Stray3),"Total losses":str(Total1)+", "+str(Total2)+", "+str(Total3),"Efficiency ":str(Efficiency1)+"% "+str(Efficiency2)+"% "+str(Efficiency3)+"%"}]}))        
    def Speed(self):
        print(json.dumps({"answer":[{"result":"Thus the speed control of DC Shunt Motor is obtained using Armature and Field control methods"}]}))
    def OC(self):
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn."}]}))
    def OCDC(self):
        print(json.dumps({"answer":[{"result":"Thus the above experiment is simulated"}]}))
    def trf(self):
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
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn.","Efficiency E1":"Zero at no load","Efficiency E2":str(E2)+"%","Efficiency E3":str(E3)+"%","Efficiency E4":str(E4)+"%","Efficiency E5":str(E5)+"%","Regulation R1":"Zero at no load","Regulation R2":str(R2)+"%","Regulation R3":str(R3)+"%","Regulation R4":str(R4)+"%","Regulation R5":str(R5)+"%"}]}))
    def SWINBURNE(self):
        argument = self.arg[:]
        Ia= round((float(argument[3])-float(argument[4])),2)
        def R(x,y):return(y/x)
        def IA(x,y):return(x+y)
        def ia(x,y):return(x-y)
        def IR(x):return(x**2)*RA
        def TL(x):return(W+x)
        def OP(x):return(V*x)/10
        def IP(x,y):return(x+y)
        def E(x,y):return(x/y)*100
        V= float(argument[1])
        R1=(R(float(argument[5]),float(argument[6])))
        R2=R(float(argument[7]),float(argument[8]))
        R3=R(float(argument[9]),float(argument[10]))
        R4=R(float(argument[11]),float(argument[12]))
        R5=R(float(argument[13]),float(argument[14]))
        RA=round((R1+R2+R3+R4+R5)/5,2)
        W= round(((float(argument[1])*float(argument[3]))-((Ia**2)*RA)),3)
        I1=round(IA(float(argument[16]),float(argument[17])),2)
        I2=round(IA(float(argument[19]),float(argument[20])),2)
        I3=round(IA(float(argument[22]),float(argument[23])),2)
        I4=round(IA(float(argument[25]),float(argument[26])),2)

        IR1=round(IR(I1),2)
        IR2=round(IR(I2),2)
        IR3=round(IR(I3),2)
        IR4=round(IR(I4),2)
        TL1=round(TL(IR1),2)
        TL2=round(TL(IR2),2)
        TL3=round(TL(IR3),2)
        TL4=round(TL(IR4),2)
        OP1=round(OP(float(argument[15])),2)
        OP2=round(OP(float(argument[18])),2)
        OP3=round(OP(float(argument[21])),2)
        OP4=round(OP(float(argument[24])),2)
        IP1=round(IP(OP1,TL1),2)
        IP2=round(IP(OP2,TL2),2)
        IP3=round(IP(OP3,TL3),2)
        IP4=round(IP(OP4,TL4),2)
        E1=round(E(OP1,IP1),2)
        E2=round(E(OP2,IP2),2)
        E3=round(E(OP3,IP3),2)
        E4=round(E(OP4,IP4),2)
        ia1=round(ia(float(argument[28]),float(argument[29])),2)
        ia2=round(ia(float(argument[31]),float(argument[32])),2)
        ia3=round(ia(float(argument[34]),float(argument[35])),2)
        ia4=round(ia(float(argument[37]),float(argument[38])),2)
        ir1=round(IR(ia1),2)
        ir2=round(IR(ia2),2)
        ir3=round(IR(ia3),2)
        ir4=round(IR(ia4),2)
        tl1=round(TL(ir1),2)
        tl2=round(TL(ir2),2)
        tl3=round(TL(ir3),2)
        tl4=round(TL(ir4),2)
        ip1=round((float(argument[1])*float(argument[28])))
        ip2=round((float(argument[1])*float(argument[31])),2)
        ip3=round((float(argument[1])*float(argument[34])),2)
        ip4=round((float(argument[1])*float(argument[37])),2)
        op1=round(ia(ip1,tl1),2)
        op2=round(ia(ip2,tl2),2)
        op3=round(ia(ip3,tl3),2)
        op4=round(ia(ip4,tl4),2)
        e1=round(E(op1,ip1),2)
        e2=round(E(op2,ip2),2)
        e3=round(E(op3,ip3),2)
        e4=round(E(op4,ip4),2)
        print(json.dumps({"answer":[{"To predetermine the efficiency of the given DC shunt machine while running as a motor and as a generator  by conducting Swinburne’s test.":str(),"Armature current(Ia)":str(Ia),"Armature Resistance(Ra)":str(RA),"Constant load":str(W),"GENERATOR":str(),"Armature current(Ia)":str(I1)+" Amp, "+str(I2)+" Amp, "+str(I3)+" Amp, "+str(I4)+" Amp, ","Ia2R":str(IR1)+", "+str(IR2)+" , "+str(IR3)+" , "+str(IR4),
        "Total losses":str(TL1)+" , "+str(TL2)+" , "+str(TL3)+" , "+str(TL4),"Output power":str(OP1)+" , "+str(OP2)+" , "+str(OP3)+" , "+str(OP4),
        "Input power": str(IP1)+", "+str(IP2)+", "+str(IP3)+", "+str(IP4),
        "Efficiency":str(E1)+"%, "+str(E2)+"%, "+str(E3)+"%, "+str(E4)+"%, ",
        "MOTOR":str(),"Ia":str(ia1)+" Amp, "+str(ia2)+" Amp, "+str(ia3)+" Amp, "
        +str(ia4)+" Amp","Ia^2R":str(ir1)+", "+str(ir2)+", "+str(ir3)+", "+str(ir4)+", ","Total_Loss":str(tl1)+", "+str(tl2)+", "+str(tl3)+", "+str(tl4)+", ","Input Power":str(ip1)+", "+str(ip2)+", "+str(ip3)+"," +str(ip4)+", ","Output_power":str(op1)+", "+str(op2)+", "+str(op3)+", "+str(op4),"Efficiency ":str(e1)+"% , "+str(e2)+"% , "+str(e3)+"% , "+str(e4)+"%"
        }]}))
    
        



        

    












        




        





