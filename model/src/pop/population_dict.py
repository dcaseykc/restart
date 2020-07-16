"""Population Data Read.

Read in the population from the model dictionary
"""
import logging
import pandas as pd  # type: ignore # noqa: F401
import numpy as np  # type: ignore
# https://www.python.org/dev/peps/pep-0420/
from base import Base
# in this new version we cannot depend on Model to be preformed
# from model import Model
from typing import Optional, Dict
from util import Log, set_dataframe
from population import Population


class PopulationDict(Population):
    """Population Data Readers.

    Reads the population data. The default is to read from the model.data
    """
    # no variable here unless you want them the same across all instances

    def __init__(
        self,
        # model: Model,
        log_root: Optional[Log] = None,
        source: Dict = None,
        label: Dict = None,
        index: str = None,
        columns: str = None,
    ):
        """Initialize the population object.

        This uses the Frame object and populates it with default data unless yo
        override it
        """
        # https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init/7059529
        super().__init__()

        # https://stackoverflow.com/questions/35328286/how-to-use-numpy-in-optional-typing
        self.attr_pd_arr: Optional[np.ndarray] = None
        self.attr_pd_df: Optional[pd.DataFrame] = None

        # create a sublogger if a root exists in the model
        # self.model: Model = model
        if log_root is not None:
            self.log_root: Log = log_root
            log = log_root.log_class(self)
            # breakpoint()
            log.debug(f"{log_root=}, {log_root.con=}")
            self.log_root.con.setLevel(logging.DEBUG)
            log.debug(f"in {__name__=}")
            self.log_root.con.setLevel(logging.WARNING)
        else:
            log = logging.getLogger(__name__)
            log.debug(f"no log_root using {log=}")
            raise ValueError("log_root is null")
        self.log = log

        # the sample code to move up the logging for a period and then turn it
        # off

        log.debug(f"{source=}")

        # we just use one dimension of source
        # if source is not None:
        #     self.data_arr = np.array(source['Size'])
        #     log.debug(f"{type(self.data_arr)=}")
        # why is this here?
        # if index is not None and columns is not None:
        #     self.data_df = set_dataframe(
        #         self.data_arr,
        #        label=label,
        #        index=index,
        #        columns=columns
        #    )
        # this check is here to make the type checker happy.
        if label is None:
            raise ValueError(f"{label=} is null")
        self.attr_pd_arr = source
        self.attr_pd_df = set_dataframe(
            self.attr_pd_arr,
            label=label,
            index=index,
            columns=columns,
        )

        log.debug(f"{self.attr_pd_df=}")
        log.debug(f"{self.attr_pd_df.index.name=}")
        log.debug(f"{self.attr_pd_df.columns.name=}")
