import json
import math

class PHY_acet:
    def __init__(self, arg):
        self.arg = arg
    def VB_Mag(self):
        argument = self.arg[0:]
        def CR_l(x,y):
            ans = x+(y*0.01)
            return ans
        def CR_b(x,y):
            return x+(y*0.01)
        def TP1(x):
            return x/5
        def TP2(x):
            return x/10
        def TP3(x):
            return (x*10)/30
        def l2(x):
            return x**2
        def b2(x):
            return x**2
        CR1 = CR_l(float(argument[3]),float(argument[4]))
        CR2 = CR_l(float(argument[5]),float(argument[6]))
        CR3 = CR_l(float(argument[7]),float(argument[8]))
        CR4 = CR_l(float(argument[9]),float(argument[10]))
        CR5 = CR_l(float(argument[11]),float(argument[12]))
        CR_Mean = round((CR1+CR2+CR3+CR4+CR5)/5,2)
        OR1=CR_l(float(argument[15]),float(argument[16]))
        OR2=CR_l(float(argument[17]),float(argument[18]))
        OR3=CR_l(float(argument[19]),float(argument[20]))
        OR4=CR_l(float(argument[21]),float(argument[22]))
        OR5=CR_l(float(argument[23]),float(argument[24]))
        CRb1= CR_b(OR1,(float(argument[14])))
        CRb2= CR_b(OR1,(float(argument[14])))
        CRb3= CR_b(OR1,(float(argument[14])))
        CRb4= CR_b(OR1,(float(argument[14])))
        CRb5= CR_b(OR1,(float(argument[14])))
        CRb_Mean = round((CRb1+CRb2+CRb3+CRb4+CRb5)/5,2)
        T1= round(TP1(float(argument[26])),2)
        T2= round(TP2(float(argument[27])),2)
        T3= round(TP3(float(argument[28])),2)
        T4= round(TP1(float(argument[29])),2)
        T5= round(TP2(float(argument[30])),2)
        T6= round(TP3(float(argument[31])),2)
        Mean_T1 = round((T1+T2+T3)/3,2)
        Mean_T2 = round((T4+T5+T6)/3,2)
        Mean_T= round((Mean_T1+Mean_T2)/2,2)
        length=round((l2(CR_Mean))/10,2)
        breadth=round((b2(CRb_Mean))/100,2)
        lb=round((length+breadth)/12,3)
        lb_n= lb*10
        Inertia = round(((float(argument[25]))*lb_n)*10,3)
        T= round(Mean_T**2,1)      
        Mh= round((39.43 * Inertia)/T,2)
        m=round((Mh/(2*CR_Mean))*10,3)
        #print(json.dumps({"ans":[{"mean b":str(m),"s":str(CR_Mean)}]}))
        print(json.dumps({"Result":[{"Vibrational Magnetometer":"Length of the bar magnet ","Mean(length)" : str(CR_Mean),"Mean(breadth)":str(CRb_Mean),"Time period of oscillator":str(Mean_T),"Inertia":str(Inertia),"The magnetic moment of the given bar magnet(Mh)":str(Mh)+"x 10^-5 Am^2","The pole strength of the given bar magnet(m)":str(m)+"x10^-4 Am"}]}))
    def Air_wed(self):
        argument = self.arg[0:]
        def CR(x,y):
            return (x+(y*0.001))
        def W5(x,y):
            return (y-x)
        def MW(x):
            return(x/5)
        def EOF1(x,y):
            return(y+(x*0.01))
        CR1= CR(float(argument[1]),float(argument[2]))
        CR2= CR(float(argument[3]),float(argument[4]))
        CR3= CR(float(argument[5]),float(argument[6]))
        CR4= CR(float(argument[7]),float(argument[8]))
        CR5= CR(float(argument[9]),float(argument[10]))
        CR6= CR(float(argument[11]),float(argument[12]))
        CR7= CR(float(argument[13]),float(argument[14]))
        CR8= CR(float(argument[15]),float(argument[16]))
        CR9= CR(float(argument[17]),float(argument[18]))
        CR10=CR(float(argument[19]),float(argument[20]))
        CR11=CR(float(argument[21]),float(argument[22]))
        Width_2= (W5(CR1,CR2))
        Width_3= (W5(CR2,CR3))
        Width_4= (W5(CR3,CR4))
        Width_5= (W5(CR4,CR5))
        Width_6= (W5(CR5,CR6))
        Width_7= (W5(CR6,CR7))
        Width_8= (W5(CR7,CR8))
        Width_9= (W5(CR8,CR9))
        Width_10= (W5(CR9,CR10))
        Width_11= (W5(CR10,CR11))
        Mean_width2= MW(Width_2)
        Mean_width3= MW(Width_3)
        Mean_width4= MW(Width_4)
        Mean_width5= MW(Width_5)
        Mean_width6= MW(Width_6)
        Mean_width7= MW(Width_7)
        Mean_width8= MW(Width_8)
        Mean_width9= MW(Width_9)
        Mean_width10=MW (Width_10)
        Mean_width11= MW(Width_11)
        MeanBeta= round((Mean_width2 + Mean_width3+Mean_width4+Mean_width5+Mean_width6+Mean_width7+Mean_width8+Mean_width9+Mean_width10+Mean_width11)/12,4)
        R1 = CR(float(argument[23]),float(argument[24]))
        R2 = CR(float(argument[25]),float(argument[26]))
        l= round((R1-R2),3)
        t= ((5896*l)/(2*MeanBeta))
        ts=round(t/1000000,3)
        print(json.dumps({"ans":[{"Mean frindge width(β)":str(MeanBeta)+"x 10-2 m","The distance between edge of contact and wire(l)":str(l)+"m","Thickness of given specimen is found by forming interfernce fringe using air wedge arrangement - Thickness ofspeciemnt(t)=":str(ts)}]}))
    def prism(self):
        argument = self.arg[0:]
        def TR(x,y):
            return(x+(y*0.01))  
        def VA(x,y):
            return (y-x)
        def VB(x,y):
            return(x-y)
        tr_al= TR(float(argument[1]),float(argument[2]))
        tr_bl= TR(float(argument[3]),float(argument[4]))
        tr_ar= TR(float(argument[5]),float(argument[6]))
        tr_br= TR(float(argument[7]),float(argument[8]))
        trA= round(VA(tr_al,tr_ar))
        trB=VB(tr_bl,tr_br)
        VA= round(trA,2)
        VB=round(trB/2,2)
        A= round((VA+VB)/4)
        #print(json.dumps({"ans":[{"Mean frindge width(β)":str(A)}]}))
        Dtr_a=round(TR(float(argument[9]),float(argument[10])),2)
        Vtr_a=round(TR(float(argument[13]),float(argument[14])),2)
        Btr_a=round(TR(float(argument[17]),float(argument[18])),2)
        BGtr_a=round(TR(float(argument[21]),float(argument[22])),2)
        Gtr_a=round(TR(float(argument[25]),float(argument[26])),2)
        Ytr_a=round(TR(float(argument[29]),float(argument[30])),2)
        Otr_a=round(TR(float(argument[33]),float(argument[34])),2)
        Rtr_a=round(TR(float(argument[37]),float(argument[38])),2)

        Dtr_b=round(TR(float(argument[11]),float(argument[12])),2)
        Vtr_b=round(TR(float(argument[15]) ,float(argument[16])),2)
        Btr_b=round(TR(float(argument[19]),float(argument[20])),2)
        BGtr_b=round(TR(float(argument[23]),float(argument[24])),2)
        Gtr_b=round(TR(float(argument[27]),float(argument[28])),2)
        Ytr_b=round(TR(float(argument[31]),float(argument[32])),2)
        Otr_b=round(TR(float(argument[35]),float(argument[36])),2)
        Rtr_b=round(TR(float(argument[39]),float(argument[40])),2)

        vva= round((Dtr_a - Vtr_a),2)
        bva= round((Dtr_a - Btr_a),2)
        bgva=round((Dtr_a - BGtr_a),2)
        gva= round((Dtr_a - Gtr_a),2)
        yva= round((Dtr_a - Ytr_a),2)
        ova= round((Dtr_a - Otr_a),2)
        rva=round(( Dtr_a - Rtr_a),2)

        degree= Dtr_b - 366

        vvb= round((degree - Vtr_b),2)
        bvb= round((degree - Btr_b),2)
        bgvb= round((degree - BGtr_b),2)
        gvb= round((degree - Gtr_b),2)
        yvb= round((degree - Ytr_b),2)
        ovb= round((degree - Otr_b),2)
        rvb= round((degree - Rtr_b),2)

        MeanD1= round((vva+vvb)/2,2)
        MeanD2= round((bva+bvb)/2,2)
        MeanD3= round((bgva+bgvb)/2,2)
        MeanD4= round((gva+gvb)/2,2)
        MeanD5= round((yva+yvb)/2,2)
        MeanD6= round((ova+ovb)/2,2)
        MeanD7= round((rva+rvb)/2,2)
        # print(json.dumps({"ans":[{"Me":str(MeanD5),"a":str(gvb)}]}))

        V=round((math.sin(math.radians(A+MeanD1)/2))/(math.sin(math.radians(A/2))),4)
        B=round((math.sin(math.radians(A+MeanD2)/2))/(math.sin(math.radians(A/2))),4)        
        BG=round((math.sin(math.radians(A+MeanD3)/2))/(math.sin(math.radians(A/2))),4)        
        G=round((math.sin(math.radians(A+MeanD4)/2))/(math.sin(math.radians(A/2))),4)        
        Y=round((math.sin(math.radians(A+MeanD5)/2))/(math.sin(math.radians(A/2))),4)        
        O=round((math.sin(math.radians(A+MeanD6)/2))/(math.sin(math.radians(A/2))),4)
        R=round((math.sin(math.radians(A+MeanD7)/2))/(math.sin(math.radians(A/2))),4)      
        # print(json.dumps({"ans":[{"Me":str(R)}]}))
        mu1=V
        mu2=BG
        mu3=Y
        mu4=R
        mu5=B
        mu6=G
        mu7=R
        mu8=O

        MU1 = round((mu1+mu5)/2,2)
        MU2=  round((mu2+mu6)/2,2)
        MU3=  round((mu3+mu7)/2,2)
        MU4=  round((mu8+mu4)/2,2)
        W1=round(((mu1-mu5)/(MU1-1)),4)
        W2=round(((mu2-mu6)/(MU2-1)),4)
        W3=round(((mu3-mu7)/(MU3-1)),4)
        W4=round(((mu8-mu4)/(MU4-1)),4)
        power=round((W1+W2+W3+W4)/4,4)
        print(json.dumps({"ans":[{"The angle of the given prism :(VA)":str(VA) +"degree","(VB)":str(VB)+"degree","A":str(A),"The dispersion power of the given prism W":str(power)+" No unit"}]}))

    def laser(self):
        argument= self.arg[0:]
        def TR(x,y):
            return(x+(y*0.01))  
        def VA(x,y):
            diff = abs(y-x)
            if diff > 30:
             return abs(math.radians(y)-math.radians(x))
            else:
             return abs(y-x)  
        def theta45(a,b,c):
            avg = (b+c)/2
            thetaa = math.degrees(math.atan(b/45))
            lamda = (math.sin(math.radians(thetaa))/(a*N))*10**10
            return lamda
        def theta50(a,b,c):
            avg = (b+c)/2
            thetaa = math.degrees(math.atan(b/50))
            lamda = (math.sin(math.radians(thetaa))/(a*N))*10**10
            return lamda
        def theta55(a,b,c):
            avg = (b+c)/2
            thetaa = math.degrees(math.atan(b/55))
            lamda = (math.sin(math.radians(thetaa))/(a*N))*10**10
            return lamda
        cr_al= round(TR(float(argument[1]),float(argument[2])),2)
        cr_bl= round(TR(float(argument[3]),float(argument[4])),2)
        cr_ar= round(TR(float(argument[5]),float(argument[6])),2)
        cr_br= round(TR(float(argument[7]),float(argument[8])),2)
        DA=VA(cr_al,cr_ar)
        DB=VA(cr_bl,cr_br)
        MeanA=round(((DA+DB)/4),2)
        # Tan1= math.degrees(float(argument[10])/45)
        N=math.sin(math.radians(3.52))/(5893*10**-10)
        # N=round((math.sin(math.radians(MeanA)))/589.3*10000,4)
        theta1=theta45(float(argument[9]),float(argument[10]),float(argument[11]))
        theta2=theta45(float(argument[12]),float(argument[13]),float(argument[14]))
        theta3=theta45(float(argument[15]),float(argument[16]),float(argument[17]))
        theta4=theta45(float(argument[18]),float(argument[19]),float(argument[20]))
        theta5=theta45(float(argument[21]),float(argument[22]),float(argument[23]))
        theta6=theta50(float(argument[24]),float(argument[25]),float(argument[26]))
        theta7=theta50(float(argument[27]),float(argument[28]),float(argument[29]))
        theta8=theta50(float(argument[30]),float(argument[31]),float(argument[32]))
        theta9=theta50(float(argument[33]),float(argument[34]),float(argument[35]))
        theta10=theta50(float(argument[36]),float(argument[37]),float(argument[38]))
        theta11=theta55(float(argument[39]),float(argument[40]),float(argument[41]))
        theta12=theta55(float(argument[42]),float(argument[43]),float(argument[44]))
        theta13=theta55(float(argument[45]),float(argument[46]),float(argument[47]))
        theta14=theta55(float(argument[48]),float(argument[49]),float(argument[50]))
        theta15=theta55(float(argument[51]),float(argument[52]),float(argument[53]))
        avg=(theta1+theta2+theta3+theta4+theta5+theta6+theta7+theta8+theta9+theta10+theta11+theta12+theta13+theta14+theta15)/15
        avground=round(avg,2)
        print(json.dumps({"ans":[{"Wave Length of given light Source in Amstrong":str(avground)+"Amstrong","Wave Length of given light Source in meter":str(avground)+"*10^-10meter"}]}))
    def newton(self):
        argument = self.arg[0:]
        def CR(x,y):
            return (x+(y*0.001))
        def D(x,y):
            return ((x-y)**2)
        def MW(x):
            return(x/5)
        def EOF1(x,y):
            return(y+(x*0.01))
        CR1=CR(float(argument[1]),float(argument[2]))
        CR2=CR(float(argument[5]),float(argument[6]))
        CR3=CR(float(argument[9]),float(argument[10]))
        CR4=CR(float(argument[13]),float(argument[14]))
        CR5=CR(float(argument[17]),float(argument[18]))
        CR6=CR(float(argument[21]),float(argument[22]))
        CR7=CR(float(argument[25]),float(argument[26]))
        CR8=CR(float(argument[29]),float(argument[30]))
        CR9=CR(float(argument[33]),float(argument[34]))
        CR10=CR(float(argument[37]),float(argument[38]))
        CR11=CR(float(argument[41]),float(argument[42]))

        CRR1=CR(float(argument[3]),float(argument[4]))
        CRR2=CR(float(argument[7]),float(argument[8]))
        CRR3=CR(float(argument[11]),float(argument[12]))
        CRR4=CR(float(argument[15]),float(argument[16]))
        CRR5=CR(float(argument[19]),float(argument[20]))
        CRR6=CR(float(argument[23]),float(argument[24]))
        CRR7=CR(float(argument[27]),float(argument[28]))
        CRR8=CR(float(argument[31]),float(argument[32]))
        CRR9=CR(float(argument[35]),float(argument[36]))
        CRR10=CR(float(argument[39]),float(argument[40]))
        CRR11=CR(float(argument[43]),float(argument[44]))

        D1= round(D(CR1,CRR1),3)
        D2= round(D(CR2,CRR2),3)
        D3= round(D(CR3,CRR4),3)
        D4= round(D(CR4,CRR4),3)
        D5= round(D(CR5,CRR5),3)
        D6= round(D(CR6,CRR6),3)
        D7= round(D(CR7,CRR7),3)
        D8= round(D(CR8,CRR8),3)
        D9= round(D(CR9,CRR9),3)
        D10= round(D(CR10,CRR10),3)
        D11= round(D(CR11,CRR11),3)

        d1= ((D6-D1))
        d2= ((D7-D2))
        d3= ((D8-D3))
        d4= ((D9-D4))
        d5= ((D10-D5))

        MeanR1=round((d1+d2+d3+d4+d5)/5,6)
       
        CR_1=CR(float(argument[45]),float(argument[46]))
        CR_2=CR(float(argument[49]),float(argument[50]))
        CR_3=CR(float(argument[53]),float(argument[54]))
        CR_4=CR(float(argument[57]),float(argument[58]))
        CR_5=CR(float(argument[61]),float(argument[62]))
        CR_6=CR(float(argument[65]),float(argument[66]))
        CR_7=CR(float(argument[69]),float(argument[70]))
        CR_8=CR(float(argument[73]),float(argument[74]))
        CR_9=CR(float(argument[77]),float(argument[78]))
        CR_10=CR(float(argument[81]),float(argument[82]))
        CR_11=CR(float(argument[85]),float(argument[86]))

        CR_R1=CR(float(argument[47]),float(argument[48]))
        CR_R2=CR(float(argument[51]),float(argument[52]))
        CR_R3=CR(float(argument[55]),float(argument[56]))
        CR_R4=CR(float(argument[59]),float(argument[60]))
        CR_R5=CR(float(argument[63]),float(argument[64]))
        CR_R6=CR(float(argument[67]),float(argument[68]))
        CR_R7=CR(float(argument[71]),float(argument[72]))
        CR_R8=CR(float(argument[75]),float(argument[76]))
        CR_R9=CR(float(argument[79]),float(argument[80]))
        CR_R10=CR(float(argument[83]),float(argument[84]))
        CR_R11=CR(float(argument[87]),float(argument[88]))

        D_1= round(D(CR_1,CR_R1),3)
        D_2= round(D(CR_2,CR_R2),3)
        D_3= round(D(CR_3,CR_R4),3)
        D_4= round(D(CR_4,CR_R4),3)
        D_5= round(D(CR_5,CR_R5),3)
        D_6= round(D(CR_6,CR_R6),3)
        D_7= round(D(CR_7,CR_R7),3)
        D_8= round(D(CR_8,CR_R8),3)
        D_9= round(D(CR_9,CR_R9),3)
        D_10= round(D(CR_10,CR_R10),3)
        D_11= round(D(CR_11,CR_R11),3)

        d_1= ((D_6-D_1))
        d_2= ((D_7-D_2))
        d_3= ((D_8-D_3))
        d_4= ((D_9-D_4))
        d_5= ((D_10-D_5))
        MeanR2=round((d_1+d_2+d_3+d_4+d_5)/5,6)
        R1= (MeanR1/353580)
        R2=(MeanR2/353580)
        R= round(((R1+R2)/2),10)
        f1= 1/R1
        f2=1/R2
        f=f1+f2
        ftemp=1/(0.5*f)
        F=round(ftemp,10)
        print(json.dumps({"ans":[{"Mean[R1]":str(MeanR1)+"10^-4 m^2","Mean[R2]":str(MeanR2)+"10^-4 m^2","Radial of curvature of the given convex lens(R)=":str(R),"Focal length of the given convex lens(f)":str(F)}]}))

    def Radial(self):
            argument = self.arg[0:]
            def CR(x,y):
                return (x+(y*0.001))
            OCR1=round(CR(float(argument[6]),float(argument[7])),3)
            OCR2=round(CR(float(argument[10]),float(argument[11])),3)
            OCR3=round(CR(float(argument[14]),float(argument[15])),3)
            OCR4=round(CR(float(argument[18]),float(argument[19])),3)
            ICR1=round(CR(float(argument[8]),float(argument[9])),3)
            ICR2=round(CR(float(argument[12]),float(argument[13])),3)
            ICR3=round(CR(float(argument[16]),float(argument[17])),3)
            ICR4=round(CR(float(argument[20]),float(argument[21])),3)
            D1=round(OCR1-OCR2,3)
            D2=round(ICR1-ICR2,3)
            D3= round(OCR4-OCR3,3)
            D4=round(ICR4-ICR3,3)
            R1=round((D1+D2)/2,2)
            R2=round((D3+D4)/2,2)
            time=float(argument[4])*60
            sec=float(argument[5])
            t=round(time+sec)
            w1=float(argument[22])
            w2= float(argument[23])
            c1= float(argument[24])
            c2= float(argument[25])
            l= float(argument[26])
            Initial_temp=round(float(argument[1])+273)
            Final_temp=round(float(argument[3])+273)
            temp= Final_temp -  Initial_temp
            w=w2-w1
            k1=((w1*c1) + (w* (c2*temp)))/1000
            k2=(6.28*l*t)/100
            r=round(R2/R1,3)
            log= round((math.log10(r)),4)
            k3=2.303*log
            steam_temp= 373
            temp_1=(Final_temp +Initial_temp) / 2
            k4=steam_temp - temp_1
            Kb=(k3/k4)
            Ka= round(k1/k2,3)
            K= round(Ka*Kb,5)
            print(json.dumps({"ans":[{"Mean(R1)":str(R1),"Mean(R2)":str(R2),"The thermal condcutivity of rubber tube is determined by radial low mthod(k)=":str(K)+"w/m/k"}]}))
    def grating(self):
        argument = self.arg[0:]
        def TR(x,y):
            return(x+(y*0.01))  
        def VA(x,y):
            return (y-x)
        
        def M(x,y):return((x+y)/4)
        def MM(x,y):return(-(x+y)/4)
        tr_al= TR(float(argument[1]),float(argument[2]))
        tr_bl= TR(float(argument[3]),float(argument[4]))
        tr_ar= TR(float(argument[5]),float(argument[6]))
        tr_br= TR(float(argument[7]),float(argument[8]))
        trA= VA(tr_al,tr_ar)
        trB=VA(tr_bl,tr_br)
        A= round(trA,2)
        B=round(trB,2)
        C= round((A+B)/4,2)
        N= round(((math.sin(math.radians(C)))/5893*10000)*10,3)
        # print(json.dumps({"ans":[{"Mean(R1)":str(N)}]}))
        Vl_a=round(TR(float(argument[9]),float(argument[10])),2)
        Bl_a=round(TR(float(argument[17]),float(argument[18])),2)
        Gl_a=round(TR(float(argument[25]),float(argument[26])),2)
        Yl_a=round(TR(float(argument[33]),float(argument[34])),2)
        Ol_a=round(TR(float(argument[41]),float(argument[42])),2)
        Rl_a=round(TR(float(argument[49]),float(argument[50])),2)

        Vl_b=round(TR(float(argument[11]),float(argument[12])),2)
        Bl_b=round(TR(float(argument[19]),float(argument[20])),2)
        Gl_b=round(TR(float(argument[27]),float(argument[28])),2)
        Yl_b=round(TR(float(argument[35]),float(argument[36])),2)
        Ol_b=round(TR(float(argument[43]),float(argument[44])),2)
        Rl_b=round(TR(float(argument[51]),float(argument[52])),2)

        Vr_a=round(TR(float(argument[13]) ,float(argument[14])),2)
        Br_a=round(TR(float(argument[21]),float(argument[22])),2)
        Gr_a=round(TR(float(argument[29]),float(argument[30])),2)
        Yr_a=round(TR(float(argument[37]),float(argument[38])),2)
        Or_a=round(TR(float(argument[45]),float(argument[46])),2)
        Rr_a=round(TR(float(argument[53]),float(argument[54])),2)

        Vr_b=round(TR(float(argument[15]) ,float(argument[16])),2)
        Br_b=round(TR(float(argument[23]),float(argument[24])),2)
        Gr_b=round(TR(float(argument[31]),float(argument[32])),2)
        Yr_b=round(TR(float(argument[39]),float(argument[40])),2)
        Or_b=round(TR(float(argument[47]),float(argument[48])),2)
        Rr_b=round(TR(float(argument[55]),float(argument[56])),2)

        CRV_a=round(VA((Vl_a),(Vr_a)),2)
        CRB_a=round(VA((Bl_a),(Br_a)),2)
        CRG_a=round(VA((Gl_a),(Gr_a)),2)
        CRY_a=round(VA((Yl_a),(Yr_a)),2)
        CRO_a=round(VA((Ol_a),(Or_a)),2)
        CRR_a=round(VA((Rl_a),(Rr_a)),2)

        CRV_b=round(VA((Vl_b),(Vr_b)),2)
        CRB_b=round(VA((Bl_b),(Br_b)),2)
        CRG_b=round(VA((Gl_b),(Gr_b)),2)
        CRY_b=round(VA((Yl_b),(Yr_b)),2)
        CRO_b=round(VA((Ol_b),(Or_b)),2)
        CRR_b=round(VA((Rl_b),(Rr_b)),2)

        Mean1= round(M(CRV_a,CRV_b),2)
        Mean2= round(MM(CRB_a,CRB_b),2)
        Mean3= round(M(CRG_a,CRG_b),2)
        Mean4= round(M(CRY_a,CRY_b),2)
        Mean5= round(M(CRO_a,CRO_b),2)
        Mean6= round(M(CRR_a,CRR_b),2)

        Violet = round((math.sin(math.radians(Mean1)))/5.908*100000,2)
        Blue = round((math.sin(math.radians(Mean2)))/5.908*100000,2)
        Green = round((math.sin(math.radians(Mean3)))/5.908*100000,2)
        Yellow = round((math.sin(math.radians(Mean4)))/5.908*100000,2)
        Orange = round((math.sin(math.radians(Mean5)))/5.908*100000,2)
        Red = round((math.sin(math.radians(Mean6)))/5.908*100000,2)

        print(json.dumps({"ans":[{"The wavelngth of prominent spectral lines of mercuy md spectrum are found tabulated. Violet":str(Violet)+"Å","Blue":str(Blue)+"Å","Green":str(Green)+"Å","Yellow":str(Yellow)+"Å","Orange":str(Orange)+"Å","Red":str(Red)+"Å"}]}))
    def lee(self):
        argument = self.arg[0:]
        def R(x,y):return(x+(y*0.01))
        def cr(x):return(x+0.03)
        def m(a,b,c,d,e):return((a+b+c+d+e)/10)
        def mean(a,b,c,d,e):return((a+b+c+d+e)/5)

        R_CR1=R(float(argument[3]),float(argument[4]))
        R_CR2=R(float(argument[5]),float(argument[6]))
        R_CR3=R(float(argument[7]),float(argument[8]))
        R_CR4=R(float(argument[9]),float(argument[10]))
        R_CR5=R(float(argument[11]),float(argument[12]))
        Mean_R=round(m(R_CR1,R_CR2,R_CR3,R_CR4,R_CR5),2)

        H_CR1=R(float(argument[15]),float(argument[16]))
        H_CR2=R(float(argument[17]),float(argument[18]))
        H_CR3=R(float(argument[19]),float(argument[20]))
        H_CR4=R(float(argument[21]),float(argument[22]))
        H_CR5=R(float(argument[23]),float(argument[24]))
        
        CR1=cr(H_CR1)
        CR2=cr(H_CR2)
        CR3=cr(H_CR3)
        CR4=cr(H_CR4)
        CR5=cr(H_CR5)
        Mean_H=round(mean(CR1,CR2,CR3,CR4,CR5),2)

        d_CR1=R(float(argument[27]),float(argument[28]))
        d_CR2=R(float(argument[29]),float(argument[30]))
        d_CR3=R(float(argument[31]),float(argument[32]))
        d_CR4=R(float(argument[33]),float(argument[34]))
        d_CR5=R(float(argument[35]),float(argument[36]))
        
        dCR1=cr(d_CR1)
        dCR2=cr(d_CR2)
        dCR3=cr(d_CR3)
        dCR4=cr(d_CR4)
        dCR5=cr(d_CR5)
        Mean_d=round(mean(dCR1,dCR2,dCR3,dCR4,dCR5),2)
        theta = float(argument[37])-float(argument[38])

        K1=round((8151.23*Mean_d)/ (3.14*theta*((Mean_R)**2)*100),4)
        K2=round((Mean_R + (2*Mean_H))/((2*Mean_R)+(2*Mean_H)),4)
        K=round(K1*K2,4)
        print(json.dumps({"ans":[{"The thermal conductivity of a bad conductir using lee's disc method":str(K)+" W m k"}]}))
    def half(self):
        argument = self.arg[0:]
        def TR(x,y):return(x+(y*0.06))
        def VA(x,y):return(y-x)
        def Va(x,y):return(x-y)
        def M(x,y):return((x+y)/2)
        def J(x):return((x*0.021))
        def deg(x,y):return(-(x/y))
        
        S_CR1=TR(float(argument[2]),float(argument[3]))
        S_CR2=TR(float(argument[7]),float(argument[8]))
        S_CR3=TR(float(argument[12]),float(argument[13]))
        S_CR4=TR(float(argument[17]),float(argument[18]))
        S_CR5=TR(float(argument[22]),float(argument[23]))

        S_CR6=TR(float(argument[4]),float(argument[5]))
        S_CR7=TR(float(argument[9]),float(argument[10]))
        S_CR8=TR(float(argument[14]),float(argument[15]))
        S_CR9=TR(float(argument[19]),float(argument[20]))
        S_CR10=TR(float(argument[24]),float(argument[25]))

        A1=round(VA(S_CR2,S_CR1),2)
        A2= round(VA(S_CR3,S_CR1),2)
        A3=round(VA(S_CR4,S_CR1),2)
        A4= round(VA(S_CR5,S_CR1),2)
        A5= round(VA(S_CR7,S_CR6),2)
        A6=round(VA(S_CR8,S_CR6),2)
        A7=round(VA(S_CR9,S_CR6),2)
        A8=round(VA(S_CR10,S_CR6),2) 
        
        Mean1=M(A1,A5)
        Mean2=M(A2,A6)
        Mean3=M(A3,A7)
        Mean4=M(A4,A8)
        L2= J(float(argument[6]))
        L3= J(float(argument[11]))
        L4= J(float(argument[16]))
        L5= J(float(argument[21]))
        S1=round(deg(Mean1,L2),2)
        S2= round(deg(Mean2,L3),2)
        S3= round(deg(Mean3,L4),2)
        S4= round(deg(Mean4,L5),2)
        S=(S1+S2+S3+S4)/4

        print(json.dumps({"ans":[{"The specific rotator of an optically active solution is determined and found to be"
        :str(S)+"deg dm-1 cc-1"}]}))
    def Deflection(self):
        argument = self.arg[0:]
        def Mean(a,b,c,d,e,f,g,h): return((a+b+c+d+e+f+g+h)/8)
        thetha1=Mean(float(argument[1]),float(argument[2]),float(argument[3]),float(argument[4]),float(argument[5]),float(argument[6]),float(argument[7]),float(argument[8]))
        thetha2=Mean(float(argument[9]),float(argument[10]),float(argument[11]),float(argument[12]),float(argument[13]),float(argument[14]),float(argument[15]),float(argument[16]))
        thetha3=Mean(float(argument[17]),float(argument[18]),float(argument[19]),float(argument[20]),float(argument[21]),float(argument[22]),float(argument[23]),float(argument[24]))
        thetha4=Mean(float(argument[25]),float(argument[26]),float(argument[27]),float(argument[28]),float(argument[29]),float(argument[30]),float(argument[31]),float(argument[32]))
        thetha5=Mean(float(argument[33]),float(argument[34]),float(argument[35]),float(argument[36]),float(argument[37]),float(argument[38]),float(argument[39]),float(argument[40]))
        thetha6=Mean(float(argument[41]),float(argument[42]),float(argument[43]),float(argument[44]),float(argument[45]),float(argument[46]),float(argument[47]),float(argument[48]))
        tan1=round(math.tan(math.radians(thetha1)),3)
        tan2=round(math.tan(math.radians(thetha2)),3)
        tan3=round(math.tan(math.radians(thetha3)),3)
        tan4=round(math.tan(math.radians(thetha4)),3)
        tan5=round(math.tan(math.radians(thetha5)),3)
        tan6=round(math.tan(math.radians(thetha6)),3)
        H1= round(36.397*(1/tan1),3)
        H2= round(36.397*(1/tan2),3)
        H3=round(36.397*(1/tan3),3)
        H4=round(24.478*(1/tan4),3)
        H5=round(24.478*(1/tan5),3)
        H6=round(24.478*(1/tan6),3)
        Average= round((H1+H2+H3+H4+H5+H6)/6,3)
        H= round(((Average *4*(math.pi))/100),3)
        print(json.dumps({"ans":[{"The Horizontl component of earth's magnetic field(Bh)=":str(H)+"x10^5 tesla"}]}))

