from EX_11_1_city_Country import city_function

def test_city_country():
    '''Testa se o resultado será como a sentença assert'''
    formated_name=city_function('santiago', 'chile')
    assert formated_name=='Santiago, Chile'
