def text_to_html(file, access):
    file_one = open(file, access)
    res = f'''<div>
    <pre><span style="font-size: 36px;">{file}:</span></pre>
    <ol>'''
    for text in file_one:
        res = res + '''        </li>
        <li style="color: rgb(65, 168, 95); font-size: 30px;">
            <pre><strong>''' + text + '''</strong></pre>'''
    res = res + '''        </li>
    </ol>
    <pre>

</pre>
</div>'''
    file_one.close()
    return res