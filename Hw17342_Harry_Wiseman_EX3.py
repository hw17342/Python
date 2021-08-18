import matplotlib.pyplot as plt
import numpy as np
"""
Created on Mon Jan 28 21:31:39 2019
Harry Wiseman EX3 Falling Felix

Parts a,b,c are for a falling sphere.
Parts e,d are for falling felix.
"""

'''
Firstly I put in all the constants and starting values required
'''
#Sphere constants
C_d = 0.47
m = 10
Air_density = 1.2
A = 1

#Felix constants
C_d_f = 1.3
Air_density_f = 0.4566
m_f = 137
y_f = 38969

k = (C_d*Air_density*A)/2
g = 9.81

#start & end values
dt = 0.1    #nNUMBER OF STEPS (time-steps) 
y=1000
Y = 0       #STOP POINT.WHEN OBJECT HITS THE GROUND
v=0
t=0 
N = 250
t = []              #EMPTY LIST
Time_1=range(N)      
New_Height=[]
New_Velocity=[]     #VELOCITY LIST 
rho=[Air_density]   #THIS IS USED FOR PART D

'''
Next the equations required were defined here which were called later on.
'''
#CHECK IF STRING CAN BE CONVERTED TO FLOAT (USED IN PART B TO DEAL WITH INVALID CHARACTERS FOR USER INPUT)
def checkFloat(string):
    try:
        float(string)
    except ValueError:
        return False
    return True

def Euler(dt):   
    t=0
    v=0
    y=1000
    Height=[y]      #POSITION DATA STORED IN LIST HERE
    Velocity=[v]    #VELOCITY DATA STORED IN  LIST HERE
    Time=[t]        #TIME DATA STORED IN  LIST HERE
    
    while (y>0):
    
        y+=dt*v 
        v-=dt*(g+((k/m)*((abs(v))*v)))
        t+=dt 
    
        Height.append(y)        #   BASICALLY ADDING EACH Y VALUE 
        Velocity.append(v)      #   '                    ' V VALUE
        Time.append(t)          #   '                    ' T VALUE
        
    return Height,Velocity,Time

def Euler_mod(dt):      #MODIFIED METHOD USING THE MIDPOINTS
    
    t=0
    v=0
    y=1000
    Mod_Height=[y]  
    Mod_Velocity=[v]
    Time=[t]    
    
    while (y>0):
    
        y+=(dt/2)*v 
        v-=(dt/2)*(g+((k/m)*((abs(v))*v)))
        t+=(dt/2)
        Mod_Height.append(y) 
        Mod_Velocity.append(v) 
        Time.append(t) 
        
    return Mod_Height,Mod_Velocity,Time

def Felix(dt):      #THE EQUATION IS FOR PART D&E TAKING INTO ACCOUNT AIR DENSITY  
    t=0
    v=0
    y=38969
    f_Height=[y]
    f_Velocity=[v]
    f_Time=[t]
    
    while (y>0):
    
        y+=dt*v 
        k_y= C_d_f*(A/2)*Air_density_f*np.exp(-y/7640)
        v-=dt*(g+((k_y/m_f)*((abs(v))*v)))
        t+=dt 
        rho.append(Air_density)
        f_Height.append(y) 
        f_Velocity.append(v) 
        f_Time.append(t)  
        
    return f_Height,f_Velocity,f_Time

