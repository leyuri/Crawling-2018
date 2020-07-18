# KPOPTrend-NLPAnalysis

- KPOP 키워드를 활용하여 Twitterscraper를 활용해 데이터를 수집하고, zeplin을 이용하여 wordcloud 시각화 및 분석

  

### About

- 개인프로젝트

- 기간: 2018.11 ~ 2018.12



### OverView

방탄 소년단의 글로벌한 행보등으로 인한 KPOP의 부상이 잇따르고 있습니다. 따라서 BTS를 중심으로 KPOP 글로벌 확산의 성공요인 분석 및 KPOP에 미치는 영향력 탐색을 목표로 하였습니다. 과거의 KPOP 데이터와 현재의 KPOP데이터를 수집하였고, 많은 양의 데이터를 관리하기 위해 hadoop을 활용하였습니다. Local -> Centos -> HDFS에 수집된 데이터를 올렸습니다. Hive(HDFS나 Hbase와 같은 데이터 저장 시스템에 저장되어 있는 대용량 데이터 집합을 분석하는데 적합)에서 HDFS에 저장된 데이터를 이용하여 external table생성하였습니다. 이후 Spark SQL(Spark는 데이터를 읽고, 변형, 합계를 내는 등 복잡한 통계 모델을 쉽게 학습 가능) 을 통하여 Hive테이블의 데이터 소스를 가져와 External table의 데이터를 spark를 통하여 전처리(pyspark) 해당 데이터를 Zeplin을 통하여 wordcloud를 통해 확인해보았습니다.



### Architecture

<img width="816" alt="Screen Shot 2020-06-23 at 5 54 11 PM" src="https://user-images.githubusercontent.com/33794732/85383107-92197180-b57a-11ea-85f9-8a2ae2d742f0.png">



### Dataset

본 프로젝트에서 가장 중요한 것은 흐름 분석, 년도 별 차곡차곡 모을 수 있는 데이터가 필요했습니다. 쇼셜 미디어 중 하나인 twitter 를 이용하고자 했습니다. Github open source 인 Twitterscraper(https://github.com/taspinar/twitterscraper)를 통해 데이터 수집을 하였습니다. 



### Data analysis method

1. Tokenizer: 텍스트를 단어로 분리

```
tokens = nltk.word_tokenize(df['text'][0]) # 첫번째 내용에서 토큰 추출
tokens = [token.lower() for token in tokens if len(token) > 1]
```

2. Stopwords: “Enlish”를 기준으로 불용어 제거 

```
stop_words = stopwords.words('english')
tokens_clean = [token for token in tokens if not token in stop_words]
```

3. Pos(part-of-speech): 명사(NN,NNP에 해당하는 것을 찾아 결과값 저장

```
tokens_tagged = nltk.pos_tag(tokens_clean)
tokens_noun = [word for word, pos in tokens_tagged if pos in ['NN', 'NNP’]]
```



### Results

| <img width="284" alt="Screen Shot 2020-06-23 at 5 41 17 PM" src="https://user-images.githubusercontent.com/33794732/85381568-0e12ba00-b579-11ea-81df-1c6d1a4de809.png"> | <img width="284" alt="Screen Shot 2020-06-23 at 5 41 26 PM" src="https://user-images.githubusercontent.com/33794732/85381593-14a13180-b579-11ea-894b-4696641a8b4a.png"> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |


KPOP의 2013 데이터에 비하여 2018에는 BTS가 도출되었음을 확인할 수 있었습니다. 즉 BTS는 KPOP의 동향 분석에서 파급 효과를 가지고 있음을 추론할 수 있었습니다. 



