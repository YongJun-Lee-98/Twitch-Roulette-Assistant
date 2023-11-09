from multiprocessing import Pool
from csv_processor import logger
import csv_processor
import multiprocessing

# 로깅 설정
logger.setup_logging()
log_message = logger.get_logger()

# 각 CSV 파일에 대한 처리를 병렬로 실행할 함수
def process_csv_file(csv_path):
    log_message.info(f"Processing file {csv_path}")
    try:
        df = csv_processor.DataProcessor.load_csv_to_dataframe(csv_path)
        df = csv_processor.DataProcessor.clean_message_column(df)
        new_df = csv_processor.DataProcessor.create_new_dataframe(df)
        result = csv_processor.DataProcessor.count_messages(new_df)
        csv_processor.ExcelGenerator.generate_excel(result, csv_path)
        log_message.info(f"Completed processing file {csv_path}")
    except Exception as e:
        log_message.error(f"Error with file {csv_path}: {e}")

def main():
    print("프로그램이 실행 중입니다.")
    log_message.info("Main process started.")
    with Pool(processes=4) as pool:
        csv_paths = csv_processor.FileSelector.select_csv_files()
        pool.map(process_csv_file, csv_paths)  # 병렬 처리를 시작합니다.
        pool.close()  # 병렬 처리가 끝나면 풀을 닫습니다.
        pool.join()  # 모든 프로세스가 끝날 때까지 기다립니다.
    log_message.info("Main process finished.")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()