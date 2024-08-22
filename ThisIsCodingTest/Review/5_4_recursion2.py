def recursive_function(i):
    if i == 100:
        return

    print(i, 'th recursive function to', i+1, 'th recursive function')
    recursive_function(i+1)
    print(i, 'th recursive function fini')

recursive_function(1)
