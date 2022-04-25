import json
import math

class TE2:
    def __init__(self, arg):
        self.arg = arg
    def Port_diagram(self):
        argument = self.arg[1:]
        def mean(x,y,z):
            ans = (x+y+z)/3
            return ans
        IPO = mean(float(argument[1]),float(argument[2]),float(argument[3]))
        IPC = mean(float(argument[4]),float(argument[5]),float(argument[6]))
        EPO = mean(float(argument[7]),float(argument[8]),float(argument[9]))
        EPC = mean(float(argument[10]),float(argument[11]),float(argument[12]))
        TPO = mean(float(argument[13]),float(argument[14]),float(argument[15]))
        IPC_Af = mean(float(argument[16]),float(argument[17]),float(argument[18]))
        print(json.dumps({"Result":[{"Port Timing Diagram":"The given two stroke engine is studied and the port timing diagram is drawn for the present set of value","IPO before TDC" : str(IPO), "4IPC after TDC": str(IPC), "EPO before BDC ": str(EPO),"EPC after BDC":str(EPC) ,"TPO before BDC":str(TPO),"IPC after BDC":str(IPC_Af)}]}))
    def Valve_diagram(self):
        argument = self.arg[1:]
        circumference = 1250
        Angle1 = float(argument[1])*360 / circumference
        Angle2 = float(argument[2])*360 / circumference
        Angle3 = float(argument[3])*360 / circumference
        Angle4 = float(argument[4])*360 / circumference
        print(json.dumps({"Result":[{"Value Timing Diagram":"The given four stroke compressed ignition engine is studied and the value timing diagram is drawn for the present set of value","Angle_1" : float(argument[1]), "Angle_2": float(argument[2]), "Angle_3 ": float(argument[3]),"Angle_4":float(argument[4])}]}))
    def Single_petrol(self):
        argument = self.arg[0:]
        def mass(a,b):
            return 1000*0.78*(a/1000)**2*(b/100)
        def RE(a,b,c):
            return a*4.178*(b-c)/1500
        def Work(a,b):
            return 3600*10/(a*b)
        def cop(a,b):
            return(a/b)
        def h(a,b,c,d):
            return a+b/(c-d)
        mass1 = mass(float(argument[1]),float(argument[15]))
        mass2 = mass(float(argument[1]),float(argument[28]))
        mass3 = mass(float(argument[1]),float(argument[41]))
        RE1 = RE(mass1,float(argument[3]),float(argument[4]))
        RE2 = RE(mass2,float(argument[16]),float(argument[17]))
        RE3 = RE(mass3,float(argument[29]),float(argument[30]))
        W1=Work(float(argument[2]),float(argument[14]))
        W2=Work(float(argument[2]),float(argument[27]))
        W3=Work(float(argument[2]),float(argument[40]))
        mcop=(cop(RE1,W1)+cop(RE2,W2)+cop(RE3,W3))/3
        h1=h(420.44,1070,float(argument[6]),float(argument[7]))
        h4=h(393.715,891.9,float(argument[9]),float(argument[8]))
        h3=259.35
        cop_theo=(h1-h3)/(h1-h4)
        print(json.dumps({"Result":[{"The performance test was conducted in refrigeration test rig and the result are : The co-efficient of performance of refrigeration":str(mcop),"The Theoritical value of COP":str(cop_theo)}]}))
    # def heat_4stroke(self):
    #     argument = self.arg[0:]
        
    #     def BP(a):
    #         return 11.22*a/60000
    #     def TFC(a):
    #         return 29790/(a*1000)
    #     def heat_io(a):
    #         return a*42000                                      #         return a*0.0042
    #     def eq_uw(a):
    #         return a*3600
    #     def per_eq_uw(a,b):
    #         return a*100/b
    #     def Qw(a):
    #         return 150408*(2/a)
    #     def Ha(a):
    #         return (a*10)/1.23
    #     def Va(a):
    #         return math.sqrt(19.62*a)
    #     def Ma(a):
    #         return a*1.23
    #     def Mg(a,b):
    #         return a+b
    #     def heat_egas(a):
    #         return a*32.654
    #     def veff(a,b,c,d,e):
    #         t=0.64*0.785*(a/100)**2*b
    #         d=(c/100)*0.785*(d)**2*(e/120)
    #         return t / d
    #     def unacc_loss(a,b,c,d):
    #         return a-(b+c+d)
    #     BP1 = BP(float(argument[8]))
    #     BP2 = BP(float(argument[14]))
    #     BP3 = BP(float(argument[20]))
    #     BP4 = BP(float(argument[26]))
    #     BP5 = BP(float(argument[32]))
    #     TFC1= TFC(float(argument[9]))
    #     TFC2= TFC(float(argument[15]))
    #     TFC3= TFC(float(argument[21]))
    #     TFC4= TFC(float(argument[27]))
    #     TFC5= TFC(float(argument[33]))
    #     heat_io1 = heat_io(TFC1)
    #     heat_io2 = heat_io(TFC2)
    #     heat_io3 = heat_io(TFC3)
    #     heat_io4 = heat_io(TFC4)
    #     heat_io5 = heat_io(TFC5)
    #     eq_uw1= eq_uw(BP1)
    #     eq_uw2= eq_uw(BP2)
    #     eq_uw3= eq_uw(BP3)
    #     eq_uw4= eq_uw(BP4)
    #     eq_uw5= eq_uw(BP5)
    #     per_eq_uw1=per_eq_uw(eq_uw1,heat_io1)
    #     per_eq_uw2=per_eq_uw(eq_uw1,heat_io2)
    #     per_eq_uw3=per_eq_uw(eq_uw1,heat_io3)
    #     per_eq_uw4=per_eq_uw(eq_uw1,heat_io4)
    #     per_eq_uw5=per_eq_uw(eq_uw1,heat_io5)
    #     Qw1=Qw(float(argument[36]))
    #     Qw2=Qw(float(argument[41]))
    #     Qw3=Qw(float(argument[46]))
    #     Qw4=Qw(float(argument[51]))
    #     Qw5=Qw(float(argument[56]))
    #     Ha1=Ha(float(argument[56]))
    #     Va1=Va(Ha1)
    #     Ma1=Ma(Va1)
    #     Mg1=Mg(Ma1,TFC1)
    #     Mg2=Mg(Ma2,TFC2)
    #     Mg3=Mg(Ma3,TFC3)
    #     Mg4=Mg(Ma4,TFC4)
    #     Mg5=Mg(Ma5,TFC5)

    def enginetestrig (self):
        argument = self.arg[0:]
        def diff(a,b):
            return abs(a-b)
        delw1=diff(float(argument[1]),float(argument[2]) )*9.81
        delw2=diff(float(argument[7]),float(argument[8]) )*9.81
        delw3=diff(float(argument[13]),float(argument[14]) )*9.81
        delw4=diff(float(argument[19]),float(argument[20]) )*9.81
        delw5=diff(float(argument[25]),float(argument[26]) )*9.81
        w1=diff(float(argument[5]),float(argument[6]) )
        w2=diff(float(argument[11]),float(argument[12]) )
        w3=diff(float(argument[17]),float(argument[18]) )
        w4=diff(float(argument[23]),float(argument[24]) )
        w5=diff(float(argument[29]),float(argument[30]) )
    def coolingtower (self):
        argument = self.arg[0:]
        eff = (float(argument[1])-float(argument[2]))/(float(argument[1])-float(argument[3]))
        overalleff=round((eff*100),2)
        # humidity= (float(argument[1])-float(argument[2]))/(float(argument[1])-float(argument[3]))
        # print(json.dump({"The efficiency of cooling tower is", str(overalleff)}))
        print(json.dumps({"Impact":[{"The efficiency of cooling tower is":str(overalleff)+ "%" }]}))
    def singlecylinderper (self):
        argument = self.arg[0:]
        def bhp(a,b):
            return a*b*1.341/1000
        bhp1 = (float(argument[3]),float(argument[4]))
        bhp2 = (float(argument[19]),float(argument[20]))
        bhp3 = (float(argument[35]),float(argument[36]))
        bhp4 = (float(argument[51]),float(argument[52]))
        def tfc(t):
            return 100*1*3600/(t*1000)
        tfc1 = float(argument[2])
        tfc1 = float(argument[18])
        tfc1 = float(argument[34])
        tfc1 = float(argument[50])
        fhp1 = tfc1*12000*4.2/(3600*1000)
        fhp2 = tfc2*12000*4.2/(3600*1000)
        fhp3 = tfc3*12000*4.2/(3600*1000)
        fhp4 = tfc4*12000*4.2/(3600*1000)
        hi1=(tfc1*12000)/1000
        hi2=(tfc1*12000)/1000
        hi3=(tfc1*12000)/1000
        hi4=(tfc1*12000)/1000
        bte1=(bhp1/fhp1)*100
        bte2=(bhp2/fhp2)*100
        bte3=(bhp3/fhp3)*100
        bte4=(bhp4/fhp4)*100
        # indicated Hp , Indicated thermal eff, ,echinacal eff
        print(json.dumps({"Impact":[{"The Graph":"the graph has to be plotted" }]}))
    def porttiming (self):
        argument = self.arg[0:]
        def mean(a,b,c):
            return ((a+b+c)/3)
        mean1 = round(mean(float(argument[1]),float(argument[2]),float(argument[3])),2)
        mean2 = round(mean(float(argument[4]),float(argument[5]),float(argument[6])),2)
        mean3 = round(mean(float(argument[7]),float(argument[8]),float(argument[9])),2)
        mean4 = round(mean(float(argument[10]),float(argument[11]),float(argument[12])),2)
        mean5 = round(mean(float(argument[13]),float(argument[14]),float(argument[15])),2)
        mean6 = round(mean(float(argument[16]),float(argument[17]),float(argument[18])),2)
        print(json.dumps({"Impact":[{"Averagre IPO before TDC is ":str(mean1),"Averagre IPC after TDC is ":str(mean2),"Averagre EPO before BDC is ":str(mean3),"Averagre EPC after BDC is ":str(mean4),"Averagre TPO before BDC is ":str(mean5),"Averagre TPC after BDC is ":str(mean6) }]}))
    def valvetiming (self):
        argument = self.arg[0:]
        def angle(a):
            return ((360*a)/(2*math.pi*200))
        angle1 = round(angle(float(argument[1])),2)
        angle2 = round(angle(float(argument[2])),2)
        angle3 = round(angle(float(argument[3])),2)
        angle4 = round(angle(float(argument[4])),2)
    
        print(json.dumps({"Impact":[{"Angle of IVO Before TDC":str(angle1),"Angle of IVC After BDC":str(angle2),"Angle of EVO Before BDC":str(angle3),"Angle of EVC After TDC":str(angle4) }]}))

    def regvet (self):
        argument = self.arg[0:]
        tl1=(5*9.81)*(0.3/2)
        tl2=(10*9.81)*(0.3/2)
        tl3=(15*9.81)*(0.3/2)
        TF1=round(tl1*(float(argument[3])/(float(argument[2])-float(argument[3]))),2)
        TF2=round(tl2*(float(argument[6])/(float(argument[5])-float(argument[6]))),2)
        TF3=round(tl3*(float(argument[9])/(float(argument[8])-float(argument[9]))),2)
        FP1=round(2*math.pi*float(argument[1])*TF1/60,2)
        FP2=round(2*math.pi*float(argument[4])*TF2/60,2)
        FP3=round(2*math.pi*float(argument[7])*TF3/60,2)
        BP1=2*math.pi*float(argument[1])*tl1/60
        BP2=2*math.pi*float(argument[1])*tl2/60
        BP3=2*math.pi*float(argument[1])*tl3/60
        IP1= BP1+FP1
        IP2= BP2+FP2
        IP3= BP3+FP3
        mecheff1=round(BP1/IP1,2)
        mecheff2=round(BP2/IP2,2)
        mecheff3=round(BP3/IP3,2)
        print(json.dumps({"Impact":[{"The frictional Torque , Frictional Power and Mechanical efficienct at 5 kg load is":str(TF1)+", "+str(FP1)+" and "+str(mecheff1)+"respectively","The frictional Torque , Frictional Power and Mechanical efficienct at 10 kg load is":str(TF2)+", "+str(FP2)+" and "+str(mecheff2)+"respectively","The frictional Torque , Frictional Power and Mechanical efficienct at 15 kg load is":str(TF3)+", "+str(FP3)+" and "+str(mecheff3) +"respectively"}]}))
    def junker (self):
        argument = self.arg[0:]
        cv= round((float(argument[1])/float(argument[5]))*(float(argument[4]) - float(argument[3]))*1000,2)
        print(json.dumps({"Result":[{"The calorific value of the given gas is":str(cv)}]}))

    def twincylinder (self):
        argument = self.arg[0:]
        def bp(a,b):
            return a*b/1000
        bp1 = (float(argument[2]),float(argument[3]))
        bp2 = (float(argument[13]),float(argument[14]))
        bp3 = (float(argument[24]),float(argument[25]))
        def massoffuel(a):
            return (10*0.867*3600)/(a*1000)
        massoffuel1 = massoffuel(float(argument[4]))
        massoffuel2 = massoffuel(float(argument[15]))
        massoffuel3 = massoffuel(float(argument[26]))
        FP=3.5
        IP1=bp1+FP
        IP2=bp2+FP
        IP3=bp3+FP
        sfc1=massoffuel1/bp1
        sfc2=massoffuel2/bp2
        sfc3=massoffuel3/bp3
        mecheff1= bp1/IP1*100
        mecheff2= bp2/IP2*100
        mecheff3= bp3/IP3*100
        bte1=(3600*1000)/(sfc1*42000)
        bte2=(3600*1000)/(sfc2*42000)
        bte3=(3600*1000)/(sfc3*42000)
        effit=()/()
        def massoffuel(a):
            return (10*0.867*3600)/(a*1000)
        massoffuel1 = massoffuel(float(argument[4]))
        massoffuel2 = massoffuel(float(argument[15]))
        massoffuel3 = massoffuel(float(argument[26]))
       

