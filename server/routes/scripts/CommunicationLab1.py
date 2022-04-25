import json
import math
class CL1:
    def __init__(self, arg):
        self.arg = arg
    def Tuned(self):
        argument = self.arg[:]
        Vin=float(argument[1])*float(argument[2])

        G1 = float(argument[5])*float(argument[3])/Vin
        G2 = float(argument[7])*float(argument[3])/Vin
        G3 = float(argument[9])*float(argument[3])/Vin
        G4 = float(argument[11])*float(argument[3])/Vin
        DB1 = round(20*math.log10(G1),2)
        DB2 = round(20*math.log10(G2),2)
        DB3 = round(20*math.log10(G3),2)
        DB4 =round( 20*math.log10(G4),2)
        T1 =( float(argument[12])-float(argument[13]) )
        g1 = float(argument[17])*float(argument[15])/float(argument[14])*10**3
        g2 = float(argument[19])*float(argument[15])/float(argument[14])*10**3
        g3 =float(argument[21])*float(argument[15])/float(argument[14])*10**3
        g4 = float(argument[23])*float(argument[15])/float(argument[14])*10**3
        dB1 = round(20*math.log10(g1),2)
        dB2 = round(20*math.log10(g2),2)
        dB3 = round(20*math.log10(g3),2)
        dB4 = round(20*math.log10(g4),2)
        T2 = float(argument[24])-float(argument[25])
        print(json.dumps({"length":[{"Result":"Thus the tuned amplifier and wide amplifier are constructed and their frequency response also determined."}], "breadth":[{"BW for tuned" : str(T1)+"Hz"}], "width":[{"B.W for wideband" : str(T2)+"HZ"}],"Gain1":[{"Gain in db_Tuned amplifier":str(DB1)+", "+str(DB2)+", "+str(DB3)+", "+str(DB4)+", "}],"WB":[{"Gain in db_Wideband amplifier":str(dB1)+", "+str(dB2)+", "+str(dB3)+", "+str(dB4)}]}))
   
     
    def Frequency(self):
        argument = self.arg[:]
        Amp1 = float(argument[2])*float(argument[1])
        Amp2 = float(argument[6])*float(argument[1])
        Amp3 = float(argument[10])*float(argument[1])
        T1=round(float(argument[3])*float(argument[4]),2)
        T2=float(argument[7])*float(argument[8])
        f=float(argument[9])
        F=float(argument[5])
        C=float(argument[11])
        E=float(argument[12])
        FF=float(argument[13])
        print(json.dumps({"answer":[{"Result":"The frequency modulator and demodulator circuits are constructed and the output waveform is observed","Message Signal":str(),"Amplitude ":str(Amp1),"Time signal":str(T1),"Frequency":str(F),"Carrier Signal":str()," Amplitude":str(Amp2),"Time signal ":str(T2),"frequency":str(f),"Modulated Signal":str(),"Amplitude":str(Amp3)," Compressed cycle":str(C),"Expanded cycle":str(E),"Frequency(Hz)":str(FF)}]})) 
     
    def Amplitude(self):
        argument = self.arg[:]
        Amp1=float(argument[2])*float(argument[3])
        Amp2=float(argument[7])*float(argument[8])
        Vmax=float(argument[12])*float(argument[13])
        Vmin=float(argument[17])*float(argument[18])
        Amp5=float(argument[19])*float(argument[20])
        Ts1=float(argument[4])*float(argument[5])
        Ts2=float(argument[9])*float(argument[10])
        Ts3=float(argument[14])*float(argument[15])
        Ts4=float(argument[21])*float(argument[22])
        MI=(Vmax-Vmin)/(Vmax+Vmin)
        print(json.dumps({"Amplitude":[{"Result":"The amplitude modulator and demodulator circuits was constructed and their output waveform with observed and Modulation index is observed","Modulation Index":str(MI)}]}))

    def emphasis(self):
        argument = self.arg[:]
        G1 = float(argument[4])*float(argument[1])
        G2 = float(argument[7])*float(argument[1])
        G3 = float(argument[10])*float(argument[1])
        G4 = float(argument[13])*float(argument[1])
        G5 = float(argument[16])*float(argument[1])
        g1 = float(argument[5])*float(argument[2])
        g2 = float(argument[8])*float(argument[2])
        g3 = float(argument[11])*float(argument[2])
        g4 = float(argument[14])*float(argument[2])
        g5 = float(argument[17])*float(argument[2])
        Gain1= round(20*math.log10(G1),2)
        Gain2= round(20*math.log10(G2),2)
        Gain3= round(20*math.log10(G3),2)
        Gain4= round(20*math.log10(G4),2)
        Gain5= round(20*math.log10(G5),2)
        gain1= round(20*math.log10(g1),2)
        gain2= round(20*math.log10(g2),2)
        gain3=round( 20*math.log10(g3),2)
        gain4= round(20*math.log10(g4),2)
        gain5=round( 20*math.log10(g5),2)
        print(json.dumps({"answer":[{"The pre Emphasis and De Emphasis are constructed and frequency response is determined and Gain ": str(),
        "Pre-Emphasis":str(Gain1)+", "+str(Gain2)+", "+str(Gain3)+", "+str(Gain4)+", "+str(Gain5),"De - Emphasis":str(gain1)+", "+str(gain2)+", "+str(gain3)+", "+str(gain4)+", "+str(gain5)}]}))

    def Sample(self):
        argument = self.arg[:]
        G1=float(argument[1])*float(argument[2])
        G2=float(argument[6])*float(argument[7])
        G3=float(argument[11])*float(argument[12])
        T1=float(argument[3])*float(argument[4])
        T2=float(argument[8])*float(argument[9])
        T3=float(argument[13])*float(argument[14])
        g1=float(argument[16])*float(argument[17])
        g2=float(argument[21])*float(argument[22])
        g3=float(argument[26])*float(argument[27])
        g4=float(argument[31])*float(argument[32])
        t1=float(argument[18])*float(argument[19])
        t2=float(argument[23])*float(argument[24])
        t3=float(argument[28])*float(argument[29])
        t4=float(argument[33])*float(argument[34])
        print(json.dumps({"answer":[{"Result":" Thus the sample and hold circuit and PAM circuit are constructed under operation both studied."}]}))
    def Automatic(self):
        argument = self.arg[:]
        G1=float(argument[2])*float(argument[3])
        G2=float(argument[8])*float(argument[9])
        G3=float(argument[14])*float(argument[15])
        G4=float(argument[20])*float(argument[21])
        G5=float(argument[26])*float(argument[27])
        G6=float(argument[32])*float(argument[33])
        g1=float(argument[5])*float(argument[6])
        g2=float(argument[11])*float(argument[12])
        g3=float(argument[17])*float(argument[18])
        g4=float(argument[23])*float(argument[24])
        g5=float(argument[29])*float(argument[30])
        g6=float(argument[35])*float(argument[36])
        print(json.dumps({"answer":[{"Result":"Thus the sample AGC circle is constructed and it performance characteristics was studied"}]}))
    def Delayed(self):
        argument = self.arg[:]
        G1 = float(argument[3])*float(argument[1])
        G2 = float(argument[5])*float(argument[1])
        G3 = float(argument[7])*float(argument[1])
        G4 = float(argument[9])*float(argument[1])
        G5 = float(argument[11])*float(argument[1])
        print(json.dumps({"answer":[{"The delayed automatic gain control circuit is constructed and its performance is studied.":str(),"Delayed AGC _Vo":str(G1)+", "+str(G2)+", "+str(G3)+", "+str(G4)+", "+str(G5)}]}))

    def Pulse(self):
        argument = self.arg[:]
        G1=float(argument[1])*float(argument[2])
        G2=float(argument[6])*float(argument[7])
        G3=float(argument[11])*float(argument[12])
        G4=float(argument[16])*float(argument[17])
        T1=float(argument[3])*float(argument[4])
        T2=float(argument[8])*float(argument[9])
        T3=float(argument[13])*float(argument[14])
        T4=float(argument[18])*float(argument[19])
        print(json.dumps({"answer":[{"Result":" Thus the pulse width modulator and Pulse position modulation waveform are constructed and their operation are studied."}]}))
    def Mixer(self):
        argument = self.arg[:]
        G1 = float(argument[1])*2
        G2 = float(argument[4])*2
        G3 = float(argument[7])*2
        g1 = float(argument[2])*2
        g2 = float(argument[5])*2
        g3 = float(argument[8])*2
        R=(float(argument[22])-float(argument[18]))/(float(argument[22])+float(argument[18]))
        print(json.dumps({"answer":[{"Result":"Thus the frequency mixer and ring  modulator circuits are constructed and their performance characteristics are studied."}], "breadth":[{"Modulation Index":str(R)}]}))





