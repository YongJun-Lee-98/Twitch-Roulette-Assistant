import pandas as pd

class DataProcessor:
    @staticmethod
    def load_csv_to_dataframe(csv_path):
        return pd.read_csv(csv_path)

    @staticmethod
    def clean_message_column(df):
        df[' Message'] = df[' Message'].str.replace('뽑기 후원 -', '')
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
