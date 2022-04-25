import json

class PowerElec:
    def __init__(self, arg):
        self.arg = arg
        
    def Gate_Pulse_Generation(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the R, RC &UJT triggering circuit for SCR was constructed and its output waveforms were plotted."}]}))
        
    def CHARACTERISTICS_OF_SCR (self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the Characteristics of SCR and the Output waveforms were obtained."}]}))
        
    def CHARACTERISTICS_OF_TRIAC(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the Characteristics of TRIAC and the Output waveforms were obtained."}]}))
        
        
    def MOSFET_IGBT(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the Characteristics of MOSFET & IGBT were obtained."}]}))
        
        
    def HALF_CONTROLLED(self):
        argument = self.arg[0:]
        Vo1 = float(argument[4])*20
        Vo2 = float(argument[8])*20
        Vo3 = float(argument[15])*20
        mean = (Vo1+Vo2+Vo3)/3
        print(json.dumps({"Mean":[{"The Step down and step up MOSFET based choppers are" : str(mean)}]}))

        
    def FULLY_CONTROLLED(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"The Input and Output waveforms of Full Wave Rectifier."}]}))

    def MOSFET_BASED_CHOPPERS(self):
        argument = self.arg[0:]
        Vo1 = float(argument[1])/float(argument[2])
        Vo2 = float(argument[4])/float(argument[5])
        Vo3 = float(argument[7])/float(argument[8])
        mean_1 =  (Vo1+Vo2+Vo3)/3
        print(json.dumps({"Ton_1":[{"The Step up MOSFET based choppers T1 are" : str(Vo1)}] ,"Ton_2":[{"The Step up MOSFET based choppers T2 are" : str(Vo2)}] ,"Ton_3":[{"The Step up MOSFET based choppers T3  are" : str(Vo3)}] ,"Mean":[{"The Step up MOSFET based choppers mean are" : str(mean_1)}]}))
        SD1 = float(argument[10])/float(argument[11])
        SD2 = float(argument[13])/float(argument[14])
        SD3 = float(argument[16])/float(argument[17])
        mean_2 =  (SD1+SD2+SD3)/3
        print(json.dumps({"Ton_3":[{"The Step down MOSFET based choppers T1 are" : str(SD1)}] ,"Ton_5":[{"The Step down MOSFET based choppers T2 are" : str(SD2)}] ,"Ton_6":[{"The Step down MOSFET based choppers T3  are" : str(SD3)}] ,"Mean":[{"The Step up MOSFET based choppers mean are" : str(mean_2)}]}))


        
    def SINGLE_PHASE_PWM_INVERTER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the output waveform for IGBT inverter (PWM) was obtained."}]}))

    def THREE_PHASE_PWM_INVERTER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the output waveform for IGBT inverter (PWM) was obtained."}]}))
        
        
    def AC_VOLTAGE_CONTROLLER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the operation and performance of the single phase AC voltage control using TRIAC is done and output Verified."}]}))
        
        
    def SWITCHED_MODE_POWER_CONVERTER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":" Thus the output of Switched mode power convertor is obtained."}]}))

 