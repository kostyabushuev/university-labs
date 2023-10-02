content_A = ''
content_B = ''

with open('./static/Sam7_5_a.txt', 'r') as file:
    content_A = file.read()

with open('./static/Sam7_5_b.txt', 'r') as file:
    content_B = file.read()

with open('./static/Sam7_5_a.txt', 'w') as file:
    file.write(content_B)

with open('./static/Sam7_5_b.txt', 'w') as file:
    file.write(content_A)