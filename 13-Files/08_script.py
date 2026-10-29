js_code = '''
console.log('Hola desde un archivo JS generado con Python')

const suma = (a, b) => {
    return a + b
}
'''

with open('script.js', mode='w') as file:
    file.write(js_code)

with open('script.js', mode='r') as file:
    print(file.read())