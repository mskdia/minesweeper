# Python 지뢰찾기 (Windows)

간단한 Windows용 지뢰찾기 게임 (Tkinter 기반)

요구사항
- Python 3.6 이상 (권장 3.8+)
- 표준 라이브러리만 사용 (추가 패키지 불필요)

실행 방법
1. 이 저장소(또는 파일)를 받은 후 `minesweeper.py` 파일을 같은 폴더에 둡니다.
2. 명령 프롬프트에서 다음을 실행합니다:
   python minesweeper.py

조작 방법
- 왼쪽 클릭: 셀 열기 (첫 클릭은 안전함 — 첫 클릭 위치에 지뢰가 배치되지 않음)
- 오른쪽 클릭: 깃발 토글 (지뢰로 의심되는 위치 표시)
- 메뉴에서 난이도 선택: Easy / Medium / Hard / Custom
- Custom 선택 시 행, 열, 지뢰 개수를 직접 설정 가능

윈도우용 실행 파일(.exe) 만들기 (선택)
- PyInstaller 설치: `pip install pyinstaller`
- exe 생성:
  `pyinstaller --onefile --windowed minesweeper.py`
- 빌드 후 `dist/minesweeper.exe`를 실행 파일로 사용할 수 있습니다.

내가 한 일
- Tkinter 기반 GUI와 전체 게임 로직을 단일 파일로 제공했습니다.
- 첫 클릭 안전 보장, 플래그 기능, 재귀(영역) 자동 오픈, 승리/패배 처리, 타이머 및 남은 지뢰 카운터를 구현했습니다.

다음
- 원하시면 아이콘 추가, 테마(컬러/이미지), 고급 기능(하이라이트/레벨 저장 등)도 추가해 드립니다.
