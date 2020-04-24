from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
import numpy


numpy.random.seed(2)
diabetescsv = numpy.loadtxt("c.csv", delimiter=",")
inputs = diabetescsv[:,0:8]
final = diabetescsv[:,8]
inputs_train, inputs_test, final_train, final_test = train_test_split(inputs, final, test_size=0.2, random_state=42)
model = Sequential()
model.add(Dense(15, input_dim=8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(1, activation='sigmoid')) 

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
model.fit(inputs_train, final_train, epochs = 1000, batch_size=20, validation_data=(inputs_test, final_test))
model.save('output.h5')

