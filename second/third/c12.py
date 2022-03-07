'''
    注释
'''
print('name:' + __name__)
print('package:'+__package__ or '当前没有任何包名')
print('doc:' + (__doc__ or '当前无注释'))
print('file:'+__file__)