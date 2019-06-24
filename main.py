import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from dataloader import load

def main():
    samples = []
    load(samples)

    space_groups = {}
    for i in samples:
        grp = i.space_group
        if (grp in space_groups): space_groups[grp] += 1
        else: space_groups[grp] = 1
    print(len(space_groups))

    X = []
    y = []
    for i in samples:
        X_temp = i.image_stack
        X.append(X_temp)
        y_temp = i.space_group
        y.append(y_temp)
    X = np.array(X)
    y = np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(3, 512, 512)),
        keras.layers.Dense(1000, activation=tf.nn.relu),
        keras.layers.Dense(231, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam', 
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=3)

    test_loss, test_acc = model.evaluate(X_test, y_test)
    print('Test accuracy:', test_acc)

if __name__ == "__main__":
    main()