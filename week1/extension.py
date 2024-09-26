x = input("file name:").lower().strip()
i = x.rfind('.')
extension = x[i+1 : len(x)]

if extension == 'gif':
    print('image/gif') 
elif extension == 'jpg' or extension =='jpeg':
    print('image/jpeg')
elif extension =='png':
    print('image/png')
elif extension =='txt':
    print('text/plain')
elif extension =='pdf':
    print('application/pdf')
elif extension =='zip':
    print('application/zip')
else:
    print('application/octet-stream')