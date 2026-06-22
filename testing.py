import sys
import time

try:
    import numpy as np
    import pandas as pd
    
    print("=" * 50)
    print("SUCCESS: Environment is configured correctly!")
    print("=" * 50)
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"NumPy Version:  {np.__version__}")
    print(f"Pandas Version: {pd.__version__}")
    print("-" * 50)

    # 1. Test NumPy Utilization (Matrix Multiplication)
    print("Testing NumPy performance...")
    start_time = time.time()
    # Create two large 2000x2000 random matrices
    matrix_a = np.random.rand(2000, 2000)
    matrix_b = np.random.rand(2000, 2000)
    # Perform dot product to utilize CPU/RAM
    np.dot(matrix_a, matrix_b)
    numpy_time = time.time() - start_time
    print(f"-> NumPy successfully processed heavy matrix math in {numpy_time:.4f} seconds.")

    # 2. Test Pandas Utilization (Dataframe Manipulation)
    print("\nTesting Pandas performance...")
    start_time = time.time()
    # Create a DataFrame with 1 million rows
    df = pd.DataFrame({
        'A': np.random.randn(1000000),
        'B': np.random.choice(['Group1', 'Group2', 'Group3'], size=1000000)
    })
    # Perform an aggregation operation
    summary = df.groupby('B').mean()
    pandas_time = time.time() - start_time
    print(f"-> Pandas successfully aggregated 1,000,000 rows in {pandas_time:.4f} seconds.")
    print("-" * 50)
    print("Status: Both libraries are fully functional and utilizing your machine hardware.")
    print("=" * 50)

except ImportError as e:
    print("=" * 50)
    print("ERROR: Missing dependencies!")
    print("=" * 50)
    print(f"Details: {e}")
    print("\nMake sure you have selected the correct interpreter in VS Code.")
    print("You can install them by running this in your terminal:")
    print("pip install numpy pandas")
    print("=" * 50)







    import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Generate random data using NumPy
np.random.seed(42)
x = np.random.rand(50, 1) * 10
y = 2.5 * x + np.random.randn(50, 1) * 2

# 2. Put it into a Pandas DataFrame
df = pd.DataFrame({'Feature': x.flatten(), 'Target': y.flatten()})
print("Sample Data:\n", df.head())

# 3. Train a Machine Learning Model using Scikit-Learn
model = LinearRegression()
model.fit(df[['Feature']], df['Target'])
predictions = model.predict(df[['Feature']])

# 4. Plot the results using Matplotlib
plt.scatter(df['Feature'], df['Target'], color='blue', label='Actual Data')
plt.plot(df['Feature'], predictions, color='red', linewidth=2, label='ML Prediction Line')
plt.title('Your Machine Learning Stack is Working!')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show()
