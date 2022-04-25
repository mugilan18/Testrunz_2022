import json
import math

class FirstYCivil:
    def __init__(self, arg):
        self.arg = arg
    def Impact_test_charpy(self):
        argument = self.arg[:]
        s1 = float(argument[1])*float(argument[2])
        s2 = float(argument[3])*float(argument[4])
        s3 = float(argument[1])*float(argument[2])

        A1 = float(argument[5])*float(argument[6])
        A2 = float(argument[7])*float(argument[8])
        A3 = float(argument[9])*float(argument[10])
        #print(f'A1: {A1}')
        #print(f'A2: {A2}')
        #print(f'A3: {A3}')

        I1 = float(argument[1])/float(argument[2])
        I2 = float(argument[3])/float(argument[4])
        I3 = float(argument[5])/float(argument[6])

        #print(f'I1: {I1}')
        #print(f'I2: {I2}')
        #print(f'I3: {I3}')
        Avg = (I1+I2+I3)/3
        #print(f'Avg: {Avg}')

    

        print(json.dumps({"Impact":[{"Impact 1" : str(I1) }], "Impact":[{"Impact 2" : str(I2) }],"Impact":[{"Impact 3" : str(I3) }], "Average":[{"The  Average of impact test charpy " : str(Avg)}]}))


    def Impact_test_diode(self):
        argument = self.arg[:]
        s1 = float(argument[1])*float(argument[2])
        s2 = float(argument[3])*float(argument[4])
        s3 = float(argument[1])*float(argument[2])

        A1 = float(argument[5])*float(argument[6])
        A2 = float(argument[7])*float(argument[8])
        A3 = float(argument[9])*float(argument[10])
        #print(f'A1: {A1}')
        #print(f'A2: {A2}')
        #print(f'A3: {A3}')

        I1 = float(argument[1])/float(argument[2])
        I2 = float(argument[3])/float(argument[4])
        I3 = float(argument[5])/float(argument[6])

        #print(f'I1: {I1}')
        #print(f'I2: {I2}')
        #print(f'I3: {I3}')
        Avg = (I1+I2+I3)/3
        #print(f'Avg: {Avg}')

    

        print(json.dumps({"Impact":[{"Impact 1" : str(I1) }], "Impact":[{"Impact 2" : str(I2) }],"Impact":[{"Impact 3" : str(I3)}], "Average":[{"The  Average of impact test charpy " : str(Avg)}]}))


    def Erichsen_sheet_metal_test(self):
        argument = self.arg[:]
        A = (float(argument[1])+float(argument[2])+float(argument[0]))/3
        #print(f'A: {A}')

        #print(json.dumps({"Average":[{"The Average of Erichsen sheet metal test" : str(A) +}]}))
        
    def Hardness_test(self):
        argument = self.arg[:]
        BHM1 = (2*float(argument[0]))/((math.pi*float(argument[1]))*(float(argument[2])-(math.sqrt(float(argument[3])**2-float(argument[4])**2))))
        #print(f'BHM1: {BHM1}')
        BHM2 = (2*float(argument[0]))/((math.pi*float(argument[1]))*(float(argument[2])-(math.sqrt(float(argument[3])**2-float(argument[4])**2))))
        #print(f'BHM2: {BHM12}')
        BHM3 = (2*float(argument[0]))/((math.pi*float(argument[1]))*(float(argument[2])-(math.sqrt(float(argument[3])**2-float(argument[4])**2))))
        #print(f'BHM3: {BHM3}')
        A1 = (BHM1+BHM2+BHM3)/3
        #print(f'A1: {A1}')

    
        print(json.dumps({"Average":[{"The Average of hardness test" : str(A1) }]}))
        
    def Rockwell_hardness(self):
        argument = self.arg[:]
        C1 = (float(argument[0])+float(argument[1])+float(argument[2]))/3
        #print(f'C1: {C1}')
        C2 = (float(argument[0])+float(argument[1])+float(argument[2]))/3
        #print(f'C2: {C2}')
        C3 = (float(argument[0])+float(argument[1])+float(argument[2]))/3
        #print(f'C3: {C3}')
        
        print(json.dumps({"Hardness":[{"The  Rock well hardness 1" : str(C1) }], "Hardness":[{"The  Rock well hardness 2" : str(C2) }], "Hardness":[{"The  Rock well hardness 3" : str(C3) }]}))

        
    def Spring_test(self):
        argument = self.arg[:]
        S1 = float(argument[0])/float(argument[6])
        S2 = float(argument[1])/float(argument[7])
        S3 = float(argument[2])/float(argument[8])
        S4 = float(argument[3])/float(argument[9])
        S5 = float(argument[4])/float(argument[0])
        S6 = float(argument[5])/float(argument[1])
        K = (S1+S2+S3+S4+S5+S6)/6
        #print(f'K: {K}')

        MD=(float(argument[0])+float(argument[1]))/2
        #Radius of the spring
        R = MD/2
        #print(f'R: {R}')

        P = (float(argument[2])/(float(argument[3])-1))
        #print(f'P: {P}')

        d = (float(argument[4])-float(argument[5]))/2
        #print(f'd: {d}')

        F = 1/K
        #print(f'F: {F}')

        #import math
        Alpha = P/(2*math.pi*R)
        A = math.cos(Alpha)
        #print(f'A: {A}')

        Zmax = (16*R**3*n*A)/(math.pi*(d**4))*K
        #print(f'Zmax: {Zmax}')
    
        print(json.dumps({"Test":[{"The Spring test rigidity modulus is" : str(Zmax) }]}))
        
       
    def Tension_test(self):
        argument = self.arg[:]
        #import math 
        A0 = (math.pi/4)*float(argument[1])**2
        #print(A0)
        #print(f'A0: {A0}')

        S = float(argument[1])/A0
        #print(f'S: {S}')

        S1 = float(argument[2])/A0
        #print(f'S1: {S1}')

        E = ((float(argument[3])-float(argument[1]))/float(argument[1]))*100
        #print(f'E: {E}')


        N = (math.pi/4)*float(argument[1])**2
        #print(f'N: {N}')

        #% reduction in area
        A = ((A0-N)/A0)*100
        #print(f'A: {A}')

        #Linear strain
        LS1 = (float(argument[7])-float(argument[2]))/float(argument[1])
        #print(f'LS1: {LS1}')
        LS2 = (float(argument[0])-float(argument[1]))/float(argument[2])
        #print(f'LS2: {LS2}')

        print(json.dumps({"Test":[{"The Tension test Linear strain 1 is" : str(LS1) }], "Test":[{"The Tension test Linear strain 2 is" : str(LS2) }]}))
 

    def Torsion_test(self):
        argument = self.arg[:]
        OR = float(argument[0])/2
        #print(f'OR: {OR}')

        #For solid shaft
        #import math
        J = (math.pi*float(argument[1])**4)/32
        #print(f'J: {J}')

        duct = ((float(argument[2]) - float(argument[3]))/float(argument[4]))*100
        #print(f'Dictionary: {duct}')

        Jmax = (float(argument[5])*OR)/J
        #print(f'Jmax: {Jmax}')

        print(json.dumps({"Test":[{"The Tension test is" : str(Jmax) }]}))
                                     
 