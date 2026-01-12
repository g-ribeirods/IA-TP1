from owlready2 import *

onto = get_ontology("http://test.org/esporte.owl")

with onto:
    class Biotipo(Thing): pass
    class Ectomorfo(Biotipo): pass
    class Mesomorfo(Biotipo): pass
    class Endomorfo(Biotipo): pass

    class Objetivo(Thing): pass
    class Resistencia(Objetivo): pass
    class Forca(Objetivo): pass
    class Agilidade(Objetivo): pass
    class Explosao(Objetivo): pass
    class PerdaPeso(Objetivo): pass

    class Esporte(Thing): pass
    
    class tem_recomendacao(Biotipo >> Esporte): pass

    # Instâncias de Esportes
    maratona = Esporte("Maratona")
    musculacao = Esporte("Musculacao")
    natacao = Esporte("Natacao")
    rugby = Esporte("Rugby")
    basquete = Esporte("Basquete")
    crossfit = Esporte("Crossfit")

    # Regras básicas na Ontologia (Indivíduos de exemplo)
    Ectomorfo.tem_recomendacao = [maratona, basquete]
    Mesomorfo.tem_recomendacao = [musculacao, crossfit]
    Endomorfo.tem_recomendacao = [rugby, natacao]

onto.save(file="esporte.owl", format="rdfxml")