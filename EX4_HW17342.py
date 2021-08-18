#HENRY WISEMAN DEADLINE 22/3/19 EXERCISE 4
'''Firstly this code is set out to calculate a basic orbit of a rocket
   using 4th order Runge-Kutta approach (improvement on Euler method)'''
   
import matplotlib.pyplot as plt
import numpy as np

'''Global constants (change this later bad practice)'''
G = 6.67E-11
mE = M = 5.9742e24      #earth mass
mM = 7.35e22            #moon mass
x_m = 384.4e6     #hypothesised distance from moon
h = 100                 #Step size

'''CHECK IF STRING CAN BE CONVERTED TO FLOAT 
(USED TO DEAL WITH INVALID CHARACTERS FOR USER INPUT)'''
def checkFloat(string):
    try:
        float(string)
    except ValueError:
        return False
    return True

'''Velocity equations '''
def f1(v_x):   
    return v_x
def f2(v_y):   
    return v_y

''' make empty lists/arrays'''
Distance_x = []
Distance_y = []
Velocity_x = []
Velocity_y = []
Time = []
KEnergy = []
PEnergy = []
TEnergy =[]
MOON_APPROACH=[]

''' Orbit equations'''
def orbit(h,x,y,v_x,v_y,t,m,MA):
    
    m = 10000
    '''Energy equations'''
    KE = 0.5*m*(np.sqrt((v_x**2)+(v_y**2)))**2   #Pythagoras used to combine the velocities
    PE = -G*m*M/(np.sqrt((x**2)+(y**2))) 
    TE = KE+PE
    MA = ((abs(3.84e8-x)**2 + abs(y)**2)**0.5)- (1737000)  #THIS IS THE CLOSEST APPROACH DISTANCE
    
    ''' Assigning lists'''    
    Distance_x = [x]
    Distance_y = [y]
    Velocity_x = [v_x]
    Velocity_y = [v_y]
    Time = [t]
    KEnergy = [KE]
    PEnergy = [PE]
    TEnergy =[TE]
    MOON_APPROACH=[MA]
      
    while (t > 0):
        
        ''' K values '''
        k1_x = f1(v_x)
        k1_y = f2(v_y)
        k1_vx = f3(x, y)
        k1_vy = f4(x, y)
        
        k2_x = f1(v_x + 0.5*h*k1_vx)
        k2_y = f2(v_y + 0.5*h*k1_vy)
        k2_vx = f3(x + 0.5*h*k1_x, y + 0.5*h*k1_y)
        k2_vy = f4(x + 0.5*h*k1_x, y + 0.5*h*k1_y)
        
        k3_x = f1(v_x + 0.5*h*k2_vx)
        k3_y = f2(v_y + 0.5*h*k2_vy)
        k3_vx = f3(x + 0.5*h*k2_x, y + 0.5*h*k2_y)
        k3_vy = f4(x + 0.5*h*k2_x, y + 0.5*h*k2_y)
        
        k4_x = f1(v_x + h*k3_vx)
        k4_y = f2(v_y + h*k3_vy)
        k4_vx = f3(x + h*k3_x, y + h*k3_y)
        k4_vy = f4(x + h*k3_x, y + h*k3_y)
        
        x += h * ((k1_x + 2*k2_x + 2*k3_x + k4_x) /6)
        y += h * ((k1_y + 2*k2_y + 2*k3_y + k4_y) /6)
        v_x += h * ((k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) /6)
        v_y += h * ((k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) /6)
        t += h 
        
        '''Energy Equations'''
        
        KE = 0.5*m*(np.sqrt((v_x**2)+(v_y**2)))**2   #Pythagoras used to combine the velocities
        PE = -G*m*M/(np.sqrt((x**2)+(y**2)))
        TE = KE+PE
    
        '''Appending lists'''
        
        Distance_x.append(x)
        Distance_y.append(y)
        Velocity_x.append(v_x)
        Velocity_y.append(v_y)
        Time.append(t)
        KEnergy.append(KE)  #KINETIC ENERGY
        PEnergy.append(PE)  #POTENTIAL ENERGY
        TEnergy.append(TE)  #TOTAL ENERGY
        MOON_APPROACH.append(MA)
        ''' This break statement stop time going on infinitly
            it only allows10000 iterations of the time step
            before stopping'''
    
        if t == 2000 +  20000*h:
            break
    
    return Distance_x, Distance_y, Velocity_x, Velocity_y, Time, KEnergy, PEnergy, TEnergy, MOON_APPROACH


