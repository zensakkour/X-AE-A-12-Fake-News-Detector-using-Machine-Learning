import pandas as pd
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
test = os.path.dirname(os.path.realpath(__file__))
src = os.path.dirname(test)
root = os.path.dirname(src)
sys.path.append(src)
sys.path.append(root)

import Machine_Learning as ML

train_data_file = os.path.abspath(os.path.join(root, 'data','LIAR.csv'))
partial_train = os.path.abspath(os.path.join(root, 'data','pytest_data', 'partial_train.csv'))
partial_test = os.path.abspath(os.path.join(root, 'data', 'pytest_data','partial_test.csv'))



def test_full_data_accuracy():
    """
    Test the accuracy of the 'predict_on_database' function on the full test dataset.
    """
    ML.MIN_PROB=0.1
    # Load the full training dataset
    df_Full_test = pd.read_csv(train_data_file)
    df_Full_test_COMP = df_Full_test.copy()

    # Use the 'predict_on_database' function to predict fake news labels and probabilities
    predicted_full_test_df = ML.predict_on_database(df_Full_test, train_data_file)

    # Calculate accuracy on full test data
    accuracy_full_test = accuracy_score(predicted_full_test_df["fake_value"], df_Full_test_COMP["fake_value"])

    # Print the accuracy
    print(f"Accuracy on full test data: {accuracy_full_test*100}%")
    ML.MIN_PROB=0.4
    # Assert that the accuracy is within an acceptable range 
    assert 0.5 <= accuracy_full_test <= 1.0

def test_partial_data_accuracy():
    """
    Test the accuracy of the 'predict_on_database' function on the partial test dataset.
    """
    # Load the full training dataset
    df_Full_test = pd.read_csv(train_data_file)
    ML.MIN_PROB=0.1
    # Split the training dataset into train and test sets
    partial_train_df, partial_test_df = train_test_split(df_Full_test, test_size=0.8)
    partial_test_df_COMP = partial_test_df.copy()
 

    partial_train_df.to_csv(partial_train, index=False)
    partial_test_df.to_csv(partial_test, index=False)

    # Use the 'predict_on_database' function to predict fake news labels and probabilities on the partial test dataset
    predicted_partial_test_df = ML.predict_on_database(partial_test_df, partial_train)

    # Calculate accuracy on partial test data
    accuracy_partial_test = accuracy_score(predicted_partial_test_df["fake_value"], partial_test_df_COMP["fake_value"])
    ML.MIN_PROB=0.4
    # Print the accuracy
    print(f"Accuracy on partial test data: {accuracy_partial_test*100}%")

    # Assert that the accuracy is within an acceptable range 
    assert 0.4 <= accuracy_partial_test <= 1.0


test_full_data_accuracy()
test_partial_data_accuracy()