# Import necessary code

import os
import numpy as np
from tardis.io.atom_data.util import download_atom_data
from stardis.base import run_stardis
from stardis.opacities.base import calc_alphas
from stardis.transport.base import raytrace
from astropy import units as u, constants as const


class Benchmarkrunstardis:
    """
    Class to benchmark run_stardis function
    """

    timeout = 1800  # Worst case timeout of 30 mins

    def setup(self):
        self.curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.args_dict = {}

    def time_run_tardis(self):
        os.chdir(self.curr_dir)
        tracing_lambdas = np.arange(6540, 6590, 0.01) * u.Angstrom
        run_stardis("benchmark_config.yml", tracing_lambdas, args_dict=self.args_dict)

    def time_raytrace(self):
        key = "raytrace"
        if key in self.args_dict:
            args = self.args_dict[key]
            raytrace(**args)

    def time_calc_alphas(self):
        key = "calc_alphas"
        if key in self.args_dict:
            args = self.args_dict[key]
            calc_alphas(**args)
