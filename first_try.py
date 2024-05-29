from .action import *
from .functions import copy_with_different_name


class Anotation(Action):

    def __init__(self, current_caf_file_paths , current_hardmacros_object , elaboration_configuration) :

        #Workspace for anotation 
        self.sdf_files_dir = elaboration_configuration['file_tree']['/sdf_directory'] 
        self.mix_netlist_path = elaboration_configuration['netlists']
        self.new_netlist_file_path = self.mix_netlist_path[0].split('/')[-1].replace('.v.gz','')+"_with_sdf_ann_.gz"
        self.current_caf_file_path = current_caf_file_paths[0]
        #New file name 
        copy_with_different_name(self.mix_netlist_path[0],self.sdf_files_dir,self.new_netlist_file_path)
        #Parameters
        self.current_hardmacros_object = current_hardmacros_object
        self.elaboration_configuration = elaboration_configuration
        #Master netlist variables
        self.all_netlists_list = list()
        self.all_netlists_list.append(self.mix_netlist_path)
        #Master sdf variables
        self.all_sdf_list = list()
        self.all_module_list = list()
        #Run anotation
        self.start_anotating_design()


    def start_anotating_design(self):

        #Getting path from caf
        standart_path = self.getting_standart_path_for_netlists()
        #Start by getting the netlists and sdfs for harmacros
        for each_hardmacros in self.current_hardmacros_object:
            
            #Getting info from hardmacros 
            self.current_sdf_paths = standart_path + self.current_hardmacros_object['sdf']
            self.current_netlist = standart_path + self.current_hardmacros_object['netlist']
            self.current_module = self.current_hardmacros_object['module']
            
            self.all_module_list.append(self.current_module)
            self.all_netlists_list.append(self.current_netlist)
            self.all_sdf_list.append(self.current_sdf_paths)

def create_anotatable_file (self ):
        
        for each_netlist in self.all_netlists_list:
            top_module_from_file = self.take_top_module(each_netlist)
            self.write_it_on_anotatable_netlist(top_module_from_file)

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


    def anotate(self, complete_netlist_file):

        #Anotating the netlist         
        with open(complete_netlist_file,'r+') as netlist_file:
            lines = netlist_file.readlines()
            for each_line,i in enumerate(lines):
                if self.current_module in each_line :  
                    for each_line,i in enumerate(lines):
                        if 'endmodule' in each_line: 
                            each_line[i] = self.anotation()
                            break

        # final_anotation_path  =  standart_path_for_netlist +'/' + possible_hardcoded_path + '/' + module

    def getting_standart_path_for_netlists (self):


        #Checking if sdf file exists also for corresponding caf 
        if os.path.isfile(self.current_sdf_paths) is not True : info("SDF full path is not given, searching in caf files")
        else: self.final_anotation_path = self.current_sdf_paths 
        if os.path.isfile(self.current_caf_file_path) is not True : return info("No caf files have been found, for corresponding caf: "+self.current_caf_file_path+" Continuing")
        #Getting hardmacros file path 
        with open(self.current_caf_file_path , 'r') as  caf_file:
            lines = caf_file.readlines()
            for each_line in lines:
                if self.current_module in each_line: 
                    standart_path_for_netlist = each_line.split('/'+self.current_module)[0]
                    try: standart_path_for_netlist =standart_path_for_netlist.split('+incdir+',1)[1] 
                    except: pass
                    return standart_path_for_netlist

    def building_final_sdf_path(self):
        pass
                  
    def anotation(self):

        main_string = ' initial begin\n'
        main_string += '$display($display("%t:  Annotating '+self.current_module+' SDF",$time);\n'
        main_string += '$sdf_annotate (' + self.final_sdf_path + ',' + self.current_module + ');\n'
        main_string += ' end\n'
        main_string += 'endmodule\n'

