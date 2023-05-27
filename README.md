# ImageStitcher
The program automatically finds matching points between the images and combines them into one unified image.
<br/><br/><br/>  
  
## Version
Python: 3.7.16
Opencv: 3.4.2
<br/><br/><br/>  

## 설명
SURF 알고리즘을 사용하여 이미지의 특징점을 검출하고, 이를 통해 추출한 정보를 바탕으로 여러 이미지를 하나의 이미지로 합쳐줍니다.
<br/><br/><br/>  

## 사용 방법
ImageStitcher.py파일의 imread('파일이름', ...)  부분의 파일이름에 사용할 이미지를 연결 후 실행해주세요.
<br/><br/><br/>  

## example1
- 각 두 장의 사진  
<img src="https://github.com/pianoop/ImageStitcher/assets/86285421/5faf5d12-bb95-4197-849f-d70e8b0048fe.png" width="500" height="400"/>  
<img src="https://github.com/pianoop/ImageStitcher/assets/86285421/ee83574c-7f88-455c-8158-6c009f198db8.png" width="500" height="400"/>  
<br/><br/><br/>  

- 결과  

![image](https://github.com/pianoop/ImageStitcher/assets/86285421/cb061d7b-9068-4cf0-8b6c-f1e04cdd6f16)  
<br/><br/><br/>  

## example2
- 각 두 장의 사진  
<img src="https://github.com/pianoop/ImageStitcher/assets/86285421/612955fe-2431-45a9-9bde-a10651f18305.png" width="500" height="400"/>  
<img src="https://github.com/pianoop/ImageStitcher/assets/86285421/dbe0faef-8ba2-42c9-b16a-5d5b38e02a5c.png" width="500" height="400"/>  
<br/><br/><br/>  

- 결과  

![image](https://github.com/pianoop/ImageStitcher/assets/86285421/28b6eb74-f8ad-4567-a541-cf08c6365310)  
<br/><br/><br/>  


## 보완해야할 점
2장을 매칭할 때 매칭 순서에 따라 결과물의 퀄리티가 달라짐 -> 순서에 상관 없게 하거나 자동으로 여러 순서로 처리 후 잘 나온 것을 출력하도록 보완  
3장 이상을 합침, 카메라가 바라보는 각도가 달라지는 경우 매칭이 잘 이루어지지 않음 -> bundle adjustment, 전역 최적화 등을 사용
<br/><br/><br/>  

