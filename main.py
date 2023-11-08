from multiprocessing import Pool
import csv_processor
import multiprocessing

# 각 CSV 파일에 대한 처리를 병렬로 실행할 함수
def process_csv_file(csv_path):
    df = csv_processor.DataProcessor.load_csv_to_dataframe(csv_path)
    df = csv_processor.DataProcessor.clean_message_column(df)
    new_df = csv_processor.DataProcessor.create_new_dataframe(df)
    result = csv_processor.DataProcessor.count_messages(new_df)
    csv_processor.ExcelGenerator.generate_excel(result, csv_path)

def main():
    with Pool(processes=4) as pool:
        csv_paths = csv_processor.FileSelector.select_csv_files()
        pool.map(process_csv_file, csv_paths)  # 병렬 처리를 시작합니다.
        pool.close()  # 병렬 처리가 끝나면 풀을 닫습니다.
        pool.join()  # 모든 프로세스가 끝날 때까지 기다립니다.

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()