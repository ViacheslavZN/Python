import sys

param=sys.argv[1] if len(sys.argv) > 1 else '.'
with open ('sales_data.csv','a',encoding='utf-8') as f:
    param_1=''.join(param)
    f.write(param_1)

# Read file
import sys

param=len(sys.argv[1]) if len(sys.argv) > 1 else '.'
if param==1:
    with open ('sales_data.csv','a',encoding='utf-8') as f:
        content=f.read()
        print(content,end=' ')
elif param==2:
    with open('sales_data.csv', 'r', encoding='utf-8') as f:
        for line in f:
            content=f.readlines()[int(argv[1])-1:]
            print(content, end=' ')






