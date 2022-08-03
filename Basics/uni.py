for i in range(1000, 16000):
    print(f'{i} : {chr(i)}', end='\t\t')
    if i%10==0:
        print()