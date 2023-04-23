import cv2
import cv2.aruco as aruco

aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_250)


parameters = aruco.DetectorParameters_create()


cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        

    
    if len(corners) > 0:
        #rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients,distortion_coefficients)
        aruco.drawDetectedMarkers(frame, corners, ids)
        #aruco.drawAxis(frame,matrix_coefficients,distortion_coefficients,rvec,tvec,0.01)

    cv2.imshow('Aruco markers detected', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
