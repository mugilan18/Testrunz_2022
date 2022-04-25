#Import library
import json
import math


class EVS:
    def __init__(self, arg):
        self.arg = arg

    def total_solids(self):
        argument = self.arg[0:]
        TS = ((float(argument[2])-float(argument[1]))/float(argument[3]))*10**6
        print(json.dumps({"hardness":[{"Total solids present in the given water sample" : str(TS) + " mg/L" }]}))

    def alkalinity(self):
        argument = self.arg[0:]
        #print(argument)
        P = (float(argument[2])+float(argument[6]))/2

        C = (float(argument[4])+float(argument[8]))/2
        M2 = ((P*0.05)/1)*(2/C)
        P1 = (float(argument[10])+float(argument[15]))/2
        C1 = (float(argument[13])+float(argument[18]))/2
        M1 = ((P1*M2)/1)*(1/C1)
        co3 = M1*60*1000

        print(json.dumps({"alkalinity":[{"The alkalinity of given water sample" : str(co3) + " mg/L" }]}))


    def chloride(self):
        argument = self.arg[0:]
        #print(argument)
        P = ( float(argument[2])+ float(argument[6]))/2
        B = ( float(argument[4])+ float(argument[8]))/2
        A = (float(argument[12])+float(argument[16]))/2
        Acl = ((A-B)*0.0172*35.45*1000)/P
        print(json.dumps({"chloride":[{"Amount of chloride present in the given sample" : str(Acl) + " mg/L" }]}))
   
    def total_hardness(self):
        argument = self.arg[0:]
        C1 = (float(argument[4])+float(argument[8]))/2
        C2 = (float(argument[12])+float(argument[16]))/2
        V = (C2/C1)*1000

        print(json.dumps({"hardness":[{"Total hardness of the given sample" : str(V) + " mg/L" }]}))
    

    def chlorine(self):
        argument = self.arg[0:]
        #print(argument)
        P = (float(argument[2])+float(argument[6]))/2
        B = (float(argument[4])+float(argument[8]))/2
        M2 = (((P*0.002)/1)*(6/B))
        A = (float(argument[12])+float(argument[16]))/2
        Acl = ((35.45)*A*M2*1000)/P
        print(json.dumps({"chlorine":[{"Amount of residual chlorine present in the given sample" : str(Acl) + " mg/L" }]}))

    def dissolved_oxygen(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
        wt_1= float(argument[1])
        N1_1=((wt_1*1000)/9806)  #WT1
        V2_1=int(argument[2])   #20
        N_2=round((V2_1*N1_1)/V1_1,4) #1
        wt_2=int(argument[8]) #wt2
        V2_2=int(argument[10]) # 50ML
        V2 = v1(float(argument[11]),float(argument[12])) #FINAL
        N2= round((V2 * N_2 )/V2_2,4) #2
        Water_sample= (N2*8*1000)
        print(json.dumps({"ans":[{"Amount of dissolved oxygen present in given eater sample":str(Water_sample)+"ppm"}]}))

    def COD(self):
        argument = self.arg[0:]
        #print(argument)
        V1 = (float(argument[2]) + float(argument[6]))/2
        N1 = (float(argument[3]) + float(argument[7]))/2
        V2 = (float(argument[4]) + float(argument[8]))/2
        K = (float(argument[1]) + float(argument[1]))/2
        #print (f'K: {K}')
        N2 = (V1 * N1)/V2
        #print(f'N2: {N2}')
    
        V4 = (float(argument[10]) + float(argument[14]))/2
        V3 = (float(argument[12]) + float(argument[16]))/2
        N3 = (float(argument[13]) * float(argument[17]))/2
        N = (V3 * N3)/V4
        #print(f'N2: {N2}')
        M = (N * float(argument[1]) * 100)/1000
        #print(f'A: {A}'
        print(json.dumps({"Normality":[{"The  Normality of fas" : str(N2) + " N"}], "Normality":[{"The  Normality of COD" : str(N) + " N"}], "Amount":[{"The  amount of copper " : str(M) + " "}]}))
    
    # def SS(self):
    #     argument = self.arg[0:]
    #     a= float(argument[1])
    #     print(json.dumps({"ans":[{"The concentration of settleable solids in the given water sample is" : str(a)+"ml/lit"}]}))
