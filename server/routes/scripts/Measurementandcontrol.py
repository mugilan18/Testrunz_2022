import json
import math as m

class MAC:
    def __init__(self, arg):
        self.arg = arg[0:]
    def Single_energy(self):
        argument = self.arg[0:]
        W1=float(argument[2]) * float(argument[3])
        W2=float(argument[6]) * float(argument[7])
        W3=float(argument[10]) * float(argument[11])
        W4=float(argument[14]) * float(argument[15])

        ME1=round(float(argument[5])/float(argument[1]),5)
        ME2=round(float(argument[9])/float(argument[1]),5)
        ME3=round(float(argument[13])/float(argument[1]),5)
        ME4=round(float(argument[17])/float(argument[1]),5)

        TE1=round(W1*float(argument[4])/(1000*3600),5)
        TE2=round(W2*float(argument[8])/(1000*3600),5)
        TE3=round(W3*float(argument[12])/(1000*3600),5)
        TE4=round(W4*float(argument[16])/(1000*3600),5)

        E1=round((ME1-TE1)*100/TE1,2)
        E2=round((ME2-TE2)*100/TE2,2)
        E3=round((ME3-TE3)*100/TE3,2)
        E4=round((ME4-TE4)*100/TE4,2)
        # print(json.dumps({ "True":[{"The Measured Energy are " : str(ME2) }]} ))

        print(json.dumps({ "True":[{"The Measured Energy are " : str(ME1)+" , "+str(ME2)+" , "+str(ME3)+" and "+str(ME4),"The True energy are " : str(TE1)+" , "+str(TE2)+" , "+str(TE3)+" and "+str(TE4),"The Error percentage are " : str(E1)+"% , "+str(E2)+"% , "+str(E3)+"% and "+str(E4)+"%"}] }))
    def Network(self):
        argument = self.arg[0:]
        Il1 = round(float(argument[3])*1000/(float(argument[2])+float(argument[1])),2)
        Il2 = round(float(argument[6])*1000/(float(argument[5])+float(argument[4])),2)

        Ild= (float(argument[9])/(float(argument[8])+float(argument[9])) )* float(argument[10])
        Ildd= (float(argument[9])/(float(argument[8])+float(argument[9])) )* float(argument[11])
        
        # print(json.dumps({"length":[{"Thus the Thevenin's and Superposition theorem have been verified theoretically and practically."}], "breadth":[{"Ans" : str(R)}]}))
        print(json.dumps({ "True":[{"Thevenin’s theorem" : "The Inductance value are "+str(Il1)+" and "+str(Il2),"Superposition theorem" : "The Inductance value are "+str(Ild)+" and "+str(Ildd) }] }))
    
    def Bridge(self):
        argument = self.arg[0:]
        R1 = (float(argument[1]) + float(argument[2]) +float(argument[3]))/3
        R2 = (float(argument[5]) + float(argument[6]) +float(argument[7]))/3
        R3 = (float(argument[9]) + float(argument[10]) +float(argument[11]))/3
        R4 = (float(argument[13]) + float(argument[14]) +float(argument[15]))/3
        R5 = (float(argument[17]) + float(argument[18]) +float(argument[19]))/3
        R=(R1+R2+R3+R4+R5)/5
        K1= (float(argument[21]) * float(argument[23])) /float(argument[22])
        K2= (float(argument[24]) * float(argument[26])) /float(argument[25])
        K3= (float(argument[27]) * float(argument[29])) /float(argument[28])
        K4= (float(argument[30]) * float(argument[32])) /float(argument[31])
        K5= (float(argument[33]) * float(argument[35])) /float(argument[34])
        RX1= K1*0.1
        RX2= K2*0.1
        RX3= K3*0.1
        RX4= K4*0.1
        RX5= K5*0.1
        Rx=(RX1+RX2+RX3+RX4+RX5)/5
        print(json.dumps({"length":[{"Thus the values of the medium and low resistance are measured using Wheatstone and Kelvin’s double bridge."}], "breadth":[{"Observed Resistance in Ohms" : str(R)}], "bread":[{"Set value RX" : str(Rx)}]}))
    def VOLTMETER(self):
        argument = self.arg[0:]
        R1 = (float(argument[1]) / float(argument[2]))
        R2 = (float(argument[3]) / float(argument[4]))
        R3 = (float(argument[5]) / float(argument[6]))
        R4 = (float(argument[7]) / float(argument[8]))
        R5 = (float(argument[9]) / float(argument[10]))
        R6 = (float(argument[11]) / float(argument[12]))
        R =(R1+R2+R3+R4+R5+R6)/6
        E1 = ((float(argument[14]) - float(argument[15])) /float(argument[15]))*100
        E2 = ((float(argument[17]) - float(argument[18])) /float(argument[18]))*100
        E3 = ((float(argument[20]) - float(argument[21])) /float(argument[21]))*100
        E4 = ((float(argument[23]) - float(argument[24])) /float(argument[24]))*100
        E5 = ((float(argument[26]) - float(argument[27])) /float(argument[27]))*100
        E6 = ((float(argument[29]) - float(argument[30])) /float(argument[30]))*100
        E=(E1+E2+E3+E4+E5+E6)/6
        print(json.dumps({"length":[{"Thus the range of voltmeter and ammeter is extended to the desired value."}], "breadth":[{"Resistance" : str(R)}], "bread":[{"Error Percentage" : str(E)}]}))
    
    def VOLTAGE(self):
        print(json.dumps({"answer":[{"result":"Thus the characteristics of signal converter circuits using grounded load and floating load is determined."}]}))

    def INSTRUMENTATION(self):
        argument = self.arg[0:]
        
        Vd1= float(argument[1]) - float(argument[2])
        Vd2= float(argument[4]) - float(argument[5])
        Vd3= float(argument[7]) - float(argument[8])
        Vd4= float(argument[10]) - float(argument[11])
        Vd5= float(argument[12]) - float(argument[13])

        A1=float(argument[3])/Vd1
        A2=float(argument[6])/Vd2
        A3=float(argument[9])/Vd3
        A4=float(argument[12])/Vd4
        A5=float(argument[15])/Vd5
        vo1 = round(A1*Vd1,2)
        vo2 = round(A2*Vd2,2)
        vo3 = round(A3*Vd3,2)
        vo4 = round(A4*Vd4,2)
        vo5 = round(A5*Vd5,2)
        print(json.dumps({"length":[{"The Theoritical Voltage values are ":str(vo1)+"V , "+str(vo2)+"V , "+str(vo3)+"V , "+str(vo4)+"V and "+str(vo5)}]}))
    def TRANSFER(self):
        argument = self.arg[0:]
        E1= float(argument[1]) - (float(argument[2])* 1.6)
        E2= float(argument[4]) - (float(argument[5])* 1.6)
        E3= float(argument[7]) - (float(argument[8])* 1.6)
        E4= float(argument[10]) - (float(argument[11])* 1.6)
        E5= float(argument[13]) - (float(argument[14])* 1.6)
        w1=2*m.pi*float(argument[3])/60
        w2=2*m.pi*float(argument[6])/60
        w3=2*m.pi*float(argument[9])/60
        w4=2*m.pi*float(argument[12])/60
        w5=2*m.pi*float(argument[15])/60

        Ra1 = (float(argument[16]) / float(argument[17]))
        Ra2 = (float(argument[18]) / float(argument[19]))
        Ra3 = (float(argument[20]) / float(argument[21]))
        Ra4 = (float(argument[22]) / float(argument[23]))
        Ra5 = (float(argument[24]) / float(argument[25]))
        Ra=round((Ra1+Ra2+Ra3+Ra4+Ra5)/5,3)

        Za1=(float(argument[26]) / float(argument[27]))
        Za2=(float(argument[28]) / float(argument[29]))
        Za3=(float(argument[30]) / float(argument[31]))
        Za4=(float(argument[32]) / float(argument[33]))
        Za5=(float(argument[34]) / float(argument[35]))
        Za=(Za1+Za2+Za3+Za4+Za5)/5
        Xa = m.sqrt(Za**2 - Ra**2)
        If=0.7
        J=21
        La =round( Xa/2*J*If,3)
        print(json.dumps({"length":[{"The  average  armature resiatance is":str(Ra)+"ohm" , "The  average  armature inductance is":str(La)+"H"}]}))
    def LDR(self):
        print(json.dumps({"answer":[{"result":"Thus the V-I characteristics of LDR was drawn for various  illuminations level at constant supply voltage and various and supply voltage as constant illumination level."}]}))
    def THERMOCOUPLE(self):
        print(json.dumps({"answer":[{"result":"Thus the characteristics of temperature transducer using RTD and thermocouple have been studied and plotted."}]}))
    def THERMOCOUPLE(self):
        print(json.dumps({"answer":[{"result":"Thus the ratio between V and F is compared with theoretical value and it is verified."}]}))
    def DISPLACEMENT(self):
        argument = self.arg[0:]
        R1 = (float(argument[2]) -float(argument[3]))
        R2 = (float(argument[5]) - float(argument[6]))
        R3 = (float(argument[8]) - float(argument[9]))
        R4 = (float(argument[11]) - float(argument[12]))
        R5 = (float(argument[14]) - float(argument[15]))
        Ra=(R1+R2+R3+R4+R5)/5
        print(json.dumps({"length":[{"Thus the characteristics of Linear Variable Displacement Transducer  are studied and plotted."}], "breadth":[{"V" : str(R)}]}))
    def Three(self):
        argument = self.arg[0:]
        TE1 = (float(argument[4]) * float(argument[6]))/(60*60*1000)
        TE2 = (float(argument[10]) * float(argument[12]))/(60*60*1000)
        TE3 = (float(argument[16]) * float(argument[18]))/(60*60*1000)
        TE4 = (float(argument[22]) * float(argument[24]))/(60*60*1000)
        TE5 = (float(argument[28]) * float(argument[30]))/(60*60*1000)
        TE=(TE1+TE2+TE3+TE4+TE5)/5
        RE1=60/(float(argument[1]) * float(argument[2]))
        RE2=60/(float(argument[7]) * float(argument[8]))
        RE3=60/(float(argument[13]) * float(argument[14]))
        RE4=60/(float(argument[19]) * float(argument[20]))
        RE5=60/(float(argument[25]) * float(argument[26]))
        RE=(RE1+RE2+RE3+RE4+RE5)/5
        Error = ((TE-RE)/RE)*100
        print(json.dumps({"length":[{"The  three phase meters are calibrated using wattmeter and the respective graphs are drawn."}], "True":[{"True Energy" : str(TE)}], "breadth":[{"Record Energy" : str(RE)}], "breadth":[{"Error" : str(Error)}]}))
    
    def inductance(self):
        argument = self.arg[0:]
        Lx1 =round(float(argument[4])* float(argument[1])/float(argument[2]),2)
        Lx2=round(float(argument[8])* float(argument[5])/float(argument[6]),2)
        Lx3=round(float(argument[12])* float(argument[9])/float(argument[10]),2)
        Lx4=round(float(argument[16])* float(argument[13])/float(argument[14]),2)

        Rx1=round(float(argument[1])* float(argument[3])/float(argument[2]),2)
        Rx2=round(float(argument[5])* float(argument[7])/float(argument[6]),2)
        Rx3=round(float(argument[9])* float(argument[11])/float(argument[10]),2)
        Rx4=round(float(argument[13])* float(argument[15])/float(argument[14]),2)

        print(json.dumps({ "True":[{"the unknown inductance are " : str(Lx1)+" , "+str(Lx2)+" , "+str(Lx3)+" and "+str(Lx4),"the unknown resistance are " : str(Rx1)+" , "+str(Rx2)+" , "+str(Rx3)+" and "+str(Rx4)}] }))
    def capacitances(self):
        argument = self.arg[0:]
        Cx1=round(float(argument[3])* float(argument[2])/float(argument[1]),2)
        Cx2=round(float(argument[6])* float(argument[5])/float(argument[4]),2)
        Cx3=round(float(argument[9])* float(argument[8])/float(argument[7]),2)
        Cx4=round(float(argument[12])* float(argument[11])/float(argument[10]),2)
        print(json.dumps({ "True":[{"the unknown capacitances are " : str(Cx1)+"uF , "+str(Cx2)+"uF , "+str(Cx3)+"uF and "+str(Cx4)+"uF"}] }))
        

    def voltagetocurrent(self):
        argument = self.arg[0:]
        Il1=round(float(argument[2])/float(argument[1]),2)
        Il2=round(float(argument[4])/float(argument[1]),2)
        Il3=round(float(argument[6])/float(argument[1]),2)
        Il4=round(float(argument[8])/float(argument[1]),2)
        Il5=round(float(argument[10])/float(argument[1]),2)
        Il6=round(float(argument[12])/float(argument[1]),2)

        Vs1=round(float(argument[15])/float(argument[14]),2)
        Vs2=round(float(argument[17])/float(argument[14]),2)
        Vs3=round(float(argument[19])/float(argument[14]),2)
        Vs4=round(float(argument[21])/float(argument[14]),2)
        Vs5=round(float(argument[23])/float(argument[14]),2)
        Vs6=round(float(argument[25])/float(argument[14]),2)
        print(json.dumps({ "True":[{"The Current values are " : str(Il1)+"A , "+str(Il2)+"A , "+str(Il3)+"A , "+str(Il4)+"A , "+str(Il5)+"A and "+str(Il6)+"A","The Voltage values are " : str(Vs1)+"V , "+str(Vs2)+"V , "+str(Vs3)+"V , "+str(Vs4)+"V , "+str(Vs5)+"V and "+str(Vs6)+"V"}] }))
        




        