'''
Next using wjile loops if, elif and else statements are used for the menu and alowwing the user to input values
'''

 
MyInput = '0'
while MyInput != 'q':                                       #THIS WHILE LOOP SETSTHE MENU
    print(' ')
    print('Welcome to Harry Wisemans program for free-fall of a spherical ball and Felix. Please choose one of the options below.')
    print(' ')
    print('a = Euler method with of sphere')
    print(' ')
    print('b = Comparison of analytical method of a sphere')
    print(' ')
    print('c = Modified Euler method of a sphere')
    print(' ')
    print('d = Varying air density applied to Felix')
    print(' ')
    print('e = User input for Part d')
    print(' ')
    MyInput = input('Enter a choice, "a", "b", "c", "d", "e " or "q" to quit: ')
    print('You entered the choice: ',MyInput)
    
    """ Part A: Using Euler's method y(t) and v_y(t) are calculated
    for a falling body (ball) starting at 1km and u=0 """
    
    if MyInput == 'a':
        print(' ')
        print('You have chosen part (a)')
        print('Height 1km, starting velocity 0')
        
        input_A = input("Enter a value for the an area in m^2: ")
        input_m = input("Enter a value for mass in kg: ")
        if checkFloat(input_A) and checkFloat(input_m):
            A = float(input_A)
            m = float(input_m)
                                        
            Fig1, axRHS = plt.subplots()        #SUB PLOTS USED WHEN WANTING 2 GRAPHS ON SAME AXES
            Height,Velocity,Time = Euler(dt)    #CALLING EQUATION DEFINED ABOVE
            color = 'tab:red'
            axRHS.set_xlabel('time (s)')
            axRHS.set_ylabel('Velocity (m/s)', color=color)
            axRHS.plot(Time,Velocity, color=color)
            axRHS.tick_params(axis='y', labelcolor=color)
            axLHS = axRHS.twinx()               #THIS MAKES THE GRAPHS HAVE THE SAME X AXIS AND DIFFERENT Y
            
            color = 'tab:green'
            axLHS.set_ylabel('Height (m)', color=color)  
            axLHS.plot(Time,Height, color=color)
            axLHS.tick_params(axis='y', labelcolor=color)
            axLHS.grid()
            plt.show()
            
        else: print("One of the values you have entered is invalid.")

            #Part B has the anaylitical method and compares it to Eulers for different time steps
            
            
    elif MyInput == 'b':
        print(' ')
        print('You have chosen part (b)')
        print(' ')
        print('Comparing the 2 equations for position & velocity of a spherical body falling from 1km, with Mass = 10kg and Area = 1m^2')
        
        New_Height=[]
        New_Velocity=[]
        input_dt = input("Enter a value for dt between 0.0001 & 1: ")
        if checkFloat(input_dt):
            if 0.0001<=float(input_dt)<=1:
                dt = float(input_dt)
                           
            
                for t in Time_1:                
                    y_A =1000-((m/(2*k))*np.log((np.cosh(np.sqrt((k*g)/m)*t))**2))
                    New_Height.append(y_A)
                    
                    v = -(np.sqrt((m*g)/k))*(np.tanh(np.sqrt((k*g)/m)*t))
                    New_Velocity.append(v)
           
                Height,Velocity,Time = Euler(dt)            #NORMAL PLOT USED SO BOTH GRAPHS CAN BE COMPARED AGAINST EACH OTHER
                plt.plot(Time,Height,c='r',label='Euler') 
                plt.title("Free fall of a spherical body") 
                plt.xlabel(" Time/s") 
                plt.ylabel("Position/ m")
                plt.plot(Time_1,New_Height,c='b',label='Other')
                plt.ylim(0, 1000)
                plt.xlim(0,65)
                plt.legend()
                plt.grid()
                
                plt.figure(2) 
                plt.title("Free fall of a spherical body") 
                plt.xlabel(" Time/s") 
                plt.ylabel("Velocity/ m/s") 
                plt.plot(Time,Velocity,c='r',label='Euler') 
                plt.plot(Time_1,New_Velocity,c='b',label='Other')
                plt.xlim(0, 15)
                plt.legend()
                plt.grid() 
                plt.show()
            
            else: print("One of the values you have entered is invalid.")
        else: print("One of the values you have entered is invalid.")       #THIS FOR IF USER PUTS ANY NON NUMERICAL CHARACTER IN (.isnumeric cannot be used because only works for integer floats)

    #PART C ALLOWS USER INPUTS USING FLOATS, AND INPUT STATEMENST

    elif MyInput == 'c':
        print(' ')
        print('You have chosen part (c)')
        print(' ')
        
        input_A = input("Enter a value for the an area in m^2: ")
        input_m = input("Enter a value for mass in kg: ")
        input_dt = input("Enter a value for dt between 0.0001 & 3: ")
        if checkFloat(input_A) and checkFloat(input_dt) and checkFloat(input_m): #THESE ONLY ALLOW NUMBERS TO BE INPUTTED
            A = float(input_A)
            m = float(input_m)
            dt = float(input_dt)
            
            Fig1, axRHS = plt.subplots()
            Mod_Height,Mod_Velocity,Time= Euler_mod(dt) #CALLING MODIFIED METHOD STATED ABOVE
            color = 'tab:orange'
            axRHS.set_xlabel('time (s)')
            axRHS.set_ylabel('Velocity (m/s)', color=color)
            axRHS.plot(Time,Mod_Velocity, color=color)
            axRHS.tick_params(axis='y', labelcolor=color)
            axLHS = axRHS.twinx()
            
            color = 'tab:purple'
            axLHS.set_ylabel('Height (m)', color=color)  
            axLHS.plot(Time,Mod_Height, color=color)
            axLHS.tick_params(axis='y', labelcolor=color)
            axLHS.grid()
            plt.title('Modified Euler Method velocity/time and position/time plot')
            plt.show()
            
            plt.figure(3)
            Height,Velocity,Time = Euler(dt)
            plt.plot(Time,Height,c='r',label='Euler') 
            plt.title("Height difference between the two methods") 
            plt.xlabel(" Time/s") 
            plt.ylabel("Position/ m")
            Mod_Height,Mod_Velocity,Time_1= Euler_mod(dt)
            plt.plot(Time_1,Mod_Height,c='b',label='Mod_Euler')
            plt.ylim(0, 1010)
            plt.legend()
            plt.grid()
            
            plt.figure(4)
            plt.title("Velocity difference of the two methods") 
            plt.xlabel(" Time/s") 
            plt.ylabel("Velocity/ m/s") 
            plt.plot(Time,Velocity,c='r',label='Euler') 
            plt.plot(Time_1,Mod_Velocity,c='b',label='Mod_Euler')
            plt.legend()
            plt.grid() 
            plt.show()
            
        #PART D SHOWS FELIXS JUMP PREDICTIONS USING MY PROGRAM
        else: print("One of the values you have entered is invalid.")
        
    elif MyInput == 'd':
        print(' ')
        print('You have chosen part (d)')
        print(' ')
        print('This is Felixs jump')
        print('Felix fell 38 969m')
        print('Drag coeffiecent 1.3')
        print('Air density 0.4566kg/m^3')
        print('With a mass of 137kg (110kg him+suit and 27kg parachute)')
        print('His max speed plotted in top corner of graph')
        
            
        Fig2, axLHS = plt.subplots()
        f_Height,f_Velocity,f_Time = Felix(dt)
        color = 'tab:red'
        axLHS.set_xlabel('time (s)')
        axLHS.set_ylabel('Velocity (m/s)', color=color)
        axLHS.plot(f_Time,f_Velocity, color=color)
        axLHS.tick_params(axis='y', labelcolor=color)
        axLHS.text(150,-10,min(f_Velocity))        #THIS SHOWS THE MINIMUM ON HE GRAPH (HIS MAX SPEED)
        axRHS = axLHS.twinx()
        
        color = 'tab:green'
        axRHS.set_ylabel('Height (m)', color=color) 
        axRHS.plot(f_Time,f_Height, color=color)
        axRHS.tick_params(axis='y', labelcolor=color)
        axRHS.grid()
        plt.show()

        #PART E this allows the user to alter Felixs parameters
        
    elif MyInput == 'e':
        print(' ')
        print('You have chosen part (e)')
        print(' ')
        print('Felix fell 38 969m With a mass of 137kg')
        print('Here you can change the parameters of his jump')
        
        
