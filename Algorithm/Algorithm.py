# coding: utf-8

class Algorithm:
    # The variable `opt` seems to be a dictionary
    # which has to be transfered to the initial function.
    # opt = {"exp_dir":"", 
    #       best_metric(optional), 
    #       'networks':{}, }
    def __init__(self, opt):
        self.set_experiment_dir(opt["exp_dir"])


    def set_experiment_dir(self,directory_path):
        self.exp_dir = directory_path   # Expexted directory

        if not os.path.isdir(self.exp_dir): # Check whether the expected dir exist
            os.makedirs(self.exp_dir)       # If not, create one

        self.vis_dir = os.path.join(directory_path,'visuals')
                                            # Create a new dir for visuals
        if (not os.path.isdir(self.vis_dir)):
            os.makedirs(self.vis_dir)

        self.preds_dir = os.path.join(directory_path,'preds') # Prediction
        if (not os.path.isdir(self.preds_dir)):
            os.makedirs(self.preds_dir)

    # This function seems to be only called for once
    # Documenting the start time of the algorithm
    def set_log_file_handler(self):
        self.logger = logging.getLogger(__name__)
        strHandler = logging.StreamHandler()
        formatter = logging.Formatter(
                '%(asctime)s - %(name)-8s - %(levelname)-6s - %(message)s')
        strHandler.setFormatter(formatter)
        self.logger.addHandler(strHandler)
        self.logger.setLevel(logging.INFO)

        log_dir = os.path.join(self.exp_dir, 'logs')
        if (not os.path.isdir(log_dir)):
            os.makedirs(log_dir)

        now_str = datetime.datetime.now().__str__().replace(' ','_')

        self.log_file = os.path.join(log_dir, 'LOG_INFO_'+now_str+'.txt')
        self.log_fileHandler = logging.FileHandler(self.log_file)
        self.log_fileHandler.setFormatter(formatter)
        self.logger.addHandler(self.log_fileHandler)

    def init_all_networks(self):
        networks_defs = self.opt['networks']
        self.networks = {}
        self.optim_params = {}

        for key, val in networks_defs.items():
            self.logger.info('Set network %s' % key)
            def_file = val['def_file']
            net_opt = val['opt']
            self.optim_params[key] = val['optim_params'] if ('optim_params' in val) else None
            pretrained_path = val['pretrained'] if ('pretrained' in val) else None
            self.networks[key] = self.init_network(def_file, net_opt, pretrained_path, key)




import os
import os.path
import imp

class Algorithm():
	def __init__(self, opt):
		

	def set_experiment_dir(self, directory_path):

