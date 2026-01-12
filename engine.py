class MotorInferência:
    def __init__(self):
        # Base de Conhecimento: Regras SE-ENTÃO [cite: 19]
        self.regras = [
            {"se": {"biotipo": "Ectomorfo", "objetivo": "Resistência"}, "então": "Maratona ou Ciclismo"},
            {"se": {"biotipo": "Ectomorfo", "objetivo": "Agilidade"}, "então": "Basquete ou Salto em Altura"},
            {"se": {"biotipo": "Mesomorfo", "objetivo": "Força"}, "então": "Musculação Tradicional ou Powerlifting"},
            {"se": {"biotipo": "Mesomorfo", "objetivo": "Explosão"}, "então": "Crossfit ou Sprint (100m)"},
            {"se": {"biotipo": "Endomorfo", "objetivo": "Força"}, "então": "Strongman ou Rugby"},
            {"se": {"biotipo": "Endomorfo", "objetivo": "Perda de Peso"}, "então": "Natação ou Lutas (Jiu-Jitsu)"},
        ]

    def inferir(self, fatos):
        # Motor de inferência aplicando as regras sobre os fatos 
        # Implementação de Encadeamento para Frente simples
        recomendacoes = []
        for regra in self.regras:
            match = True
            for chave, valor in regra["se"].items():
                if fatos.get(chave) != valor:
                    match = False
                    break
            if match:
                recomendacoes.append(regra["então"])
        
        return recomendacoes if recomendacoes else ["Caminhada e consulta com especialista"]