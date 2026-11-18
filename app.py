"""ParkSmart GUI (Python standard library only). All allocation and data logic executes in C."""
import os
import subprocess
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXE = ROOT / ('parksmart.exe' if os.name == 'nt' else 'parksmart')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('ParkSmart | Intelligent Parking Platform')
        self.geometry('1050x720')
        self.configure(bg='#101827')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#101827')
        self.style.configure('TLabel', background='#101827', foreground='#e7eefb', font=('Arial', 11))
        self.style.configure('TButton', font=('Arial', 10), padding=9)
        self.style.configure('TEntry', padding=7)
        self.style.configure('TNotebook', background='#101827')
        self.style.configure('TNotebook.Tab', padding=(15, 10))
        tk.Label(self, text='PARKSMART', font=('Arial', 28, 'bold'), bg='#101827', fg='#61dafb').pack(anchor='w', padx=24, pady=(17, 0))
        tk.Label(self, text='Urban mobility • intelligent allocation • C-powered algorithm engine', bg='#101827', fg='#aabbd0').pack(anchor='w', padx=26, pady=(0, 12))
        tabs=ttk.Notebook(self);tabs.pack(fill='both',expand=True,padx=20,pady=10)
        for name, builder in [('Dashboard',self.dashboard),('Reservations',self.reservations),('Find Parking',self.find),('Allocation Lab',self.allocation),('Benchmarks & Scenarios',self.benchmarks)]:
            frame=ttk.Frame(tabs);tabs.add(frame,text=name);builder(frame)
        self.output=tk.Text(self,height=11,bg='#19263a',fg='#e7eefb',insertbackground='white',font=('Consolas',10),relief='flat',padx=12,pady=12)
        self.output.pack(fill='both',expand=False,padx=20,pady=(0,20))
        self.run('report')
    def run(self,*args):
        if not EXE.exists():
            messagebox.showerror('Build required',f'Compile the C engine first.\nExpected: {EXE}')
            return
        try:
            env=os.environ.copy();env['PARKSMART_DATA']=str(ROOT/'data')
            result=subprocess.run([str(EXE),*map(str,args)],cwd=ROOT,env=env,capture_output=True,text=True,timeout=20)
            self.output.delete('1.0','end');self.output.insert('end',result.stdout or result.stderr or 'No output')
            return result.stdout
        except Exception as exc:messagebox.showerror('Engine error',str(exc))
    def entry(self,frame,label,default,row,col):
        cell=ttk.Frame(frame);cell.grid(row=row,column=col,sticky='ew',padx=10,pady=12)
        ttk.Label(cell,text=label).pack(anchor='w',pady=(0,6));var=tk.StringVar(value=default);ttk.Entry(cell,textvariable=var,width=23).pack(fill='x');return var
    def dashboard(self,f):
        ttk.Label(f,text='Parking inventory and current occupancy',font=('Arial',15,'bold')).pack(anchor='w',padx=12,pady=12)
        ttk.Button(f,text='Refresh spaces',command=lambda:self.run('list')).pack(anchor='w',padx=12)
        ttk.Button(f,text='Occupancy report',command=lambda:self.run('report')).pack(anchor='w',padx=12,pady=8)
        ttk.Label(f,text='Lot IDs 1–8 correspond to the sample city network. All changes are saved to CSV.').pack(anchor='w',padx=12,pady=15)
    def reservations(self,f):
        idv=self.entry(f,'Parking lot ID','1',0,0);driver=self.entry(f,'Driver name','Alex',0,1)
        start=self.entry(f,'Start hour (integer)','10',1,0);end=self.entry(f,'End hour (integer)','12',1,1)
        ttk.Button(f,text='Reserve space',command=lambda:self.run('reserve',idv.get(),driver.get(),start.get(),end.get())).grid(row=2,column=0,padx=10,pady=15,sticky='w')
        cancel=self.entry(f,'Reservation ID to cancel','1',3,0)
        ttk.Button(f,text='Cancel reservation',command=lambda:self.run('cancel',cancel.get())).grid(row=4,column=0,padx=10,sticky='w')
    def find(self,f):
        source=self.entry(f,'Driver starting node (0–7)','0',0,0);start=self.entry(f,'Start hour','10',0,1);end=self.entry(f,'End hour','12',1,0)
        ttk.Button(f,text='Find nearest available parking (Dijkstra)',command=lambda:self.run('nearest',source.get(),start.get(),end.get())).grid(row=2,column=0,padx=10,pady=15,sticky='w')
    def allocation(self,f):
        nodes=self.entry(f,'Driver nodes, comma-separated','0,1,2,3,4,5',0,0);start=self.entry(f,'Start hour','10',0,1);end=self.entry(f,'End hour','12',1,0)
        ttk.Button(f,text='Compare greedy vs exact min-cost matching',command=lambda:self.run('compare',nodes.get(),start.get(),end.get())).grid(row=2,column=0,columnspan=2,padx=10,pady=15,sticky='w')
        ttk.Label(f,text='Exact strategy maximizes assignments, then minimizes total travel distance.').grid(row=3,column=0,columnspan=2,padx=10,sticky='w')
    def benchmarks(self,f):
        ttk.Label(f,text='Repeatable algorithm comparisons',font=('Arial',15,'bold')).pack(anchor='w',padx=12,pady=12)
        ttk.Button(f,text='Benchmark sorting: merge vs quick',command=lambda:self.run('benchmark')).pack(anchor='w',padx=12,pady=8)
        ttk.Button(f,text='Run 3 urban mobility scenarios',command=lambda:self.run('demo')).pack(anchor='w',padx=12,pady=8)
        ttk.Label(f,text='Scenarios: normal demand, capacity shock, and 32-driver stress case.').pack(anchor='w',padx=12,pady=12)

if __name__=='__main__':App().mainloop()
