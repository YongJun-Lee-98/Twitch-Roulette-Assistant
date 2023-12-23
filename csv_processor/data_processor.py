import pandas as pd

class DataProcessor:
    @staticmethod
    def update_csv(csv_path):
        new_file_path = 'processed_input.csv'
        with open(csv_path, 'r', encoding='utf-8') as file, open(new_file_path, 'w', encoding='utf-8') as new_file:
            first_line = True
            for line in file:
                if first_line:
                    # 첫 번째 줄(헤더)은 그대로 씁니다.
                    new_file.write(line)
                    first_line = False
                else:
                    # 줄을 쉼표로 구분합니다.
                    parts = line.split(',')
                    # 네 번째 쉼표 이후의 텍스트를 큰따옴표로 묶습니다.
                    modified_line = ','.join(parts[:4]) + ',"' + ','.join(parts[4:]).strip() + '"\n'
                    # 수정된 줄을 새 파일에 씁니다.
                    new_file.write(modified_line)
        return pd.read_csv(new_file_path)
    
    @staticmethod
    def clean_message_column(df):
        # '- '와 그 앞의 텍스트를 제거
        df[' Message'] = df[' Message'].str.replace('.*?-\s*', '', regex=True)
        df[' Message'] = df[' Message'].str.split(',').apply(lambda x: [i.strip() for i in x])
        return df

    @staticmethod
    def create_new_dataframe(df):
        new_df = pd.DataFrame({
            ' Account': df[' Account'],
            ' Name': df[' Name'],
            ' Message': df[' Message']
        })
        return new_df.explode(' Message')

    @staticmethod
    def count_messages(new_df):
        return new_df.groupby([' Account', ' Name', ' Message']).size().reset_index(name='Count')