MyInput = '0'
while MyInput != 'q':                                       #This while loop creates my menu for people using the code to add values 
    print(' ')
    print('Welcome to Harry Wisemans program for Exercise 4 Orbits. Please choose one of the options below.')
    print(' ')
    print('a = Use of the basic equation and Earth Orbit')
    print(' ')
    print('b = Advanced equation and Slingshot orbit of Moon')
    print(' ')
    MyInput = input('Enter a choice, "a", "b", or "q" to quit: ')
    print('You entered the choice: ',MyInput)
    
    """ Part A: Using Euler's method y(t) and v_y(t) are calculated
    for a falling body (ball) starting at 1km and u=0 """
    
    if MyInput == 'a':
        print(' ')
        print('You have chosen part (a)')
        print('')
        
        def f3(x,y):
            a_x = -(G*M*x)*(((x**2)+(y**2))**(-3/2))#-moon
            return a_x
        
        def f4(x,y):
            a_y = -(G*M*y)*(((x**2)+(y**2))**(-3/2))
            return a_y
        x = 6000000
        y = 6000000
        v_x = 5000
        v_y = -5000
        t = 200
        m = 100000
        
        MyInput = '0'
        while MyInput != 'q':                                       #This while loop creates my menu for people using the code to add values 
            print(' ')
            print('This section used the simple equation, each part here will show the orbit and energy')
            print(' ')
            print('a = Perfectly circular orbit')
            print(' ')
            print('b = User input options')
            print(' ')
            
            MyInput = input('Enter a choice, "a", "b", or "q" to quit: ')
            print('You entered the choice: ',MyInput)
            
            if MyInput == 'a':
                print(' ')
                print('You have chosen part (a)')
                print('')
                
                h = 10
                ''' Plot of the orbit'''
                Distance_x, Distance_y, Velocity_x, Velocity_y, Time, KEnergy, PEnergy, TEnergy, MOON_APPROACH = orbit(h,x,y,v_x,v_y,t,m,MA)                
                plt.figure(1)
                plt.plot(Distance_x,Distance_y,linestyle='--',c='r')
                plt.scatter(0,0,c='c',s=637.1 )
                plt.title("Graph of Orbit") 
                plt.xlabel("X/m") 
                plt.ylabel("Y/m")
                plt.grid()
                plt.show()
                
                '''Plot of the Energies'''
                
                plt.figure(2)
                plt.plot(Time,KEnergy,c='c')
                plt.title("Graph of Kinetic Energy") 
                plt.xlabel("Time/s") 
                plt.ylabel("Energy/J")
                plt.grid()
                plt.show()
                
                plt.figure(3)
                plt.title("Graph of Potential Energy") 
                plt.xlabel("Time/s") 
                plt.ylabel("Energy/J")
                plt.plot(Time,PEnergy,c='r')
                plt.grid()
                plt.show()
                
                plt.figure(4)
                plt.title("Graph of Energy against time of orbiting object") 
                plt.xlabel("Time/s") 
                plt.ylabel("Energy/J")
                plt.plot(Time,KEnergy,c='c',label='Kinetic Energy')
                plt.plot(Time,PEnergy,c='r',label='Potential Energy')
                plt.plot(Time,TEnergy,c='purple',label='Potential Energy')
                plt.rcParams['axes.facecolor'] = 'white'
                plt.legend()
                plt.grid()
                plt.show()
                
            elif MyInput == 'b':
                print(' ')
                print('You have chosen part (b)')
                print(' ')
                print('Please enter sensible parameters')
                
                input_m = input("Enter a value for the mass of the rocket kg between 1e3 & 1e10: ")
                input_x = input("Enter a value for x position in m: ")
                input_y = input("Enter a value for y position in m: ")
                input_v_x = input("Enter a value for speed in  x direction m/s: ")
                input_v_y = input("Enter a value for speed in y direction m/s: ")
                
                if checkFloat(input_m) and 1e3<=float(input_m)<=1e10 and checkFloat(input_x) and checkFloat(input_y) and checkFloat(input_v_y) and -3e8<=float(input_v_y)<=3e8 and checkFloat(input_v_x) and -3e8<=float(input_v_x)<=3e8: #THESE ONLY ALLOW NUMBERS TO BE INPUTTED
                    
                    m = float(input_m)
                    x = float(input_x)
                    y = float(input_y)
                    v_x = float(input_v_x)
                    v_y = float(input_v_y)
                    
                    ''' Plot of the orbit'''
                    Distance_x, Distance_y, Velocity_x, Velocity_y, Time, KEnergy, PEnergy, TEnergy, MOON_APPROACH = orbit(h,x,y,v_x,v_y,t,m,MA) #CALLING METHOD ORBIT EQUATION ABOVE                
                    plt.figure(6)
                    plt.plot(Distance_x,Distance_y,linestyle='--',c='r',label='Orbit')
                    plt.scatter(0,0,c='c',s=637.1 )
                    plt.title("Graph of Orbit") 
                    plt.xlabel("X/m") 
                    plt.ylabel("Y/m")
                    plt.legend()
                    plt.grid()
                    plt.show()
                    
                    plt.figure(7)
                    plt.title("Graph of Energy against time of orbiting object") 
                    plt.xlabel("Time/s") 
                    plt.ylabel("Energy/J")
                    plt.plot(Time,KEnergy,c='c',label='Kinetic Energy')
                    plt.plot(Time,PEnergy,c='r',label='Potential Energy')
                    plt.plot(Time,TEnergy,c='purple',label='Potential Energy')
                    plt.rcParams['axes.facecolor'] = 'white'
                    plt.legend()
                    plt.grid()
                    plt.show()
                    
                else: print("   WARNING!!!!!  One of the values you have entered is invalid.")
            
                
            elif MyInput == "q":    
                print('You have chosen to finish - goodbye xxx.') 
            
            elif MyInput != 'q'or'a'or'b': print('This is not a valid choice')
            
            
    elif MyInput == 'b':
        print(' ')
        print('You have chosen part (b)')
        print(' ')
        print('This section used the Advanced equation, each part here will show the orbit and energy')
        print(' ')
        print('a = Slingshot orbit')
        print(' ')
        print('b = User input options')
        print(' ')
        
        '''Acceleration equations for PART B'''
        def f3(x,y):
            a_x = -((G*mE*x)*(((x**2)+(y**2))**(-1.5)))-((G*mM*(x-x_m))*((((x-x_m)**2)+(y**2))**(-1.5)))
            return a_x
        
        def f4(x,y):
            a_y = -(G*mE*y)*(((x**2)+(y**2))**(-1.5))-(G*mM*y)*((((x-x_m)**2)+(y**2))**(-1.5)) #CHECK THIS EQUATION
            return a_y
        
        
        MyInput2 = '0'
    while MyInput2 != 'q':           
        MyInput2 = input('Enter a choice, "a", "b", or "q" to quit: ')
        print('You entered the choice: ',MyInput2)
            
        if MyInput2 == 'a':
                print(' ')
                print('You have chosen part (a)')
                print('')
                print('SLINGSHOT ORBIT')
                print('')
                
                ''' Parameter required'''
                x = -6747.475e3
                y = 0
                v_x = 0
                v_y = 10.7593E3#lower 10.77249e3
                t = 200
                m = 75e3
                
                Distance_x, Distance_y, Velocity_x, Velocity_y, Time, KEnergy, PEnergy, TEnergy, MOON_APPROACH = orbit(h,x,y,v_x,v_y,t,m,MA)
                
                plt.figure(9)
                plt.plot(Distance_x,Distance_y,linestyle='--',c='r')
                plt.scatter(0,0,c='b',s=63.71 )
                plt.scatter(384.4e6,0,c='g',s=17.6 )
                plt.rcParams['axes.facecolor'] = 'black' #gives black background
                plt.title("Graph of Orbit") 
                plt.xlabel("X/m") 
                plt.ylabel("Y/m")
                plt.grid()
                plt.show()
                
                print('Closest approach is  '+str( min(MOON_APPROACH) )+'m') #this is the distance of closest aproach from above
                
               
        elif MyInput2 == 'b':
                print(' ')
                print('You have chosen part (b)')
                print(' ')
                print('Choose parameters')
                
                input_m = input("Enter a value for the rocket kg between 1e3 & 1e10: ")
                input_x = input("Enter a value for position in m: ")
                input_y = input("Enter a value for position in m: ")
                input_v_x = input("Enter a value for speed in m/s: ")
                input_v_y = input("Enter a value for speed in m/s: ")
            
                if checkFloat(input_m) and 1e3<=float(input_m)<=1e10 and checkFloat(input_x) and checkFloat(input_y) and checkFloat(input_v_y) and -10000<=float(input_v_y)<=10000 and checkFloat(input_v_x) and -10000<=float(input_v_x)<=10000: #THESE ONLY ALLOW NUMBERS TO BE INPUTTED
                
                    m = float(input_m)
                    x = float(input_x)
                    y = float(input_y)
                    v_x = float(input_v_x)
                    v_y = float(input_v_y)
                    
                    Distance_x, Distance_y, Velocity_x, Velocity_y, Time, KEnergy, PEnergy, TEnergy, MOON_APPROACH = orbit(h,x,y,v_x,v_y,t,m,MA)
                
                    plt.figure(10)
                    plt.plot(Distance_x,Distance_y,linestyle='--',c='r')
                    plt.scatter(0,0,c='b',s=63.71 )
                    plt.scatter(384.4e6,0,c='g',s=17.6 )
                    plt.rcParams['axes.facecolor'] = 'black' #gives black background
                    plt.title("Graph of Orbit") 
                    plt.xlabel("X/m") 
                    plt.ylabel("Y/m")
                    plt.grid()
                    plt.show
               
                else: print("One of the values you have entered is invalid.")
                
        elif MyInput2 != 'q':
            print("This is not an option")
            
                
   
    print('You have chosen to finish - goodbye xxx.') 
            
