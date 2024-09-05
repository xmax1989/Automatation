import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize('string, result', [ 
    ("москва", "Москва"), 
    ("астрахань", "Астрахань"), 
    ("astana", "Astana"),
    ("london", "London")      
    ] )
@pytest.mark.test_positive
def test_positive_capitilize(string, result):
    res = string_utils.capitilize(string)
    assert res == result
    
@pytest.mark.parametrize('string, result', [ 
    ("Минск", "Минск"),    #негатив текст введен с большой буквы
    ("999", "999"),        #негатив введены цифры 
    ("   ", "   "),        #негатив пробелы в поле       
    ("$$$", "$$$"),        #негатив спецсимволы
    ("ди ван", "Ди ван"),  #негатив пробелы в тексте
    ("","") ],              #негатив пустое поле
    [] )                #негатив пустой список
def test_negative_capitilize(string, result):
    res = string_utils.capitilize(string)
    assert res == result


@pytest.mark.test_positive
def test_positive_trim():
    assert string_utils.trim(" water") == "water"
    assert string_utils.trim("     water") == "water"
    assert string_utils.trim(" water ") =="water "
    
def test_negative_trim():   
    assert string_utils.trim("water") == "water"  #негатив без пробела
    assert string_utils.trim("") == ""            #негатив пустое поле
    assert string_utils.trim("   ") == ""         #негатив пробелы в поле

@pytest.mark.xfail()    
def test_negative_trim():       
    assert string_utils.trim(12345) == "12345"  #негатив введены цифры
    

@pytest.mark.test_positive
def test_positive_to_list():
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3:4", ":") == ["1", "2", "3", "4"]
    assert string_utils.to_list("а,б,в,г") == ["а", "б", "в", "г"]
    assert string_utils.to_list("это,просто,длинный,текст") == ["это","просто","длинный","текст"]
    
def test_negative_to_list():
    assert string_utils.to_list("a;b;c;d", ";") == ["a", "b", "c", "d"] #негатив меняем разделитель
    assert string_utils.to_list("a b c d", " ") == ["a", "b", "c", "d"] #негатив меняем разделитель
    assert string_utils.to_list("a!b!c!d", "!") == ["a", "b", "c", "d"] #негатив меняем разделитель
    
@pytest.mark.xfail()
def test_negative_to_list():    
    assert string_utils.to_list("abcd", "") == ["abcd"]                 #негатив пустой разделитель



@pytest.mark.test_positive
def test_positive_contains():
    assert string_utils.contains("SkyPro", "S")
    assert string_utils.contains("Скайпро", "С")
    assert string_utils.contains("SkyPro Super", "e")
    assert string_utils.contains("SkyPro2024", "0")
    assert string_utils.contains("SkyPro Super", " ")
    
@pytest.mark.xfail()
def test_negative_contains():
    assert string_utils.contains("SkyPro Super", "b") #негатив отсутствующий символ
    assert string_utils.contains("SkyPro2024", "7")   #негатив отсутствующий символ
    assert string_utils.contains("SkyPro", "s")       #негатив другой регистр
    assert string_utils.contains("     ", " ")        #негатив пробелы в поле
    assert string_utils.contains("", "")              #негатив пустые поля


@pytest.mark.test_positive
def test_positive_delete_symbol():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro2024", "20") == "SkyPro24"
    assert string_utils.delete_symbol("SkyPro", "SkyPro") == ""
    assert string_utils.delete_symbol("SkyPro 2024", " ") == "SkyPro2024"
    
@pytest.mark.xfail()
def test_negative_delete_symbol():
        assert string_utils.delete_symbol("SkyPro", "M") == "SkyPro"    #негатив отсутствующий символ
        assert string_utils.delete_symbol("S", "S") == ""               #негатив единственный символ
        assert string_utils.delete_symbol("SSSS", "S") == ""            #негатив одинаковые символы
        

