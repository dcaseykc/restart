"""Demand Model.

Demand modeling
"""
from typing import Optional

import confuse  # type: ignore
import numpy as np  # type: ignore # noqa: F401
import pandas as pd  # type: ignore # noqa: F401

from base import Base
from log import Log
from population import Population
from resourcemodel import Resource


class Demand(Base):
    """Calculate consumption based on Population and Resource.

    Take in Pop and and Res and into model.data["Pop Res Demand pn"]
    Some parameters are to use:
    - Washington estimate
    - Mitre burn rates
    - Johns Hopkins burn rates
    - CDPH estimates
    - Ensemble

    If pop and res aren't set by default take the existing Population and
    resource already in the model.data

    With dimensions ["Population p"]["Resource n"]

    This uses https://realpython.com/documenting-python-code/
    docstrings using the NumPy/SciPy syntax
    Uses a modified standard project
    Uses https://www.sphinx-doc.org/en/master/ to generate the documentation
    """

    def __init__(
        self,
        config: confuse.Configuration,
        pop: Population = None,
        res: Resource = None,
        log_root: Optional[Log] = None,
        type: Optional[str] = None,
    ):
        """Initialize the Economy object.

        This uses the Frame object and populates it with default data unless yo
        override it
        """
        # https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init/7059529
        super().__init__(log_root=log_root)
        log = self.log
        log.debug(f"In {__name__}")

        self.level_to_res_mn_arr: Optional[np.ndarray] = None
        self.level_to_res_mn_df: Optional[pd.DataFrame] = None
        self.level_pm_arr: Optional[np.ndarray] = None
        self.level_pm_df: Optional[pd.DataFrame] = None
        self.demand_pn_df: Optional[pd.DataFrame] = None
        self.level_pl_arr: Optional[np.ndarray] = None
        self.level_pl_df: Optional[pd.DataFrame] = None
        self.level_demand_ln_df: Optional[pd.DataFrame] = None
        self.total_demand_pn_arr: Optional[np.ndarray] = None
        self.total_demand_pn_df: Optional[pd.DataFrame] = None
        self.level_total_demand_ln_df: Optional[pd.DataFrame] = None
        self.level_total_cost_ln_df: Optional[pd.DataFrame] = None