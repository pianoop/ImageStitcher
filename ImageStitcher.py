import cv2
import numpy as np

def stitch_images(img1, gray1, img2, gray2):
    # 특징점 추출기 생성 (SIFT 사용)
    sift = cv2.xfeatures2d.SURF_create()

    # 이미지에서 키 포인트와 디스크립터 추출
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # 매칭을 위한 FLANN 기반 매처 설정
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # 좋은 매칭점 찾기
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7*n.distance:  # Lowe's ratio test
            good_matches.append(m)

    # Homography를 찾기 위한 포인트 생성
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # 결과 이미지의 크기 계산 (두 이미지를 모두 포함하도록 설정)
    width = img1.shape[1] + img2.shape[1]
    height = img1.shape[0] + img2.shape[0]

    # 두 번째 이미지 관점에서 첫 번째 이미지 변환
    transformed_img = cv2.warpPerspective(img1, M, (width, height))

    # 변환된 이미지에 원본 두 번째 이미지 추가
    transformed_img[0:img2.shape[0], 0:img2.shape[1]] = img2

    # 이미지 크기 조절
    max_height = 800
    if transformed_img.shape[0] > max_height:
        scaling_factor = max_height / float(transformed_img.shape[0])
        transformed_img = cv2.resize(transformed_img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return transformed_img


# 이미지 불러오기
img_1 = cv2.imread('image4.jpg', cv2.IMREAD_COLOR)
img_2 = cv2.imread('image3.jpg', cv2.IMREAD_COLOR)
#img_3 = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# 특징 추출을 위한 그레이스케일 이미지 생성
gray_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
gray_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
#gray_3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)

# 첫 번째와 두 번째 이미지를 병합
stitched_img_1_2 = stitch_images(img_1, gray_1, img_2, gray_2)

# 첫 번째와 두 번째 이미지가 병합된 이미지와 세 번째 이미지를 병합
#stitched_img_1_2_3 = stitch_images(stitched_img_1_2, gray_1, img_3, gray_3)

cv2.imshow('Stitched Image', stitched_img_1_2)
#cv2.imshow('Stitched Image', stitched_img_1_2_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
