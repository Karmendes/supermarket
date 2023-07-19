from src.etl.factory import create_etl
if __name__ == '__main__':
    etl = create_etl('prix')
    etl.run()