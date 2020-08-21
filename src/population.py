"""Population class.

This is the base class for all models. It instantiates the population to be
filled in.

It also includes a default() for setting up the main attribute matrix,
detail_pd_arr and then a calc() which calculates the rest of the related data
"""

from typing import Dict, Optional

# Insert the classes of data we support here
import confuse  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type:ignore

# Note that pip install data-science-types caused errors
from base import Base
from log import Log

# import pandas as pd  # type:ignore


class Population(Base):
    """Population objects are created here.

    It has a default model in it for testing which is the Bharat model
    You should override it with a new child class

    Population statistics and model for population
    Initially this containes population of p x 1
    Later it will be p x d where d are the detail columns
    For instance the number of covid patients
    The number of trips or visits or runs for a given population

    The second matrix p population describes is how to map population to:w

    l demand levels to give a p x l. Long term this becomes d x p x l
    So that you can have a different run rate for each detail d of population

    How are resources consumed by different levels in a population
    This is the key first chart in the original model.
    It takes a set of l protection levels and then for each of n resources,
    provides their burn rate. So it is a dataframe that is l x n

    In this first version, burn rates are per capita, that is per person in a
    given level.

    In a later version, we will allow different "burn rates" by population
    attributes so this becomes a 3 dimensional model. For convenience, the
    Frame object we have retains objects in their simple dataframe form since
    it is easy to extract

    For multidimenstional indices, we keep both the n-dimensional array
    (tensor) and also have a method ot convert it to a multiindex for use by
    Pandas

    There is a default mode contained here for testing, you should override
    this by creating a child class and overriding the init

    We also create a friendly name and long description as document strings
    eventually this will become a file we read in that is a data description
    but for now it is a dictionary
    """

    # https://satran.in/b/python--dangerous-default-value-as-argument
    # https://stackoverflow.com/questions/2…

    # These are the default structures
    # detail_pd_arr = np.array([735.2, 7179.6])
    # level_pm_arr = np.array(
    #     [
    #         [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5],
    #         [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    #     ]
    # )

    # res_demand_mn_arr = np.array(
    #     [[0, 1], [0, 2], [0, 2], [0.1, 3], [0.2, 4], [0.3, 6], [1.18, 0]]
    # )

    # No need for initialization get it from model.data
    #        detail_pd_df: Optional[pd.DataFrame] = None,
    #        level_pm_df: Optional[pd.DataFrame] = None,
    #        res_demand_mn_df: Optional[pd.DataFrame] = None,
    #        level_pl_df: Optional[pd.DataFrame] = None,
    def __init__(self, config: confuse.Configuration, log_root: Log = None):
        """Initialize all variables.

        All initialization here and uses type to determine which method to call
        The default is PopulationDict which reads from the model.data
        """
        # https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init/7059529
        # to pick up the description
        super().__init__(log_root=log_root)
        log = self.log
        log.debug("In %s", __name__)

        self.detail_pd_arr: Optional[np.ndarray] = None
        self.detail_pd_df: Optional[pd.DataFrame] = None
        self.level_pm_labs: Optional[list] = None
        self.level_pm_arr: Optional[np.ndarray] = None
        self.level_pm_df: Optional[pd.DataFrame] = None
        self.config: Optional[Dict] = config
        self.codes: Optional[list] = None