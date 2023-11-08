import pandas as pd
import os

class ExcelGenerator:
    @staticmethod
    def generate_excel(result, csv_path):
        
        """결과 데이터를 바탕으로 같은 이름의 CSV 파일명으로 엑셀 파일을 생성합니다.

        Args:
            result (DataFrame): 'Account', 'Name', 'Message', 'Count' 열을 포함한 pandas DataFrame.
            csv_path (str): 원본 CSV 파일의 경로.
        """
        
        # 파일 경로에서 순수 파일 이름만 추출 (확장자 제외)
        base_name = os.path.basename(csv_path)
        file_name, _ = os.path.splitext(base_name)

        # 추출한 파일 이름으로 Excel 파일명 생성
        excel_file = f'{file_name}.xlsx'
        writer = pd.ExcelWriter(excel_file)

        account_list = result[' Account'].unique()
        for account in account_list:
            df_account = result[result[' Account'] == account]
            df_account.set_index([' Account', ' Name'], inplace=True)
            df_account.to_excel(writer, sheet_name=account)

        # 엑셀 파일 저장
        writer._save()
        print(f'Excel 파일이 저장되었습니다: {excel_file}')

