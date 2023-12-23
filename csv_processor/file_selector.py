from tkinter import filedialog
from tkinter import Tk  # 추가: Tk를 사용하여 루트 윈도우를 숨깁니다.

class FileSelector:
    @staticmethod
    def select_csv_files():
        """파일 선택 대화상자를 표시하고 선택된 CSV 파일들의 경로를 반환합니다.
        Returns:
            list: 선택된 파일들의 경로 목록.
        """
        root = Tk()  # 루트 윈도우 생성
        root.withdraw()  # 루트 윈도우를 화면에서 숨깁니다.
        csv_paths = filedialog.askopenfilenames(title="다운로드 된 csv 파일들을 선택하세요", filetypes=[("CSV files", "*.csv")])
        print("선택한 파일 경로들:", csv_paths)
        root.destroy()  # 루트 윈도우를 파괴하여 자원을 해제합니다.
        return csv_paths
