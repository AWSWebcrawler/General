from crawler.header_creater.create_header import generate_header



test_map = {'client': "android"}

test_header = generate_header(test_map)
print(test_header)
