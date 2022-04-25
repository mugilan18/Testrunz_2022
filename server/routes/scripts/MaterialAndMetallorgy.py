import json
import math
class MAM:
    def __init__(self, arg):
        self.arg = arg
    def Impact_test_charpy(self):
        argument = self.arg[0:]
        def Avg(x,y):return(x+y)/2
        C1= round(Avg(float(argument[6]),float(argument[11])),2)
        C2=round(Avg(float(argument[7]),float(argument[12])),4)
        C3= round(Avg(float(argument[8]),float(argument[13])),2)
        C4= round(Avg(float(argument[9]),float(argument[14])),3)
        print(json.dumps({"Impact":[{"Average charpy impact value":str(C1)+ "kgfm" ,"Average charpy impact strength":str(C2)+ "Kgfm/mm2","Average Izod impact value":str(C3)+ "Kgfm","Average Izod impact strength":str(C4)+ "Kgfm/mm2"}]}))


    def Impact_test_diode(self):
        argument = self.arg[0:]
        def Impact(x,y,z):
            return((x-y)/z)
        I1=Impact(float(argument[12]),float(argument[11]),float(argument[14]))
        I2=Impact(float(argument[16]),float(argument[15]),float(argument[18]))
        
        print(json.dumps({"Impact":[{"Impact strength of the specimen_1":str(I1)+ " joules/mm2","Impact strength of the specimen_2":str(I2)+ " joules/mm2" }]}))


    def Erichsen_sheet_metal_test(self):
        argument = self.arg[:]
        A = (float(argument[4])+float(argument[8])+float(argument[12]))/3
        print(json.dumps({"Average":[{"Average Erichsen value for aluminium" : str(A)}]}))
        
    def Hardness_test(self):
        argument = self.arg[:]
        #got output
        BHM1 = (2*float(argument[2]))/((math.pi*float(argument[1]))*(float(argument[1])-(math.sqrt(float(argument[1])**2-float(argument[3])**2))))
        BHM2 = (2*float(argument[5]))/((math.pi*float(argument[4]))*(float(argument[4])-(math.sqrt(float(argument[4])**2-float(argument[6])**2))))
        BHM3 = (2*float(argument[8]))/((math.pi*float(argument[7]))*(float(argument[7])-(math.sqrt(float(argument[7])**2-float(argument[9])**2))))
        BHM = (BHM1+BHM2+BHM3)/3
        BH1 = (2*float(argument[11]))/((math.pi*float(argument[10]))*(float(argument[10])-(math.sqrt(float(argument[10])**2-float(argument[12])**2))))
        BH2 = (2*float(argument[14]))/((math.pi*float(argument[13]))*(float(argument[13])-(math.sqrt(float(argument[13])**2-float(argument[15])**2))))
        BH3 = (2*float(argument[17]))/((math.pi*float(argument[16]))*(float(argument[16])-(math.sqrt(float(argument[16])**2-float(argument[18])**2))))
        BH = (BH1+BH2+BH3)/3
        B1 = (2*float(argument[20]))/((math.pi*float(argument[19]))*(float(argument[19])-(math.sqrt(float(argument[19])**2-float(argument[21])**2))))
        B2 = (2*float(argument[23]))/((math.pi*float(argument[22]))*(float(argument[22])-(math.sqrt(float(argument[22])**2-float(argument[24])**2))))
        B3 = (2*float(argument[26]))/((math.pi*float(argument[25]))*(float(argument[25])-(math.sqrt(float(argument[25])**2-float(argument[27])**2))))
        B = (B1+B2+B3)/3
        print(json.dumps({"Average":[{"Brinell hardness number for Copper" : str(BHM),"Brinell hardness number for Aluminium" : str(BH),"Brinell hardness number for Cast iron" : str(B) }]}))
        
    def Rock_well_hardness(self):
        argument = self.arg[0:]
        #print(argument)got output
        C1 = round((float(argument[3])+float(argument[4])+float(argument[5]))/3,2)
        C2 =round((float(argument[8])+float(argument[9])+float(argument[10]))/3,2)
        C3 =round((float(argument[13])+float(argument[14])+float(argument[15]))/3,2)
        print(json.dumps({"length":[{"Rock well hardness number in copper" : str(C1)}], "breadth":[{"Rock well hardness number in Aluminium" : str(C2) }], "width":[{"Rock well hardness number in cast iron" : str(C3)}]}))

    def Torsion(self):
        argument = self.arg[0:]
        L= float(argument[1])
        D=float(argument[2])
        J=D**4*0.0981
        def T(x):
            return(x*9.81*10)
        def ang(x):
            return(x*0.017)
        def G(t,a):
            return((t*L)/(a*J))
        T1=T(float(argument[3]))
        T2=round(T(float(argument[5])),2)
        T3=round(T(float(argument[7])),2)
        T4=round(T(float(argument[9])),2)
        ang1=math.radians(float(argument[4]))
        ang2=round(ang(float(argument[6])),2)
        ang3=round(ang(float(argument[8])),2)
        ang4=round(ang(float(argument[10])),2)
        G1=round(G(T1,ang1),3)
        G2=round(G(T2,ang2),3)
        G3=round(G(T3,ang3),3)
        G4=round(G(T4,ang4),3)
        print(json.dumps({"Torsion_test":[{"The shears stress are " :str(G1)+" , "+str(G2)+" , "+str(G3)+" and "+str(G4)}]}))


     
    def Bend(self):
        argument = self.arg[0:]
        M= float(argument[1])
        L=float(argument[2])
        B= float(argument[3])
        D=float(argument[4])
        Y= float(argument[5])
        W = M*9.81
        bm = W*L/4
        I=(B*D**3)/12
        bs = bm*Y/I
        def defl(x,y):
            return((y*0.01)-x)
        def E(x):
            return((W*L**3)/(48*x*I))
        def1=round(defl(float(argument[6]),float(argument[7])),2)
        def2=round(defl(float(argument[8]),float(argument[9])),2)
        def3=round(defl(float(argument[10]),float(argument[11])),2)
        def4=round(defl(float(argument[12]),float(argument[13])),2)
        E1=round(E(def1),2)
        E2=round(E(def2),2)
        E3=round(E(def3),2)
        E4=round(E(def4) ,2)  
        print(json.dumps({"Bend_test":[{"Test for the ductility of mild is still by 180-degree bend test" :str(),"Deflection(δ)":str(def1)+", "+str(def2)+","+str(def3)+","+str(def4),"Bending moment(M)":str(bm),"Bending stress(σ)":str(bs),"Young's Modulus(E)":str(E1)+" N/mm, "+str(E2)+" N/mm, "+str(E3)+" N/mm, "+str(E4)+" N/mm"}]}))


    def Tension_test(self):
        argument = self.arg[0:]
        def Stress(x):return(x/A0)
        def Strain(x):return(x/L)
        D0=float(argument[1])
        D1=float(argument[5])
        L0=float(argument[8])
        L1=float(argument[7])
        Af=float(argument[6])
        A0=float(argument[2])
        L=float(argument[3])
        Mload= float(argument[9])
        Bload = float(argument[10])
        S1=round(Stress(float(argument[11])),3)
        S2=round(Stress(float(argument[14])),3)
        S3=round(Stress(float(argument[17])),3)
        S4=round(Stress(float(argument[20])),3)
        S5=round(Stress(float(argument[23])),3)
        S6=round(Stress(float(argument[26])),3)
        S7=round(Stress(float(argument[29])),3)
        S8=round(Stress(float(argument[32])),3)
        S9=round(Stress(float(argument[35])),3)
        S10=round(Stress(float(argument[38])),3)
        S11=round(Stress(float(argument[41])),3)
        S12=round(Stress(float(argument[44])),3)
        S13=round(Stress(float(argument[47])),3)
        S14=round(Stress(float(argument[50])),3)
        S15=round(Stress(float(argument[53])),3)
        S16=round(Stress(float(argument[56])),3)
        S17=round(Stress(float(argument[59])),3)
        S18=round(Stress(float(argument[62])),3)
        S19=round(Stress(float(argument[65])),3)

        M1=round(Strain(float(argument[12]))*10000,2)
        M2=round(Strain(float(argument[15]))*10000,2)
        M3=round(Strain(float(argument[18]))*10000,2)
        M4=round(Strain(float(argument[21]))*10000,2)
        M5=round(Strain(float(argument[24]))*10000,2)
        M6=round(Strain(float(argument[27]))*1000,2)
        M7=round(Strain(float(argument[30]))*1000,2)
        M8=round(Strain(float(argument[33]))*1000,2)
        M9=round(Strain(float(argument[36]))*1000,2)
        M10=round(Strain(float(argument[39]))*1000,2)
        M11=round(Strain(float(argument[42]))*1000,2)
        M12=round(Strain(float(argument[45]))*1000,2)
        M13=round(Strain(float(argument[48]))*1000,2)
        M14=round(Strain(float(argument[52]))*1000,2)
        M15=round(Strain(float(argument[55]))*1000,2)
        M16=round(Strain(float(argument[58]))*1000,2)
        M17=round(Strain(float(argument[61]))*1000,2)
        M18=round(Strain(float(argument[64]))*1000,2)
        M19=round(Strain(float(argument[67]))*1000,2)
        Elong= round(((L1-L0)/(L0))*100,3)
        Reduction= round(((A0-Af)/A0)*100,3)
        tensile=round((Mload/A0)*1000,3)
        Break=round((Bload/A0)*1000,3)
        s1=(float(argument[68]))-float(argument[69])
        s2=(float(argument[70]))-float(argument[71])
        Slope = round((s1/s2),2)
        print(json.dumps({"Test":[{"The given M.S specimen is tested and static tension up to failure and mechanical proportional are":str(),"Stress(σ)":str(S1)+" N/mm2 "+str(S2)+" N.mm2, "+str(S3)+" N.mm2, "+str(S4)+" N.mm2, "+str(S5)+" N.mm2,"+str(S6)+" N.mm2, "+str(S7)+"N.mm2, "+str(S8)+" N.mm2, "+str(S9)+" N.mm2, "+str(S10)+" N.mm2, "+str(S11)+" N.mm2, "+str(S12)+" N/mm2, "+str(S13)+" N/mm2, "+str(S14)+" N/mm2, "+str(S15)+" N/mm2, "+str(S16)+" N/mm2, "+str(S17)+"N/mm2, "+str(S18)+"N/mm2,"+str(19)+"N/mm2,","Strain(E)":str(M1)+"x10^-3, "+str(M2)+"x10^-3, "+str(M3)+"x10^-3, "+str(M4)+"x10^-3, "+str(M5)+"x10^-3, "+str(M6)+"x10^-3, "+str(M7)+"x10^-3, "+str(M8)+"x10^-3, "+str(M9)+"x10^-3 "+str(M10)+"x10^3, "+str(M11)+"x10^-3, "+str(M12)+"X10^-3, "+str(M13)+"X10^-3, "+str(M14)+"X10^-3, "+str(M15)+"X10^-3, "+str(M16)+"X10^-3, "+str(M17)+"X10^-3, "+str(M18)+"X10^-3, "+str(M19)+"X10^-3, ","Young's Module":str(Slope)+"x 10^ 5 N/mm","% Elongation":str(Elong)+"%","% Reduction in area =":str(Reduction)+"%","Ultimate tensile stress":str(tensile)+"N/mm2","Breaking stress=":str(Break)+"N/mm2"}]}))
    def Annealing(self):
        print(json.dumps({"answer":[{"result":"Thus the given specimen was annealed and its hardness was studied"}]}))        #Thus the given specimen was annealed and its hardness was studied.
    def Normalizing(self):
        print(json.dumps({"answer":[{"result":"Thus the normalizing was done on the steel and properties were studied"}]}))

    def Heat(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the heat treatment process was performed"}]}))
    
        #Thus the heat treatment process was performed.

    def Hardening(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the heat treatment process was performed"}]}))

    def Microstructure(self):
        argument = self.arg[0:]
        #print(argument)
        R = str(argument[1])
        print(json.dumps({"answer":[{"Thus the given specimen was polished and the microstructure of the given metal is ":str(R)}]}))
    
    def Metallurgical(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the Metallurgical Microscope is studied."}]}))
 
    def Microscopic(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the specimen preparation has been done to study its structure under microscope and metallographic result haven been obtained"}]}))
    def Hardenability(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Then the hardness test was done on mild steel and a graph was drawn."}]}))
    def Etchants(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the preparation and application of the etchants are studied."}]}))
    
    def Brinell(self):
        argument = self.arg[0:]
        BHN=round((2*float(argument[1]))/((3.14*float(argument[2]))*(float(argument[2])-(math.sqrt((float(argument[2])**2)-(float(argument[3])**2))))),3)
        print(json.dumps({"answer":[{"The Brinell hardness number for the given specimen using the Hardness Testing machine is determined":str(),"BHN":str(BHN)}]}))