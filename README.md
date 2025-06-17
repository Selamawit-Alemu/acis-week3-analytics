# acis-week3-analytics
# 📊 Insurance Risk Segmentation & Predictive Pricing

This project explores insurance policy data to uncover risk patterns, segment customers, and build a dynamic, risk-based premium pricing model. The workflow includes rigorous EDA, statistical validation, and predictive modeling — all tracked via Git and DVC for full auditability and reproducibility.

---

## 🔍 Project Objectives

- Identify low-risk market segments through exploratory and statistical analysis.
- Use DVC for reproducible, version-controlled workflows.
- Build predictive models for claim severity and premium optimization.
- Derive business insights to support risk-adjusted pricing strategies.

---

## 🗂️ Repository Structure

```bash
    .
    ├── .dvc/                        # DVC tracking configuration
    ├── .github/workflows/          # CI/CD workflows
    ├── config/                     # Configuration files
    ├── data/                       # Input data (DVC-tracked)
    ├── notebooks/                  # Jupyter notebooks (e.g., for data cleaning)
    │   └── 1-data-cleaning.ipynb
    ├── plots/                      # Visualizations (auto-generated or EDA plots)
    │   ├── TotalClaims_distribution.png
    │   └── TotalPremium_distribution.png
    ├── reports/                    # Task reports and markdown summaries
    │   └── task_3_summary.md
    ├── scripts/                    # Modular Python scripts
    │   ├── data_utils.py
    │   ├── eda_quality_univariate.py
    │   ├── eda_descriptive_stats.py
    │   ├── eda_bivariate_multivariate.py
    │   ├── eda_summary.py
    │   ├── task3_Statistical_Testing.py
    │   ├── task_3_hypothesis_testing.py
    │   ├── task_3_segmentation_analysis.py
    │   └── visualization.py
    ├── test/                       # Unit tests
    │   └── test.py
    ├── README.md                   # 📌 You are here
    ├── requirements.txt            # Project dependencies
    └── .gitignore / .dvcignore     # Ignore rules for Git/DVC

🧪 Completed Tasks & Progress
Task	Description	Branch
Task 1	Data Cleaning & EDA Initialization	task-1
Task 2	Thematic & Sentiment Analysis (for ACIS)	task-2
Task 3	Statistical Validation & Risk Segmentation	task-3
Task 4	🚧 Predictive Modeling (in progress)	task-4

    ✅ All datasets are version-controlled with DVC. Tasks are modularized into scripts under scripts/ and documented via markdown under reports/.

⚙️ DVC Workflow

    Initialized: dvc init

    Remote Setup: Local remote configured for tracking artifacts.

    Tracked Files: data/MachineLearningRating_v3.txt.dvc

    Pipeline: Scripts are modularized and reproducible through DVC-tracked inputs/outputs.

    Auditability: Enables full lineage tracking of data and model files.

📊 Data Visualizations

The following plots are available under plots/ and generated via scripts/visualization.py:

    Claim frequency & severity distributions

    Premium margin distributions

    Outlier detection via boxplots

    Province/ZipCode level segmentation charts

Each visualization is annotated and tied to specific EDA/statistical insights.
🧠 Key Insights (from Task 3)

    Provinces and Zip Codes show statistically significant differences in claim frequency → supports geographic segmentation.

    Tracking Device presence correlates with higher claim severity, suggesting potential risk exposure among high-value assets.

    Gender data is incomplete; not reliable for segmentation.

    Margin does not significantly differ by location, suggesting uniform profitability across regions.

Full findings available in reports/task_3_summary.md
📊 Tasks 3 & 4 Summary
In Task 3, I conducted hypothesis testing to explore risk segmentation across customer demographics and regions. Key insights included statistically significant differences in claim frequency and severity by gender and province. Task 4 focused on building predictive models for claim severity and premium optimization. I experimented with Decision Trees, Random Forests, and XGBoost, evaluating performance using RMSE and R². SHAP was applied for model interpretability, and the insights were used to propose a risk-based pricing strategy.

Full findings available in reports/task_4_summary.md

📦 Setup Instructions

    # Clone the repository
    git clone https://github.com/yourusername/insurance-risk-segmentation.git
    cd insurance-risk-segmentation

    # Create virtual environment
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

    # Install dependencies
    pip install -r requirements.txt

    # Pull data using DVC
    dvc pull   
        
    Usage Guide

Add after Setup Instructions:
---

## 🔄 Usage Guide

After setup, you can run various analysis stages using modular scripts.

### Run Exploratory Data Analysis

```bash
python scripts/eda_summary.py

ther scripts:

    eda_quality_univariate.py: Missing values & univariate checks

    eda_bivariate_multivariate.py: Relationships across features

    task_3_hypothesis_testing.py: Statistical testing on risk metrics

Each script contains inline documentation and can be executed independently or imported as a module.
Generate Visualizations

python scripts/visualization.py
This generates updated plots in the plots/ directory.
🧪 Running Tests

python test/test.py

This will run unit tests on data utility functions (e.g., null checks, custom encoders) to ensure EDA and preprocessing code functions reliably.


---

#### 📄 **Clarify Tasks Done (Update Completed Tasks Table)**

Modify the "Completed Tasks" section to clarify **implementation scope**, e.g.:

```markdown
| Task | Description | Branch |
|------|-------------|--------|
| Task 1 | Data Cleaning: Handled missing values, performed univariate analysis | `task-1` |
| Task 2 | Bivariate/Multivariate EDA, Visualizations | `task-2` |
| Task 3 | Statistical testing for segmentation & loss ratio analysis | `task-3` |
| Task 4 | 🚧 Risk-Based Pricing Models: Regression & Classification (in progress) | `task-4` |

📘 Script Documentation (New Section to Mention)

Add a sentence in the “Repository Structure” or new “Documentation” section like:

All Python scripts in the `scripts/` directory are modular and include:
- Function-level docstrings
- Inline comments for assumptions
- Reusable structures to enable pipeline integration

