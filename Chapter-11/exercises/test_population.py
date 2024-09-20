from EX_11_2_population import city_function

def test_city_country():
    '''Testa se o resultado será como a sentença assert'''
    formated_name=city_function('santiago', 'chile', '5000000')
    assert formated_name=='Santiago, Chile - Population 5000000'
