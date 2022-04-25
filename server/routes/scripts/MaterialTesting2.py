import json
import math

class MT2:
    def __init__(self, arg):
        self.arg = arg

    def Gravity(self):
        argument = self.arg[0:]
        G1=(float(argument[2]) - float(argument[1]))
        G2=(float(argument[3]) - float(argument[4]))
        G = round(G1/( (G1 - G2)  * 0.79),2)
        print(json.dumps({"gravity":[{"Specific gravity of cement" : str(G)}]}))

    def Fine_aggregate(self):
        argument = self.arg[0:]
        W1=(float(argument[1]))
        W2=(float(argument[2]))
        W3=(float(argument[3]))
        W4=(float(argument[4]))
        W= round(W4 /(W3 - (W1-W2)),2)
        S= round(((W3-W4)/W4)*100,2)
        print(json.dumps({"gravity":[{"Specific gravity of fine aggregate" : str(W),"Water absorption":str(S)}]}))

    def coarse_aggregate(self):
        argument = self.arg[:]
        W1=(float(argument[1]))
        W2=(float(argument[2]))
        W3=(float(argument[3]))
        W4=(float(argument[4]))
        W= round(W4 /(W3 - (W1-W2)),2)
        S= round(((W3-W4)/W4)*100,2)
        print(json.dumps({"gravity":[{"Specific gravity of coarse aggregate" : str(W),"Water absorption":str(S)}]}))

    def Slump(self):
        argument = self.arg[:]
        G = float(argument[1])
        print(json.dumps({"Consistency":[{"The slump value of the concrete is " : str(G)+"mm"}]}))

    def Bulk(self):
        argument = self.arg[:]
        h1 = float(argument[1])
        h2 = float(argument[2])
        B = ((h1-h2)/h2)*100
        print(json.dumps({"bulk":[{"Bulking of a given sample of fine aggregate is found to be " : str(B) + "minutes"}]}))

    def Size_aggregate(self):
        argument = self.arg[:]
        #print(argument)
        C1 = (float(argument[2]) - float(argument[1]))
        C2 = (float(argument[6]) - float(argument[5]))
        C3 = (float(argument[10]) - float(argument[9]))
        C4 = (float(argument[14]) - float(argument[13]))
        C5 = (float(argument[18]) - float(argument[17]))
        C6 = (float(argument[22]) - float(argument[21])) 
    
        F1 = (100 - float(argument[4]))
        F2 = (100 - float(argument[8]))
        F3 = (100 - float(argument[12]))
        F4 = (100 - float(argument[16]))
        F5 = (100 - float(argument[20]))
        F6 = (100 - float(argument[24]))
    
        F = (float(argument[4]) + float(argument[8]) + float(argument[12]) + float(argument[16]) + float(argument[20])+ float(argument[24]))/100

        print(json.dumps({"gravity":[{"The finess modulus of coarse aggregate" : str(F)}]}))

    def particle_aggregate(self):
        argument = self.arg[:]
        E1 = (float(argument[1]) + float(argument[1]))
        E2 = E1 + float(argument[3])
        E3 = E2 + float(argument[5])
        E4 = E3 + float(argument[7])
        E5 = E4 + float(argument[9])
        E6 = E5 + float(argument[11]) 
    
        R1 = E1/10
        R2 = E2/10
        R3 = E3/10
        R4 = E4/10
        R5 = E5/10
        R6 = E6/10
    
        F = (R1+R2+R3+R4+R5+R6)/100
        print(json.dumps({"gravity":[{"The finess modulus of a given sample of fine aggregate is " : str(F)}]}))

    def Consistency(self):
        argument = self.arg[:]
        G = float(argument[1])
        print(json.dumps({"Consistency":[{"The normal consistency of a given sample if cement is " : str(G)}]}))

    def Setting_time(self):
        argument = self.arg[:]
        I = float(argument[7])
        F = float(argument[9])
        Consistency= (I/100)*F
        print(json.dumps({"initial":[{"The given sample of cement the standard consistency is achieved with waterpercentage of = ":str(Consistency)+"gms"}]}))

    def Vee_Bee(self):
        argument = self.arg[:]
        G = float(argument[1])
        print(json.dumps({"Consistency":[{"The consistency of the concrete is " : str(G)+ "Seconds"}]}))

    def compaction(self):
        argument = self.arg[:]
        G = (float(argument[2])-float(argument[1]))/(float(argument[3])-float(argument[1]))
        print(json.dumps({"Compaction":[{"The compaction factor of the given sample of concrete is " : str(G)}]}))
    def compression(self):
        argument = self.arg[:]
        Area = float(argument[2])*float(argument[3])
        Volume =( (float(argument[4]))*(float(argument[5]))*(float(argument[6])))
        CS =( float(argument[1])*1000)/Area
        print(json.dumps({"Compression":[{"The compressive strength of cement concrete" : str(),"Area":str(Area)+"mm2","Volume":str(Volume)+"mm3","Compressive Strength":str(CS)+" N/mm2"}]}))

    def Flexural(self):
        argument = self.arg[:]
        a= float(argument[3])
        def Fsk1(a,b,c,d):return(((a*1000)*(b*10))/((c*10)*((d*10)**2)))
        def Fsk2(a,b,c,d):return((3*a*b)/(c*(d**2)))
        F1= round(Fsk1(float(argument[1]),float(argument[2]),float(argument[4]),float(argument[5])),2)
        F2= round(Fsk2(float(argument[1]),float(argument[2]),float(argument[4]),float(argument[5])),2)
        if a>20:
            print(json.dumps({"strenght":[{"The strength of the concrete by using a flexure test(Fck)" : str(F1)+"N/mm2"}]}))
        else:
            print(json.dumps({"strenght":[{"The strength of the concrete by using a flexure test(Fck)" : str(F2)+"N/mm2"}]}))


