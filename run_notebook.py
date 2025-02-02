import papermill as pm

# Define notebook paths
input_notebook = "../preprocess_notebook.ipynb"
output_notebook = "../preprocess_output_notebook.ipynb"

# Execute the Jupyter Notebook
pm.execute_notebook(input_notebook, output_notebook)