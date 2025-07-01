
# 🎬 IMDb Rating Prediction Project

IMDb rating prediction using machine learning models (Gradient Boosting, Random Forest, CatBoost). Includes model comparison, feature importance, and performance evaluation with hyperparameter tuning.
## 📊 Models Evaluated

| Model             | R² Score |
|------------------|----------|
| Gradient Boosting| 0.685    |
| Random Forest    | 0.653    |
| CatBoost         | 0.612    |

## 📁 Project Structure
notebooks/ ← Jupyter notebook with full code
data/ ← (Optional) Raw or cleaned dataset
src/ ← Python scripts for modular ML pipeline
models/ ← Trained model pickle files
outputs/ ← Plots and evaluation results


## 📦 Setup

```bash
pip install -r requirements.txt

📈 Insights

rank had ~89% importance in predictions.
Gradient Boosting performed best after tuning.
CatBoost handled categorical columns directly.


