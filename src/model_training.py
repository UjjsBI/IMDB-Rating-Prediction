from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

def train_gradient_boosting(X_train, y_train):
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5],
        'learning_rate': [0.01, 0.05]
    }
    grid = GridSearchCV(GradientBoostingRegressor(), param_grid, cv=5, scoring='r2')
    grid.fit(X_train, y_train)
    return grid.best_estimator_

