import json
import math

class com3:
    def __init__(self, arg):
        self.arg = arg
        
    def GUNN_DIODE(self):
        argument = self.arg[0:]
        g1 =float(argument[21])*2*10**-2
        g2 = float(argument[22])*2*10**-2
        g3 = float(argument[25])*2*10**-2
        c1 = float(argument[19])*2
        c2 = float(argument[19])*2/10
        c3 = float(argument[19])*2/10
        lo1=math.sqrt((1/g1**2)+(1/c1**2))
        lo2=math.sqrt((1/g2**2)+(1/c2**2))
        lo3=math.sqrt((1/g3**2)+(1/c3**2))
        f1 = float(argument[26])*10**2/lo1
        f2 = float(argument[26])*10**2/lo2
        f3 = float(argument[26])*10**2/lo3

        print(json.dumps({"Software":[{"The Gunn Diode Characteristics is completed sucessfully":str(f1)}]}))

        
    def REFLEX_KLYSTRON(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Mode Characteristics of Reflex Klystron is completed sucessfully"}]}))
        
    def ISOLATOR_CIRCULATOR(self):
        argument = self.arg[:]

        ref1=float(argument[1])*float(argument[2])
        mv1=float(argument[3])*float(argument[2])
        mv2=float(argument[4])*float(argument[2])
        In1 =  round(20*math.log10(ref1/mv1),2)
        In2= round(20*math.log10(ref1/mv2),2)
        Is1= round(20*math.log10(mv1/ref1),2)
        Is2= round(20*math.log10(mv2/ref1),2)
        ref2=float(argument[5])*float(argument[6])
        Vm1=float(argument[7])*float(argument[6])
        Vm2=float(argument[8])*float(argument[6])
        Inl1 =  round(20*math.log10(ref2/Vm1),2)
        Inl2= round(20*math.log10(ref2/Vm2),2)
        Isl1= round(20*math.log10(Vm1/ref2),2)
        Isl2= round(20*math.log10(Vm2/ref2),2)
        print(json.dumps({"Loss":[{"Thus the insertion loss and isolation loss for given circular and isolator were measured":str(),"ISOLATION_Insertion Loss":str(In1)+" db "+str(In2)+" db ","ISOLATION_Isolation loss":str(Is1)+" db "+str(Is2)+" db ","CIRCULATOR_Insertion loss":str(Inl1)+" db "+str(Inl2)+" db ","CIRCULATOR_Isolation loss":str(Isl1)+" db "+str(Isl2)+" db "}]}))
        
        
    def EPLANE_AND_HIPLANE_TEE(self):
        argument = self.arg[0:]
        Amp1 = float(argument[1])*float(argument[2])
        Amp2 = float(argument[5])*float(argument[6])
        Amp3 = float(argument[9])*float(argument[10])
        Amp4 = float(argument[13])*float(argument[14])
        Amp5 = float(argument[17])*float(argument[18])
        Amp6 = float(argument[21])*float(argument[22])
        T1=float(argument[3])*float(argument[4])
        T2=float(argument[7])*float(argument[8])
        T3=float(argument[11])*float(argument[12])
        T4=float(argument[15])*float(argument[16])
        T5=float(argument[19])*float(argument[20])
        T6=float(argument[23])*float(argument[24])
        print(json.dumps({"Software":[{"The Characteristics of E-Plane and H-Plane Tee is completed sucessfully":str(Amp1)}]}))
                
        
    def MAGIC_TEE(self):
        argument = self.arg[0:]
        Vi=float(argument[1])
        Vo1=float(argument[2])*float(argument[3])
        Vo2=float(argument[4])*float(argument[5])
        Vo3=float(argument[6])*float(argument[7])
        Vo4=float(argument[8])*float(argument[9])
        Vo5=float(argument[10])*float(argument[11])
        Vo6=float(argument[12])*float(argument[13])
        Vo7=float(argument[14])*float(argument[15])
        Vo8=float(argument[16])*float(argument[17])
        Vo9=float(argument[18])*float(argument[19])
        Vo10=float(argument[20])*float(argument[21])
        Vo11=float(argument[22])*float(argument[23])
        Vo12=float(argument[24])*float(argument[25])
        A1=20*math.log10(Vi/Vo1)
        A2=20*math.log10(Vi/Vo2)
        A3=20*math.log10(Vi/Vo3)
        A4=20*math.log10(Vi/Vo4)
        A5=20*math.log10(Vi/Vo5)
        A6=20*math.log10(Vi/Vo6)
        A7=20*math.log10(Vi/Vo7)
        A8=20*math.log10(Vi/Vo8)
        A9=20*math.log10(Vi/Vo9)
        A10=20*math.log10(Vi/Vo10)
        A11=20*math.log10(Vi/Vo11)
        A12=20*math.log10(Vi/Vo12)
        CF1=10**(-A1/20)
        CF2=10**(-A2/20)
        CF3=10**(-A3/20)
        CF4=10**(-A4/20)
        CF5=10**(-A5/20)
        CF6=10**(-A6/20)
        CF7=10**(-A7/20)
        CF8=10**(-A8/20)
        CF9=10**(-A9/20)
        CF10=10**(-A10/20)
        CF11=10**(-A11/20)
        CF12=10**(-A12/20)

        print(json.dumps({"Software":[{"The Characteristics of Magic Tee is completed sucessfully":str(A1)}]}))
                
        
    def DIRECTIONAL_COUPLER(self):
        argument = self.arg[0:]
        Amp1 = float(argument[4])*float(argument[2])
        Amp2 = float(argument[6])*float(argument[2])
        Amp3 = float(argument[8])*float(argument[2])
        T1=float(argument[5])*float(argument[3])
        T2=float(argument[7])*float(argument[3])
        T3=float(argument[9])*float(argument[3])

        print(json.dumps({"Software":[{"The Characteristics of Directional Coupler is completed sucessfully":str(Amp1)}]}))
                
        
    def HORN_ANTENNA(self):
        argument = self.arg[0:]
        Vi=float(argument[1])
        A1=20*math.log10(Vi/float(argument[3]))
        A2=20*math.log10(Vi/float(argument[6]))
        A3=20*math.log10(Vi/float(argument[9]))
        A4=20*math.log10(Vi/float(argument[12]))
        A5=20*math.log10(Vi/float(argument[15]))
        a1=20*math.log10(Vi/float(argument[4]))
        a2=20*math.log10(Vi/float(argument[7]))
        a3=20*math.log10(Vi/float(argument[10]))
        a4=20*math.log10(Vi/float(argument[13]))
        a5=20*math.log10(Vi/float(argument[16]))
        print(json.dumps({"Software":[{"The Radiation Pattern of Horn Antenna completed sucessfully":str(A1)}]}))
                
        
    def MEASUREMENT_OF_IMPEDANCE(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Measurement of impedance is completed sucessfully"}]}))

    def FIBRE_OPTIC_MEASUREMENTS(self):
        argument = self.arg[0:]
        Bl1=20*math.log10(float(argument[2])/float(argument[3]))
        Bl2=20*math.log10(float(argument[5])/float(argument[6]))
        Bl3=20*math.log10(float(argument[8])/float(argument[9]))
        Bl4=20*math.log10(float(argument[11])/float(argument[12]))
        R1=(float(argument[14])+float(argument[15]))/4
        R2=(float(argument[17])+float(argument[18]))/4
        R3=(float(argument[20])+float(argument[21]))/4
        R4=(float(argument[23])+float(argument[24]))/4
        R5=(float(argument[26])+float(argument[27]))/4
        NA1=R1/math.sqrt(float(argument[13])+R1)
        NA2=R2/math.sqrt(float(argument[13])+R2)
        NA3=R3/math.sqrt(float(argument[13])+R3)
        NA4=R4/math.sqrt(float(argument[13])+R4)
        NA5=R5/math.sqrt(float(argument[13])+R5)
        MEAN=(NA1+NA2+NA3+NA4+NA5)/5
        Ang=math.asin(MEAN)
        print(json.dumps({"Software":[{"The Fiber Optics Measurement is completed sucessfully":str(Bl1)}]}))
                
        
    def FIBRE_OPTIC_LED(self):
        argument = self.arg[0:]
        eff=float(argument[1])
        Fc=float(argument[2])
        Pi1=float(argument[3])*float(argument[4])
        Pi2=float(argument[5])*float(argument[6])
        Pi3=float(argument[7])*float(argument[8])
        Pi4=float(argument[9])*float(argument[10])
        Pi5=float(argument[11])*float(argument[12])
        Pi6=float(argument[13])*float(argument[14])
        Pi7=float(argument[15])*float(argument[16])
        Pi8=float(argument[17])*float(argument[18])
        Pi9=float(argument[19])*float(argument[20])
        Pi10=float(argument[21])*float(argument[22])
        po1=Pi1*eff
        po2=Pi2*eff
        po3=Pi3*eff
        po4=Pi4*eff
        po5=Pi5*eff
        po6=Pi6*eff
        po7=Pi7*eff
        po8=Pi8*eff
        po9=Pi9*eff
        po10=Pi10*eff
        R1=(0.8*po1)/Fc
        R2=(0.8*po2)/Fc
        R3=(0.8*po3)/Fc
        R4=(0.8*po4)/Fc
        R5=(0.8*po5)/Fc
        R6=(0.8*po6)/Fc
        R7=(0.8*po7)/Fc
        R8=(0.8*po8)/Fc
        R9=(0.8*po9)/Fc
        R10=(0.8*po10)/Fc

        print(json.dumps({"Software":[{"The Characteristics of LED completed sucessfully":str(Pi1)}]}))

        
    def APD(self):
        argument = self.arg[0:]
        p1 = float(argument[1])*float(argument[2])
        p2 = float(argument[3])*float(argument[4])
        p3 = float(argument[5])*float(argument[6])
        p4 = float(argument[7])*float(argument[8])
        p5 = float(argument[9])*float(argument[10])
        p6 = float(argument[11])*float(argument[12])
        print(json.dumps({"Software":[{"The Characteristics of APD is completed sucessfully":str(p1)}]}))

         