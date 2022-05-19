import cv2
import sys

# check cv2 version 
print('Hello OpenCV', cv2.__version__)

# 영상 불러오기
# Opencv는 영상 데이터를 numpy.ndarray로 표현
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.imwrite('cat_gray.png', img) # format에 맞게 파일 저장
cv2.namedWindow('image') # 창의 이름 지정
# cv2.namedWindow('image', cv2.WINDOW_NORMAL) -> 창 크기 조절 가능 (resizes 가능)

cv2.imshow('image', img) # 영상 출력하기
cv2.waitKey() # 키보드 입력 대기

while True:
    if cv2.waitKey() == 27:
        break
print(key)

# 특수키 코드: 27(esc), 13(Enter), 9(Tab)

# 창 닫기
# cv2.destroyWindow(winname) # 괄호 안은 닫고자 하는 창 이름
# cv2.destroyAllWindows()

# 창 크기 변경
# cv2.resizeWindow(winname, width, height)

