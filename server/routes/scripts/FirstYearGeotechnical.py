import json
import math

class FirstYGtech:
    def __init__(self, arg):
        self.arg = arg
        
    def UCT(self):
        argument = self.arg[0:]
        #load factor lf
        lf = float(argument[33])
        #deformation daia dd
        Dd = float(argument[34])
        # initital length lo
        lo = float(argument[35])
        # initital area lo
        A = float(argument[36])
        # Axial load 
        P1 = float(argument[1]) * lf
        P2 = float(argument[3]) * lf
        P3 = float(argument[5]) * lf
        P4 = float(argument[7]) * lf
        P5 = float(argument[9]) * lf
        P6 = float(argument[11]) * lf
        P7 = float(argument[13]) * lf
        P8 = float(argument[15]) * lf
        P9 = float(argument[17]) * lf
        P10 = float(argument[19]) * lf
        P11 = float(argument[21]) * lf
        P12 = float(argument[23]) * lf
        P13 = float(argument[25]) * lf
        P14 = float(argument[27]) * lf
        P15 = float(argument[29]) * lf
        P16 = float(argument[31]) * lf

        #total displacement

        L1 = float(argument[2]) * Dd
        L2 = float(argument[4]) * Dd
        L3 = float(argument[6]) * Dd
        L4 = float(argument[8]) * Dd
        L5 = float(argument[10]) * Dd
        L6 = float(argument[12]) * Dd
        L7 = float(argument[14]) * Dd
        L8 = float(argument[16]) * Dd
        L9 = float(argument[18]) * Dd
        L10 = float(argument[20]) * Dd
        L11 = float(argument[22]) * Dd
        L12 = float(argument[24]) * Dd
        L13 = float(argument[26]) * Dd
        L14 = float(argument[28]) * Dd
        L15 = float(argument[30]) * Dd
        L16 = float(argument[32]) * Dd        

        #Corrected Area
        AC1 = A/(1-(L1/lo))
        AC2 = A/(1-(L2/lo))
        AC3 = A/(1-(L3/lo))
        AC4 = A/(1-(L4/lo))
        AC5 = A/(1-(L5/lo))
        AC6 = A/(1-(L6/lo))
        AC7 = A/(1-(L7/lo))
        AC8 = A/(1-(L8/lo))
        AC9 = A/(1-(L9/lo))
        AC10 = A/(1-(L11/lo))
        AC11 =  A/(1-(L11/lo))
        AC12 =  A/(1-(L12/lo))
        AC13 =  A/(1-(L13/lo))
        AC14 =  A/(1-(L14/lo))
        AC15 =  A/(1-(L15/lo))
        AC16 =  A/(1-(L16/lo))
      

        #stress
        S1 = round(float(P1)/AC1,2)
        S2 = round(float(P2)/AC2,2)
        S3 = round(float(P3)/AC3,2)
        S4 = round(float(P4)/AC4,2)
        S5 = round(float(P5)/AC5,2)
        S6 = round(float(P6)/AC6,2)
        S7 = round(float(P7)/AC7,2)
        S8 = round(float(P8)/AC8,2)
        S9 = round(float(P9)/AC9,2)
        S10 = round(float(P10)/AC10,2)
        S11 = round(float(P11)/AC11,2)
        S12 = round(float(P12)/AC12,2)
        S13 = round(float(P13)/AC13,2)
        S14 = round(float(P14)/AC14,2)
        S15 = round(float(P15)/AC15,2)
        S16 = round(float(P16)/AC16,2)
    
        # shear stress
        SS1 = round(S1/2,2)
        SS2 = round(S2/2,2)
        SS3 = round(S3/2,2)
        SS4 = round(S4/2,2)
        SS5 = round(S5/2,2)
        SS6 = round(S6/2,2)
        SS7 = round(S7/2,2)
        SS8 = round(S8/2,2)
        SS9 = round(S9/2,2)
        SS10 = round(S10/2,2)
        SS11 = round(S11/2,2)
        SS12 = round(S12/2,2)
        SS13 = round(S13/2,2)
        SS14 = round(S14/2,2)
        SS15 = round(S15/2,2)
        SS16 = round(S16/2,2)

        print(json.dumps({"Test":[{"The Stress  is" : str(S1)+" and the strain is : "+str(SS1)}]}))
        
        
    def Core_cutter_method(self):
        argument = self.arg[0:]
        Water_content = ((float(argument[0]) - float(argument[1]))/(float(argument[2])-float(argument[3])))*100
        w = Water_content/100

        #Bulk unit weight
        mass = float(argument[4])*9.81
        BUW = mass/float(argument[5])

        # Dry unit weight
        DUW = BUW/(1+w)

        #Void ratio
        G = 2.6
        e = ((G*9.81)/DUW)-1

        # Degree of saturation
        Sr = (G*w)/e

        #porosity
        n = e/(1+e)

        print(json.dumps({"Test":[{"The porosity of Core cutter method is" : str(n)}]}))
        
        
    def Grain_size_analysis(self):
        argument = self.arg[0:]

        #percentage weight of soil retaining
        PW1 = (float(argument[0])/float(argument[8]))*100
        PW2 = (float(argument[1])/float(argument[9]))*100
        PW3 = (float(argument[2])/float(argument[0]))*100
        PW4 = (float(argument[3])/float(argument[1]))*100
        PW5 = (float(argument[4])/float(argument[2]))*100
        PW6 = (float(argument[5])/float(argument[3]))*100
        PW7 = (float(argument[5])/float(argument[4]))*100
        PW8 = (float(argument[6])/float(argument[5]))*100
        PW9 = (float(argument[7])/float(argument[6]))*100

        #Cumulative relative percentage
        CP1 = PW1
        CP2 = CP1+PW2
        CP3 = CP2+PW3
        CP4 = CP3+PW4
        CP5 = CP4+PW5
        CP6 = CP5+PW6
        CP7 = CP6+PW7
        CP8 = CP7+PW8
        CP9 = CP8+PW9

        # find uniform co-efficient
        Cu=float(argument[0])/float(argument[1])

        #Co_efficient of curvature
        Cc=(float(argument[1])**2)/(float(argument[1])*float(argument[2]))

        print(json.dumps({"Test":[{"The Co_efficient of curvature in Grain size analysis is" : str(Cc)}]}))

        
    def Sedimentation_Analysis(self):
        argument = self.arg[0:]

        D = math.sqrt((30*float(argument[0]))/980*(float(argument[1])-float(argument[2])))* math.sqrt(float(argument[3])/float(argument[4]))
        NF = ((100*float(argument[1]))/(float(argument[2])*(float(argument[3])-1)))*(float(argument[4]) - float(argument[5]))

        print(json.dumps({"Test":[{"The output of Sedimentation Analysis is" : str(NF)}]}))
    
    def Permiability_of_hydraaulic_conductivity(self):
        argument = self.arg[0:]
            #average
        t1=(float(argument[0])+float(argument[3])+float(argument[6]))/3
        t2=(float(argument[1])+float(argument[4])+float(argument[7]))/3
        t3=(float(argument[2])+float(argument[5])+float(argument[8]))/3

        #Co-efficient of permibility
        Rs1 = t1*float(argument[0])/(float(argument[3])*float(argument[6])*float(argument[9]))
        Rs2 = t2*float(argument[1])/(float(argument[4])*float(argument[7])*float(argument[0]))
        Rs3 = t3*float(argument[2])/(float(argument[5])*float(argument[8])*float(argument[1]))


        k1 =(((2.3*float(argument[0])*float(argument[1]))/(float(argument[2])*float(argument[3])))*(math.log(float(argument[1])/float(argument[2]))))
        k2 =(((2.3*float(argument[1])*float(argument[2]))/(float(argument[3])*float(argument[4])))*(math.log(float(argument[1])/float(argument[1]))))
        k3 =(((2.3*float(argument[2])*float(argument[4]))/(float(argument[4])*float(argument[4])))*(math.log(float(argument[4])/float(argument[5]))))

        print(json.dumps({"Test":[{"The Permiability of hydraaulic conductivity is" : str(k3)}]}))

        
    def Liquid_and_plastic_limit_final(self):
        argument = self.arg[0:]
        #Water content calculation
        WC1 = ((float(argument[0])-float(argument[6]))/(float(argument[2])-float(argument[8])))*100
        WC2 = ((float(argument[1])-float(argument[7]))/(float(argument[3])-float(argument[9])))*100
        WC3 = ((float(argument[2])-float(argument[8]))/(float(argument[4])-float(argument[0])))*100
        WC4 = ((float(argument[3])-float(argument[9]))/(float(argument[5])-float(argument[1])))*100
        WC5 = ((float(argument[4])-float(argument[0]))/(float(argument[6])-float(argument[2])))*100
        WC6 = ((float(argument[5])-float(argument[1]))/(float(argument[7])-float(argument[3])))*100
        Wl= (WC1+WC2+WC3+WC4+WC5+WC6)/6


        Wc1 = ((float(argument[1])-float(argument[3]))/(float(argument[5])-float(argument[7])))*100
        Wc2 = ((float(argument[2])-float(argument[4]))/(float(argument[6])-float(argument[6])))*100
        Wp = (Wc1+Wc2)/2

        Ip = Wl-Wp

        #flow index
        #import math
        W1 = (float(argument[1])+float(argument[3]))/2
        W2 = (float(argument[2])+float(argument[4]))/2
        If =(W2-W1)/(math.log10(float(argument[1])/float(argument[2])))

        #toughness index
        It = If/Ip


        print(json.dumps({"Test":[{"The toughness index of Liquid and plastic limit final is" : str(It)}]}))
        
    def Direct_shear_test(self):
        argument = self.arg[0:]
     
        phi= 31
        def theta(a):
            return ((a*1000000)/(float(argument[9])*1000))
        theta1=round(theta(float(argument[1])),2)
        theta2=round(theta(float(argument[3])),2)
        theta3=round(theta(float(argument[5])),2)
        theta4=round(theta(float(argument[7])),2)
        def stress(a):
            return ((a*1000000)/(float(argument[9])*1000))
        stress1=round(stress(float(argument[2])),2)
        stress2=round(stress(float(argument[4])),2)
        stress3=round(stress(float(argument[6])),2)
        stress4=round(stress(float(argument[8])),2)
        print(json.dumps({"Impact":[{"The Normal stress and Shear stress failure are at Row 1  ": str(theta1)+" and "+str(stress1)+" respectively","The Normal stress and Shear stress failure are at Row 2  ":str(theta2)+" and "+str(stress2)+" respectively","The Normal stress and Shear stress failure are at Row 3  ":str(theta3)+" and "+str(stress3)+" respectively","The Normal stress and Shear stress failure are at Row 4  ":str(theta4)+" and "+str(stress4)+" respectively"}]}))
      


        
        
    def Determination_of_shrinkage_limit(self):
        argument = self.arg[0:]

        #Volume of wet soil pat
        v1 = float(argument[1])/13.6
        v2 = float(argument[2])/13.6

        #Shrinkage limit
        Ws1 = (float(argument[1])-(((v1-float(argument[2]))/float(argument[3]))*100))

        Ws2 = (float(argument[3])-(((v2-float(argument[4]))/float(argument[5]))*100))

        Ws = (Ws1+Ws2)/2

            #shrinkage ratio
        wd = (float(argument[1])+float(argument[2]))/2
        Sr = wd/(float(argument[3])*float(argument[4]))

        #volumetric shrinkage
        Vs = (float(argument[1])-Ws)*Sr
        
        print(json.dumps({"Test":[{"The volumetric shrinkage output is" : str(Vs)}]}))
        
        
    def Specific_Gravity(self):
        argument = self.arg[0:]

        #Specific gravity of CG soil
        CGs = round(float(argument[4])/(float(argument[3])-(float(argument[1])-float(argument[2]))),2)
        #Specific gravity of CG soil
        FGs = round((float(argument[6])-float(argument[5]))/((float(argument[8])-float(argument[5]))-(float(argument[7])-float(argument[6]))),2)
        print(json.dumps({"Soil":[{"The Specific gravity of CG soil is" : str(CGs),"The Specific gravity of FG soil is" : str(FGs)}]}))
        
        
    def Determination_of_free_swell_index(self):
        argument = self.arg[0:]

        #free swell Index
        FSI = ((float(argument[1])-float(argument[3]))/float(argument[2]))*100


        print(json.dumps({"Test":[{"The free swell Index is" : str(FSI)}]}))

        
    def Standard_proctor(self):
        argument = self.arg[0:]
        A=float(argument[1])
        B=float(argument[2])
        print(json.dumps({"Test":[{"The maximum dry density of the given soil sample is":str(A),"The optimum moisture content is":str(B)}]}))
   

 
    def Triaxial_Shear_test(self):
        argument = self.arg[0:]

        #strain
        E1 = (float(argument[1])/float(argument[1]))
        E2 = (float(argument[2])/float(argument[2]))
        E3 = (float(argument[3])/float(argument[3]))
        E4 = (float(argument[4])/float(argument[4]))
        E5 = (float(argument[5])/float(argument[5]))
        E6 = (float(argument[6])/float(argument[5]))
        E7 = (float(argument[7])/float(argument[6]))
        E8 = (float(argument[8])/float(argument[6]))
        E9 = (float(argument[9])/float(argument[7]))
        E10 = (float(argument[0])/float(argument[8]))
        E11 = (float(argument[1])/float(argument[9]))
        E12 = (float(argument[2])/float(argument[0]))
        E13 = (float(argument[3])/float(argument[1]))
        E14 = (float(argument[4])/float(argument[2]))
        E15 = (float(argument[5])/float(argument[3]))
        E16 = (float(argument[6])/float(argument[4]))
        E17 = (float(argument[7])/float(argument[5]))
        E18 = (float(argument[8])/float(argument[6]))

        AC1 = (float(argument[1])/(1-E1))
        AC2 = (float(argument[2])/(1-E2))
        AC3 = (float(argument[3])/(1-E3))
        AC4 = (float(argument[4])/(1-E4))
        AC5 = (float(argument[5])/(1-E5))
        AC6 = (float(argument[6])/(1-E6))
        AC7 = (float(argument[6])/(1-E7))
        AC8 = (float(argument[7])/(1-E8))
        AC9 = (float(argument[8])/(1-E9))
        AC10 = (float(argument[9])/(1-E10))
        AC11 = (float(argument[0])/(1-E11))
        AC12 = (float(argument[1])/(1-E12))
        AC13 = (float(argument[2])/(1-E13))
        AC14 = (float(argument[3])/(1-E14))
        AC15 = (float(argument[4])/(1-E15))
        AC16 = (float(argument[6])/(1-E16))
        AC17 = (float(argument[7])/(1-E17))
        AC18 = (float(argument[8])/(1-E18))

        #stress
        S1 = float(argument[0])/float(argument[0])
        S2 = float(argument[1])/float(argument[1])
        S3 = float(argument[2])/float(argument[2])
        S4 = float(argument[3])/float(argument[3])
        S5 = float(argument[4])/float(argument[4])
        S6 = float(argument[5])/float(argument[5])
        S7 = float(argument[5])/float(argument[6])
        S8 = float(argument[6])/float(argument[6])
        S9 = float(argument[7])/float(argument[7])
        S10 = float(argument[8])/float(argument[7])
        S11 = float(argument[9])/float(argument[4])
        S12 = float(argument[0])/float(argument[2])
        S13 = float(argument[1])/float(argument[4])
        S14 = float(argument[2])/float(argument[1])
        S15 = float(argument[3])/float(argument[2])
        S16 = float(argument[4])/float(argument[4])
        S17 = float(argument[5])/float(argument[5])
        S18 = float(argument[6])/float(argument[6])

        #strain
        e1 = (float(argument[0])/float(argument[0]))
        e2 = (float(argument[1])/float(argument[1]))
        e3 = (float(argument[2])/float(argument[2]))
        e4 = (float(argument[3])/float(argument[3]))
        e5 = (float(argument[4])/float(argument[4]))
        e6 = (float(argument[5])/float(argument[4]))
        e7 = (float(argument[6])/float(argument[5]))
        e8 = (float(argument[7])/float(argument[6]))
        e9 = (float(argument[8])/float(argument[1]))
        e10 = (float(argument[9])/float(argument[3]))
        e11 = (float(argument[0])/float(argument[3]))
        e12 = (float(argument[1])/float(argument[4]))
        e13 = (float(argument[2])/float(argument[4]))
        e14 = (float(argument[3])/float(argument[5]))
        e15 = (float(argument[4])/float(argument[6]))
        e16 = (float(argument[5])/float(argument[1]))
        e17 = (float(argument[6])/float(argument[4]))
        e18 = (float(argument[1])/float(argument[5]))
        e19 = (float(argument[2])/float(argument[1]))
        e20 = (float(argument[2])/float(argument[5]))
        e21 = (float(argument[5])/float(argument[5]))

        S1 = float(argument[0])/float(argument[1])
        S2 = float(argument[2])/float(argument[2])
        S3 = float(argument[3])/float(argument[3])
        S4 = float(argument[4])/float(argument[3])
        S5 = float(argument[5])/float(argument[4])
        S6 = float(argument[6])/float(argument[5])
        S7 = float(argument[7])/float(argument[6])
        S8 = float(argument[7])/float(argument[7])
        S9 = float(argument[8])/float(argument[7])
        S10 = float(argument[8])/float(argument[1])
        S11 = float(argument[9])/float(argument[2])
        S12 = float(argument[0])/float(argument[4])
        S13 = float(argument[1])/float(argument[0])
        S14 = float(argument[2])/float(argument[1])
        S15 = float(argument[3])/float(argument[3])
        S16 = float(argument[4])/float(argument[2])
        S17 = float(argument[5])/float(argument[4])
        S18 = float(argument[6])/float(argument[5])
        s19 = float(argument[6])/float(argument[6])
        s20 = float(argument[7])/float(argument[7])
        s21 = float(argument[9])/float(argument[7])

        gama1 = float(argument[0])+float(argument[2])
        gama2 = float(argument[1])+float(argument[3])
        ratio1 = gama1/float(argument[4])
        ratio2 = gama2/float(argument[5])

        print(json.dumps({"Test":[{"The ratio of Triaxial Shear test is" : str(ratio1),"and":str(ratio2)}]}))        
        # print(json.dumps({"Test":[{"The ratio of Triaxial Shear test  is" : str(ratio2)}]}))

