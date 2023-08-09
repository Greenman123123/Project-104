import cv2
planets = cv2.imread("solar-system.jpg")

cv2.putText(planets,"Sun",(20,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),1)
cv2.putText(planets,"Mercury",(120,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Venus",(190,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Earth",(280,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Moon",(320,160),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Mars",(390,160),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Jupiter",(450,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Saturn",(750,120),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Uranus",(950,120),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)
cv2.putText(planets,"Neptune",(1100,120),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,255,255),1)

cv2.imshow("Solar System image",planets)
cv2.waitKey(3000)

