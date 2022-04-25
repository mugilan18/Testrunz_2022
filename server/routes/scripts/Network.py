import json
import math
class NT:
    def __init__(self, arg):
        self.arg = arg
    def K_type(self):
        argument = self.arg[0:]
        Vin1 = float(argument[1])
        def theta(a,b):
            return (a/(b*2))*360 
        def gain(a):
            return 20* math.log10(a)
        theta1=round(theta(float(argument[5]),float(argument[4])),2)
        theta2=round(theta(float(argument[9]),float(argument[8])),2)
        theta3=round(theta(float(argument[13]),float(argument[12])),2)
        theta4=round(theta(float(argument[17]),float(argument[16])),2)
        theta5=round(theta(float(argument[21]),float(argument[20])),2)
        theta6=round(theta(float(argument[25]),float(argument[24])),2)
        theta7=round(theta(float(argument[29]),float(argument[28])),2)
        theta8=round(theta(float(argument[33]),float(argument[32])),2)
        theta9=round(theta(float(argument[37]),float(argument[36])),2)
        theta10=round(theta(float(argument[41]),float(argument[40])),2)
        theta11=round(theta(float(argument[45]),float(argument[44])),2)
        theta12=round(theta(float(argument[49]),float(argument[48])),2)
        theta13=round(theta(float(argument[53]),float(argument[52])),2)
        theta14=round(theta(float(argument[57]),float(argument[56])),2)
        theta15=round(theta(float(argument[61]),float(argument[60])),2)
        theta16=round(theta(float(argument[65]),float(argument[64])),2)
        theta17=round(theta(float(argument[69]),float(argument[68])),2)
        theta18=round(theta(float(argument[73]),float(argument[72])),2)
        theta19=round(theta(float(argument[77]),float(argument[76])),2)
        theta20=round(theta(float(argument[81]),float(argument[80])),2)
        theta21=round(theta(float(argument[85]),float(argument[84])),2)
        theta22=round(theta(float(argument[89]),float(argument[88])),2)
        theta23=round(theta(float(argument[93]),float(argument[92])),2)
        theta24=round(theta(float(argument[97]),float(argument[96])),2)
        gain1=round(gain(float(argument[3])),2)
        gain2=round(gain(float(argument[7])),2)
        gain3=round(gain(float(argument[11])),2)
        gain4=round(gain(float(argument[15])),2)
        gain5=round(gain(float(argument[19])),2)
        gain6=round(gain(float(argument[23])),2)
        gain7=round(gain(float(argument[27])),2)
        gain8=round(gain(float(argument[31])),2)
        gain9=round(gain(float(argument[35])),2)
        gain10=round(gain(float(argument[39])),2)
        gain11=round(gain(float(argument[43])),2)
        gain12=round(gain(float(argument[47])),2)
        gain13=round(gain(float(argument[51])),2)
        gain14=round(gain(float(argument[55])),2)
        gain15=round(gain(float(argument[59])),2)
        gain16=round(gain(float(argument[63])),2)
        gain17=round(gain(float(argument[67])),2)
        gain18=round(gain(float(argument[71])),2)
        gain19=round(gain(float(argument[75])),2)
        gain20=round(gain(float(argument[79])),2)
        gain21=round(gain(float(argument[83])),2)
        gain22=round(gain(float(argument[87])),2)
        gain23=round(gain(float(argument[91])),2)
        gain24=round(gain(float(argument[95])),2)
       
        # print(json.dumps({"answer":[{"result":str(theta6)}]}))

        print(json.dumps({"length":[{"The theate values for band pass filter t sec": str(theta1)+" , "+str(theta2)+" , "+str(theta3)+" , "+str(theta4)+" , "+str(theta5)+" and "+str(theta6),"The theate values for band pass filter tt sec": str(theta7)+" , "+str(theta8)+" , "+str(theta9)+" , "+str(theta10)+" , "+str(theta11)+" and "+str(theta12),"The theate values for band stop filter t sec": str(theta13)+" , "+str(theta14)+" , "+str(theta15)+" , "+str(theta16)+" , "+str(theta17)+" and "+str(theta18),"The theate values for band stop filter tt sec": str(theta19)+" , "+str(theta20)+" , "+str(theta21)+" , "+str(theta22)+" , "+str(theta23)+" and "+str(theta24),"The theate values for band pass filter t sec": str(theta1)+" , "+str(theta2)+" , "+str(theta3)+" , "+str(theta4)+" , "+str(theta5)+" and "+str(theta6),"The gain values for band pass filter t sec": str(gain1)+" , "+str(gain2)+" , "+str(gain3)+" , "+str(gain4)+" , "+str(gain5)+" and "+str(gain6),"The gain values for band pass filter tt sec": str(gain7)+" , "+str(gain8)+" , "+str(gain9)+" , "+str(gain10)+" , "+str(gain11)+" and "+str(gain12),"The gain values for band stop filter t sec": str(gain13)+" , "+str(gain14)+" , "+str(gain15)+" , "+str(gain16)+" , "+str(gain17)+" and "+str(gain18),"The gain values for band stop filter tt sec": str(gain19)+" , "+str(gain20)+" , "+str(gain21)+" , "+str(gain22)+" , "+str(gain23)+" and "+str(gain24)}] }))
    def Band(self):
        argument = self.arg[0:]
        Vin1 = float(argument[1])
        def theta(a,b):
            return (a/(b*2))*360 
        def gain(a):
            return 20* math.log10(a)
        theta1=round(theta(float(argument[5]),float(argument[4])),2)
        theta2=round(theta(float(argument[9]),float(argument[8])),2)
        theta3=round(theta(float(argument[13]),float(argument[12])),2)
        theta4=round(theta(float(argument[17]),float(argument[16])),2)
        theta5=round(theta(float(argument[21]),float(argument[20])),2)
        theta6=round(theta(float(argument[25]),float(argument[24])),2)
        theta7=round(theta(float(argument[29]),float(argument[28])),2)
        theta8=round(theta(float(argument[33]),float(argument[32])),2)
        theta9=round(theta(float(argument[37]),float(argument[36])),2)
        theta10=round(theta(float(argument[41]),float(argument[40])),2)
        theta11=round(theta(float(argument[45]),float(argument[44])),2)
        theta12=round(theta(float(argument[49]),float(argument[48])),2)
        theta13=round(theta(float(argument[53]),float(argument[52])),2)
        theta14=round(theta(float(argument[57]),float(argument[56])),2)
        theta15=round(theta(float(argument[61]),float(argument[60])),2)
        theta16=round(theta(float(argument[65]),float(argument[64])),2)
        theta17=round(theta(float(argument[69]),float(argument[68])),2)
        theta18=round(theta(float(argument[73]),float(argument[72])),2)
        theta19=round(theta(float(argument[77]),float(argument[76])),2)
        theta20=round(theta(float(argument[81]),float(argument[80])),2)
        theta21=round(theta(float(argument[85]),float(argument[84])),2)
        theta22=round(theta(float(argument[89]),float(argument[88])),2)
        theta23=round(theta(float(argument[93]),float(argument[92])),2)
        theta24=round(theta(float(argument[97]),float(argument[96])),2)
        gain1=round(gain(float(argument[3])),2)
        gain2=round(gain(float(argument[7])),2)
        gain3=round(gain(float(argument[11])),2)
        gain4=round(gain(float(argument[15])),2)
        gain5=round(gain(float(argument[19])),2)
        gain6=round(gain(float(argument[23])),2)
        gain7=round(gain(float(argument[27])),2)
        gain8=round(gain(float(argument[31])),2)
        gain9=round(gain(float(argument[35])),2)
        gain10=round(gain(float(argument[39])),2)
        gain11=round(gain(float(argument[43])),2)
        gain12=round(gain(float(argument[47])),2)
        gain13=round(gain(float(argument[51])),2)
        gain14=round(gain(float(argument[55])),2)
        gain15=round(gain(float(argument[59])),2)
        gain16=round(gain(float(argument[63])),2)
        gain17=round(gain(float(argument[67])),2)
        gain18=round(gain(float(argument[71])),2)
        gain19=round(gain(float(argument[75])),2)
        gain20=round(gain(float(argument[79])),2)
        gain21=round(gain(float(argument[83])),2)
        gain22=round(gain(float(argument[87])),2)
        gain23=round(gain(float(argument[91])),2)
        gain24=round(gain(float(argument[95])),2)
       
        # print(json.dumps({"answer":[{"result":str(theta6)}]}))

        print(json.dumps({"length":[{"The theate values for band pass filter t sec": str(theta1)+" , "+str(theta2)+" , "+str(theta3)+" , "+str(theta4)+" , "+str(theta5)+" and "+str(theta6),"The theate values for band pass filter tt sec": str(theta7)+" , "+str(theta8)+" , "+str(theta9)+" , "+str(theta10)+" , "+str(theta11)+" and "+str(theta12),"The theate values for band stop filter t sec": str(theta13)+" , "+str(theta14)+" , "+str(theta15)+" , "+str(theta16)+" , "+str(theta17)+" and "+str(theta18),"The theate values for band stop filter tt sec": str(theta19)+" , "+str(theta20)+" , "+str(theta21)+" , "+str(theta22)+" , "+str(theta23)+" and "+str(theta24),"The theate values for band pass filter t sec": str(theta1)+" , "+str(theta2)+" , "+str(theta3)+" , "+str(theta4)+" , "+str(theta5)+" and "+str(theta6),"The gain values for band pass filter t sec": str(gain1)+" , "+str(gain2)+" , "+str(gain3)+" , "+str(gain4)+" , "+str(gain5)+" and "+str(gain6),"The gain values for band pass filter tt sec": str(gain7)+" , "+str(gain8)+" , "+str(gain9)+" , "+str(gain10)+" , "+str(gain11)+" and "+str(gain12),"The gain values for band stop filter t sec": str(gain13)+" , "+str(gain14)+" , "+str(gain15)+" , "+str(gain16)+" , "+str(gain17)+" and "+str(gain18),"The gain values for band stop filter tt sec": str(gain19)+" , "+str(gain20)+" , "+str(gain21)+" , "+str(gain22)+" , "+str(gain23)+" and "+str(gain24)}] }))
    def Design(self):
        argument = self.arg[0:]
        Vin1 = float(argument[1])
        amp1=float(argument[2])
        t1=float(argument[3])
        delt1=float(argument[4])
        def theta(a,b):
            return ((a*t1)/(b*delt1))*360 
        def gain(a):
            return 20* math.log10((a*amp1)/Vin1)
        theta1=round(theta(float(argument[8]),float(argument[7])),2)
        theta2=round(theta(float(argument[12]),float(argument[11])),2)
        theta3=round(theta(float(argument[16]),float(argument[15])),2)
        theta4=round(theta(float(argument[20]),float(argument[19])),2)
        theta5=round(theta(float(argument[24]),float(argument[23])),2)
        theta6=round(theta(float(argument[28]),float(argument[27])),2)
        gain1=round(gain(float(argument[6])),2)
        gain2=round(gain(float(argument[10])),2)
        gain3=round(gain(float(argument[14])),2)
        gain4=round(gain(float(argument[18])),2)
        gain5=round(gain(float(argument[22])),2)
        gain6=round(gain(float(argument[26])),2)

        Vin2 = float(argument[29])
        amp2=float(argument[30])
        t2=float(argument[32])
        delt2=float(argument[33])
        def thetaa(a,b):
            return ((a*t2)/(b*delt2))*360 
        def gaina(a):
            return 20* math.log10((a*amp2)/Vin2)

        theta7=round(thetaa(float(argument[36]),float(argument[35])),2)
        theta8=round(thetaa(float(argument[40]),float(argument[39])),2)
        theta9=round(thetaa(float(argument[44]),float(argument[43])),2)
        theta10=round(thetaa(float(argument[48]),float(argument[47])),2)
        theta11=round(thetaa(float(argument[52]),float(argument[51])),2)
        theta12=round(thetaa(float(argument[56]),float(argument[55])),2)
        gain7=round(gaina(float(argument[34])),2)
        gain8=round(gaina(float(argument[38])),2)
        gain9=round(gaina(float(argument[42])),2)
        gain10=round(gaina(float(argument[46])),2)
        gain11=round(gaina(float(argument[50])),2)
        gain12=round(gaina(float(argument[54])),2)

        Vin3 = float(argument[57])
        amp3=float(argument[58])
        t3=float(argument[59])
        delt3=float(argument[60])
        def thetab(a,b):
            return ((a*t3)/(b*delt3))*360 
        def gainb(a):
            return 20* math.log10((a*amp3)/Vin3)

        theta13=round(thetab(float(argument[64]),float(argument[63])),2)
        theta14=round(thetab(float(argument[68]),float(argument[67])),2)
        theta15=round(thetab(float(argument[72]),float(argument[71])),2)
        theta16=round(thetab(float(argument[76]),float(argument[75])),2)
        theta17=round(thetab(float(argument[80]),float(argument[79])),2)
        theta18=round(thetab(float(argument[84]),float(argument[83])),2)
        gain13=round(gainb(float(argument[62])),2)
        gain14=round(gainb(float(argument[66])),2)
        gain15=round(gainb(float(argument[70])),2)
        gain16=round(gainb(float(argument[74])),2)
        gain17=round(gainb(float(argument[78])),2)
        gain18=round(gainb(float(argument[82])),2)

        Vin4 = float(argument[85])
        amp4=float(argument[86])
        t4=float(argument[87])
        delt4=float(argument[88])
        def thetac(a,b):
            return ((a*t4)/(b*delt4))*360 
        def gainc(a):
            return 20* math.log10((a*amp4)/Vin4)

        theta19=round(thetac(float(argument[92]),float(argument[91])),2)
        theta20=round(thetac(float(argument[96]),float(argument[95])),2)
        theta21=round(thetac(float(argument[100]),float(argument[99])),2)
        theta22=round(thetac(float(argument[104]),float(argument[103])),2)
        theta23=round(thetac(float(argument[108]),float(argument[107])),2)
        theta24=round(thetac(float(argument[112]),float(argument[111])),2)
        gain19=round(gainc(float(argument[90])),2)
        gain20=round(gainc(float(argument[94])),2)
        gain21=round(gainc(float(argument[98])),2)
        gain22=round(gainc(float(argument[102])),2)
        gain23=round(gainc(float(argument[106])),2)
        gain24=round(gainc(float(argument[10])),2)
        print(json.dumps({"length":[{"M derived LPF (1-SEC) The theate values are": str(theta1)+" , "+str(theta2)+" , "+str(theta3)+" , "+str(theta4)+" , "+str(theta5)+" and "+str(theta6),"M derived LPF (1-SEC) The gain values for band pass filter t sec": str(gain1)+" , "+str(gain2)+" , "+str(gain3)+" , "+str(gain4)+" , "+str(gain5)+" and "+str(gain6),"M derived LPF (Π-SEC) The theate values are": str(theta7)+" , "+str(theta8)+" , "+str(theta9)+" , "+str(theta10)+" , "+str(theta11)+" and "+str(theta12),"M derived LPF (Π-SEC) The gain values for band pass filter t sec": str(gain7)+" , "+str(gain8)+" , "+str(gain9)+" , "+str(gain10)+" , "+str(gain11)+" and "+str(gain12),"M derived HPF (T-SEC) The theate values are": str(theta13)+" , "+str(theta14)+" , "+str(theta15)+" , "+str(theta16)+" , "+str(theta17)+" and "+str(theta18),"M derived HPF (T-SEC) The gain values for band pass filter t sec": str(gain13)+" , "+str(gain14)+" , "+str(gain15)+" , "+str(gain16)+" , "+str(gain17)+" and "+str(gain18),"M derived HPF (Π-SEC) The theate values are": str(theta19)+" , "+str(theta20)+" , "+str(theta21)+" , "+str(theta22)+" , "+str(theta23)+" and "+str(theta24),"M derived HPF (Π-SEC) The gain values for band pass filter t sec": str(gain19)+" , "+str(gain20)+" , "+str(gain21)+" , "+str(gain22)+" , "+str(gain23)+" and "+str(gain24)}]}))
        # print(json.dumps({"length":[{"M derived LPF (1-SEC) The theate values are": str(theta1)+" , "+str(theta2)+" , "+str(theta3)+" , "+str(theta4)+" , "+str(theta5)+" and "+str(theta6),"M derived LPF (1-SEC) The gain values for band pass filter t sec": str(gain1)+" , "+str(gain2)+" , "+str(gain3)+" , "+str(gain4)+" , "+str(gain5)+" and "+str(gain6),"M derived LPF (Π-SEC) The theate values are": str(theta7)+" , "+str(theta8)+" , "+str(theta9)+" , "+str(theta10)+" , "+str(theta11)+" and "+str(theta12),"M derived LPF (Π-SEC) The gain values for band pass filter t sec": str(gain7)+" , "+str(gain8)+" , "+str(gain9)+" , "+str(gain10)+" , "+str(gain11)+" and "+str(gain12),"M derived HPF (T-SEC) The theate values are": str(theta13)+" , "+str(theta14)+" , "+str(theta15)+" , "+str(theta16)+" , "+str(theta17)+" and "+str(theta18),"M derived HPF (T-SEC) The gain values for band pass filter t sec": str(gain13)+" , "+str(gain14)+" , "+str(gain15)+" , "+str(gain16)+" , "+str(gain17)+" and "+str(gain18),"M derived HPF (Π-SEC) The theate values are": str(theta19)+" , "+str(theta20)+" , "+str(theta21)+" , "+str(theta22)+" , "+str(theta23)+" and "+str(theta24),"M derived HPF (Π-SEC) The gain values for band pass filter t sec": str(gain19)+" , "+str(gain20)+" , "+str(gain21)+" , "+str(gain22)+" , "+str(gain23)+" and "+str(gain24)}]}))
    def Switched(self):
        argument = self.arg[0:]
        Vin1 = float(argument[1])
        amp=float(argument[2])
        t=float(argument[3])
        delt=float(argument[4])
        def theta(a,b):
            return ((a*t)/(b*delt))*360 
        def gain(a):
            return 20* math.log10((a*amp)/Vin1)
        theta1=round(theta(float(argument[8]),float(argument[7])),2)
        theta2=round(theta(float(argument[12]),float(argument[11])),2)
        theta3=round(theta(float(argument[16]),float(argument[15])),2)
        theta4=round(theta(float(argument[20]),float(argument[19])),2)
        theta5=round(theta(float(argument[24]),float(argument[23])),2)
        theta6=round(theta(float(argument[28]),float(argument[27])),2)
        gain1=round(gain(float(argument[6])),2)
        gain2=round(gain(float(argument[10])),2)
        gain3=round(gain(float(argument[14])),2)
        gain4=round(gain(float(argument[18])),2)
        gain5=round(gain(float(argument[22])),2)
        gain6=round(gain(float(argument[26])),2)
        # print(json.dumps({"length":[{"The theate values are": "'","The gain values for band pass filter t sec": str(gain1)}]}))

        print(json.dumps({"length":[{"The theate values are": str(theta1)+" , "+str(theta2)+" , "+str(theta3)+" , "+str(theta4)+" , "+str(theta5)+" and "+str(theta6),"The gain values for band pass filter t sec": str(gain1)+" , "+str(gain2)+" , "+str(gain3)+" , "+str(gain4)+" , "+str(gain5)+" and "+str(gain6)}]}))
    def LC(self):
        argument = self.arg[:]
        Vin=2*0.5
        G1 = (float(argument[2])*0.5)/Vin
        G2 = (float(argument[4])*0.5)/Vin
        G3 = (float(argument[6])*0.5)/Vin
        G4 = (float(argument[8])*0.5)/Vin
        G5 = (float(argument[10])*0.5)/Vin
        G6 = (float(argument[12])*0.5)/Vin
        DB1 = round(20*math.log10(G1),2)
        DB2 = round(20*math.log10(G2),2)
        DB3 = round(20*math.log10(G3),2)
        DB4 = round(20*math.log10(G4),2)
        DB5 = round(20*math.log10(G5),2)
        DB6 = round(20*math.log10(G6),2)
       
        Vin=2*0.5
        g1 = (float(argument[14])*0.5)/Vin
        g2 = (float(argument[16])*0.5)/Vin
        g3 = (float(argument[18])*0.5)/Vin
        g4 = (float(argument[20])*0.5)/Vin
        g5 = (float(argument[22])*0.5)/Vin
        g6 = (float(argument[24])*0.5)/Vin
        db1 = round(20*math.log10(g1),2)
        db2 = round(20*math.log10(g2),2)
        db3 = round(20*math.log10(g3),2)
        db4 = round(20*math.log10(g4),2)
        db5 = round(20*math.log10(g5),2)
        db6 = round(20*math.log10(g6),2)
        
        print(json.dumps({"length":[{"Thus gain for LC resonant series circuit are":str(DB1)+" , "+str(DB2)+" , "+str(DB3)+" , "+str(DB4)+" , "+str(DB5)+" and "+str(DB6) , "Thus gain for LC resonant shunt circuit are":str(db1)+" , "+str(db2)+" , "+str(db3)+" , "+str(db4)+" , "+str(db5)+" and "+str(db6)}]}))
    def Open(self):
        print(json.dumps({"answer":[{"Result":"Thus the open circuit impedance parameter and ABCD parameter  of transmission line was contructed and output was taken."}]}))
    def Equalizer(self):
        argument = self.arg[:]
        Vin=1*1
        G1 = (float(argument[2])*0.2)/Vin
        G2 = (float(argument[4])*0.2)/Vin
        G3 = (float(argument[6])*0.2)/Vin
        G4 = (float(argument[8])*0.2)/Vin
        G5 = (float(argument[10])*0.2)/Vin
        G6 = (float(argument[12])*0.2)/Vin
        G7 = (float(argument[14])*0.2)/Vin
        G8 = (float(argument[16])*0.2)/Vin
        G9 = (float(argument[18])*0.2)/Vin
        DB1 = round(20*math.log10(G1),2)
        DB2 = round(20*math.log10(G2),2)
        DB3 = round(20*math.log10(G3),2)
        DB4 = round(20*math.log10(G4),2)
        DB5 = round(20*math.log10(G5),2)
        DB6 = round(20*math.log10(G6),2)
        DB7 = round(20*math.log10(G7),2)
        DB8 = round(20*math.log10(G8),2)
        DB9 = round(20*math.log10(G9),2)
        Vin=1*1
        g1 = (float(argument[20])*0.2)/Vin
        g2 = (float(argument[22])*0.2)/Vin
        g3 = (float(argument[24])*0.2)/Vin
        g4 = (float(argument[26])*0.2)/Vin
        g5 = (float(argument[28])*0.2)/Vin
        g6 = (float(argument[30])*0.2)/Vin
        g7 = (float(argument[32])*0.2)/Vin
        g8 = (float(argument[34])*0.2)/Vin
        g9 = (float(argument[36])*0.2)/Vin
        db1 = round(20*math.log10(g1),2)
        db2 = round(20*math.log10(g2),2)
        db3 = round(20*math.log10(g3),2)
        db4 = round(20*math.log10(g4),2)
        db5 = round(20*math.log10(g5),2)
        db6 = round(20*math.log10(g6),2)
        db7 = round(20*math.log10(g7),2)
        db8 = round(20*math.log10(g8),2)
        db9 = round(20*math.log10(g9),2)
        print(json.dumps({"length":[{"Thus gain for LC resonant series circuit are":str(DB1)+" , "+str(DB2)+" , "+str(DB3)+" , "+str(DB4)+" , "+str(DB5)+" , "+str(DB6)+" , "+str(DB7)+" , "+str(DB8)+" and "+str(DB9) , "Thus gain for LC resonant shunt circuit are":str(db1)+" , "+str(db2)+" , "+str(db3)+" , "+str(db4)+" , "+str(db5)+" , "+str(db6)+" , "+str(db7)+" , "+str(db8)+" and "+str(db9)}]}))
    def Attenuator(self):
        argument = self.arg[:]
        a=float(argument[1])
        p1=float(argument[3]) * float(argument[4])*a
        p2=float(argument[6]) * float(argument[7])*a
        p3=float(argument[9]) * float(argument[10])*a
        p4=float(argument[12]) * float(argument[13])*a
        p5=float(argument[15]) * float(argument[16])*a
        
        pout1= (float(argument[4]) *a)**2 * 1000/ 1.2 
        pout2= (float(argument[7]) *a)**2 * 1000/ 1.2 
        pout3= (float(argument[10]) *a)**2 * 1000/ 1.2 
        pout4= (float(argument[13]) *a)**2 * 1000/ 1.2 
        pout5= (float(argument[16]) *a)**2 * 1000/ 1.2 

        d1= round(20*math.log10(pout1/p1),2)
        d2= round(20*math.log10(pout2/p2),2)
        d3= round(20*math.log10(pout3/p3),2)
        d4= round(20*math.log10(pout4/p4),2)
        d5= round(20*math.log10(pout5/p5),2)
        Vin=1.4
        G1 = (float(argument[18]))/Vin
        G2 = (float(argument[20]))/Vin
        G3 = (float(argument[22]))/Vin
        G4 = (float(argument[24]))/Vin
        G5 = (float(argument[26]))/Vin
        G6 = (float(argument[28]))/Vin
        G7 = (float(argument[30]))/Vin
        G8 = (float(argument[32]))/Vin
        G9 = (float(argument[34]))/Vin
        G10 = (float(argument[36]))/Vin
        DB1 = round(20*math.log10(G1),3)
        DB2 = round(20*math.log10(G2),3)
        DB3 = round(20*math.log10(G3),3)
        DB4 = round(20*math.log10(G4),3)
        DB5 = round(20*math.log10(G5),3)
        DB6 = round(20*math.log10(G6),3)
        DB7 = round(20*math.log10(G7),3)
        DB8 = round(20*math.log10(G8),3)
        DB9 = round(20*math.log10(G9),3)
        DB10 = round(20*math.log10(G10),3)
        DB=(DB1+DB2+DB3+DB4+DB5+DB6+DB7+DB8+DB9+DB10)/10
        Vin=1.2
        g1 = (float(argument[38])*0.1)/Vin
        g2 = (float(argument[40])*0.1)/Vin
        g3 = (float(argument[42])*0.1)/Vin
        g4 = (float(argument[44])*0.1)/Vin
        g5 = (float(argument[46])*0.1)/Vin
        g6 = (float(argument[48])*0.1)/Vin
        g7 = (float(argument[50])*0.1)/Vin
        g8 = (float(argument[52])*0.1)/Vin
        g9 = (float(argument[54])*0.1)/Vin
        g10 = (float(argument[56])*0.1)/Vin
        dB1 = round(20*math.log10(g1),3)
        dB2 = round(20*math.log10(g2),3)
        dB3 = round(20*math.log10(g3),3)
        dB4 = round(20*math.log10(g4),3)
        dB5 = round(20*math.log10(g5),3)
        dB6 = round(20*math.log10(g6),3)
        dB7 = round(20*math.log10(g7),3)
        dB8 = round(20*math.log10(g8),3)
        dB9 = round(20*math.log10(g9),3)
        dB10 = round(20*math.log10(g10),3)
        print(json.dumps({"length":[{"Gain for bride type attenuator":str(d1)+" , "+str(d2)+" , "+str(d3)+" , "+str(d4)+" and "+str(d5),"Gain for T type attenuator":str(DB1)+" , "+str(DB2)+" , "+str(DB3)+" , "+str(DB4)+" , "+str(DB5)+" , "+str(DB6)+" , "+str(DB7)+" , "+str(DB8)+" , "+str(DB9)+" and "+str(DB10),"Gain for Pi type attenuator":str(dB1)+" , "+str(dB2)+" , "+str(dB3)+" , "+str(dB4)+" , "+str(dB5)+" , "+str(dB6)+" , "+str(dB7)+" , "+str(dB8)+" , "+str(dB9)+" and "+str(dB10)}] }))









