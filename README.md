# chicken_runner
크롬 브라우저의 T-Rex 게임을 모방하여 만든 게임입니다.

![Play](/ReadMe_Img/Play.png)
![Result](/ReadMe_Img/result_window.png)


https://github.com/jsm150/chicken_runner

jsm150님의 소스로 만들어진 프로젝트 입니다. jsm150님에게 소스를 받은 것에 대해 감사함을 전합니다.



# 작업환경

파이썬  Python 3.10.9

에디션	Windows 10 Pro

버전	21H2

설치 날짜	‎2022-‎08-‎28

OS 빌드	19044.2364

경험	Windows Feature Experience Pack 120.2212.4190.0


# 사용한 소프트웨어

Visual Studio Code v1.74

Sourcetree V3.4.11


# Run이 안되는 경우

## game.error: failed loading libmpg123-0.dll: 지정된 모듈을 찾을 수 없습니다.

https://ko.dll-files.com/libmpg123-0.dll.html 에서 LIBMPG123-0.DLL을 다운 후,

DLL 파일을 시스템 디렉토리 (C:\Windows\System32, C:\Windows\SysWOW64\의 64 비트)로 이동시킨다.

## import에서 에러가 발생 한 경우

파이썬으로 실행 시 일부 모듈이 필요할 수 있다.

명령 프롬포트에서 pip install pygame.. 등으로 설치를 해야 한다.