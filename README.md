# dudaji-todo
### Quick Starter
1. install poetry
```
brew install poetry
```
2. clone git repository
```  
git clone <git-repository>
```
3. set virtual env 
```
# 생성되는 가상 환경 정보가 해당 프로젝트 루트 디렉토리에 생성되는 config 설정.
poetry config virtualenvs.in-project true

# 파이썬 3.11이 없다면 install
# 다른 가상 환경 사용도 무방
poetry env use <파이썬 3.11 경로> 
```
4. 가상 환경 activate
```
poetry shell
```
5. 라이브러리 설치
```
poetry install
```  

6-1. 서버 구동
```
flask run
```
6-2. 테스트 코드 구동
```
python -m pytest
```