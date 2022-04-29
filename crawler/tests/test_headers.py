from crawler.header_creater.create_header import generate_header
from crawler.header_creater.user_agent_creator import *


test_map = {"android"}

test_header = generate_header(test_map)
print(test_header)
