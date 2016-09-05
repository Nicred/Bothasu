def mb(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

@mb
def ho():
    return "hihihiHH";

print (ho);
