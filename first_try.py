    def create_anotatable_file (self ):
        
        for each_netlist in self.all_netlists_list:
            top_module_from_file = take_top_module(each_netlist)
            write_it_on_anotatable_netlist(top_module_from_file)

def take_top_module(self, netlist):

    # this function should take all the lines from 'topmodule' untill endmodule
    # and return the name of the module   
    
    with open(netlist, 'r') as f:
        for i,line in f:
            if 'topmodule' in line:
                return line.split()[1]
                def take_top_module(self, netlist):
                    module_lines = []
                    is_module_started = False

def write_it_on_anotatable_netlist(self, top_module):
    # this function should write the topmodule to a file
    with open('anotatable_netlist.v', 'w') as f:
        f.write(top_module)
