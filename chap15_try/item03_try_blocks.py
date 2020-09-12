import time
from try_logger import logger


def read_file_timed(path):
    """ Return the content of the file at 'path' """
    start_time = time.time()
    
    try:
        file = open(path, mode="rb")
        print( f"Data (Binary) of {path} is { file.read() }" )
    except FileNotFoundError as error:
        logger.error( f"Error is {error}" )
    else:
        logger.info( f"If no error  close the file {path} " )
        file.close()
    finally:
        stop_time = time.time()
        delta_time = stop_time - start_time
        logger.info( f"Time required to open {path} is {delta_time} " )


if __name__ == '__main__':    
    read_file_timed( 'data.txt' )
    read_file_timed( 'data2.txt' )    
