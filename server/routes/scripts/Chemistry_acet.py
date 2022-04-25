# import json

# class Chem_acet:
#     def __init__(self, arg):
#         self.arg = arg
#     def Acetic_acid(self):
#         argument = self.arg[0:]
#         def v1(x,y):return x+y
#         V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
#         wt_1= float(argument[1])
#         N1_1=((wt_1*1000)/12600)  #WT1
#         V2_1=int(argument[2])   #20
#         N_2=round((V1_1*N1_1)/V2_1,4) #1
#         wt_2=int(argument[8]) #wt2
#         N2_2=((wt_2*100))
#         V2 = v1(float(argument[10]),float(argument[11])) #FINAL
#         N2= round((V2_1 * N_2 )/V2,4) #2
#         Vinegar= (N2*60)/10
#         Percentage = round(((10000*Vinegar)/ N2_2),2)
#         print(json.dumps({"ans":[{"Amount of acidic acide present in the given vinegar sample =":str(Vinegar)+"N","Percentge of acidic percent in the given vinegar sample=":str(Percentage)+"%"}]}))
#     def oxygen(self):
#         argument = self.arg[0:]
#         def v1(x,y):return x+y
#         V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
#         wt_1= float(argument[1])
#         N1_1=((wt_1*1000)/9806)  #WT1
#         V2_1=int(argument[2])   #20
#         N_2=round((V2_1*N1_1)/V1_1,4) #1
#         wt_2=int(argument[8]) #wt2
#         V2_2=int(argument[10]) # 50ML
#         V2 = v1(float(argument[11]),float(argument[12])) #FINAL
#         N2= round((V2 * N_2 )/V2_2,4) #2
#         Water_sample= (N2*8*1000)
#         print(json.dumps({"ans":[{"Amount of dissolved oxygen present in given eater sample":str(Water_sample)+"ppm"}]}))
#     def edta(self):
#         argument = self.arg[0:]
#         def v1(x,y):return x+y
#         V1_1=v1(float(argument[2]),float(argument[3])) #FINAL
#         V2_1=int(argument[1])   #20
#         N_2=round((V2_1)/V1_1,3) #1

#         V2 = v1(float(argument[8]),float(argument[9])) #FINAL
#         N2= round((V2/ N_2),4) #2
#         sample_hard= round((N2*1000)/20,1)
#         print(json.dumps({"ans":[{"1000 ml of sample hard water contain hardness":str(sample_hard)}]}))
#     def Carbonate(self):
#         argument = self.arg[0:]
#         def v1(x,y):return x+y
#         Wt=float(argument[1]) # weigth
#         N_wt= (Wt*1000/12400)
#         V1=float(argument[2]) # 20ml
#         V2=v1(float(argument[3]),float(argument[4]))
#         N2 = round(V1*N_wt/V2,2)
#         Na2co3=round(N2*2*float(argument[12])/V1,4)
#         NN=round(Na2co3*6200/1000,2)
#         V1_1=float(argument[12])
#         V2_1=float(argument[13])
#         V= round(V2_1- (2*V1_1))
#         N_Na2co3=((NN*V)/V1)
#         NaHCO3=round(N_Na2co3*84/100,2)
#         print(json.dumps({"ans":[{"Amount of Na2co3 present in given solution":str(NN)+"g","Normality of NaHco3=":str(N_Na2co3)+"N","Amount of NaHCO3 present in given solution":str(NaHCO3)+"g"}]}))  
       
#     def mohr(self):
#         argument = self.arg[0:]
#         def v1(x,y):return x+y
#         A= float(argument[15])
#         B= float(argument[16])
#         N2=float(argument[1])
#         V1= float(argument[2])
#         V2=  (A-B)
#         N1= N2*V2 / V1
#         Chloride = round(N1*35.45*1000,2)
#         print(json.dumps({"Answer":[{"Amount of chloride ion present in the given water sample =":str(Chloride)+"ppm"}]}))
        
#     def copper(self):
#         argument = self.arg[0:]
#         def v1(x,y):return x+y
#         V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
#         wt_1= float(argument[1])
#         N1_1=((wt_1*1000)/9806)  #WT1
#         V2_1=int(argument[2])   #20
#         N_2=round((V2_1*N1_1)/V1_1,4) #1
#         wt_2=int(argument[8]) #wt2
#         V2_2=int(argument[10]) # 50ML
#         V2 = v1(float(argument[11]),float(argument[12])) #FINAL
#         N2= round((V2 * N_2 )/V2_2,4) #2
#         Water_sample= round((N2*63.5*100)/1000,3)
#         print(json.dumps({"ans":[{"Amount of chlorine present":str(V2_1)}]}))


import json

