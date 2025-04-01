from flask import Flask, render_template, request

app = Flask(__name__)

# teamwork te yazdigimiz 'convert' fonksiyonu
def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    
    return num_to_roman

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form.get('number')  # Formdan gelen 'number' verisini al
        try:
            num = int(number)  # Sayıyı tam sayıya dönüştür
            if 1 <= num <= 3999:  # Geçerli bir aralıkta olup olmadığını kontrol et
                result = convert(num)  # Roman rakamına dönüştür
                
                # Kullanıcıya dönüştürülmüş sonucu ve girdiği sayıyı göster
                return render_template('result.html', 
                                       number_decimal=num, 
                                       number_roman=result,
                                       developer_name="seyma" )  
            else:
                # Hatalı giriş için uyarı
                return render_template('index.html', not_valid=True)
        except ValueError:
            # Sayı değilse hata
            return render_template('index.html', not_valid=True)
    
    # İlk kez sayfa açıldığında sadece formu göster
    return render_template('index.html', not_valid=False)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