#        input_y = input("Enter jumping height in m: ")
        input_A_f = input("Enter a value for the an area in m^2: ")
        input_m_f = input("Enter a value for mass in kg: ")
        input_C_d_f = input("Enter a value for the drag coeffiecent: ")
        if checkFloat(input_A_f) and checkFloat(input_m_f) !=0 and checkFloat(input_C_d_f):
#            y = float(input_y)
            A_f = float(input_A_f)
            m_f = float(input_m_f)
            C_d_f = float(input_C_d_f)
            
            
            f_Height,f_Velocity,f_Time = Felix(dt) #CALLING FELIX EQUATION
            plt.figure(5) 
            plt.title("Free fall of a body") 
            plt.xlabel(" Time/s") 
            plt.ylabel("Position/ m")
            plt.grid()
            plt.plot(f_Time,f_Height,c='r') 

            plt.figure(6) 
            plt.title("Free fall of a body") 
            plt.xlabel(" Time/s") 
            plt.ylabel("Velocity/ m/s") 
            plt.grid()
            plt.plot(f_Time,f_Velocity,c='g')
            plt.text(0,-10,min(f_Velocity))
            plt.show() 
            
            print('maximum speed of:')
            print(min(f_Velocity)) #THIS WILL SHOW THE NEW MAX SPEED REACHED WHEN ALTERING THE VALUES
        else: print("One of the values you have entered is invalid.")
        
    elif MyInput == "q":    
        print('You have chosen to finish - goodbye xxx.') 
    
    elif MyInput != 'q'or'a'or'b'or'c'or'd': print('This is not a valid choice') #IF THE USER PUTS WRONG VALUES IN 