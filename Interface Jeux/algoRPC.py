# Code de https://learnopencv.com/playing-rock-paper-scissors-with-ai/
# Modifié ,adapté et francisé (commentaire) par Audrey Guy 2023-04-17

# Pour entraîner un modèle, dé commenter l'entraînement et le test de détection ainsi que les imports nécessaires

import os
from statistics import StatisticsError

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


# Les imports en commentaire sont nécessaires pour l'entraînement du modèle mais inutile pour le fonctionnement normal

import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model, load_model
# from tensorflow.keras.layers import Dense, MaxPool2D, Dropout, Flatten, Conv2D, GlobalAveragePooling2D, Activation
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.utils import to_categorical

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder

from random import choice, shuffle
from scipy import stats as st

from collections import deque

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread

import RPCmarkov

"""

def gather_data(num_samples):
    global rock, paper, scissor, nothing

    # Initialize the camera
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # trigger tells us when to start recording
    trigger = False

    # Counter keeps count of the number of samples collected
    counter = 0

    # This the ROI size, the size of images saved will be box_size -10
    box_size = 234

    # Getting the width of the frame from the camera properties
    width = int(cap.get(3))

    while True:

        # Read frame by frame
        ret, frame = cap.read()

        # Flip the frame laterally
        frame = cv2.flip(frame, 1)

        # Break the loop if there is trouble  reading the frame.
        if not ret:
            break

        # If counter is equal to the number samples then reset triger and the counter
        if counter == num_samples:
            trigger = not trigger
            counter = 0

        # Define ROI for capturing samples
        cv2.rectangle(frame, (width - box_size, 0), (width, box_size), (0, 250, 150), 2)

        # Make a resizable window.
        cv2.namedWindow("Collecting images", cv2.WINDOW_NORMAL)

        # If trigger is True than start capturing the samples
        if trigger:

            # Grab only slected roi
            roi = frame[5: box_size - 5, width - box_size + 5: width - 5]

            # Append the roi and class name to the list with the selected class_name
            eval(class_name).append([roi, class_name])

            # Increment the counter
            counter += 1

            # Text for the counter
            text = "Collected Samples of {}: {}".format(class_name, counter)

        else:
            text = "Press 'r' to collect rock samples, 'p' for paper, 's' for scissor and 'n' for nothing"

        # Show the counter on the imaege
        cv2.putText(frame, text, (3, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1, cv2.LINE_AA)

        # Display the window
        cv2.imshow("Collecting images", frame)

        # Wait 1 ms
        k = cv2.waitKey(1)

        # If user press 'r' than set the path for rock directoryq
        if k == ord('r'):
            # Trigger the variable inorder to capture the samples
            trigger = not trigger
            class_name = 'rock'
            rock = []

        # If user press 'p' then class_name is set to paper and trigger set to True
        if k == ord('p'):
            trigger = not trigger
            class_name = 'paper'
            paper = []

        # If user press 's' then class_name is set to scissor and trigger set to True
        if k == ord('s'):
            trigger = not trigger
            class_name = 'scissor'
            scissor = []

        # If user press 's' then class_name is set to nothing and trigger set to True
        if k == ord('n'):
            trigger = not trigger
            class_name = 'nothing'
            nothing = []

        # Exit if user presses 'q'
        if k == ord('q'):
            break

    #  Release the camera and destroy the window
    cap.release()
    cv2.destroyAllWindows()


no_of_samples = 500
gather_data(no_of_samples)

# Set the figure size
plt.figure(figsize=[30, 20])

# Set the rows and columns
rows, cols = 4, 8

# Iterate for each class
for class_index, each_list in enumerate([rock, paper, scissor, nothing]):

    # Get 8 random indexes, since we will be showing 8 examples of each class.
    r = np.random.randint(no_of_samples, size=8)

    # Plot the examples
    for i, example_index in enumerate(r, 1):
        plt.subplot(rows, cols, class_index * cols + i)
        plt.imshow(each_list[example_index][0][:, :, ::-1])
        plt.axis('off')

# Combine the labels of all classes together
labels = [tupl[1] for tupl in rock] + [tupl[1] for tupl in paper] + [tupl[1] for tupl in scissor] +[tupl[1] for tupl in nothing]

# Combine the images of all classes together
images = [tupl[0] for tupl in rock] + [tupl[0] for tupl in paper] + [tupl[0] for tupl in scissor] +[tupl[0] for tupl in nothing]

# Normalize the images by dividing by 255, now our images are in range 0-1. This will help in training.
images = np.array(images, dtype="float") / 255.0

# Print out the total number of labels and images.
print('Total images: {} , Total Labels: {}'.format(len(labels), len(images)))

# Create an encoder Object
encoder = LabelEncoder()

# Convert Lablels to integers. i.e. nothing = 0, paper = 1, rock = 2, scissor = 3 (mapping is done in alphabatical order)
Int_labels = encoder.fit_transform(labels)

# Now the convert the integer labels into one hot format. i.e. 0 = [1,0,0,0]  etc.
one_hot_labels = to_categorical(Int_labels, 4)

# Now we're splitting the data, 75% for training and 25% for testing.
(trainX, testX, trainY, testY) = train_test_split(images, one_hot_labels, test_size=0.25, random_state=50)

# Empty memory from RAM
images = []


# This can further free up memory from RAM but be careful, if you won't be able to chage split % after this.
# rock, paper, scissor = [], [], []

# This is the input size which our model accepts.
image_size = 224

# Loading pre-trained NASNETMobile Model without the head by doing include_top = False
N_mobile = tf.keras.applications.NASNetMobile(input_shape=(image_size, image_size, 3), include_top=False,
                                              weights='imagenet')

# Freeze the whole model
N_mobile.trainable = False

# Adding our own custom head
# Start by taking the output feature maps from NASNETMobile
x = N_mobile.output

# Convert to a single dimensional vector by Global Average Pooling.
# We could also use Flatten()(x) GAP is more effective reduces params and controls overfitting.
x = GlobalAveragePooling2D()(x)

# Adding a dense layer with 512 units
x = Dense(712, activation='relu')(x)

# Dropout 20% of the activations, helps reduces overfitting
x = Dropout(0.40)(x)

# The fianl layer will contain 4 output units (no of units = no of classes) with softmax function.
preds = Dense(4, activation='softmax')(x)

# Construct the full model
model = Model(inputs=N_mobile.input, outputs=preds)

# Check the number of layers in the final Model
print("Number of Layers in Model: {}".format(len(model.layers[:])))

# Adding transformations that I know would help, you can feel free to add more.
# I'm doing horizontal_flip = False, incase you aren't sure which hand you would be using you can make that True.

augment = ImageDataGenerator(

    rotation_range=30,
    zoom_range=0.25,
    width_shift_range=0.10,
    height_shift_range=0.10,
    shear_range=0.10,
    horizontal_flip=False,
    fill_mode="nearest"
)

model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Set batchsize according to your system
epochs = 15
batchsize = 20

# Start training
history = model.fit(x=augment.flow(trainX, trainY, batch_size=batchsize), validation_data=(testX, testY),
steps_per_epoch= len(trainX) // batchsize, epochs=epochs)

# Use model.fit_generator function instead if TF version < 2.2
#history = model.fit_generator(x = augment.flow(trainX, trainY, batch_size=batchsize), validation_data=(testX, testY),
#steps_per_epoch= len(trainX) // batchsize, epochs=epochs)

# Plot the accuracy and loss curves

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('Training accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training loss')
plt.legend()

plt.show()

model.save("rps4.h5", overwrite=True)

""" # entraînement du modèle
"""

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
box_size = 234
width = int(cap.get(3))

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.rectangle(frame, (width - box_size, 0), (width, box_size), (0, 250, 150), 2)

    cv2.namedWindow("Rock Paper Scissors", cv2.WINDOW_NORMAL)

    roi = frame[5: box_size - 5, width - box_size + 5: width - 5]

    # Normalize the image like we did in the preprocessing step, also convert float64 array.
    roi = np.array([roi]).astype('float64') / 255.0

    # Get model's prediction.
    pred = model.predict(roi)

    # Get the index of the target class.
    target_index = np.argmax(pred[0])

    # Get the probability of the target class
    prob = np.max(pred[0])

    # Show results
    cv2.putText(frame, "prediction: {} {:.2f}%".format(label_names[np.argmax(pred[0])], prob * 100),
                (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Rock Paper Scissors", frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

""" # test de la détection


