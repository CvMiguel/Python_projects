class simulations:
    
    def __init__( self, simulation_name , compile_caf, timing, sdf, caf , common,sa, sd ,td ,id ,tg):
        
        self.dict_simulation = dict()
        self.simulation_name = simulation_name
        self.compile_caf = compile_caf
        self.timing = timing 
        self.sdf = sdf 
        self.caf = caf 
        self.common = common 
        self.sa = sa 
        self.sd = sd
        self.td =td 
        self.id =id 
        self.tg =tg 
    
    def construct_simulation(self):
        self.dict_simulation = {
            "simulations": {
                self.simulation_name: {
                    "compile_caf" : self.compile_caf,
                    "timing": self.timing,
                    "sdf": self.sdf,
                    "caf": self.caf,
                    "custom_force": {
                        "common": self.common,
                        "sa": self.sa,
                        "sd": self.sd,
                        "td": self.td,
                        "id": self.id,
                        "tg": self.tg
                    }
                }
            }
        }
        return self.dict_simulation

def save_to_yaml(input_text) :
    #Dumping function 
    with open(cfg_file_yaml, 'w+') as file :  
            yaml.dump( input_text  , file, default_flow_style= False, sort_keys=False)

def save_simulation():

    gui_simulation = simulations(globals()["new_simulation_name_entry"].get(),its_yes(globals()["compile_caf_bool"].get()),globals()["sim_timing_entry"].get(),globals()["sim_sdf_entry"].get(),globals()["sim_caf_entry"].get(), globals()["custom_force_common_entry"].get(), globals()["custom_force_sa_entry"].get(), 
                                globals()["custom_force_sd_entry"].get(),globals()["custom_force_td_entry"].get(),globals()["custom_force_id_entry"].get(), globals()["custom_force_tg_entry"].get() )
    
    if globals()["new_simulation_name_entry"].get() in gui_simulation.dict_simulation :
        save_to_yaml( gui_simulation.construct_simulation())
    else :
        gui_simulation.dict_simulation["simulations"][globals()["new_simulation_name_entry"].get()] = gui_simulation.dict_simulation["simulations"]
        save_to_yaml( gui_simulation.construct_simulation())

    messagebox.showinfo("Saved", "Configuration simulation saved successfully!")
