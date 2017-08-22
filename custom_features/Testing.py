import numpy as np
import copy
from FeatureOperations import FeatureNormalization, FeatureIO
__author__ = "Tam Mayeshiba"

class Testing():
    """Class for creating custom feature columns.
        New methods may be added.

    Args:
        dataframe <data object>

    Returns:
    Raises:
        ValueError if dataframe is None
    """
    def __init__(self, dataframe=None):
        """Custom data handler
            
        Attributes:
            self.original_dataframe <data object>: Dataframe
            self.df <data object>: Dataframe

        Each custom feature should take a parameter dictionary, with integers
            as keys starting from zero, followed by keyword arguments.
        """
        if dataframe is None:
            raise ValueError("No dataframe.")
        self.original_dataframe = copy.deepcopy(dataframe)
        self.df = copy.deepcopy(dataframe)
        return

    def subtraction(self, params=dict(), col1="",col2=""):
        """Testing function.
            params[0]: first parameter
            params[1]: second parameter
            col1 <str>: first feature name
            col2 <str>: second feature name
        """
        col1_data = self.df[col1]
        col2_data = self.df[col2]
        new_data = (col1_data * params[0]) - col2_data + params[1]
        fio = FeatureIO(self.df)
        new_df = fio.add_custom_features(["Subtraction_test"],new_data)
        fnorm = FeatureNormalization(new_df)
        N_new_data = fnorm.minmax_scale_single_feature("Subtraction_test")
        return N_new_data

