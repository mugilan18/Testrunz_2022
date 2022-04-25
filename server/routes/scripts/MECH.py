import json
import math


class MECH:
    def __init__(self, arg):
        self.arg = arg
    def DS_test(self):
        argument = self.arg[0:]
        #print(argument)
        Ifv1 = float(argument[1])/math.sqrt(3)
        Ifv2 = float(argument[2])/math.sqrt(3)
        pa1 = math.acos(-1)*(float(argument[1]))
        pa2 = math.acos(-1)*(float(argument[2]))
        pa3 = math.acos(-1)*(float(argument[3]))
        reg1 = (float(argument[3]) - 239.6)/239.6 * 100
        reg2 = (float(argument[4]) - 239.6)/239.6 * 100
        reg3 = (float(argument[5]) - 239.6)/239.6 * 100
        reg = (reg1+reg2+reg3)/3
        reg01 = (float(argument[6]) - 239.6)/239.6 * 100
        reg02 = (float(argument[7]) - 239.6)/239.6 * 100
        reg03 = (float(argument[8]) - 239.6)/239.6 * 100
        reg0 = (reg01+reg02+reg03)/3
        

        print(json.dumps({"Mean":[{"The Regulation of DS test is" : str(reg)}], "Mean":[{"The Regulation is" : str(reg0)}]}))

                  

                  
    def Three_Phase_Two_Wattmeter(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
         #Torque
        OR = float(argument[2])+float(argument[3])
        AR = float(argument[4])-float(argument[5])
                      
        W = float(argument[6])/float(argument[7])
        S =(math.sqrt(3))
        T = math.atan(1)
        PA = T*S*W
        PF = math.cos(PA)


        print(json.dumps({"Mean":[{"The Three Phase Two Wattmeter is" : str(PF)}]}))

                      
    def Single_Phase_Transformer(self):
        argument = self.arg[0:]
        #print(argument)
        Eff1 = (float(argument[1])/float(argument[7]))* 100
        Eff2 = (float(argument[2])/float(argument[8]))* 100
        Eff3 = (float(argument[3])/float(argument[9]))* 100
        Eff4 = (float(argument[4])/float(argument[10]))* 100
        Eff5 = (float(argument[5])/float(argument[11]))* 100
        Eff6 = (float(argument[6])/float(argument[12]))* 100
        
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5 + Eff6)/6

                      

        Vfl = 115
        Reg1 = ((Vfl-float(argument[1]))/Vfl)* 100
        Reg2 = ((Vfl-float(argument[2]))/Vfl)* 100
        Reg3 = ((Vfl-float(argument[3]))/Vfl)* 100
        Reg4 = ((Vfl-float(argument[4]))/Vfl)* 100
        Reg5 = ((Vfl-float(argument[5]))/Vfl)* 100
        Reg6 = ((Vfl-float(argument[6]))/Vfl)* 100
        
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5 + Reg6)/6
                      
        #Armature_Resistance Ra table2
        Ra1 = float(argument[1])/float(argument[2])
        Ra2 = float(argument[3])/float(argument[4])
        Ra3 = float(argument[5])/float(argument[6])
        Ra4 = float(argument[7])/float(argument[8])
        Ra5 = float(argument[9])/float(argument[10])
                      
        Ra = (Ra1 + Ra2 + Ra3 + Ra4 + Ra5)/5


        print(json.dumps({"Mean":[{"The Efficiency is" : str(Eff)}], "Mean":[{"The Regularity is" : str(Reg) + " N"}], "Mean":[{"The Armature Resistance is" : str(Ra) + " Ohm"}]}))

                      
    def Three_PHASE_SQUIRREL_CAGE(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
        #Torque
        T1 = 9.81*((float(argument[1])-float(argument[6]))+2)*0.0986
        T2 = 9.81*((float(argument[2])-float(argument[7]))+2)*0.0986
        T3 = 9.81*((float(argument[3])-float(argument[8]))+2)*0.0986
        T4 = 9.81*((float(argument[4])-float(argument[9]))+2)*0.0986
        T5 = 9.81*((float(argument[5])-float(argument[10]))+2)*0.0986
                      
        #input
        IP1 = float(argument[1]) * float(argument[2])
        IP2 = float(argument[3]) * float(argument[4])
        IP3 = float(argument[5]) * float(argument[6])
        IP4 = float(argument[7]) * float(argument[8])
        IP5 = float(argument[9]) * float(argument[10])

            #output
        OP1 = (2*math.pi*float(argument[1])*float(argument[2]))/60
        OP2 = (2*math.pi*float(argument[3])*float(argument[4]))/60
        OP3 = (2*math.pi*float(argument[5])*float(argument[6]))/60
        OP4 = (2*math.pi*float(argument[7])*float(argument[8]))/60
        OP5 = (2*math.pi*float(argument[9])*float(argument[10]))/60

        #Eff
        Eff1 = (OP1/IP1)*100
        Eff2 = (OP2/IP2)*100
        Eff3 = (OP3/IP3)*100
        Eff4 = (OP4/IP4)*100
        Eff5 = (OP5/IP5)*100
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5)/5

        Ns = 1500
        Reg1 = ((Ns - float(argument[1]))/Ns)*100
        Reg2 = ((Ns - float(argument[2]))/Ns)*100
        Reg3 = ((Ns - float(argument[3]))/Ns)*100
        Reg4 = ((Ns - float(argument[4]))/Ns)*100
        Reg5 = ((Ns - float(argument[5]))/Ns)*100
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5)/5
        

        print(json.dumps({"Mean":[{"The efficiency of Three PHASE SQUIRREL CAGE is" : str(Eff)}] , "Mean":[{"The Regularity is" : str(Reg)}]}))

                     
    def SWINBURNES_TEST(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
        Ra1 = float(argument[1])/float(argument[2])
        Ra2 = float(argument[3])/float(argument[4])
        Ra3 = float(argument[5])/float(argument[6])
        Ra4 = float(argument[7])/float(argument[8])
        Ra5 = float(argument[9])/float(argument[10])
        
        Ra = (Ra1 + Ra2 + Ra3 + Ra4 + Ra5)/5


        print(json.dumps({"Mean":[{"The SWINBURNE’S TEST is" : str(Ra)}]}))

                      
    def single_phase_induction_motor(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
                       
        #Torque
        T1 = 9.81*((float(argument[1])-float(argument[2]))+2)*0.0986
        T2 = 9.81*((float(argument[3])-float(argument[4]))+2)*0.0986
        T3 = 9.81*((float(argument[5])-float(argument[6]))+2)*0.0986
        T4 = 9.81*((float(argument[7])-float(argument[8]))+2)*0.0986
        T5 = 9.81*((float(argument[9])-float(argument[10]))+2)*0.0986
                      
        #input
        IP1 = float(argument[1]) * float(argument[2])
        IP2 = float(argument[3]) * float(argument[4])
        IP3 = float(argument[5]) * float(argument[6])
        IP4 = float(argument[7]) * float(argument[8])
        IP5 = float(argument[9]) * float(argument[10])

            #output
        OP1 = (2*math.pi*float(argument[1])*float(argument[2]))/60
        OP2 = (2*math.pi*float(argument[3])*float(argument[4]))/60
        OP3 = (2*math.pi*float(argument[5])*float(argument[6]))/60
        OP4 = (2*math.pi*float(argument[7])*float(argument[8]))/60
        OP5 = (2*math.pi*float(argument[9])*float(argument[10]))/60
        #Eff
        Eff1 = (OP1/IP1)*100
        Eff2 = (OP2/IP2)*100
        Eff3 = (OP3/IP3)*100
        Eff4 = (OP4/IP4)*100
        Eff5 = (OP5/IP5)*100
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5)/5

        Ns = 1500
        Reg1 = ((Ns - float(argument[1]))/Ns)*100
        Reg2 = ((Ns - float(argument[3]))/Ns)*100
        Reg3 = ((Ns - float(argument[5]))/Ns)*100
        Reg4 = ((Ns - float(argument[7]))/Ns)*100
        Reg5 = ((Ns - float(argument[9]))/Ns)*100
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5)/5
        

        print(json.dumps({"Mean":[{"The efficiency of single phase induction motor is" : str(Eff)}] , "Mean":[{"The Regularity is" : str(Reg)}]}))

                      
    def OC_SC_Single_phase(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
                       
        #Torque
        T1 = 9.81*((float(argument[1])-float(argument[2]))+2)*0.0986
        T2 = 9.81*((float(argument[3])-float(argument[4]))+2)*0.0986
        T3 = 9.81*((float(argument[5])-float(argument[6]))+2)*0.0986
        T4 = 9.81*((float(argument[7])-float(argument[8]))+2)*0.0986
        T5 = 9.81*((float(argument[9])-float(argument[10]))+2)*0.0986
                      
        #input
        IP1 = float(argument[1]) * float(argument[2])
        IP2 = float(argument[3]) * float(argument[4])
        IP3 = float(argument[5]) * float(argument[6])
        IP4 = float(argument[7]) * float(argument[8])
        IP5 = float(argument[9]) * float(argument[10])

            #output
        OP1 = (2*math.pi*float(argument[1])*float(argument[2]))/60
        OP2 = (2*math.pi*float(argument[3])*float(argument[4]))/60
        OP3 = (2*math.pi*float(argument[5])*float(argument[6]))/60
        OP4 = (2*math.pi*float(argument[7])*float(argument[8]))/60
        OP5 = (2*math.pi*float(argument[9])*float(argument[10]))/60
        #Eff
        Eff1 = (OP1/IP1)*100
        Eff2 = (OP2/IP2)*100
        Eff3 = (OP3/IP3)*100
        Eff4 = (OP4/IP4)*100
        Eff5 = (OP5/IP5)*100
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5)/5

        Ns = 1500
        Reg1 = ((Ns - float(argument[1]))/Ns)*100
        Reg2 = ((Ns - float(argument[3]))/Ns)*100
        Reg3 = ((Ns - float(argument[5]))/Ns)*100
        Reg4 = ((Ns - float(argument[7]))/Ns)*100
        Reg5 = ((Ns - float(argument[9]))/Ns)*100
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5)/5

        print(json.dumps({"Mean":[{"The efficiency of single phase open and short circuit is" : str(Eff)}] , "Mean":[{"The Regularity is" : str(Reg)}]}))

                      
    def efficiency_motor_generator(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra

        Ra = float(argument[1]) + float(argument[2]) + float(argument[10])/3
        Ia = float(argument[3]) + float(argument[4])
        CL = (float(argument[5])*float(argument[6]))- (Ia**2)*Ra
        CP = (float(argument[7])**2)*Ra
        OP = float(argument[9])*float(argument[8])
        #efficiency generator
        eff1 = OP/float(argument[10])
        #efficiency motor                       
        CP = (float(argument[7])**2)*Ra
        OP = float(argument[9])*float(argument[8])
        eff2 = OP/float(argument[10])
        
        
        print(json.dumps({"Mean":[{"The efficiency of generator is" : str(eff)}] , "Mean":[{"The efficiency of motor is" : str(eff2)}]}))
                       





