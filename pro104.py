import cv2
my_img = cv2.imread("solar-system.jpg")

cv2.putText(my_img,
            "Sun",
            (100,90),
            cv2.FONT_HERSHEY_TRIPLEX,
            2,
            (12,7,117)
            )
cv2.putText(my_img,
            "Mercury",
            (110,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(my_img,
            "Venus",
            (190,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(my_img,
            "Earth",
            (300,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(my_img,
            "Mars",
            (400,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(my_img,
            "Jupiter",
            (485,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(my_img,
            "Saturn",
            (700,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(my_img,
            "Uranus",
            (940,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(my_img,
            "Neptune",
            (1080,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imshow("output screen", my_img)
cv2.waitKey(0)

cv2.imwrite("solar-system.jpg",my_img)