class Chem_acet:
    def __init__(self, arg):
        self.arg = arg
    def Acetic_acid(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
        wt_1= float(argument[1])
        N1_1=((wt_1*1000)/12600)  #WT1
        V2_1=int(argument[2])   #20
        N_2=round((V1_1*N1_1)/V2_1,4) #1
        wt_2=int(argument[8]) #wt2
        N2_2=((wt_2*100))
        V2 = v1(float(argument[10]),float(argument[11])) #FINAL
        N2= round((V2_1 * N_2 )/V2,4) #2
        Vinegar= (N2*60)/10
        Percentage = round(((100*Vinegar)/ N2_2),2)
        print(json.dumps({"ans":[{"Amount of acidic acide present in the given vinegar sample =":str(N2)+"N","Percentge of acidic percent in the given vinegar sample=":str(Percentage)+"%"}]}))
    def oxygen(self):
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
    def edta(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        V1_1=v1(float(argument[2]),float(argument[3])) #FINAL
        V2_1=int(argument[1])   #20
        N_2=round((V2_1)/V1_1,3) #1

        V2 = v1(float(argument[8]),float(argument[9])) #FINAL
        N2= round((V2/ N_2),4) #2
        sample_hard= round((N2*1000)/20,1)
        print(json.dumps({"ans":[{"1000 ml of sample hard water contain hardness":str(sample_hard)}]}))
    def Carbonate(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        Wt=float(argument[1]) # weigth
        N_wt= (Wt*1000/12400)
        V1=float(argument[2]) # 20ml
        V2=v1(float(argument[3]),float(argument[4]))
        N2 = round(V1*N_wt/V2,2)
        Na2co3=round(N2*2*float(argument[12])/V1,4)
        NN=round(Na2co3*6200/1000,2)
        V1_1=float(argument[12])
        V2_1=float(argument[13])
        V= round(V2_1- (2*V1_1))
        N_Na2co3=((NN*V)/V1)
        NaHCO3=round(N_Na2co3*84/100,2)
        print(json.dumps({"ans":[{"Amount of Na2co3 present in given solution":str(NN)+"g","Normality of NaHco3=":str(N_Na2co3)+"N","Amount of NaHCO3 present in given solution":str(NaHCO3)+"g"}]}))  
       
    def mohr(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        A= float(argument[15])
        B= float(argument[16])
        N2=float(argument[1])
        V1= float(argument[2])
        V2=  (A-B)
        N1= N2*V2 / V1
        Chloride = round(N1*35.45*1000,2)
        print(json.dumps({"Answer":[{"Amount of chloride ion present in the given water sample =":str(Chloride)+"ppm"}]}))
   
    def Bleaching_powder(self):
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
        Water_sample= round((N2*35.45*100)/1000,3)
        print(json.dumps({"ans":[{"Amount of chlorine present":str(Water_sample)}]}))
    def copper(self):
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
        Water_sample= round((N2*63.5*100)/1000,4)
        print(json.dumps({"ans":[{"Amount of chlorine present":str(Water_sample)}]}))
    def Conductometry(self):
        argument = self.arg[0:]
        V1=(float(argument[43])) #20  
        N1 = (float(argument[44])) #  n  
        V2= (float(argument[45]))
        N2= round((V1*N1)/V2,4)
        print(json.dumps({"ans":[{"Amount of lead present in the given":str(N2)}]}))
    def Magnesium(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
        wt_1= float(argument[1])
        N1_1=((wt_1)/287.5)  #WT1
        V2_1=int(argument[2])   #20
        N_2=round((V2_1*N1_1)/V1_1,4) #1
        wt_2=int(argument[8]) #wt2
        V2_2=int(argument[10]) # 50ML
        V2 = v1(float(argument[11]),float(argument[12])) #FINAL
        N2= round((V2 * N_2 )/V2_2,4) #2
        Magnes= round((N2*24*100)/1000,4)
        print(json.dumps({"ans":[{"Amount of magnesium=":str(Magnes)+"g"}]}))
    def calcium(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
        wt_1= float(argument[1])
        N1_1=((wt_1*1000)/12600)  #WT1
        V2_1=int(argument[2])   #20
        N_2=round((V2_1*N1_1)/V1_1,4) #1
        wt_2=int(argument[8]) #wt2
        V2_2=int(argument[10]) # 50ML
        V2 = v1(float(argument[11]),float(argument[12])) #FINAL
        N2= round((V2 * N_2 )/V2_2,4) #2
        Permanganometry= round((N2*24*100)/1000,4)
        print(json.dumps({"ans":[{"Amount of CA2+ present in given solution=":str(Permanganometry)+"g"}]}))
    def ferrous(self):
        argument = self.arg[0:]
        def v1(x,y):return x+y
        V1_1=v1(float(argument[3]),float(argument[4])) #FINAL
        wt_1= float(argument[1])
        N1_1=((wt_1*1000)/12600)  #WT1
        V2_1=int(argument[2])   #20
        N_2=round((V2_1*N1_1)/V1_1,4) #1
        V2_2=int(argument[10]) # 50ML
        V2 = v1(float(argument[11]),float(argument[12])) #FINAL
        N2= round((V2 * N_2 )/V2_2,4) #2
        ferrous= round((N2*55.85*100)/1000,4)
        print(json.dumps({"ans":[{"Amount of Fe2+ present in given solution=":str(ferrous)+"g"}]}))