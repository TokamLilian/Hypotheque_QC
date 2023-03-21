import hypotheque
from hypotheque import *

def test():                                                                           #les differents tests unitaires
    
    def test_total_versements():
        assert total_versements(20) == 240,"Echec de versements pours 20 ans"
        assert total_versements(15) == 180,"Echec de versements pours 15 ans"
        assert total_versements(20) == 240
        assert total_versements(5) == 60,"Echec de versements pours 5 ans"
        assert total_versements(10) == 120
    
    def test_interet():
        assert interet(7.5) == 0.0062,"Echec le l'interet sur le taux 7.5"
        assert interet(5) == 0.0042,"Echec le l'interet sur le taux 5"
        assert interet(10) == 0.0083,"Echec le l'interet sur le taux 10"
        assert interet(6.5) == 0.0054
        assert interet(8) == 0.0067

    def test_total_interet():
        assert total_interet(240, 0.0062) == 0.2269
        assert total_interet(180, 0.0042) == 0.4703
        assert total_interet(240, 0.0083) == 0.1375,"Echec de l'interet total pour l'interet 0.0083"
        assert total_interet(60, 0.0054) == 0.7239,"Echec de l'interet total pour l'interet 0.0054"
        assert total_interet(120, 0.0067) == 0.4487,"Echec de l'interet total pour l'interet 0.0067"

    def test_versement():
        assert versement(90000, 0.0062, 0.2269) == 721.7695
    
        assert versement(100000, 0.0042, 0.4703) == 792.9016,"Echec du versement mensuel"
     
        assert versement(100000, 0.0083, 0.1375) == 962.3188
    
        assert versement(60000, 0.0054, 0.7239) == 1173.4879,"Echec du versement mensuel"   
   
        assert versement(65000, 0.0067, 0.4487) == 789.951,"Echec du versement mensuel"

    test_total_versements()
    test_interet()
    test_total_interet()
    test_versement()

test()