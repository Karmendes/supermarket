from src.etl.factory import create_etl
if __name__ == '__main__':
    etl = create_etl('zona_sul')
    etl.run()