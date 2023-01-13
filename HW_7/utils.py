
def get_avr(file, access):
    file_one = open(file, access)
    f = file_one.readlines()
    sum_h = 0
    sum_w = 0
    count = 0
    res = f'''<div>
            <pre><span style="font-size: 36px;"> средний рост и средний вес (в см и кг соответственно) для студентов из файла {file}:</span></pre>
            <ul>'''
    for lines in f[1::]:
        l = lines.replace(',', '').rstrip('\n')
        l = l.split(' ')
        if l[0] != '':
            sum_h += float(l[1])
            sum_w += float(l[2])
            count += 1
    res = res + '''        </li>
        <li style="color: rgb(65, 168, 95); font-size: 30px;">
            <pre><strong>''' + f'средний рост: {round(sum_h / count * 2.54, 2)} см' + '\n' + f'средний вес: {round(sum_w / count * 0.453592, 2)} кг' + '''</strong></pre>''' + '''
    </li>
    </ul>
    <pre>

</pre>
</div>'''
    file_one.close()
    return res

