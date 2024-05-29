from .action import *
from .functions import copy_with_different_name
import os

class Anotation(Action):

    def __init__(self, current_caf_file_paths , current_hardmacros_object , elaboration_configuration) :

        # Workspace for annotation 
        self.sdf_files_dir = elaboration_configuration['file_tree']['/sdf_directory'] 
        self.mix_netlist_path = elaboration_configuration['netlists']
        self.new_netlist_file_path = self.mix_netlist_path[0].split('/')[-1].replace('.v.gz','')+"_with_sdf_ann_.gz"
        self.current_caf_file_path = current_caf_file_paths[0]
        # New file name 
        copy_with_different_name(self.mix_netlist_path[0],self.sdf_files_dir,self.new_netlist_file_path)
        # Parameters
        self.current_hardmacros_object = current_hardmacros_object
        self.elaboration_configuration = elaboration_configuration
        # Master netlist variables
        self.all_netlists_list = list()
        self.all_netlists_list.append(self.mix_netlist_path)
        # Master sdf variables
        self.all_sdf_list = list()
        self.all_module_list = list()
        # Run annotation
        self.start_annotating_design()


    def start_annotating_design(self):

        # Getting path from caf
        standart_path = self.getting_standard_path_for_netlists()
        # Start by getting the netlists and sdfs for hardmacros
        for each_hardmacros in self.current_hardmacros_object:
            
            # Getting info from hardmacros 
            self.current_sdf_paths = standart_path + each_hardmacros['sdf']
            self.current_netlist = standart_path + each_hardmacros['netlist']
            self.current_module = each_hardmacros['module']
            
            self.all_module_list.append(self.current_module)
            self.all_netlists_list.append(self.current_netlist)
            self.all_sdf_list.append(self.current_sdf_paths)

    def create_annotatable_file(self):
        
        for each_netlist in self.all_netlists_list:
            top_module_from_file = self.take_top_module(each_netlist)
            self.write_it_on_annotatable_netlist(top_module_from_file)

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

    def write_it_on_annotatable_netlist(self, top_module):
        
        # This function should write the topmodule to a file
        with open('anotatable_netlist.v', 'w') as f:
            f.write(top_module)


    def annotate(self, complete_netlist_file):

        # Annotating the netlist         
        with open(complete_netlist_file,'r+') as netlist_file:
            lines = netlist_file.readlines()
            for i, each_line in enumerate(lines):
                if self.current_module in each_line :  
                    for j, each_line in enumerate(lines):
                        if 'endmodule' in each_line: 
                            lines[j] = self.annotation()
                            break
            netlist_file.seek(0)
            netlist_file.writelines(lines)

    def getting_standard_path_for_netlists(self):

        # Checking if sdf file exists also for corresponding caf 
        if not os.path.isfile(self.current_sdf_paths):
            info("SDF full path is not given, searching in caf files")
        else:
            self.final_annotation_path = self.current_sdf_paths 
        if not os.path.isfile(self.current_caf_file_path):
            return info("No caf files have been found, for corresponding caf: "+self.current_caf_file_path+" Continuing")
        # Getting hardmacros file path 
        with open(self.current_caf_file_path , 'r') as  caf_file:
            lines = caf_file.readlines()
            for each_line in lines:
                if self.current_module in each_line: 
                    standard_path_for_netlist = each_line.split('/'+self.current_module)[0]
                    try:
                        standard_path_for_netlist = standard_path_for_netlist.split('+incdir+',1)[1] 
                    except:
                        pass
                    return standard_path_for_netlist

    def building_final_sdf_path(self):
        pass
                  
    def annotation(self):

        main_string = ' initial begin\n'
        main_string += '$display($display("%t:  Annotating '+self.current_module+' SDF",$time);\n'
        main_string += '$sdf_annotate (' + self.final_sdf_path + ',' + self.current_module + ');\n'
        main_string += ' end\n'
        main_string += 'endmodule\n'
        return main_string
