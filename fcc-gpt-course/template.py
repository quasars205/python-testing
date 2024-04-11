import os
from pathlib import Path
list_of_files = [
    ".github/workflows",
    "src/__init_.py",
    "src/components/data_ingestion.py",
    "src/componenents/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evalaution.py"
    "src/pipeline/__init.py__",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "test/units/__init__.py",
    "test/integratin/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirments_dev.txt",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiment.ipynb"
    
    
    ]
    
for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        if filedir != "":
          os.makedirs(filedir, exist_ok=True)

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass # create an empty file