# streamli_test


Streamli_test/
│── data/                                   # Raw and processed datasets
│   ├── raw/                                # Unprocessed data
│   ├── processed/                          # Cleaned and transformed data
│
│── src/                                    # Source code for ML pipeline
│   ├── data_loader.py                      # Data loading and preprocessing
|   ├── eda_process.py                      # eda processing             
|   ├── preprocessing.py                    # preprocessing
│   ├── model.py                            # Model definition
│   ├── train.py                            # Training script
│   ├── inference.py                        # Inference script
│
│── models/                                 # Saved model checkpoints
│   ├── model_v1.pkl     
│   ├── model_v2.pth     
│
│── tests/                                  # Unit tests for code validation
│   ├── test_data_loader.py
│   ├── test_model.py
│
│── config/                                 # Configuration files
│   ├── config.yaml                         # Model & pipeline configurations
│   ├── params.json                         # Hyperparameters
│
│── logs/                                   # Training and debugging logs
│
│── reports/                                # Reports and documentation
│   ├── metrics.json                        # Model performance metrics
│   ├── experiment_notes.md
│
│── .github/                                # GitHub Actions for CI/CD
│   ├── workflows/
│       ├── ci.yml                          # Continuous Integration pipeline
│
│── .gitignore                              # Ignore unnecessary files (e.g., data, logs)
│── README.md                               # Project documentation
│── requirements.txt                        # Python dependencies
│── environment.yml                         # Conda environment file
│── Dockerfile                              # Docker containerization
│── Makefile                                # Automate commands
