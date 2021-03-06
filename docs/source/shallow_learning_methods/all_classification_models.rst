*********************************
Running All Classification Models
*********************************

If you are having trouble picking a model (or are simply curious about how each model compares), ManufacturingNet provides
a simple way to train all supported classification models on one dataset.

ManufacturingNet.models' **AllClassificationModels** class trains the following models on your dataset with default parameters:

- Logistic Regression
- Random Forest
- SVC
- NuSVC
- LinearSVC
- XGBoost

*AllClassificationModels(attributes=None, labels=None)*

Parameters
==========

When initializing an AllClassificationModels object, the following parameters need to be passed:

- **attributes** *(numpy array, default=None)*: A numpy array of the values of the independent variable(s).
- **labels** *(numpy array, default=None)*: A numpy array of the values of the dependent variable.

When the run() method is called, the following parameters can be modified:

- **test_size** *(float, default=0.25)*: The proportion of the dataset to be used for testing the model; the proportion of the dataset to be used for training will be the complement of test_size.
- **verbose** *(boolean, default=False)*: Determines whether logs are outputted during model training and testing.

Note: All model-specific parameters are kept as their defaults for simplicity. For more control over each model, use their
corresponding classes in ManufacturingNet.models.

Attributes
==========

- **logistic_regression** *(model)*: The underlying logistic regression model.
- **random_forest** *(model)*: The underlying random forest model.
- **SVC** *(model)*: The underlying SVC model.
- **nu_SVC** *(model)*: The underlying NuSVC model.
- **linear_SVC** *(model)*: The underlying LinearSVC model.
- **XGB_regressor** *(model)*: The underlying XGBoost model.

Methods
=======

- **run()**: Prompts for parameter input, instantiates and runs all of the above models, and outputs their results. For each model, the accuracy, five-fold cross validation score, and execution time are reported.

Accessor Methods
----------------

- **get_attributes()**: Returns attributes.
- **get_labels()**: Returns labels.

Note: If attributes wasn't passed in during initialization, get_attributes() will return None. Likewise, if labels
wasn't passed in during initialization, get_labels() will return None.

- **get_all_classification_models()**: Returns a list of all of the classification models.
- **get_logistic_regression()**: Returns logistic_regression.
- **get_random_forest()**: Returns random_forest.
- **get_SVC()**: Returns SVC.
- **get_nu_SVC()**: Returns nu_SVC.
- **get_linear_SVC()**: Returns linear_SVC.
- **get_XGB_regressor()**: Returns XGB_regressor.

Note: If run() hasn't successfully executed yet, the above accessor methods will return None.

Modifier Methods
----------------

- **set_attributes(new_attributes=None)**: Sets attributes to new_attributes. If new_attributes isn't specified, attributes is set to None.
- **set_labels(new_labels=None)**: Sets labels to new_labels. If new_labels isn't specified, labels is set to None.

Example Usage
=============

.. code-block:: python
    :linenos:

    from ManufacturingNet.models import AllClassificationModels
    from pandas import read_csv

    dataset = read_csv('/path/to/dataset.csv')
    dataset = dataset.to_numpy()
    attributes = dataset[:, 0:5]                    # Columns 1-5 contain our features
    labels = dataset[:, 5]                          # Column 6 contains our class labels
    all_classification_models = AllClassificationModels(attributes, labels)
    all_classification_models.run()                 # This will trigger the command-line interface for parameter input
                                                    # And output each model's accuracy, five-fold cross validation score, and execution time