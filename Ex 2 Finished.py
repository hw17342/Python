'''Harry Wiseman Exercise 2 "Fresnel diffraction using simpsons rule'''
import numpy as np                                 #numpy allows us to use pi
from matplotlib import pyplot as plt               #required for all graphs plotted
from scipy.integrate import simps                  #used for part c&d
    
def Simpson(x,x_1,x_2,N):                           #parameters
                                
    SR = 0.0                                        #simpsons rule sdtarting value    
    
    first_value = np.exp(((1j*k)/(2*z))*(x-x_1)**2)         #first value f(a)
    
    last_value = np.exp(((1j*k)/(2*z))*(x-x_2)**2)         #last value f(b)
    
    if x_1 > x_2:                                   #lower limit has to be larger than upper limit
        print ('Incorrect bounds')                  #preventing errors
        return None
    if N%2 != 0:                                    #another if statement because the to events aren't linked. This finds the remainder of N(%), and sees if its not equal to zero(!=), if the remainder isnt zero must be odd number therefore noit valid
        print ('Invalid choice of N')
        return None
    else:                                           #so for even integer N values
        h = (x_2 - x_1)/N 
        sum_odd = 0.0                               #The initial sum for the odd function values
        sum_even = 0.0                              #The initial sum for the odd function values
        for i in range(1, N//2 + 1):                #range for all the odd values
            sum_odd += np.exp(((1j*k)/(2*z))*(x-(x_1+2*(i)*h))**2)
        for i in range(1, N//2):                    # range integer for a even
            sum_even += np.exp(((1j*k)/(2*z))*(x-(x_1+(2*i*h)))**2)
      
    SR = (h /3.0)*((first_value + last_value) + 4*sum_odd + 2*sum_even)       #total sum (Electric field)
       
    return SR
def xIntegral(x,z,k,N,x_1prime,x_2prime):
    Xvalues = []                                                              #array for the x values
    x_prime = np.linspace(x_1prime, x_2prime, N+1)                                   #Returns evenly spaced numbers over a specified interval, np.linespace(start,end,intervals)
    for i in range(N+1):
            Xvalues.append(np.exp(((1j*k)/(2*z))*(x-(x_prime[i]))**2))
        
    return simps(Xvalues, x_prime)
        
def yIntegral(y,z,k,N,y_1,y_2):                                     #array for the y value    
        Yvalues = []                     
        y_prime = np.linspace(y_1, y_2, N+1)
        
        for i in range(N+1):
            Yvalues.append(np.exp(((1j*k)/(2*z))*(y-(y_prime[i]))**2))
        
        return simps(Yvalues, y_prime)
MyInput = '0'
while MyInput != 'q':
    MyInput = input('Enter a choice, "a", "b", "c", "d" or "q" to quit: ')
    print('You entered the choice: ',MyInput)
    
    if MyInput == 'a':
        print('You have chosen part (a)')
        print('z=0.02m,  N=100,  wavelength=100nm,  screencoordinate -5mm to 5mm,  apeture 0.00002')
        x_1 = 0
        x_2 = 2E-5                              #apertureas
        N = 100
        x = 0.005                               #actual x coordinate of screen (in x axis)
        z = 0.02                                #distance from the screen
        wavelength = 1E-06
        k = 2*np.pi/wavelength                  #k is the wavenumber
        panels = 100
        x_min = -5E-03                          #-5mm x' min
        x_max = 5E-03                           # x' max
        xvals = np.linspace(x_min,x_max,panels) #screen coordinates
        yvals = []                              #empty list (saying yvals is a list)
        for i in range(panels): yvals.append((Simpson(xvals[i],x_1,x_2,N)))
        Intensity = np.array(yvals) * np.conjugate(np.array(yvals))
        plt.plot(xvals,Intensity)
        plt.xlabel('screen coordinate (m)')
        plt.ylabel('Relative Intensity')
        plt.title('Part A')
        plt.show()
        
    elif MyInput == 'b':
        input_N = input("Enter a value for the number of iteravals (N): ")
        input_x_2 = input("Enter an apeture width (in meters): ")
        input_xcoordinate = input("Enter the width of screen coordinate in meters :")
        input_z = input("Enter distance from the screen to the apeture in meters: ")
        input_wavelength = input("Enter wavelength in meters: ")
        
        if (input_N.isnumeric() and 2 <= float(input_N) and  input_x_2.isnumeric() and input_z.isnumeric       #making sure only valid inputs allowed
        and float(input_N) != 0 and float(input_x_2) != 0 and float(input_z) != 0 and float(input_wavelength) != 0):
            x_1 = 0
            x_2 = float(input_x_2)                                   #optional aperturea width
            N = int(input_N)
            z = float(input_z)                                       #distance from the screen
            k = (2*np.pi/float(input_wavelength))                    #k is the wavenumber
            panels = 100
            x_min = (-(float(input_xcoordinate))/2)                 #x' min
            x_max = (float(input_xcoordinate)/2)                    # x' max
            xvals = np.linspace(x_min,x_max,panels)                 #screen coordinates
            yvals = []                                              #empty list (saying yvals is a list)
            for i in range(panels): yvals.append((Simpson(xvals[i],x_1,x_2,N)))
            Intensity = np.array(yvals) * np.conjugate(np.array(yvals))
            plt.plot(xvals,Intensity)
            plt.xlabel('screen coordinate (m)')
            plt.ylabel('Relative Intensity')
            plt.title('part B')
            plt.show()
        
        else: print("One of the values you have entered is invalid.")
                  
    elif MyInput == "c":
        print('You have chosen part(c)')
        input_N = input("Enter a value for the number of intervals (N): ")
        input_x_2 = input("Enter an apeture width in nanometres : ")
        input_xcoordinate = input("Enter the screen coordinate total width in mm:")
        input_z = input("Enter distance from the screen to the apeture in meters: ")
        input_wavelength = input("Enter wavelength in nanometers: ")
        input_panels = input("enter the number of points :")
        
        if (input_N.isnumeric() and 2 <= float(input_N) and  input_x_2.isnumeric() and input_z.isnumeric       #making sure only valid inputs allowed
        and float(input_N) != 0 and float(input_x_2) != 0 and float(input_z) != 0 and float(input_wavelength)
        and float(input_panels) !=0 and input_panels.isnumeric):
        
        
            N = int(input_N)
            x_1 = float(input_x_2)
            x_2 = float(input_x_2)                              
            x_min = float(input_xcoordinate)                 
            x_max = float(input_xcoordinate)
            z = float(input_z)                                       #distance from the screen
            wavelength = float(input_wavelength)                   #k is the wavenumber
            panels = int(input_panels)
            x_1 *= (-0.000000001)/2
            x_2 *= (0.000000001)/2
            x_min *= (-0.001)/2
            x_max *= (0.001)/2
            k = 2*np.pi/(0.000000001*wavelength)
        
        
            h = 4.0*np.pi / (panels - 1)         
            intensity = np.zeros( (panels,panels) )
            xvals = np.linspace(x_min,x_max,panels)
            yvals = np.linspace(x_min,x_max, panels)
            for i in np.arange(panels):                
                xpart = xIntegral(xvals[i],z,k,N,x_1,x_2)
                for j in np.arange(panels):
                    ypart = yIntegral(yvals[j],z,k,N,x_1,x_2)       #change x_1 to y_2 and give valyes for part D
                    field = xpart*ypart
                    #integral = xIntegral(xpart, ypart)
                    intense = (field * field.conjugate()).real
                        # assigns value of intensity
                    intensity[i][j] = intense
                
            # subplot creates square plot
            graph = plt.figure().add_subplot(111)
            graph.set_xlabel("$x$")
            graph.set_ylabel("$y$")
            
            # cmap determines the colour as inverse greyscale
            plt.imshow(intensity, extent=[x_min, x_max, x_min, x_max], cmap="plasma")
            plt.show()
            
        else: print("One of the values you have entered is invalid.")     
           
    elif MyInput == "d":
        print('You have chosen part(d)')
        print('please wait why the plot loads')
        x_1 = -0.5E-5
        x_2 = 0.5E-5
        y_1 = -1.5E-5
        y_2 = 1.5E-5
        N = 100
        z = 0.00002                                #distance from the screen
        wavelength = 1E-06
        k = 2*np.pi/wavelength                  #k is the wavenumber
        panels = 100
        x_min = -2E-05                          #-5mm x' min screen cooridnate
        x_max = 2E-05   
        h = 4.0*np.pi / (panels - 1) 
        intensity = np.zeros( (panels,panels) )
        xvals = np.linspace(x_min,x_max,panels)
        yvals = np.linspace(x_min,x_max, panels)
        for i in np.arange(panels):
            xpart = xIntegral(xvals[i],z,k,N,y_1,y_2)
            for j in np.arange(panels):
                ypart = yIntegral(yvals[j],z,k,N,x_1,x_2)       #change x_1 to y_2 and give valyes for part D
                field = xpart*ypart
                #integral = xIntegral(xpart, ypart)
                intense = (field * field.conjugate()).real
                # assigns value of intensity
                intensity[i][j] = intense
            
        # subplot creates square plot
        graph = plt.figure().add_subplot(111)
        graph.set_xlabel("$x$")
        graph.set_ylabel("$y$")
        
        # cmap determines the colour as inverse greyscale
        plt.imshow(intensity, extent=[x_min, x_max, x_min, x_max], cmap="plasma")
        plt.show()
        
    elif MyInput == "q":    
        print('You have chosen to finish - goodbye.') 
    
    elif MyInput != 'q'or'a'or'b'or'c'or'd': print('This is not a valid choice')