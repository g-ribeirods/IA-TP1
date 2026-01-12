from owlready2 import *

class MotorInferência:
    def __init__(self):
        # Carrega a ontologia do arquivo local
        self.onto = get_ontology("esporte.owl").load()
        sync_reasoner() # Ativa o raciocinador

    def inferir(self, fatos):
        biotipo_informado = fatos.get("biotipo")
        
        # Busca a classe correspondente na ontologia
        classe_biotipo = self.onto.search_one(is_a=self.onto.Biotipo, name=biotipo_informado)
        
        recomendacoes = []
        if classe_biotipo:
            # Busca esportes relacionados via propriedade 'tem_recomendacao'
            for esporte in classe_biotipo.tem_recomendacao:
                recomendacoes.append(esporte.name)
        
        return recomendacoes if recomendacoes else ["Consulte um especialista"]