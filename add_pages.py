import requests
import os
from dotenv import load_dotenv
import json
from time import sleep as s

load_dotenv(r'/home/aarjav/Documents/Automation Programs/add_pages.env')
NOTION_TOKEN = os.getenv('NOTION_TOKEN')

phy_chaps = '''- Complex numbers
quadratic equations
- Matrices & determinants
- Sets & relations
- Functions
- Mathematical induction
- Permutations & combinations
- Probability
- Mathematical reasoning
- Limits, continuity & differentiability
Method of Differentiation
- Applications of Derivatives
- Indefinite integration
- Definite integration
- Area under the curve
- Three-dimensional geometry
- Differential equations
- Binomial theorem
- Sequence & Series
- Vector algebra
- Statistics
- Compound Angles
- Inverse Trigonometric Functions
Properties of triangles
Straight lines
Circles
Conic sections'''

phy_chaps = phy_chaps.split('\n')
phy_chaps.reverse()
for i in phy_chaps:
    i = i.title().replace('And', 'and').replace('Of', 'of').replace('- ', '')
    data = { "parent": { "database_id": "c54c09c01b734c0a935dae00e00cac54" }, "properties": { "Chapter": { "title": [ { "text": { "content": i } } ] }, "Subject": { "select": { "name": 'Mathematics' } }, "Prep Level": { "select": { "name": "A-" } } } }
    data = json.dumps(data)
    headers = {
    'Authorization': f"Bearer {NOTION_TOKEN}",
    'Notion-Version': '2022-02-22',
    'Content-Type': 'application/json',
    }
    response = requests.post('https://api.notion.com/v1/pages', headers=headers, data=data)
    print(response.text)