import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,filename=r"D:\Breast_cancer project\log\logs")
project_name='Breast_cancer'



list_of_files =[
    # ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_tranier.py",
    
    f"src/pipeline/__init__.py",
    f"src/pipeline/predict_pipeline.py",
    f"src/pipeline/train_pipeline.py",
    f"src/exception.py",
    f"src/logger.py",
    f"src/utils.py",
    "import_data.py",
    "setup.py",
    "app.py",
    "notebook/model.ipynb",
    "notebook/EDA.ipynb",
    "requirements.txt",
    ".gitignore",
    "README.md",
    "LICENSE"
        
    
]


for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename= os.path.split(filepath)  
    
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
        
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
        
        
        
    else:
        logging.info(f"{filename} is already exists")    
        
        