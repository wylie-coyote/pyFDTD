import math

epsilon_0=8.85418782*10**-12
mu_0=1.2566370614*10**−6
c=2.99792458*10**8


class point:
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x=x
        self.y=y
        self.z=z
    def __self__(self):
        return math.sqrt(self.x**2+self.y**2+self.y**2)
    def __add__(self,p):
        tmp = point()
        tmp.x=self.x+p.x
        tmp.y=self.y+p.y
        tmp.z=self.z+p.z
        return tmp
    def __iadd__(self,p):
        self.x+=p.x
        self.y+=p.y
        self.z+=p.z

class Source_point:
    def __init__(self,location=point(),offset=0):
        self.location=location
        self.offset=offset

class Signal:
    def __init__(self,E_sig,H_sig):
        assert len(E_sig)==len(H_sig),"E and H signal lists not same lengths"
        self.len=len(E_sig)
        self.E_sig=E_sig
        self.H_sig=H_sig
class Source:
    def __init__(self,points,signal):
        self.signal=signal
        self.points=points
        self.num_points=len(points)

class simulation:
    # grid_space: the spacing of the grid cells, units in meters, class point
    # dim the number of grid cells of the E-field, class point
    # time_step is the delta t of the sim
    # source_array is the array of the points of the source and there offset
    #   list of source_point
    # source_signal is the array of the 
    def __init__(self,grid_space,dim,time_step,source):
        self.grid_space=grid_space
        self.dim=dim
        self.time_step=time_step
        # creates the 3D array for the E field
        self.E=[[[point()]*int(dim.x)]*int(dim.y)]*int(dim.z)
        # creates the 3D array for epsilon of the space, with starting ep_r=1
        self.epsilon=[[[epsilon_0]*dim.x]*dim.y]*dim.z
        # creates the 3D array for the H field, dim is that of E-1, yee cell
        self.H=[[[point()]*int(dim.x-1)]*int(dim.y-1)]*int(dim.z-1)
        # creates the 3D array for mu of the space, with starting mu_r=1
        self.mu=[[[mu_0]*int(dim.x-1)]*int(dim.y-1)]*int(dim.z-1)
        self.source=source
        self.index=0
    def update_E(self):
        for i in range(self.dim.x):
            for j in range(self.dim.y):
                for k in range(self.dim.z):
                    
        
    def update_H(self):
        for i in range(self.dim.x):
            for j in range(self.dim.y):
                for k in range(self.dim.z):
                    

    def update_Source(self):
        for i in self.source.points:
            offset=(i.offset+self.index)%self.source.signal.len
            self.E[i.z][i.y][i.x]+=self.source.signal[offset].E
            self.H[i.z][i.y][i.x]+=self.source.signal[offset].H
            
        
    def update_RBC(self):
        
    def update(self,steps=1):
        for i in range(steps):
            self.update_Source()
            self.update_H()
            self.update_E()
            self.update_RBC()
            self.index+=1
            