class AlgoRPC(QThread):
    frameToDisplay = pyqtSignal(np.ndarray)
    gameWinner = pyqtSignal(str)
    roundData = pyqtSignal(list)

    returnList = []

    markovRPC = RPCmarkov.RPCMarkov()

    model = load_model("rps4.h5")

    # Cette liste sera utilisée pour cartographier les probabilités aux noms de classe.
    label_names = ['nothing', 'paper', 'rock', 'scissor']

    def findout_winner(self, user_move, Computer_move):
        """
        Détermine le gagnant de la manche et émet le résultat à l'interface.

        Papier bat Roche
        Roche bat Ciseaux
        Ciseaux bat Papier

        :param user_move:
        :param Computer_move:
        :return:
        """
        # All logic below is self-explanatory
        self.returnList.append(user_move)
        self.returnList.append(Computer_move)

        if user_move == Computer_move:
            self.returnList.append("Tie")
            self.roundData.emit(self.returnList)
            self.returnList.clear()
            return "Tie"

        elif user_move == "rock" and Computer_move == "scissor":
            self.returnList.append("User")
            self.roundData.emit(self.returnList)
            self.returnList.clear()
            return "User"

        elif user_move == "rock" and Computer_move == "paper":
            self.returnList.append("ManUS")
            self.roundData.emit(self.returnList)
            self.returnList.clear()
            return "Computer"

        elif user_move == "scissor" and Computer_move == "rock":
            self.returnList.append("ManUS")
            self.roundData.emit(self.returnList)
            self.returnList.clear()
            return "Computer"

        elif user_move == "scissor" and Computer_move == "paper":
            self.returnList.append("User")
            self.roundData.emit(self.returnList)
            self.returnList.clear()
            return "User"

        elif user_move == "paper" and Computer_move == "rock":
            self.returnList.append("User")
            self.roundData.emit(self.returnList)
            self.returnList.clear()
            return "User"

        elif user_move == "paper" and Computer_move == "scissor":
            self.returnList.append("ManUS")
            self.roundData.emit(self.returnList)
            self.returnList.clear()
            return "Computer"

    def send_winner(self, user_score, computer_score):
        """
        Vérifie le score final d'une partie et émet le gagnant à l'interface

        u == l'utilisateur a gagné
        m == ManUS a gagné
        d == égalité

        :param user_score:
        :param computer_score:
        :return:
        """
        if user_score > computer_score:
            self.gameWinner.emit("u")

        elif user_score < computer_score:
            self.gameWinner.emit("m")

        else:
            self.gameWinner.emit("d")

        return True

    cap = cv2.VideoCapture(0)
    box_size = 234  # ne pas changer, sinon ça plante...

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 640

    # Le nombre de manches par partie.
    attempts = 1

    # Initialisation des coups
    computer_move_name = 'nothing'
    final_user_move = 'nothing'
    user_move = 'nothing'

    # Initialisation des scores
    computer_score, user_score = 0, 0

    # Couleur initiale du rectangle de jeux (bleu)
    rect_color = (255, 0, 0)

    # Initialisation de la détection de la main
    hand_inside = False

    # Manche jouée dans la partie
    total_attempts = attempts

    # Nous ne considérerons que les reconnaissances dont la confiance est supérieure à ce seuil.
    confidence_threshold = 0.70

    # Au lieu de travailler sur une seule reconnaissance, nous prendrons
    # le mode de 5 reconnaissances en utilisant un objet deque.
    # De cette façon, même si nous sommes confrontés à un faux positif, nous l'ignorerons facilement.
    smooth_factor = 5

    # Notre liste initiale de deque aura 'nothing' répété 5 fois.
    de = deque(['nothing'] * 5, maxlen=smooth_factor)

    def __init__(self):
        """
        Initialisation du fil d'exécution

        """
        QThread.__init__(self)

    def run(self):
        """
        Boucle du fil, s'exécute en continu.
        Ici, on prend les captures d'écran, on les traite, on fait les prédictions et les calculs statistiques,
        on détermine le gagnant et on envoie toutes les informations à l'interface.

        :return:
        """

        while True:

            ret, frame = self.cap.read()

            if not ret:
                break

            frame = cv2.flip(frame, 1)

            # extrait la région de l'image dans le rectangle de jeux
            roi = frame[5: self.box_size - 5, self.width - self.box_size + 5: self.width - 5]

            roi = np.array([roi]).astype('float64') / 255.0

            # Reconnaissance du coup
            pred = self.model.predict(roi, verbose=0)

            # Trouver le coup dans la liste
            move_code = np.argmax(pred[0])
            self.user_move = self.label_names[move_code]

            # Trouver la confiance de la reconnaissance
            prob = np.max(pred[0])

            # Vérifie si la probabilité est supérieure au seuil défini
            if prob >= self.confidence_threshold:

                # Maintenant, ajoutez le déplacement vers la liste de deque à partir de la gauche
                self.de.appendleft(self.user_move)

                # Obtenez le mode, c'est-à-dire quelle classe s'est produite
                # le plus fréquemment au cours des 5 derniers mouvements.
                try:
                    self.final_user_move = str(st.mode(self.de, keepdims=True)[0][0])

                except StatisticsError:
                    print('Stats error')
                    continue

                # Si rien n'est faux et que hand_inside est False, continuez.
                # La variable hand_inside nous aide à ne pas prédire à plusieurs reprises pendant la boucle
                # L'utilisateur doit donc sortir ses mains de la boîte pour chaque nouvelle reconnaissance.

                if self.final_user_move != "nothing" and self.hand_inside == False:

                    self.hand_inside = True

                    # Obtenez le mouvement de l'ordinateur, puis obtenez le gagnant.
                    self.computer_move_name = choice(['rock', 'paper', 'scissor'])  # Si on veut que l'ordinateur joue aléatoirement
                    # self.computer_move_name = self.markovRPC.play(self.user_move) # Si on veut que l'ordinateur joue avec un algorithme de chaîne de Markov
                    winner = self.findout_winner(str(self.final_user_move), self.computer_move_name)

                    self.total_attempts -= 1

                    # Si le gagnant est l'ordinateur, il obtient des points et vice versa.
                    # Nous modifions également la couleur du rectangle en fonction du vainqueur de la manche.
                    # Bleu = en attente ; Blanc = égalité
                    # Rouge = défaite pour l'humain ; Vert = victoire pour l'humain

                    if winner == "Computer":
                        self.computer_score += 1
                        self.rect_color = (0, 0, 255)

                    elif winner == "User":
                        self.user_score += 1
                        self.rect_color = (0, 250, 0)

                    elif winner == "Tie":
                        self.rect_color = (255, 250, 255)

                    # Si toutes les tentatives sont terminées, trouvez notre gagnant
                    if self.total_attempts == 0:

                        play_again = self.send_winner(self.user_score, self.computer_score)

                        # Redémarrez le jeu en réinitialisant toutes les variables une fois le gagnant envoyé
                        if play_again:
                            self.user_score, self.computer_score, self.total_attempts = 0, 0, self.attempts

                        # S'il y a un problème dans l'envoie, la boucle est brisée
                        else:
                            break

                # Si la classe n'est rien, alors hand_inside devient False
                elif self.final_user_move == 'nothing':
                    self.hand_inside = False
                    self.rect_color = (255, 0, 0)

            # On écrit ici les étiquettes que l'on veut afficher sur le feedback de la caméra
            moveToShow = "rien"
            if self.final_user_move == "rock":
                moveToShow = "roche"
            elif self.final_user_move == "paper":
                moveToShow = "papier"
            elif self.final_user_move == "scissor":
                moveToShow = "ciseaux"
            else:
                pass

            cv2.putText(frame, "Votre coup: " + moveToShow,
                (420, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

            cv2.rectangle(frame, (self.width - self.box_size, 0), (self.width, self.box_size), self.rect_color, 2)

            # On envoie l'image à afficher à l'interface pour éviter les conflits
            self.frameToDisplay.emit(frame)

            # Pause pour réguler le taux d'affichage à 120 fps
            self.msleep(1000//120)

    def kill(self):
        self.cap.release()
        self.terminate()

"""

user_move = 'paper'
computer_move = choice(['rock', 'paper', 'scissor'])

winner = findout_winner(user_move, computer_move)

print("User Selected '{}' and computer selected '{}' , winner is: '{}' ".format(user_move, computer_move, winner))

"""  # test de l'algorithme de gagnant
