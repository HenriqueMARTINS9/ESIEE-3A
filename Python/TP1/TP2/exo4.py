count = 0

def decorateur(function) :
    global count
    count = count + 1
    print(count)
    function()
    return function

for i in range(10) :
    @decorateur
    def do():
        print("something")




    