@pytest.mark.test_positive
def test_positive_starts_with():
    assert string_utils.starts_with("SkyPro", "S")
    assert string_utils.starts_with("2024SkyPro", "2")
    assert string_utils.starts_with(" SkyPro", " ")
    assert string_utils.starts_with("-SkyPro", "-")
    assert string_utils.starts_with("_SkyPro", "_")
    assert string_utils.starts_with("СкайПро", "С")

@pytest.mark.xfail()
def test_negative_starts_with():
    assert string_utils.starts_with("SkyPro", "N")    #негатив отсутствующий символ
    assert string_utils.starts_with("SkyPro", "s")    #негатив другой регистр
    assert string_utils.starts_with("", "")           #негатив пустые поля
    assert string_utils.starts_with("     ", " ")     #негатив пробелы в поле


@pytest.mark.test_positive
def test_positive_end_with():
    assert string_utils.end_with("SkyPro", "o")
    assert string_utils.end_with("SkyPro2024", "4")
    assert string_utils.end_with("SkyPro ", " ")
    assert string_utils.end_with("SkyPro_", "_")
    assert string_utils.end_with("SkyPro-", "-")
    assert string_utils.end_with("СкайПро", "о")

@pytest.mark.xfail()
def test_negative_end_with():
    assert string_utils.end_with("SkyPro", "B")    #негатив отсутствующий символ
    assert string_utils.end_with("SkyPro", "O")    #негатив другой регистр
    assert string_utils.end_with("", "")           #негатив пустые поля
    assert string_utils.end_with("    ", " ")      #негатив пробелы в поле
    assert string_utils.end_with("SkyPro", "r")    #негатив непоследний символ


@pytest.mark.test_positive
def test_positive_is_empty():
    assert string_utils.is_empty("")
    assert string_utils.is_empty(" ")
    assert string_utils.is_empty("                 ")
    assert string_utils.is_empty("                                                      ")

@pytest.mark.xfail()
def test_negative_is_empty():
    assert string_utils.is_empty("SkyPro")       #негатив не пустая строка
    assert string_utils.is_empty("_")            #негатив не пустая строка
    assert string_utils.is_empty("____")         #негатив не пустая строка
    assert string_utils.is_empty("---")          #негатив не пустая строка
    assert string_utils.is_empty("S")            #негатив не пустая строка
    assert string_utils.is_empty("СкайПро")      #негатив не пустая строка
    assert string_utils.is_empty("0")            #негатив не пустая строка
    assert string_utils.is_empty("01234")        #негатив не пустая строка


@pytest.mark.parametrize('string, result',[
    ([1,2,3,4], "1, 2, 3, 4"),
    (["S","k","y","P","r","o"],"S, k, y, P, r, o"),
    (["Скай","Про"],"Скай, Про")
    ])
@pytest.mark.test_positive
def test_positive_list_to_string(string, result):
    res = string_utils.list_to_string(string)
    assert res == result

@pytest.mark.test_positive
def test_positive_list_to_string():
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"                 #позитивные менияем разделитель
    assert string_utils.list_to_string(["Sky", "Pro"], "!") == "Sky!Pro"                 #позитивные менияем разделитель
    assert string_utils.list_to_string(["Sky", "Pro"], "_") == "Sky_Pro"                 #позитивные менияем разделитель
    assert string_utils.list_to_string(["Sky", "Pro"], " ") == "Sky Pro"                 #позитивные менияем разделитель
    assert string_utils.list_to_string(["S","k","y", "P","r","o"], "-") == "S-k-y-P-r-o" #позитивные менияем разделитель
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"                 #позитивные менияем разделитель
    assert string_utils.list_to_string([1,2,3,4,], "0") == "1020304"                     #позитивные менияем разделитель

@pytest.mark.xfail()
def test_negative_list_to_string():
    assert string_utils.list_to_string([], "-") == ""                         #негатив пустой спискок
    assert string_utils.list_to_string(["Sky", "Pro"], "") == "SkyPro"        #негатив пустой разделитель
    assert string_utils.list_to_string(["", ""], "-") == "-"                  #негатив пустые поля в списке
    assert string_utils.list_to_string(["   ", "   "], "") == "   -   "       #негатив пробелы в списке

















