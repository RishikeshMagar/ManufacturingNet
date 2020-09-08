from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
import numpy as np

class LogisticRegression: 
    
    """
    Wrapper class around scikit-learn's logistic regression functionality.

    Logistic Regression is a type of Generalized Linear Model (GLM) that uses a logistic function to model a binary 
    variable based on any kind of independent variables.
    """


    def __init__(self, attributes=None, labels=None, test_size=0.25, penalty='l2', dual=False, \
                    tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, \
                        solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None):
        

        """
        Initializes a LogisticRegression object.

        The following parameters are needed to create a logistic regression model:

            - attributes: a numpy array of the desired independent variables
            - labels: a numpy array of the desired dependent variables
            - test_size: the proportion of the dataset to be used for testing the model (defaults to 0.25);
            the proportion of the dataset to be used for training will be the complement of test_size
            - fit_intercept: specifies if a constant (a.k.a. bias or intercept) should be added to the decision function. (defaults to True)
            - intercept_scaling: used only when the solver ‘liblinear’ is used and self.fit_intercept is set to True. Here, x becomes [x, self.intercept_scaling], 
            i.e. a “synthetic” feature with constant value equal to intercept_scaling is appended to the instance vector.
            - class_weight: weights associated with classes (defaults to None). If set to 'balanced' then the values of y are used 
             to automatically adjust weights inversely proportional to class frequencies in the input data.
            - random_state: used when solver == ‘sag’, ‘saga’ or ‘liblinear’ to shuffle the data (defaults to None)
            - solver: chooses the algorithm for the optimization problem, (defaults to lbfgs)
            - max_iter: maximum number of iterations taken for the solvers to converge (defaults to 100)
            - multi_class: chooses if we fit a binary problem or a multi-class problem for each label (defaults to auto)
            - verbose: used in the liblinear or lbfgs solvers, where any positive number is set (defaults to 0)
            - warm_start: when set to true, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution (defaults to False)
            - n_jobs: the number of jobs to use for the computation (defaults to None)
            - l1_ratio: this is the Elastic-Net mixing parameter. Setting this to 0 is using l2 penalty, setting this to
            1 is using l1_penalty and a value between 0 and 1 is a combination of l1 and l2. 

        The following instance data is found after successfully running linear_regression():

            - regression: the logistic regression model
            - coefficients: an array of coefficients that most closely satisfy the linear relationship between the
            independent and dependent variables
            - intercept: the y-intercept of the regression line generated by the model
            - classes: a list of class labels known to the classifier
            - n_iter : Actual number of iterations for all classes
            - accuracy: the classification accuracy score
            - roc_auc: the area under the receiver operating characteristic curve from the prediction scores
        """

        self.attributes = attributes
        self.labels = labels

        self.test_size = test_size
        self.penalty = penalty
        self.dual = dual
        self.tol = tol
        self.C = C

        self.fit_intercept = fit_intercept
        self.intercept_scaling = intercept_scaling
        self.class_weight = class_weight

        self.random_state = random_state
        self.solver = solver
        self.max_iter = max_iter
        self.multi_class = multi_class

        self.verbose = verbose
        self.warm_start = warm_start
        self.n_jobs = n_jobs
        self.l1_ratio = l1_ratio

        self.regression = None
        self.classes_ = None
        self.coef_ = None
        self.intercept_ = None
        self.n_iter_ = None

        self.accuracy = None
        self.precision = None
        self.recall = None
        self.roc_auc = None

    # Accessor methods

    def get_attributes(self):
        """
        Accessor method for attributes.

        If a LogisticRegression object is constructed without specifying attributes, attributes will be None.
        logistic_regression() cannot be called until attributes is a populated numpy array; call
        set_attributes(new_attributes) to fix this.
        """
        return self.attributes

    def get_labels(self):
        """
        Accessor method for labels.

        If a LogisticRegression object is constructed without specifying labels, labels will be None.
        logistic_regression() cannot be called until labels is a populated numpy array; call set_labels(new_labels)
        to fix this.
        """
        return self.labels

    def get_classes(self):
        """
        Accessor method for classes.

        Will return None if logistic_regression() hasn't been called, yet.
        """
        return self.classes

    def get_regression(self):
        """
        Accessor method for regression.

        Will return None if logistic_regression() hasn't been called, yet.
        """
        return self.regression

    def get_coefficents(self):
        """
        Accessor method for coefficients.

        Will return None if logistic_regression() hasn't been called, yet.
        """
        return self.coef_

    def get_n_iter_(self):
        """
        Accessor method for number of iterations for all classes.

        Will return None if logistic_regression() hasn't been called, yet.
        """
        return self.n_iter_

    def get_accuracy(self):
        """
        Accessor method for accuracy.

        Will return None if logistic_regression() hasn't been called, yet.
        """
        return self.accuracy

    def get_roc_auc(self):
        """
        Accessor method for roc-auc score.

        Will return None if logistic_regression() hasn't been called, yet.
        """
        return self.roc_auc

    # Modifier methods

    def set_attributes(self, new_attributes = None):
        """
        Modifier method for attributes.

        Input should be a populated numpy array of the desired independent variables.
        """
        self.attributes = new_attributes

    def set_labels(self, new_labels = None):
        """
        Modifier method for labels.

        Input should be a populated numpy array of the desired dependent variables.
        """
        self.labels = new_labels

    def set_test_size(self, new_test_size = None):
        """
        Modifier method for test_size.

        Input should be a number or None.
        """
        self.test_size  = new_test_size


    # Wrapper for logistic regression model

    def logistic_regression(self):
        """
        Performs logistic regression on dataset using scikit-learn's logistic_model and returns the resultant array of
        coefficients.
        """
        if self._check_inputs():
            # Instantiate LogisticRegression() object
            self.regression = LogisticRegression(penalty=self.penalty, dual=self.dual, tol=self.tol, \
                C=self.C, fit_intercept=self.fit_intercept, intercept_scaling=self.intercept_scaling, class_weight=self.class_weight, \
                    random_state=self.random_state, solver=self.solver, max_iter=self.max_iter, multi_class=self.multi_class, \
                        verbose=self.verbose, warm_start=self.warm_start, n_jobs=self.n_jobs, l1_ratio=self.l1_ratio)

            # Split into training and testing set
            dataset_X_train, dataset_X_test, dataset_y_train, dataset_y_test = \
                train_test_split(self.attributes,self.labels,test_size=self.test_size)

            # Train the model and get resultant coefficients; handle exception if arguments are incorrect
            try:
                self.regression.fit(dataset_X_train, np.ravel(dataset_y_train))
            except Exception as e:
                print("An exception occurred while training the logistic regression model. Check your inputs and try again.")
                print("Here is the exception message:")
                print(e)
                self.regression = None
                return

            # Get resultant coefficients and intercept of regression line
            self.classes_ = self.regression.classes_
            self.coefficients = self.regression.coef_
            self.intercept = self.regression.intercept_
            self.n_iter_ = self.regression.n_iter_


            # Make predictions using testing set
            y_prediction = self.regression.predict(dataset_X_test)
            y_pred_probas = self.regression.predict_proba(dataset_X_test)[::, 1]

            #Metrics
            self.accuracy = accuracy_score(y_prediction, dataset_y_test)
            self.roc_auc = roc_auc_score(y_prediction, y_pred_probas)


    # Helper method for checking inputs

    def _check_inputs(self):
        """
        Verifies if the instance data is ready for use in logistic regression model.
        """

        # Check if attributes exists
        if self.attributes is None:
            print("attributes is missing; call set_attributes(new_attributes) to fix this! new_attributes should be a",
            "populated numpy array of your independent variables.")
            return False

        # Check if labels exists
        if self.labels is None:
            print("labels is missing; call set_labels(new_labels) to fix this! new_labels should be a populated numpy",
            "array of your dependent variables.")
            return False

        # Check if attributes and labels have same number of rows (samples)
        if self.attributes.shape[0] != self.labels.shape[0]:
            print("attributes and labels don't have the same number of rows. Make sure the number of samples in each",
                  "dataset matches!")
            return False

        # Check if test_size is a float or None
        if self.test_size is not None and not isinstance(self.test_size, (int, float)):
            print("test_size must be None or a number; call set_test_size(new_test_size) to fix this!")
            return False

        return True
