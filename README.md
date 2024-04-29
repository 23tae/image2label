# Image2Label

## Overview

[Amazon Rekognition](https://aws.amazon.com/rekognition/resources/)을 사용하여 이미지에서 레이블을 탐지하고 이를 CSV 파일 형식으로 저장하는 프로그램

## Functionality

- Amazon S3 버킷에 연결하여 이미지를 찾는다.
- Rekognition을 사용하여 각 이미지에서 레이블을 감지한다.
- "labels" 디렉토리 내에 각 이미지별 CSV 파일(레이블, 신뢰도 점수)을 저장한다.

## Prerequisites

- Amazon Web Services (AWS) 계정: Amazon Rekognition 서비스에 액세스할 수 있는 AWS 계정
- Python
- 의존성 패키지: 필요한 의존성 패키지를 설치하기 위해 아래 명령을 실행:

  ```shell
  pip install -r requirements.txt
  ```

- Amazon S3 버킷에 이미지 업로드
- 환경 변수: env.sample 파일을 복사하여 `.env` 파일을 생성하고, 이미지가 위치한 S3 버킷의 이름과 폴더명을 설정
- AWS CLI credentials 설정 ([참고](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html))

## Usage

- 프로그램 실행

  ```py
  python3 main.py
  ```

- `labels/` 에서 csv 파일 확인

## Output example

- **image1.jpg**
  ![image1](/assets/images/image1.jpg)

- **image1.csv**

  ```
  Label,Confidence
  Nature,100.0
  Outdoors,100.0
  Pond,100.0
  Water,100.0
  Land,99.99502563476562
  Scenery,98.19378662109375
  Person,97.50032043457031
  Bench,97.08635711669922
  Swamp,96.99015808105469
  Construction Crane,96.9571762084961
  ```

- **image2.jpg**
  ![image2](/assets/images/image2.jpg)

- **image2.csv**

  ```
  Label,Confidence
  Indoors,99.99805450439453
  Restaurant,99.99805450439453
  Cafeteria,99.98191833496094
  Cafe,99.89547729492188
  Person,99.45893096923828
  Chair,99.38227844238281
  Cup,99.03710174560547
  Lamp,98.38184356689453
  Speaker,96.35136413574219
  Plywood,95.61605072021484
  ```

- **image3.jpg**
  ![image3](/assets/images/image3.jpg)

- **image3.csv**

  ```
  Label,Confidence
  City,99.97466278076172
  Road,99.97466278076172
  Street,99.97466278076172
  Urban,99.97466278076172
  Neighborhood,99.74077606201172
  Truck,99.69886016845703
  Person,99.37333679199219
  Box,99.04634857177734
  Car,98.82805633544922
  Shoe,98.06107330322266
  ```
