 ## 🥶 8월 21일 공부 내용
### 1) Shell  command  
 1) cd : 폴더 이동에 사용이 됩니다.
```shell
> cd 하위폴더 #하위 폴더로 가는 경우
> cd ..  #상위 폴더로 가는 경우
```
2) mkdir : 해당 명령어는 폴더를 만드는 명령어 입니다.
```shell
> mkdir dev
> mkdir dev/bin
```
3) touch : 해당 명령어는 파일을 생성하는 명령어 입니다.
```shell
> touch main.py
> touch test.docs #해당 명령어를 포함한 특정 프로그램이 있어야지 열리는 파일들은 제대로 작동을 안할 수 도 있음
```
4) vim : 해당 명령어는 cmd창 내에서 파일을 수정할 수 있게 해주는 명령어 입니다.
```shell
> vim main.py
```
5) cat : 해당 명령어는 cmd창 내에서 파일을 읽을 수 있게 해주는 명령어 입니다.
```shell
> cat main.py
```
6) mv : 파일이나 디렉토리를 이동 시킬때 사용하는 명령어입니다. 추가로 이름 변경도 가능합니다.
```shell
> mv test.txt dev
> mv test.txt test_1.txt
```
>shell을 배우는 이유는 나중에 개발을 하는데, 있어서 cmd창으로 모든 파일들을 관리해야하는 상황이 자주 생기기 때문에 배워두는 것.
#### 개인적으로 웹 개발을 하던 과정에서 Cloudtype이나 AWS 같은 서버를 사용하는 과정에서 자주 사용했기에 배우는 이유가 너무 공감되었고, 하는 과정에서 힘든 점은 따로 없었습니다.😃
### 2) git command
1) git clone : 원격 저장소를 복제할 때 사용합니다.
```shell
$ git clone <저장소URL>
```
2) git status : 현재 작업 중인 디렉토리 상태(추가/수정/삭제 여부)를 확인합니다.
```shell
 $ git status
```
3) git add "파일이름" : 특정 파일을 staging area에 올립니다. (commit 준비 단계)

```shell
$ git add main.py
$ git add .   # 모든 변경 사항 추가(되도록이면 쓰지 말 것)
```

4) git commit : staging area에 올려둔 변경 사항을 저장소에 기록합니다.

```shell
 git commit -m "메시지 작성"
```

5) git push : 로컬 저장소의 커밋을 원격 저장소로 업로드합니다.

```shell
$ git push origin main
```

6) git branch ("-r") : 브랜치를 확인하거나 관리합니다.

```shell
$ git branch        # 로컬 브랜치 목록 확인
$ git branch -r     # 원격 브랜치 목록 확인
```

7) git branch "브랜치 이름" : 새로운 브랜치를 생성합니다.

```shell
$ git branch feature/login
```

8) git switch "브랜치 이름" : 해당 브랜치로 전환합니다.
```shell
$ git switch feature/login
```

9) git checkout "브랜치 이름" : (switch 이전 방식) 브랜치를 이동하거나 특정 커밋으로 돌아갑니다.
```shell
$ git checkout feature/login
```

10) git merge "브랜치 이름" : 다른 브랜치의 변경 사항을 현재 브랜치에 병합합니다.
```shell
git merge feature/login
```

### 3) 과제
1) git branch buzz (buzz 브랜치 만들기)

2) git switch buzz (buzz 브랜치로 이동하기)

3) vi fizzbuzz.py -> elif 5의 배수라면 'buzz' (작업하기)

4) git add, git commit -> feat: (작업한 결과물 commit 하기)

5) git switch main (main 브랜치로 이동하기)

6) git merge buzz (buzz 작업결과물을 main에 merge하기)

7) git push origin main 이후 github에서 buzz 코드 확인하기

8) TIL에 오늘 내용 간략히 정리해보기(git/250821-(제목은 자유롭게).md)

9) vi git/25~.md 열어서 작업하기

10) git add, git commit, git push

#### 나의 작업
![title](http://github.com/user-attachments/assets/f29b549e-38fa-47a2-8912-7df32f89956e)   
![title](http://github.com/user-attachments/assets/3b4e7811-b596-4803-a264-af66323e9213)   

