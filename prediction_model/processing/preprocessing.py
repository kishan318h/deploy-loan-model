import os
import sys
from pathlib import Path
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


## __file__ stores the path of the current directory
## going the grandparent directory
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))


## since we have added the path of ROOT folder to sys.path,
## we can import the config file
from prediction_model.config import config


# adding assest columns
class DomainProcessing(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_add=None):
        self.variables_to_add = variables_to_add
        self.new_column = config.NEW_FEATURE_ADD

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X[self.new_column] = X[self.variables_to_add].sum(axis=1)
        return X
    

# drop column
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.drop(columns=self.variables_to_drop)
        return X
    

# customer label encoder
class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        for col_name, positive_value in self.variables.items():
            X[col_name] = X[col_name].apply(
                lambda x:1 if x.strip() in positive_value else 0
            )
        return X
    

# log transformer
class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X=X.copy()
        for colname in self.variables:
            X[colname] = np.log(X[colname])
        return X
