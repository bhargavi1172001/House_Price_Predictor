import pandas as pd
from train import train_model




def predict_new():
model = train_model()


new_house = pd.DataFrame({
'area': [3039],
'bedrooms': [3],
'bathrooms': [3],
'stories': [4],
'mainroad': [1],
'guestroom': [1],
'basement': [0],
'hotwaterheating': [0],
'airconditioning': [1],
'parking': [1],
'prefarea': [0],
'furnishingstatus': [2]
})


prediction = model.predict(new_house)
print("Predicted Price:", prediction[0])




if __name__ == "__main__":
predict_new()
