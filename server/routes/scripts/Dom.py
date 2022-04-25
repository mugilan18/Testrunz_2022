import json
import math
class Dom:
    def __init__(self, arg):
        self.arg = arg
    def Single_Helical(self):
        argument = self.arg[:]
#got output
        #print(argument)
        w1 = float(argument[4])*9.81
        w2 = float(argument[6])*9.81
        w3 = float(argument[8])*9.81
        w4 = float(argument[10])*9.81
        Avg =round((w1+w2+w3+w4)/4)
        S1 = w1/float(argument[5])
        S2 = w2/float(argument[7])
        S3 = w3/float(argument[9])
        S4 = w4/float(argument[11])
        S = round((S1+S2+S3+S4)/4)
        Ttheo1 = 2*math.pi*math.sqrt(w1/S)
        Ttheo2 = 2*math.pi*math.sqrt(w2/S)
        Ttheo3 = 2*math.pi*math.sqrt(w3/S)
        Ttheo4 = 2*math.pi*math.sqrt(w4/S)
        Theo = (Ttheo1+Ttheo2+Ttheo3+Ttheo4)/4
        Texp1 = float(argument[14])/float(argument[13])
        Texp2 = float(argument[17])/float(argument[16])
        Texp3 = float(argument[20])/float(argument[19])
        Texp4 = float(argument[23])/float(argument[22])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        print(json.dumps({"Lee":[{"Weight" : str(Avg) + "N"}], "Vernier":[{"Stiffness" : str(S) + "N/m"}], "tickness":[{"Theoretical time period" : str(Theo)}], "Thermal":[{"Periodic time" : str(Texp) + "sec"}], "The":[{"Result":"Thus the frequency of vibration of the helical spring is determined successfully both experimentally and the required graph is drawn"}]}))
    def Torsional(self):
        argument = self.arg[:]
        Texp1 = float(argument[6])/float(argument[5])
        Texp2 = float(argument[9])/float(argument[8])
        Texp3 = float(argument[12])/float(argument[11])
        Texp4 = float(argument[15])/float(argument[14])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        I = float(argument[3])*0.25**2/8
        Ip = math.pi*0.25**4/32
        K1 = 0.8*10**4*Ip/float(argument[16])
        K2 = 0.8*10**4*Ip/float(argument[17])
        K3 = 0.8*10**4*Ip/float(argument[18])
        K4 = 0.8*10**4*Ip/float(argument[19])
        K =(K1+K2+K3+K4)/4
        Ttheo1 = 2*math.pi*math.sqrt(I/K1)
        Ttheo2 = 2*math.pi*math.sqrt(I/K2)
        Ttheo3 = 2*math.pi*math.sqrt(I/K3)
        Ttheo4 = 2*math.pi*math.sqrt(I/K4)
        Ttheo = (Ttheo1+Ttheo2+Ttheo3+Ttheo4)/4
        Fnt =  round((1/Ttheo1)+(1/Ttheo2)+(1/Ttheo3)+(1/Ttheo4))/4
        Fne = round((1/Texp1)+(1/Texp2)+(1/Texp3)+(1/Texp4))/4
        error = (Fnt-Fne)/Fnt
        print(json.dumps({"Lee":[{"Torsional stiffness" : str(K) + "Nm"}], "Vernier":[{"Theoretical" : str(Ttheo)}], "tickness":[{"T experimental" : str(Texp)+"Sec"}], "Thermal":[{"Natural frequency" : str(Fnt) + "Hz"}], "Ther":[{"Percentage Error" : str(error) + "%"}], "The":[{"Result":"Thus the torsional vibration of single rotor shaft system is determined and the characteristic curve is drawn"}]}))
    def Two_Rotor(self):
        argument = self.arg[:]
        Ia1 = 2.8*(0.225**2/8)
        Ia2 = 2.8*(0.225**2/8)
        Ia3 = 2.8*(0.225**2/8)
        Ia4 = 2.8*(0.225**2/8)
        Ia =(Ia1+Ia2+Ia3+Ia4)/4
        Ib1 = 1.95*(0.19**2/8)
        Ib2 = 1.95*(0.19**2/8)
        Ib3 = 1.95*(0.19**2/8)
        Ib4 = 1.95*(0.19**2/8)
        Ib =(Ib1+Ib2+Ib3+Ib4)/4
        Texp1 = float(argument[4])/float(argument[3])
        Texp2 = float(argument[7])/float(argument[6])
        Texp3 = float(argument[10])/float(argument[9])
        Texp4 = float(argument[13])/float(argument[12])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        Ip = math.pi*0.3**4/32
        K = 0.8*10**4*Ip/float(argument[1])
        Ttheo = math.sqrt(Ia*Ib/K*(Ia+Ib))
        Fnt = 1/Ttheo
        Fne = 1/Texp
        print(json.dumps({"Lee":[{"Mass moment of inertia Disc A" : str(Ia) + "Kgm2"}], "Ver":[{"Mass moment of inertia Disc B" : str(Ib) + "Kgm2"}], "tickness":[{"Time period" : str(Ttheo)}], "Thermal":[{"T experimental" : str(Texp)}], "Ther":[{"Natural frequency Fn the0" : str(Fnt)}],"Th":[{"Natural frequency Fn exp" : str(Fne)}], "The":[{"Result":"Thus the torsional vibration of two rotor system is studied and the natural frequency of vibration is determined both experimentally and theoretically"}]}))

    def Radius(self):
        argument = self.arg[:]
        OG1= float(argument[2])/2
        OG2= float(argument[5])/2
        OG3= float(argument[8])/2
        OG4= float(argument[11])/2
        Texp1 = float(argument[4])/float(argument[3])
        Texp2 = float(argument[7])/float(argument[6])
        Texp3 = float(argument[10])/float(argument[9])
        Texp4 = float(argument[13])/float(argument[12])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        Kexp1 = 2*math.pi*math.sqrt(Texp1**2*9.81*OG1/4*math.pi**2)
        Kexp2 = 2*math.pi*math.sqrt(Texp2**2*9.81*OG2/4*math.pi**2)
        Kexp3 = 2*math.pi*math.sqrt(Texp3**2*9.81*OG3/4*math.pi**2)
        Kexp4 = 2*math.pi*math.sqrt(Texp4**2*9.81*OG4/4*math.pi**2)
        Kexp = (Kexp1+Kexp2+Kexp3+Kexp4)/4
        Ktheo1= float(argument[2])/2*math.sqrt(3)
        Ktheo2= float(argument[5])/2*math.sqrt(3)
        Ktheo3= float(argument[8])/2*math.sqrt(3)
        Ktheo4= float(argument[11])/2*math.sqrt(3)
        Ktheo = (Ktheo1+Ktheo2+Ktheo3+Ktheo4)/4
        print(json.dumps({"Lee":[{"Experimental Time Period" : str(Texp) + "Sec"}], "Vernier":[{"Radius of Gyration experimental" : str(Kexp)}]}))
    def Bifilar(self):
        argument = self.arg[:]
        Tact1=round(float(argument[4])/float(argument[3]),2)
        Tact2=round(float(argument[8])/float(argument[7]),2)
        Tact3=round(float(argument[12])/float(argument[11]),2)
        Tact4=round(float(argument[16])/float(argument[15]),2)
        Tact5=round(float(argument[20])/float(argument[19]),2)
        Tact6=round(float(argument[24])/float(argument[23]),2)
        Ktheo1= round(float(argument[1])/(2*math.sqrt(3)),2)
        Ktheo2= round(float(argument[5])/(2*math.sqrt(3)),2)
        Ktheo3= round(float(argument[9])/(2*math.sqrt(3)),2)
        Ktheo4= round(float(argument[13])/(2*math.sqrt(3)),2)
        Ktheo5= round(float(argument[17])/(2*math.sqrt(3)),2)
        Ktheo6= round(float(argument[21])/(2*math.sqrt(3)),2)
        Kact1= round((Tact1*float(argument[1])*math.sqrt(9.81/(float(argument[1]))))/ (2*math.pi),2)
        Kact2= round((Tact2*float(argument[5])*math.sqrt(9.81/(float(argument[1]))))/ (2*math.pi),2)
        Kact3= round((Tact3*float(argument[9])*math.sqrt(9.81/(float(argument[1]))))/ (2*math.pi),2)
        Kact4= round((Tact4*float(argument[13])*math.sqrt(9.81/(float(argument[1]))))/ (2*math.pi),2)
        Kact5= round((Tact5*float(argument[17])*math.sqrt(9.81/(float(argument[1]))))/ (2*math.pi),2)
        Kact6= round((Tact6*float(argument[21])*math.sqrt(9.81/(float(argument[1]))))/ (2*math.pi),2)
        percent1 = (Ktheo1-Kact1)*100/Kact1
        percent2 = (Ktheo2-Kact2)*100/Kact2
        percent3 = (Ktheo3-Kact3)*100/Kact3
        percent4 = (Ktheo4-Kact4)*100/Kact4
        percent5 = (Ktheo5-Kact5)*100/Kact5
        percent6 = (Ktheo6-Kact6)*100/Kact6
        Ttheo1=2*math.pi*Ktheo1*math.sqrt((float(argument[1])/9.81))/float(argument[2])
        Ttheo2=2*math.pi*Ktheo2*math.sqrt((float(argument[5])/9.81))/float(argument[6])
        Ttheo3=2*math.pi*Ktheo3*math.sqrt((float(argument[9])/9.81))/float(argument[10])
        Ttheo4=2*math.pi*Ktheo4*math.sqrt((float(argument[13])/9.81))/float(argument[14])
        Ttheo5=2*math.pi*Ktheo5*math.sqrt((float(argument[17])/9.81))/float(argument[18])
        Ttheo6=2*math.pi*Ktheo6*math.sqrt((float(argument[21])/9.81))/float(argument[22])
        print(json.dumps({"Lee":[{"The theoritical raduis of gyration are":str(Ktheo1)+" , "+ str(Ktheo2)+" , "+ str(Ktheo3)+" , "+ str(Ktheo4)+" and "+ str(Ktheo5),"The experimental raduis of gyration are":str(Kact1)+" , "+ str(Kact2)+" , "+ str(Kact3)+" , "+ str(Kact4)+" , "+ str(Kact5)}]}))

    def Damping(self):
        argument = self.arg[:]
        Ip = math.pi*(3**4)/32
        K = 0.8*10**4*Ip/(float(argument[3]))
        I = 8.4*0.25**2/8
        T= 2*math.pi*math.sqrt(I/K)
        ctc = math.sqrt(4*I*K)
        n = 1
        S = (1/n)*math.log(float(argument[3])/float(argument[4]))
        Ct = S/math.sqrt(4*math.pi**2+S**2)
        print(json.dumps({"Lee":[{"Time Period" : str(T) + "Sec"}], "Vernier":[{"Logarithmic decrement" : str(S)}], "tickness":[{"Critical damping fctor" : str(ctc)}],"tick":[{"Damping Ratio" : str(Ct)}], "The":[{"Result":"Thus the damped torsional oscillation and the damping coefficient is determined experimentally and respective curves are drawn"}]}))
    def Equivalent(self):
        argument = self.arg[:]
        S = float(argument[3])/float(argument[4])
        print(json.dumps({"Lee":[{"Time Period" : str(S) + "Sec"}], "Vernier":[{"Result":"Thus the forced vibration of the beam damping setup was calculated as in the tabulation"}]}))
    def Watt(self):
        argument = self.arg[:]
        W1=2*math.pi*float(argument[6])/60
        W2=2*math.pi*float(argument[8])/60
        W3=2*math.pi*float(argument[10])/60

        h1=float(argument[3])-(float(argument[7])/2)
        h2=float(argument[3])-(float(argument[9])/2)
        h3=float(argument[3])-(float(argument[11])/2)

        a1 = math.acos(h1/float(argument[1]))
        a2 = math.acos(h2/float(argument[1]))
        a3 = math.acos(h3/float(argument[1]))

        r1 = round(50+130*math.sin(a1)/10,2)
        r2 = round(50+130*math.sin(a2)/10,2)
        r3 = round(50+130*math.sin(a3)/10,2)
        
        F1= round(float(argument[2])*r1*W1**2*0.001/9.81,2)
        F2= round(float(argument[2])*r2*W2**2*0.001/9.81,2)
        F3= round(float(argument[2])*r3*W3**2*0.001/9.81,2)
        print(json.dumps({"Impact":[{"The radius of rotation are ": str(r1)+"cm , "+str(r2)+"cm and "+str(r3)+"cm","The force (F)":str(F1)+"N , "+str(F2)+"N and "+str(F3)+"N"}]}))
        # print(json.dumps({"Impact":[{"The force (F)":str(F1)+" , "+str(F2)+" and "+str(F3)}]}))
        # print(json.dumps({"Impact":[{"The radius of rotation are ": str(r1)+" , "+str(r2)+" and "+str(r3)}]}))
        # print(json.dumps({"Impact":[{"The radius of rotation are ": " saddddddddddddddddddddd"}]}))
    def Porter(self):
        argument = self.arg[:]
        W1= 2*math.pi*float(argument[6])/60
        W2= 2*math.pi*float(argument[8])/60
        W3= 2*math.pi*float(argument[10])/60
        W4= 2*math.pi*float(argument[12])/60
        W5= 2*math.pi*float(argument[14])/60

        h1=float(argument[2])-(float(argument[7])/2)
        h2=float(argument[2])-(float(argument[9])/2)
        h3=float(argument[2])-(float(argument[11])/2)
        h4=float(argument[2])-(float(argument[13])/2)
        h5=float(argument[2])-(float(argument[15])/2)
       
        a1 = math.degrees(math.acos(h1/float(argument[1])))
        a2 = math.degrees(math.acos(h2/float(argument[1])))
        a3 = math.degrees(math.acos(h3/float(argument[1])))
        a4 = math.degrees(math.acos(h4/float(argument[1])))
        a5 = math.degrees(math.acos(h5/float(argument[1])))
        
        r1 = round(50+130*math.sin(a1)/10,2)
        r2 = round(50+130*math.sin(a2)/10,2)
        r3 = round(50+130*math.sin(a3)/10,2)
        r4 = round(50+130*math.sin(a4)/10,2)
        r5 = round(50+130*math.sin(a5)/10,2)
        
        F1= round(float(argument[5])*r1*W1**2*0.001/9.81,2)
        F2= round(float(argument[5])*r2*W2**2*0.001/9.81,2)
        F3= round(float(argument[5])*r3*W3**2*0.001/9.81,2)
        F4= round(float(argument[5])*r4*W4**2*0.001/9.81,2)
        F5= round(float(argument[5])*r5*W5**2*0.001/9.81,2)
        # print(json.dumps({"answer":[{"result":str(a1)}]}))

        print(json.dumps({"Impact":[{"The radius of rotation are ": str(r1)+"cm , "+str(r2)+"cm , "+str(r3)+"cm , "+str(r4)+"cm and "+str(r4)+"cm","The force (F)":str(F1)+"N , "+str(F2)+"N , "+str(F3)+"N"+str(F4)+"N and "+str(F5)+"N"}]}))

    def Proell(self):
        argument = self.arg[:]
        h1 = (float(argument[3])-float(argument[6]))/2
        h2 =(float(argument[3])-float(argument[8]))/2
        h3 =(float(argument[3])-float(argument[10]))/2
        h4 = (float(argument[3])-float(argument[12]))/2
        h5 =(float(argument[3])-float(argument[14]))/2
        # l=float(argument[6])
        a1 = math.degrees(math.acos(h1/float(argument[4])))
        a2 = math.degrees(math.acos(h2/float(argument[4])))
        a3 = math.degrees(math.acos(h3/float(argument[4])))
        a4 = math.degrees(math.acos(h4/float(argument[4])))
        a5 = math.degrees(math.acos(h5/float(argument[4])))
        r = float(argument[2])/2
        rr1=float(argument[4]) *math.sin(a1)
        R1 =r+  float(argument[4]) *math.sin(math.radians(a1))
        R2 =r+  float(argument[4]) *math.sin(math.radians(a2))
        R3 =r+  float(argument[4]) *math.sin(math.radians(a3))
        R4 =r+  float(argument[4]) *math.sin(math.radians(a4))
        R5 =r+  float(argument[4]) *math.sin(math.radians(a5))
        
        
        W1=2*math.pi*float(argument[5])/60
        W2=2*math.pi*float(argument[7])/60
        W3=2*math.pi*float(argument[9])/60
        W4=2*math.pi*float(argument[11])/60
        W5=2*math.pi*float(argument[13])/60
        m=float(argument[1])
        F1= round((m*R1*W1**2),2)
        F2= round((m*R2*W2**2),2)
        F3= round((m*R3*W3**2),2)
        F4= round((m*R4*W4**2),2)
        F5= round((m*R5*W5**2),2)
        # # print(json.dumps({"Lee":[{"Centrifugal Force at different speed are" :  "Nadsad"}]}))
        # print(json.dumps({"answer":[{"result":str(rr1)}]}))


        print(json.dumps({"Lee":[{"Centrifugal Force at different speed are" : str(F1) + "N , "+str(F2) + "N , "+str(F3) + "N , "+str(F4) + "N and "+str(F4) + "N"}]}))
    
    def Hartnell(self):
        argument = self.arg[:]
        xi = float(argument[5])
        xs1= float(argument[8]) - xi
        xs2= float(argument[10]) - xi
        xs3= float(argument[12]) - xi
        xs4= float(argument[14]) - xi
        W1=2*math.pi*float(argument[7])/60
        W2=2*math.pi*float(argument[9])/60
        W3=2*math.pi*float(argument[11])/60
        W4=2*math.pi*float(argument[13])/60
        a=float(argument[2])
        b=float(argument[1])
        rs=float(argument[4])
        R1 = rs+(b/a*xs1)
        R2 = rs+(b/a*xs2)
        R3 = rs+(b/a*xs3)
        R4 = rs+(b/a*xs3)
        
        m= float(argument[6])

        F1= round((m*R1*W1**2),2)
        F2= round((m*R2*W2**2),2)
        F3= round((m*R3*W3**2),2)
        F4= round((m*R4*W4**2),2)
        print(json.dumps({"Lee":[{"Centrifugal Force at different speed are" : str(F1) + "N , "+str(F2) + "N , "+str(F3) + "N , "+str(F4) + "N and "+str(F4) + "N"}]}))
    def Static(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the experimental on static and dynamic balancing of four different mass is performed and the position of counter balancing weights are calculated and verfied."}]}))

    def Whirling(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the study is done on the critical speed of the shaft."}]}))
    def Gyroscopic(self):
        argument = self.arg[0:]
        mass=float(argument[1])
        d = float(argument[2])
        l = float(argument[3])
        phi =float(argument[4])
        I= (mass*d**2)/8
        def W(a):
            return (2*math.pi*a/60)
        W1=W(float(argument[5]))
        W2=W(float(argument[8]))
        W3=W(float(argument[11]))

        def Wp(a):
            return ((phi*math.pi)/(a*180))
        Wp1=Wp(float(argument[7]))
        Wp2=Wp(float(argument[10]))
        Wp3=Wp(float(argument[13]))
        ca1 = round(float(argument[6])*l*9.81,2)
        ca2 = round(float(argument[9])*l*9.81,2)
        ca3 = round(float(argument[12])*l*9.81,2)

        cr1 = round(I*W1*Wp1,2)
        cr2 = round(I*W2*Wp2,2)
        cr3 = round(I*W3*Wp3,2)
        print(json.dumps({"Impact":[{"Active couple and reactive couple for first row": str(ca1)+" and "+str(cr1)+"respectively","Active couple and reactive couple for second row":str(ca2)+" and "+str(cr2)+"respectively","Active couple and reactive couple for third row":str(ca3)+" and "+str(cr3)+"respectively"}]}))
    def Journal(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the pressure distributions are studied and graphs are plotted."}]}))
    def Cam(self):
        argument = self.arg[:]
        S = (float(argument[2])+float(argument[3])+float(argument[4]))/3
        print(json.dumps({"Lee":[{"Smean" : str(S)}], "Vernier":[{"Result":"Thus the displacement, velocity and acceleration diagram of the cam profile with roller follower is drawn."}]}))









    

