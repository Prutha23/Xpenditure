# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, r2_score
# from repository import expense_db
# from datetime import datetime, timedelta
# from flask import request, make_response
# from flask.json import jsonify
# from main import app
# from repository import expense_db
# from utils.auth import admin_required, abort
#
# # Fetch data
# obj = expense_db.ExpenseDB()
# data = obj.get_expense_data_for_prediction()
#
# # Preprocess data
# X = data.drop(columns=['Expense_ID', 'Amount', 'User_Email'])
# y = data['Amount']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Define preprocessing pipeline
# numeric_features = ['User_ID', 'Expense_Date']
# categorical_features = ['Category_ID', 'Category_Name', 'Is_Premium']
#
# numeric_transformer = StandardScaler()
# categorical_transformer = OneHotEncoder(handle_unknown='ignore')
#
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', numeric_transformer, numeric_features),
#         ('cat', categorical_transformer, categorical_features)
#     ])
#
# # Train model
# model = Pipeline(steps=[('preprocessor', preprocessor),
#                         ('regressor', RandomForestRegressor())])
# model.fit(X_train, y_train)
#
# # Evaluate model
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
#
# print(f'Mean Squared Error: {mse:.2f}')
# print(f'R^2 Score: {r2:.2f}')
#
#
# # Assuming today's date
# today = datetime.today()
#
# # Creating next month's dates (30 days into the future)
# next_month_dates = [today + timedelta(days=i) for i in range(1, 31)]
#
# # Generate the new dataset for prediction
# user_ids = data['User_ID'].unique()
# categories = data[['Category_ID', 'Category_Name']].drop_duplicates()
#
# # Create a new DataFrame with all possible combinations of User_ID and Category_ID for the next month
# new_data = pd.DataFrame(index=pd.MultiIndex.from_product([user_ids, categories['Category_ID']],
#                                                           names=['User_ID', 'Category_ID'])).reset_index()
# new_data = pd.merge(new_data, categories, on='Category_ID', how='left')
#
# # Add Is_Premium information
# new_data = new_data.merge(data[['User_ID', 'Is_Premium']].drop_duplicates(), on='User_ID', how='left')
#
# # Create a DataFrame for each date in the next month and concatenate them
# future_expenses = []
#
# for date in next_month_dates:
#     temp_df = new_data.copy()
#     temp_df['Expense_Date'] = date
#     future_expenses.append(temp_df)
#
# future_expenses_df = pd.concat(future_expenses, ignore_index=True)
#
# # Predict next month's expenses
# next_month_predictions = model.predict(future_expenses_df.drop(columns=['Category_Name']))
# future_expenses_df['Predicted_Amount'] = next_month_predictions
#
# # API for GET call for next month predictions
# @app.route("/api/reports/predictions", methods=["GET"])
# @admin_required
# def get_expense_by_user_type():
#     try:
#         res = next_month_predictions.to_dict(orient='records')
#         if res:
#             return make_response(jsonify({
#                 "statusCode": 200,
#                 "status": "Success",
#                 "message": "Success",
#                 "data": res
#             }))
#     except Exception as err:
#         app.logger.error("Exception in Next Month Predictions : %s", err)
#         abort(500)