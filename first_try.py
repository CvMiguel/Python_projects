    def create_anotatable_file (self ):
        
        for each_netlist in self.all_netlists_list:
            top_module_from_file = take_top_module(each_netlist)
            write_it_on_anotatable_netlist(top_module_from_file)

def take_top_module(self, netlist):
    module_lines = []  # Define the module_lines variable

    # This function should take all the lines from 'topmodule' until endmodule
    # and return the name of the module   
    with open(netlist, 'r') as f:
        is_module_started = False  # Initialize the is_module_started variable
        for line in f:
            if 'module' in line:
                is_module_started = True
            if is_module_started:
                module_lines.append(line)
            if 'endmodule' in line:
                break

    return module_lines

def write_it_on_anotatable_netlist(self, top_module):
    # this function should write the topmodule to a file
    with open('anotatable_netlist.v', 'w') as f:
        f.write(top_module)
