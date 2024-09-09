

## 01. 프로젝트 개요
- 프로젝트명 : 중고거래 스파르타 마켓
- 프로젝트 소개
  - 스파르타 마켓 백엔드 기능 DRF로 구현하기
 
## 02. 팀
- 팀원 : 박연재

## 03. 프로젝트 내용
- 개발기간 : 2024.09.03 ~
- 기능
  - 각 유저는 자신의 물건을 등록할 수 있습니다
  - 지역별 유저는 고려하지 않습니다
  - 구매하기 기능은 구현하지 않습니다
  - 모든 API는 RESTful 원칙을 따라야 합니다

## 04. 기능
- 필수 구현
  - accounts
    <details>
      <summary>회원가입</summary>
      <div markdown="1">
  
      - endpoint : /api/accounts/
      - method : POST
      - 조건 
        - username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수입력
        - 성별, 자기소개는 생략 가능

    ![image](./spartamarket-readme-img/signup.png)
        
      </div>
      </details>
    
      <details>
      <summary>로그인</summary>
      <div markdown="1">
  
      - endpoint : /api/accounts/login/
      - method : POST
      - 조건 : 사용자명과 비밀번호 입력 필요
        
    ![image](./spartamarket-readme-img/login.png)
        
      </div>
      </details>
    
      <details>
      <summary>프로필 조회</summary>
      <div markdown="1">
  
      - Endpoint : /api/accounts/&#60;str:username>/
      - method : POST
      - 조건 : 로그인 상태 필요
    
      로그인 됐을때 프로필 조회
    
    ![image](./spartamarket-readme-img/profile-auth-ok.png)

      로그인 안 됐을때 프로필 조회
  
    ![image](./spartamarket-readme-img/profile-not-auth.png)
        
      </div>
      </details>
    
  - product

    <details>
      <summary>상품등록</summary>
      <div markdown="1">
  
      - endpoint : /api/products/
      - method : POST
      - 조건 : 로그인 상태, 제목과 내용, 상품 이미지 입력 필요

      ![image](./spartamarket-readme-img/products-create.png)

      </div>
      </details>

      <details>
      <summary>상품 목록 조회</summary>
      <div markdown="1">
  
      - endpoint : /api/products/
      - method : GET
      - 조건 : 로그인 상태 불필요

      상품 목록 조회 (유효한 페이지)

      ![image](./spartamarket-readme-img/products-get.png)

      상품 목록 조회 (유효하지 않은 페이지)

      ![image](./spartamarket-readme-img/products-not-exist.png)

      </div>
      </details>
    
      <details>
      <summary>상품 수정</summary>
      <div markdown="1">
  
      - endpoint : /api/products/&#60;int:productID>
      - method : PUT
      - 조건 : 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능

      ![image](./spartamarket-readme-img/product-edit.png)

      </div>
      </details>
  
      <details>
      <summary>상품 삭제</summary>
      <div markdown="1">
  
      - endpoint : /api/products/&#60;int:productID>
      - method : PUT
      - 조건 : 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능

      상품 삭제 (유효한 사용자)

      ![image](./spartamarket-readme-img/products-delete.png)

      상품 삭제 불가 (유효하지 않은 사용자)

      ![image](./spartamarket-readme-img/products-cannot-delete.png)

      </div>
      </details>
  
    
- 도전 기능
  - accounts
    
    <details>
      <summary>로그아웃</summary>
      <div markdown="1">
  
      - endpoint : /api/accounts/logout/
      - method : POST
      - 조건 : 로그인 상태 필요
    
      ![image](./spartamarket-readme-img/accounts-logout.png)
    
      </div>
      </details>
    
      <details>
      <summary>본인 정보 수정</summary>
      <div markdown="1">
  
      - endpoint : /api/accounts/&#60;str:username>
      - method : PUT
      - 조건 : 이메일, 이름, 닉네임, 생일 입력 필요하며 성별, 자기소개 생략 가능
   
      ![image](./spartamarket-readme-img/profile-edit.png)
 
      </div>
      </details>
    
      <details>
      <summary>패스워드 변경</summary>
      <div markdown="1">
    
      - endpoint : /api/accounts/password/
      - method : PUT
      - 조건 : 기존 패스워드와 변경할 패스워드는 상이해야 함
        <details>
        <summary>비밀번호 변경 실패</summary>
        <div markdown="1">
     
        ![image](./spartamarket-readme-img/changepassword-not-correct.png)
    
        ![image](./spartamarket-readme-img/changepassword-not-correct2.png)
    
        ![image](./spartamarket-readme-img/changepassword-not-correct3.png)
   
        </div>
        </details>
        
        <details>
          <summary>비밀번호 변경 성공</summary>
          <div markdown="1">
       
          ![image](./spartamarket-readme-img/changepassword-success.png)
     
          </div>
          </details>
            </div>
            </details>
    
        <details>
        <summary>회원 탈퇴</summary>
        <div markdown="1">
  
        - endpoint : /api/products/
        - method : DELETE
        - 조건 : 로그인 상태, 비밀번호 재입력 필요
    
        회원 탈퇴 실패 (비밀번호 불일치)
    
        ![image](./spartamarket-readme-img/account-delete-fail.png)
    
        회원 탈퇴 성공 (비밀번호 일치)
    
        ![image](./spartamarket-readme-img/account-delete-success.png)
        </div>
        </details>
  
  - 데이터베이스 관계 모델링
    <details>
        <summary>팔로잉 시스템</summary>
        <div markdown="1">
    
    팔로우하기
    
      ![image](./spartamarket-readme-img/accounts-follow.png)

    팔로우 확인

      ![image](./spartamarket-readme-img/accounts-followinguser.png)

      </div>
      </details>
    
    <details>
        <summary>게시글 좋아요 기능</summary>
        <div markdown="1">
    
    좋아요
    
      ![image](./spartamarket-readme-img/products-like.png)

    좋아요 확인

      ![image](./spartamarket-readme-img/products-likeuser.png)

      </div>
      </details>
  

## 05. 스택
- 언어 : python
- 라이브러리 & 프레임워크 : Django
- 데이터베이스 : SQlite3

## 06. 프로젝트 구조
```
📦 
├─ .gitignore
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ products
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ requirements.txt
└─ spartamarket_DRF
   ├─ __init__.py
   ├─ asgi.py
   ├─ settings.py
   ├─ urls.py
   └─ wsgi.py
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## 07. ERD

![image](./spartamarket-readme-img/ERD.png)


