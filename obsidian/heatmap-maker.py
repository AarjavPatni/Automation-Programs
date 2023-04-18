import os
import pendulum
import re
import webbrowser
from collections import OrderedDict as od

habits = od()

# open every md file and check if '- [ ] Today' is written
for root, dirs, files in os.walk('C:\\Users\\Aarjav\\Documents\\Second Brain\\Goals'):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                if ('day-one:' in content) and ('day-one: today' not in content):
                    habits[file] = dict()
                    habits[file]['path'] = os.path.join(root, file)

# For each habit, open it and calculate days passed since day-one
for habit in habits:
    with open(habits[habit]['path'], 'r', encoding='utf-8') as f:
        content = f.read()
        day_one = content.split('day-one:')[1].split('\n')[0].strip()
        day_one = pendulum.parse(day_one)
        try:
            skips_dates = content.split(
                'skips-dates:')[1].split('---')[0].strip().replace('- ', '').split('\n')
            skips_dates = list(filter(None, skips_dates))
        except Exception:
            skips_dates = []

        print(skips_dates)
        all_dates = [day_one.add(days=i).strftime('%Y-%m-%d')
                     for i in range((pendulum.now() - day_one).days + 1)]
        data = [1 if i not in skips_dates else 0 for i in all_dates]
        if '- [ ] Today' in content:
            data[-1] = 0
            habits[habit]['today'] = False
        else:
            habits[habit]['today'] = True
        # Get the difference between day_one the Sunday before it
        jugaad = [0 for i in range(day_one.day_of_week)]
        data = jugaad + data
        habits[habit]['data'] = data
        # format as dd mmmm 'yy
        habits[habit]['startDateText'] = day_one.strftime('%d %B %Y')

function = '\n\nfunction App() {\n'
# function = ''
colours = {
    'Awake on First Alarm.md': 'ffba08',  # golden
    'Workout.md': '7678ed',  # yellow green
    'Meditation.md': '7678ed',  # yellow green
    'Fiction.md': '29BF12',  # green
    'Guitar.md': 'ff8800',  # orange
    'Math Prep for College.md': '3a86ff',  # blue
    'Touch Typing.md': '00CCCC',  # turquoise
    'Laser Focus.md': 'f94144',  # red
    'Journaling.md': '06d6a0',  # aqua
    'Brush @ Night.md': 'f4978e',  # peach
    'Water Floss.md': 'f4978e'  # purple
}

for i in colours.keys():
    colours[i] = ', '.join(
        tuple(str(int(colours[i][k:k+2], 16)) for k in (0, 2, 4)))

order = tuple(i for i in colours.keys())

habits = {k: habits[k] for k in order if k in habits}

for i in habits:
    name = i.replace('.md', '').replace(
        ' ', '').replace('&', '').replace('@', '')
    function += f'''var {name}_data = {habits[i]['data']};
        var {name}_length = {name}_data.length;
        var {name}_startDate = moment().add(-{name}_length, 'days');
        var {name}_dateRange = [{name}_startDate, moment()];
        var {name}_data = Array.from(new Array({name}_length)).map(function (_, index) {{
            return {{
                date: moment({name}_startDate).add(index, 'day'),
                value: {name}_data[index]
            }};
    }});
'''

for num, i in enumerate(habits, 5):
    name = i.replace('.md', '').replace(
        ' ', '').replace('&', '').replace('@', '')
    title = i.replace('.md', '')
    if num == 5:
        function += f'''return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(Timeline, {{
        range: {name}_dateRange,
        data: {name}_data,
        colorFunc: function colorFunc(_ref{num}) {{
            var alpha = _ref{num}.alpha;
            return "rgba({colours[i]}, ".concat(alpha, ")");
        }},
        title: '{title}',
        startDateText: "{habits[i]['startDateText']} ({habits[i]['data'].count(1)})",
    }}),
'''
    else:
        function += f'''/*#__PURE__*/React.createElement(Timeline, {{
        range: {name}_dateRange,
        data: {name}_data,
        colorFunc: function colorFunc(_ref{num}) {{
            var alpha = _ref{num}.alpha;
            return "rgba({colours[i]}, ".concat(alpha, ")");
    }},
    title: '{title}',
    startDateText: "{habits[i]['startDateText']} ({habits[i]['data'].count(1)})",
    }}),
    '''

function += ');\n}'

navbar = '  <nav>\n    <ul>\n'

for i in habits:
    # nav_text = i.replace('.md', '') + \
    #     ' ✅' if habits[i]['today'] else i.replace('.md', '')
    title = i.replace('.md', '')
    navbar += f'      <li><a href="#{title}" style="color: #25a244">{title}</a></li>\n' if habits[
        i]['today'] else f'      <li><a href="#{title}">{title}</a></li>\n'

navbar += '\n    </ul>\n  </nav>'

with open(r'C:\Users\Aarjav\Documents\Automation-Programs\obsidian\heatmap.html', 'r', encoding='utf-8') as f:
    content = f.read()
    content = re.sub(
        r'function App\(\)\s*{((?:[^{}]+|{(?:[^{}]+|{[^{}]*})*})*)\s*}', function, content)
    content = re.sub(r'\s<nav>([\s\S]*?)<\/nav>', navbar, content)
    with open(r'C:\Users\Aarjav\Documents\Automation-Programs\obsidian\heatmap.html', 'w', encoding='utf-8') as f:
        f.write(content)

# open C:\Users\Aarjav\Documents\Automation-Programs\obsidian\heatmap.html
webbrowser.open(
    r'C:\Users\Aarjav\Documents\Automation-Programs\obsidian\heatmap.html')
