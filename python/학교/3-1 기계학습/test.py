import tensorflow as tf

# tf.keras.utils.set_random_seed(42)
# tf.config.experimental.enable_op_determinism()

from tensorflow import keras

(
    (train_input, train_target),
    (test_input, test_target,),
) = keras.datasets.fashion_mnist.load_data()

from sklearn.model_selection import train_test_split

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28 * 28)

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42
)


dense1 = keras.layers.Dense(100, activation="sigmoid", input_shape=(784,))
dense2 = keras.layers.Dense(10, activation="softmax")

model = keras.Sequential([dense1, dense2])
model.summary()

model = keras.Sequential(
    [
        keras.layers.Dense(
            100, activation="sigmoid", input_shape=(784,), name="hidden"
        ),
        keras.layers.Dense(10, activation="softmax", name="output"),
    ],
    name="패션 MNIST 모델",
)

model.summary()

model = keras.Sequential()
model.add(keras.layers.Dense(100, activation="sigmoid", input_shape=(784,)))
model.add(keras.layers.Dense(10, activation="softmax"))

model.summary()

model.compile(loss="sparse_categorical_crossentropy", metrics="accuracy")

model.fit(train_scaled, train_target, epochs=5)

model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))

model.summary()

(
    (train_input, train_target),
    (test_input, test_target,),
) = keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42
)

model.compile(loss="sparse_categorical_crossentropy", metrics="accuracy")

model.fit(train_scaled, train_target, epochs=5)


model.evaluate(val_scaled, val_target)

model.compile(
    optimizer="sgd", loss="sparse_categorical_crossentropy", metrics="accuracy"
)
sgd = keras.optimizers.SGD()
model.compile(optimizer=sgd, loss="sparse_categorical_crossentropy", metrics="accuracy")
sgd = keras.optimizers.SGD(learning_rate=0.1)
sgd = keras.optimizers.SGD(momentum=0.9, nesterov=True)

adagrad = keras.optimizers.Adagrad()
model.compile(
    optimizer=adagrad, loss="sparse_categorical_crossentropy", metrics="accuracy"
)

rmsprop = keras.optimizers.RMSprop()
model.compile(
    optimizer=rmsprop, loss="sparse_categorical_crossentropy", metrics="accuracy"
)

model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))

model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics="accuracy"
)

model.fit(train_scaled, train_target, epochs=5)
model.evaluate(val_scaled, val_target)
