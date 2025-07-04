Getting Started: Setup Instructions
======================================================

To follow this tutorial and run the provided code examples successfully, please go through the following steps.

1. Create a Tutorial Folder
----------------------------

Open a terminal window (on **Windows**, use *Command Prompt* or *PowerShell*; on **macOS/Linux**, use *Terminal*), and type:

.. code-block:: bash

    mkdir marsh_tutorial
    cd marsh_tutorial

This will create a folder called ``marsh_tutorial/`` and set it as your working directory.

2. Download the Model Input Data
---------------------------------

Download the model input data from the following link:

`model_input_X_L.zip <https://github.com/christineschottmueller/x-marsh/releases/download/v1.0-data/model_input_X_L.zip>`_

Extract the archive so that the folder ``model_input_X_L`` is located inside ``marsh_tutorial/``.

You can extract the archive using your operating system's file manager, or with the command line:

.. code-block:: bash

    unzip model_input_X_L.zip

3. Create an Output Folder
---------------------------

To store the results of your model runs, create a folder called ``model_output_M``:

.. code-block:: bash

    mkdir model_output_M

4. Verify Folder Structure
---------------------------

Your folder structure should now look like this:

.. code-block:: none

    marsh_tutorial/
    ├── model_input_X_L/
    │   ├── tidal_projections/
    │   └── regional_slr_single_rcp/
    ├── model_output_M/
    └── your_notebook.ipynb

5. Run the Jupyter Notebook
----------------------------

Launch your Jupyter Notebook **from within the** ``marsh_tutorial/`` **folder**. This ensures that all file paths used in the tutorial will resolve correctly.

You can confirm your working directory in the notebook by running:

.. code-block:: python

    import os
    print(os.getcwd())

If needed, you can change the working directory:

.. code-block:: python

    os.chdir('path/to/marsh_tutorial/')
