    def create_anotatable_file (self ):
        
        for each_netlist in self.all_netlists_list:
            top_module_from_file = take_top_module(each_netlist)
            write_it_on_anotatable_netlist(top_module_from_file)
