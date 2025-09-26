# upgraded 디렉터리 구조 설명

`upgraded` 폴더는 레거시(`legacy`) 폴더의 모든 코드를 최신 Python 환경에서 작업할 수 있도록 복사한 공간입니다. 각 하위 폴더와 파일의 역할은 다음과 같습니다.

## 주요 파일 및 폴더

- `MANIFEST.in`, `README.rst`, `setup.py`, `distribute_setup.py`: 프로젝트 메타 정보, 설치 스크립트, 배포 관련 파일
- `guachi/`: 핵심 라이브러리 코드
    - `__init__.py`, `config.py`, `database.py`: 설정 관리, DB 연동 등 주요 기능 구현
    - `tests/`: 단위 및 통합 테스트 코드
        - `test_configmapper.py`, `test_configurations.py`, `test_database.py`, `test_integration.py`
- `guachi.egg-info/`: 패키징 및 배포 정보
    - `PKG-INFO`, `SOURCES.txt`, `dependency_links.txt`, `top_level.txt`
- `docs/`: Sphinx 기반 문서화 관련 파일
    - `Makefile`: 문서 빌드 자동화
    - `build/`, `source/`: 문서 소스 및 빌드 결과물

## 목적
- 레거시 코드를 최신 환경에서 유지보수 및 확장할 수 있도록 별도 디렉터리에서 관리
- 테스트 및 문서화, 패키징 등 Python 프로젝트의 표준 구조를 따름
- 향후 코드 업그레이드, 리팩토링, 패키징 개선 작업을 이 디렉터리에서 진행

---

이 파일은 `upgraded` 폴더의 구조와 각 구성 요소의 역할을 빠르게 파악할 수 있도록 돕기 위해 작성되었습니다.