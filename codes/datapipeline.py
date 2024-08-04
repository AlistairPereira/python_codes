def begin_coroutine(func):
    def inner_function(*args):
        result = func(*args)
        result.__next__()
        return result
    return inner_function

def data_pipeline_start(file, next_stage):
    while True:
        line = file.readline()
        if not line:
            break
        next_stage.send(line)
        
@begin_coroutine  
def filter_log(keyword,next_stage):
    while True:
        line = yield
        if keyword in line:
            next_stage.send(line)
            
@begin_coroutine
def db_insert():
    while True:
        line = yield
        print(f"storing {line} in db")

file = open(r"D:\git\bdp-apr24-classroom-bdp_apr24_all\codes\bible.txt")
data_pipeline_start(file,filter_log("God",db_insert()))