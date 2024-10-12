import os
import cv2


samplename=input("Enter the Sample Name...")
photoscount=int(input("Enter the No.of Images to Captured...."))

print("Press 's' to Start...\n Press 'q' to Quit")
 
try:
	os.mkdir("Images")
except FileExistsError:
	pass
try:
	os.mkdir("Images/{}".format(samplename))
except:
	print("{} File Already Exists".format(samplename))
	print("Existing Files in the Folder will be replaced")

capture=cv2.VideoCapture(0)
count=0

start=False

while True:
	ret,frame=capture.read()
	if count==photoscount:
		break
	
	cv2.rectangle(frame,(100,100),(500,500),(0,255,0),2)
	
	if start:
		photo=frame[100:500,100:500]
		path=os.path.join("Images/{}".format(samplename),"{}.jpg".format(count+1))
		cv2.imwrite(path,photo)
		count=count+1
	font=cv2.FONT_HERSHEY_TRIPLEX
	cv2.putText(frame,"Collected {} images".format(count),(5,50),font,0.6,(255,0,0),1,cv2.LINE_AA)
	cv2.imshow("Gathering Images",frame)

	key=cv2.waitKey(10)
	if key==ord('q'):
		break
	if key==ord('s'):
		start=True



print("\n{} image(s) saved to photos/{}".format(count, samplename))
capture.release()
cv2.destroyAllWindows()
