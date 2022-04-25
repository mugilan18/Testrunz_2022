import json
import math
class E2:
    def __init__(self, arg):
        self.arg = arg
    def LPF(self):
        #LPF
        argument = self.arg[:]
        Vin1 = 2
        Vo1 = float(argument[2])*0.2
        Vo2 = float(argument[4])*0.2
        Vo3 = float(argument[6])*0.2
        Vo4 = float(argument[8])*0.2
        Vo5 = float(argument[10])*0.2
        dB1 = 20*math.log(Vo1/Vin1)
        dB2 = 20*math.log(Vo2/Vin1)
        dB3 = 20*math.log(Vo3/Vin1)
        dB4 = 20*math.log(Vo4/Vin1)
        dB5 = 20*math.log(Vo5/Vin1)
        dB =(dB1+dB2+dB3+dB4+dB5)/5
        #HPF
        VO1 = float(argument[12])*0.2
        VO2 = float(argument[14])*0.2
        VO3 = float(argument[16])*0.2
        VO4 = float(argument[18])*0.2
        VO5 = float(argument[20])*0.2
        DB1 = 20*math.log(VO1/Vin1)
        DB2 = 20*math.log(VO2/Vin1)
        DB3 = 20*math.log(VO3/Vin1)
        DB4 = 20*math.log(VO4/Vin1)
        DB5 = 20*math.log(VO5/Vin1)
        DB =(DB1+DB2+DB3+DB4+DB5)/5
        print(json.dumps({"answer":[{"Result":"THUS THE DESIGN OF LOW PASS FILTER AND HIGH PASS FILTER IS VERIFIED","LOW PASS FILTER":dB,"HIGH PASS FILTER":DB}]}))
    def UJT(self):
        print(json.dumps({"answer":[{"Result":"The graph plotted and the Practical frequency is verified"}]}))
    def Astable(self):
        argument = self.arg[:]
        R=float(argument[33])
        C=float(argument[34])
        f = round(1/(0.69*(R+C)),2)
        print(json.dumps({"ans":[{"The design an astablemultivibrator using BJT and observe the output waveform" : str(f)+"Hz"}]}))
    def Monostable(self):
        #Symmetrical calculation
        argument = self.arg[:]
        #Amplitude in Volts
        A1 = float(argument[2])/float(argument[1])      
        A2 = float(argument[10])/float(argument[9]) 
        A=(A1+A2)/2
        #Time charging  
        T1 = float(argument[4])/float(argument[3])      
        T2 = float(argument[12])/float(argument[11]) 
        T=(T1+T2)/2   
        #Time(m)Discharging 
        D1 = float(argument[6])/float(argument[5])      
        D2 = float(argument[14])/float(argument[13]) 
        D=(D1+D2)/2   
        #Voltage shift(V)
        V1 = float(argument[8])/float(argument[7])      
        V2 = float(argument[16])/float(argument[15]) 
        V=(V1+V2)/2   
        #For asymmetrical configuration
        #Amplitude in Volts
        AA1 = float(argument[18])/float(argument[17])      
        AA2 = float(argument[26])/float(argument[25]) 
        AA=(AA1+AA2)/2
        #Time charging  
        AT1 = float(argument[20])/float(argument[19])      
        AT2 = float(argument[28])/float(argument[27]) 
        AT=(AT1+AT2)/2   
        #Time(m)Discharging 
        AD1 = float(argument[22])/float(argument[21])      
        AD2 = float(argument[30])/float(argument[29]) 
        AD=(AD1+AD2)/2   
        #Voltage shift(V)
        AV1 = float(argument[24])/float(argument[23])      
        AV2 = float(argument[32])/float(argument[31]) 
        AV=(AV1+AV2)/2   
        print(json.dumps({"ans":[{"For Symmetrical calculation  Amplitude in Volts" : str(A)}], "ans":[{"Time charging" : str(T)}], "ans":[{"Time Discharging":str(D)}] , "ans":[{"Voltage shift" : str(V)}], "ans":[{"For Asymmetrical calculation  Amplitude in Volts":str(AA)}], "ans":[{"Time charging":str(AT)}] , "ans":[{"Time Discharging" : str(AD)}], "ans":[{"Voltage shift":str(AV)}]   }))
    def RC(self):
        argument = self.arg[:]
        #Amplitude in volts
        A1 = float(argument[2])/float(argument[1])      
        A2 = float(argument[8])/float(argument[7])
        A3 = float(argument[14])/float(argument[13])
        A4 = float(argument[20])/float(argument[19]) 
        A=(A1+A2+A3+A4)/4
        #Time in ms
        T1 = float(argument[4])/float(argument[3])      
        T2 = float(argument[10])/float(argument[9]) 
        T3 = float(argument[16])/float(argument[15]) 
        T4 = float(argument[22])/float(argument[21]) 
        T=(T1+T2+T3+T4)/4   
        #Leading time
        L1 = float(argument[6])/float(argument[5])      
        L2 = float(argument[12])/float(argument[11]) 
        L3 = float(argument[18])/float(argument[17]) 
        L4 = float(argument[24])/float(argument[23]) 
        L=(L1+L2+L3+L4)/4  
        print(json.dumps({"answer":[{"Result":"THUS THE DESIGN OF TRANSISTOR BASED RC PHASE SHIFT OSCILLATOR VERIFIED","Amplitude in volts":A,"Time in ms":T,"Leading time":L}]}))
    def SCHMITT(self):
        argument = self.arg[:]
        #Amplitude in volts
        A1 = float(argument[2])*float(argument[1])      
        A2 = float(argument[5])*float(argument[6])
        A3 = float(argument[10])*float(argument[9])
        
        #Time in ms
        T1 = float(argument[3])*float(argument[4])      
        T2 = float(argument[7])*float(argument[8]) 
        T3 = float(argument[11])*float(argument[12]) 
        
        print(json.dumps({"answer":[{"Thus, the schmitt trigger circuit using transistor is designed and constructed and its performance":" ","Amplitude in volts":str(A1)+" V, "+str(A2)+" V, "+str(A3)+" V ","Time in ms":str(T1)+" ms, "+str(T2)+" ms, "+str(T3)+" ms"}]}))
    def single_RC(self):
        argument = self.arg[:]
        O1= float(argument[2])*float(argument[4])
        O2= float(argument[2])*float(argument[6])
        O3= float(argument[2])*float(argument[8])
        O4= float(argument[2])*float(argument[10])
        O5= float(argument[2])*float(argument[12])
        Vin=float(argument[1])
        G1 = (O1/Vin)*1000
        G2 = (O2/Vin)*1000
        G3 =( O3/Vin)*1000
        G4 = (O4/Vin)*1000
        G5= (O5/Vin)*1000

        DB1 = round(20*math.log10(G1),2)
        DB2 = round(20*math.log10(G2),2)
        DB3 = round(20*math.log10(G3),2)
        DB4 = round(20*math.log10(G4),2)
        DB5 = round(20*math.log10(G5),2)
        Bandwidth= (float(argument[13])- (float(argument[14])/10000))
        print(json.dumps({"answer":[{"To design and implement the RC coupled amplifier circuit":str(),"Gain in DB":str(DB1)+", "+str(DB2)+", "+str(DB3)+", "+str(DB4)+", "+str(DB5),"Cut off frequency":str(Bandwidth)+"Khz"}]}))