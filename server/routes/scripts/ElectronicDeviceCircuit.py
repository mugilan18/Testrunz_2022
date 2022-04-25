import json
import math
class EDC:
    def __init__(self, arg):
        self.arg = arg
    def Junction(self):
        argument = self.arg[:]
        Vd = float(argument[50])-float(argument[49])
        Id = float(argument[52])-float(argument[51])
        Rd= (Vd/Id)*10**-3
        Vg=float(argument[56])-float(argument[55])
        Ig = float(argument[58])-float(argument[57])
        Gm= (Vg/Ig)*10**-3
        A = (Rd*Gm)
        print(json.dumps({"length":[{"Drain resistance rd" : str(Rd)}], "breadth":[{"Transconductance gm " : str(Gm) }], "width":[{"Amplification factor " : str(A)}]}))
    def Semiconductor(self):
        argument = self.arg[:]
        #forward bias
        Vd = float(argument[50])-float(argument[49])
        Id = float(argument[52])-float(argument[51])
        Rd= (Vd/Id)*10**-3
        #Reverse bias
        Vg=float(argument[56])-float(argument[55])
        Ig = float(argument[58])-float(argument[57])
        Gm= (Vg/Ig)*10**-3
        #static
        Vf=(float(argument[53])/float(argument[54]))*10**-3
        #forward bias
        Vd2= float(argument[60])-float(argument[59])
        Id2 = float(argument[62])-float(argument[61])
        Rd2= (Vd2/Id2)*10**-3
        #Reverse bias
        Vg2=float(argument[66])-float(argument[65])
        Ig2 = float(argument[68])-float(argument[67])
        Gm2= (Vg2/Ig2)*10**-3
        #static
        Vf2=(float(argument[63])/float(argument[64]))*10**-3
        print(json.dumps({"length":[{"Thus the VI characteristics of the PN Junction diode, Point Contact diode, Zener diode are obtained and their static and dynamic resistance are obtained."}], "breadth":[{"PN Junction Diode forward" : str(Rd) }], "width":[{"PN Junction Diode Reverse" : str(Gm)}], "wid":[{"Point Contact diode forward" : str(Rd2)}], "wi":[{"PPoint Contact diode Reverse" : str(Gm2)}]}))
    def BJT(self):
        argument = self.arg[:]
        Vd = float(argument[2])-float(argument[1])
        Id = float(argument[4])-float(argument[3])
        Rd= (Vd/Id)*10**-3
        Vd1 = float(argument[6])-float(argument[5])
        Id1 = float(argument[8])-float(argument[7])
        Rd1= (Vd1/Id1)*10**-3
        Vf1=(float(argument[9])/float(argument[10]))*10**-3
        Vf2=(float(argument[11])/float(argument[12]))*10**-3
        print(json.dumps({"length":[{"Thus the input and Output Characteristics of a transistor in common base mode is obtained. The parameters are determined."}], "breadth":[{"Input Impedance" : str(Rd) }], "readth":[{"Output Impedance": str(Rd1)}], "read":[{"Forward Current gain": str(Vf1)}], "High":[{"Voltage gain": str(Vf2)}]}))

    def Bridge(self):
        argument = self.arg[:]
        Vd1 = float(argument[2])/float(argument[3])
        Vd2 = float(argument[6])/float(argument[7])
        Vd3 = float(argument[10])/float(argument[11])
        Vd4 = float(argument[14])/float(argument[15])
        Vd5 = float(argument[18])/float(argument[19])
        Vd6 = float(argument[22])/float(argument[23])
        Vd7 = float(argument[26])/float(argument[27])
        Vd8 = float(argument[30])/float(argument[31])
        Vg1 = (200-float(argument[3]))/float(argument[3])
        Vg2 = (200-float(argument[7]))/float(argument[7])
        Vg3 = (200-float(argument[11]))/float(argument[11])
        Vg4 = (200-float(argument[15]))/float(argument[15])
        Vg5 = (200-float(argument[19]))/float(argument[19])
        Vg6 = (200-float(argument[23]))/float(argument[23])
        Vg7 = (200-float(argument[27]))/float(argument[27])
        Vg8 = (200-float(argument[31]))/float(argument[31])
        print(json.dumps({"answer":[{"Result":"Thus the performance of the bridge rectifier is used and its output waveform is obtained."}]}))

    def CE(self):
        argument = self.arg[:]
        Vd = float(argument[2])-float(argument[1])
        Id = float(argument[4])-float(argument[3])
        Rd= (Vd/Id)*10**-3
        print(json.dumps({"length":[{"Thus the input and Output Characteristics of a transistor in common emitter mode is obtained. The parameters are determined."}], "breadth":[{"Input Impedance" : str(Rd) }]}))
    def Clipper(self):
        argument = self.arg[:]
        Vd1 = float(argument[1])*10
        Vd2 = float(argument[5])*10
        Vd3 = float(argument[9])*10
        Vd4 = float(argument[13])*10
        V1 = float(argument[2])*0.5
        V2 = float(argument[6])*0.5
        V3 = float(argument[10])*0.5
        V4 = float(argument[14])*0.5
        d1 = float(argument[3])*10
        d2 = float(argument[7])*10
        d3 = float(argument[11])*10
        d4 = float(argument[15])*10
        v1 = float(argument[4])*0.5
        v2 = float(argument[8])*0.5
        v3 = float(argument[12])*0.5
        v4 = float(argument[16])*0.5
        i1 = float(argument[17])*1
        i2 = float(argument[21])*1
        I1 = float(argument[18])*0.5
        I2 = float(argument[22])*0.5
        o1 = float(argument[19])*1
        o2 = float(argument[23])*1
        O1 = float(argument[20])*0.5
        O2 = float(argument[24])*0.5
        print(json.dumps({"answer":[{"Result":"Thus the positive and negative biased and clamper are constructed using diodes and output waves are obtained."}]}))
    def Biasing(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the following circuit are designed and tested for Fixed bias, Collector to base bias, Self Bias."}]}))

    def UJT(self):
        argument = self.arg[:]
        n1=round(( float(argument[31])+ float(argument[32]))/2)
        print(json.dumps({"answer":[{"Result":"The characteristics of UJT is obtained and the intrensic stand - off ratio(η) is determined","Ratio - η":str(n1)}]}))         

    def Photo(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the VI characteristics of a Phototransistor is obtained."}]}))
    def TRIAC(self):
        argument = self.arg[0:]
        FV = float(argument[19])
        RV = float(argument[39])
        print(json.dumps({"answer":[{"Result":"Thus the V-I characteristics of TRIAC was obtained and graph was drawn.","Break over voltage in forward direction of TRIAC (VBO)":str(FV),"Break over voltage in reverse direction of TRIAC (VBO)":str(RV)}]}))
    def SCR(self):
        print(json.dumps({"answer":[{"Result":"The Characteristics of SCR was studied and the graphs were plotted."}]})) 
    def LED(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the VI characteristics of LEDs are obtained."}]}))
    def MOSFET(self):
        argument = self.arg[:]
        Id = float(argument[34])
        Vd = float(argument[35])
        gm= (Id/Vd)
        rd = (float(argument[36])/float(argument[37]))*1000
        μ = rd*gm
        
        V= float(argument[38])
        print(json.dumps({"answer":[{"Result":"Thhe transfer  and drain characteristics of the MOSFET is plotted and the following values are obtained","VGS(Threshold)":str(V),"Trans conductance (gm)":str(gm),"Drain resistance(rd)":str(rd),"Amplification factor(μ)":str(μ)}]}))

















