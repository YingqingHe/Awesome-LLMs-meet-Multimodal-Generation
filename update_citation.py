import requests
import re
import json
import json

def save_citation_json():
    # Open and read the README.md file
    with open('README.md', 'r') as file:
        readme_content = file.read()

    # Extracting paper IDs
    paper_ids = re.findall(r"https://www.semanticscholar.org/paper/[^/]+/(\w{40})", readme_content)


    # Define the list of paper IDs
    # paper_ids = ['8f0a24d1678e4d0e584b0932196cd257d5c53c7d', 'another_paper_id', ...]  # Add more paper IDs
    api_key = 'cviF8wQpWXmGBYiyTugi9LR14F0JICV4D0jMRYcb'
    # Specify the headers, if any, for the GET request
    headers = {
        'x-api-key': api_key
    }


    # Initialize an empty list to collect dictionaries
    data_dict = {}
    # print(paper_ids)
    # exit()
    # Iterate over each paper ID
    for paper_id in paper_ids:
        # Construct the request URL
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=citationCount"
        # Send the GET request
        response = requests.get(url, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            # Convert the response to JSON format
            data = response.json()
            # Append the dictionary to the list
            data_dict[data['paperId']] = data['citationCount']
    # Write the dictionary to a JSON file
    with open('citation.json', 'w') as f:
        json.dump(data_dict, f, indent=4)


def updata_readme():
    # 读取存储有citation计数的JSON文件
    with open('citation.json', 'r') as f:
        citation_data = json.load(f)

    readme_path = 'README.md'  # README文件路径
    new_lines = []  # 存储修改后的文件内容

    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 遍历每一行，寻找特定格式的行并进行替换
    for line in lines:
        if '[![citation]' in line and 'semanticscholar.org/paper/' in line:
            paper_id = line.split('/')[-1][:40]
            citation_count = citation_data.get(paper_id, 'N/A')  # 如果找不到则返回'N/A'
            print(f'paper_id:{paper_id}')
            print(f'citation_count:{citation_count}')
            new_citation_tag = f'[![citation](https://img.shields.io/badge/citation-{citation_count}-blue.svg?paper={paper_id})](https://www.semanticscholar.org/paper/{paper_id})'
            
            # 替换行中的内容
            new_line = line[:line.find('[![citation]')] + new_citation_tag + '\n'
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # 将修改后的内容写回README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
 
if __name__ == "__main__":
    save_citation_json()
    updata_readme()