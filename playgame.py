from keras.models import *
import cv2
import numpy as np
from random import choice


game={
0: "rock",
1: "paper",
2: "scissors",
3: "none"

}

model=load_model("rock-paper-scissors-model.h5")
capture=cv2.VideoCapture(0)
last_move=None

while True:
	ret,frame=capture.read()
	cv2.rectangle(frame, (100, 100), (500, 500), (0, 255,0), 2)
	cv2.rectangle(frame, (800, 100), (1200, 500), (0, 0, 255), 2)
	photo = frame[100:500, 100:500]
	image = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
	image = cv2.resize(image, (224, 224))
	prediction=model.predict(np.array([image]))
	user_move=np.argmax(prediction[0])
	user_move=game[user_move]
	if last_move != user_move:
		if user_move != "none":
			computer_move = choice(['rock', 'paper', 'scissors'])
			if user_move==computer_move:
				winner='tie'
			if user_move=='rock':
				if computer_move=='paper':
					winner='computer'
				if computer_move=='scissors':
					winner='user'
			if user_move=='paper':
				if computer_move=='scissors':
					winner='computer'
				if computer_move=='rock':
					winner='user'
			if user_move=='scissors':
				if computer_move=='rock':
					winner='computer'
				if computer_move=='paper':
					winner='user'
		else:
			computer_move= "none"
			winner = "Waiting..."
	last_move = user_move


	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, "Your Move: " + user_move,(50, 50), font, 1.2, (255,0,0),1, cv2.LINE_AA)
	cv2.putText(frame, "Computer's Move: " + computer_move,(750, 50), font, 1.2, (255,0,0), 1, cv2.LINE_AA)
	cv2.putText(frame, "Winner: " + winner,(100, 200), font, 1, (0,255,0), 2, cv2.LINE_AA)
	if computer_move!= "none":
		computer= cv2.imread("computerimages/{}.png".format(computer_move))
		computer= cv2.resize(computer, (400, 400))
		region_height,region_width,_=computer.shape
		frame_height,frame_width,_=frame.shape
		new_frame_height=max(100+region_height,frame_height)
		new_frame_width=max(800+region_width,frame_width)
		new_frame=np.zeros((new_frame_height,new_frame_width,3),dtype=np.uint8)
		new_frame[:frame_height,:frame_width]=frame
		new_frame[100:100+region_height,800:800+frame_width]=computer 
		frame=new_frame
	cv2.imshow("Rock Paper Scissors", frame)
	key = cv2.waitKey(10)
	if key == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
