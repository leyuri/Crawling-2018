# Big Data Programming 

### Period

2018.11 ~ 2018.12

### Overview

방탄 소년단의 글로벌한 행보( 빌보드 점령 등)로 인한 KPOP의 부상이 이어지고 있다. 

따라서 BTS를 중심으로 KPOP 글로벌 확산의 성공요인 분석 및 KPOP에 미치는 영향력을 탐색하고자 한다.

과거의 KPOP 데이터를 바탕으로 흐름 경향 분석 시스템을 구축하자!

### Architecture

<img width="932" alt="Screen Shot 2019-12-19 at 11 08 20 PM" src="https://user-images.githubusercontent.com/33794732/71179932-7e800c00-22b4-11ea-851b-bc3e16c3df3f.png">

Local -> CentOS -> HDFS에 차례로 수집된 데이터를 올림

HDFS에 저장된 데이터를 이용하여 Hive에서 external table 생성

(external table은 데이터의 이동과정없이 폴더 안의 데이터를 바탕으로 테이블이 생성되므로 cost를 줄일 수 있음)

이후 Zeplin에서 pyspark를 이용하여 hive의 external table의 소스를 가져와 데이터 전처리 및 시각화 


### Data Collection

본 프로젝트에서 가장 중요한 것은 흐름분석으로 년도 별 모을 수 있는 데이터와 그에 따라 시시각각 변화하는 팬덤의 데이터가 필요했다.

따라서 쇼셜 미디어 중 하나인 twitter 데이터를 활용하였다. 

github open source 인 twitterscraper을 이용
https://github.com/taspinar/twitterscraper

20130101~20131231 당 100000으로 트윗을 제한하였고 년도 별 약 90MB의 데이터를 수집


### Data Analysis

nltk를 이용한 NLP분석

Tokenizer: 텍스트를 단어로 분리

Stopwords: "English"를 기준으로 불용어 제거

Part Of Speech: 명사(NN, NNP에 해당하는 것을 찾아 결과값 저장)



