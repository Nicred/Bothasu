def mb(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def mi(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
 

def hello():
    return "hello habr"
op = (mb(mi(hello)));
print (op);

