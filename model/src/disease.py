# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
import logging
import pandas as pd
import numpy as np
from base import Base
from model import Model

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.WARNING)


class Disease(Base):
    """Resource - Manages all the resources that are used in the model
    This creates for all r resources, the list of attributes a

    This contains
    This uses https://realpython.com/documenting-python-code/
    docstrings using the NumPy/SciPy syntax
    Uses a modified standard project
    Uses https://www.sphinx-doc.org/en/master/ to generate the documentation
    """
    def __init__(self, model: Model):
        """Initialize the Disease object

        This uses the Frame object and populates it with default data unless yo
        override it
        """
        # https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init/7059529
        super().__init__()
