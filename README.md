# Image2Label

## Overview

[Amazon Rekognition](https://aws.amazon.com/rekognition/)을 사용하여 이미지에서 레이블을 탐지하고 이를 CSV 파일 형식으로 저장하는 프로그램

## Functionality

- [Amazon S3](https://aws.amazon.com/s3/) 버킷에 연결하여 이미지를 찾는다.
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

| 이미지                          | 결과                                                                 |
|----------------------------------|---------------------------------------------------------------------|
| ![image1](/assets/images/image1.jpg) | **Label,Confidence**<br>Nature,100.0<br>Outdoors,100.0<br>Pond,100.0<br>Water,100.0<br>Land,99.99502563476562<br>Scenery,98.19378662109375<br>Person,97.50032043457031<br>Bench,97.08635711669922<br>Swamp,96.99015808105469<br>Construction Crane,96.9571762084961 |
| ![image2](/assets/images/image2.jpg) | **Label,Confidence**<br>Indoors,99.99805450439453<br>Restaurant,99.99805450439453<br>Cafeteria,99.98191833496094<br>Cafe,99.89547729492188<br>Person,99.45893096923828<br>Chair,99.38227844238281<br>Cup,99.03710174560547<br>Lamp,98.38184356689453<br>Speaker,96.35136413574219<br>Plywood,95.61605072021484 |
| ![image3](/assets/images/image3.jpg) | **Label,Confidence**<br>City,99.97466278076172<br>Road,99.97466278076172<br>Street,99.97466278076172<br>Urban,99.97466278076172<br>Neighborhood,99.74077606201172<br>Truck,99.69886016845703<br>Person,99.37333679199219<br>Box,99.04634857177734<br>Car,98.82805633544922<br>Shoe,98.06107330322266 |