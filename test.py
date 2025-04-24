URL = [
    {"category": "육아/교육", "link": "/news/articleList.html?sc_section_code=S1N4&view_type=sm"},
    {"category": "여성/가족", "link": "/news/articleList.html?sc_section_code=S1N8&view_type=sm"},
    {"category": "오피니언", "link": "/news/articleList.html?sc_section_code=S1N6&view_type=sm"},
]

for i in range(len(URL)):
    print(URL[i]['category'])
    print(URL[i]['link'])
    print("=" * 30)