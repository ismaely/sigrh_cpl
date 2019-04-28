import json

SUSPENSAO = {
('1 Mes de Cadeia', '1 Mes de Cadeia'),
('2 Mes de Cadeia', '2 Mes de Cadeia'),
('3 Mes de Cadeia', '3 Mes de Cadeia'),
('1 Ano de Cadeia', '1 Ano de Cadeia'),
('2 Ano de Cadeia', '2 Ano de Cadeia'),
('Retirada da Patente', 'Retirada da Patente'),
('outro', 'outro'),
('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza'),

}


REFORMA_ANTICIPADA = (
    ('', ''),
    ('Anticipada', 'Anticipada'),
)

CARGOS_POLICIAL = (
    ('Delegado', 'Delegado'),
    ('Investigador', 'Investigador'),
    ('Auxiliar de Investigador', 'Auxiliar de Investigador'),
    ('Escrivão', 'Escrivão'),
    ('Perito Criminal', 'Perito Criminal'),
    ('perito Medico-Legista', 'perito Medico-Legista'),
)

PENAS_DISCIPLINAR = (
   ('Repreensão simples', 'Repreensão simples'),
   ('Repreensão registada', 'Repreensão registada'),
   ('Patrulha, guarda e piquete até 5 mês', 'Patrulha, guarda e piquetes até 5 mês'),
   ('Rondas, guarda e piquete até 5 mês', 'Ronda, guarda e piquetes até 5 mês'),
   ('Multa correspondente a 1 dia', 'Multa correspondente a 1 dia'),
   ('Multa correspondente a 20 dias', 'Multa correspondente a 20 dias'),
   ('Detenção até 25 dias', 'Detenção até 25 dias'),
   ('Prisão até 15 dias', 'Prisão até 15 dias'),
   ('Prisão até 30 dias', 'Prisão até 30 dias'),
   ('Prisão até 45 dias', 'Prisão até 45 dias'),
   ('Despromoção', 'Despromoção'),
   ('Delegado', 'Delegado'), 
)

MOTIVO_DISCILINAR = (
    ('Homicído', 'Homicído'),
    ('Desvio de informação', 'Desvio de informação'),
    ('Calúnia e Difamação', 'Calúnia e Difamação'),
    ('Ausência', 'Ausência'),
    ('Desacato a Lei', 'Desacato a Lei'),
    ('Outro', 'Outro'),
    

)


CATEGORIA_USUARIO = (
    ('Agente', 'Agente'),
    ('Gestor', 'Gestor'),
    ('Admin', 'Administrador'),
)

AREA_TRABALHO = (
    ('Gestor', 'Gestor'),
    ('Formacao', 'Formação'),
    ('Pessoal-Quadro', 'Pessoal e Quadro'),
    ('Admin', 'Administrador'),
)


RAZAO_DA_POSSE = (
    ('Bolsa Interna', 'Bolsa Interna'),
    ('Bolsa Externa', 'Bolsa Externa'),
)


INSTITUICAO = (
    ('Centro Polivalente Nzoji', 'Centro Polivalente Nzoji'),
    ('Escola Nacional de Policia de Ordem Publica', 'Escola Nacional de Policia de Ordem Publica'),
    ('Escola Nacional de Policia de protecção e Intervenção', 'Escola Nacional de Policia de protecção e Intervenção'),
    ('Instituto Superior de Ciências Policias e Criminais', 'Instituto Superior de Ciências Policias e Criminais'),
    ('Instituto Médio de Ciências Policias', 'Instituto Médio de Ciências Policias'),
)


CURSOS_POLICIAL = (
   ('Agente de Vigilância e Escolta', 'Agente de Vigilância e Escolta'),
   ('Técnico de Inteligência', 'Técnico de Inteligência'),
   ('Agente de Inteligência', 'Agente de Inteligência'),
   ('Escrivão de policia', 'Escrivão de policia'),
   ('Perito Criminal Geral', 'Perito Criminal Geral'),
   ('Investigador de Policia Civil', 'Investigador de Policia Civil'),
   ('Auxiliar de Perícia Médica', 'Auxiliar de Perícia Médica'),
   ('Agente de Segurança Penitenciária', 'Agente de Segurança Penitenciária'),
   ('Noções de Direitos Humanos', 'Noções de Direitos Humanos'),
   ('Pilotagem', 'Pilotagem'),
   ('Auditoria', 'Auditoria'),
   ('Exercícios de Direito Administrativo', 'Exercícios de Direito Administrativo'), 
)



PAIS_PRESPECTIVA = (
    (' ', ' '),
    ('Africa do Sul', 'Africa do Sul'),
    ('Afeganistão', 'Afeganistão'),
    ('Albânia', 'Albânia'),
    ('Alemanha', 'Alemanha'),
    ('Andorra', 'Andorra'),
    ('Argélia', 'Argélia'),
    ('Argentina', 'Argentina'),
    ('Austrália', 'Austrália'),
    ('Bélgica', 'Bélgica'),
    ('Bolívia', 'Bolívia'),
    ('Brasil', 'Brasil'),
    ('Botsuana', 'Botsuana'),
    ('Cabo Verde', 'Cabo Verde'),
    ('Canada', 'Canada'),
    ('China', 'China'),
    ('Costa Rica', 'Costa Rica'),
    ('cuba', 'cuba'),
    ('Espanha', 'Espanha'),
    ('Estados Unidos', 'Estados Unidos'),
    ('França', 'França'),
    ('Gabão', 'Gabão'),
    ('Grécia', 'Grécia'),
    ('Holanda', 'Holanda'),
    ('Russia', 'Russia'),
    
)



GENERO = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
)



APROVEITAMENTO = (
    ('Desistente', 'desistente'),
    ('Reprovado', 'reprovado'),
    ('Aprovado', 'aprovado'),
)



ESTADO_CIVIL = (
    ('Solteiro (a)', 'solteiro (a)'),
    ('Casado (a)', 'casado (a)'),
    ('Divorciado (a)', 'Divorciado (a)'),
    ('Viuvo (a)', 'viuvo (a)'),

)



ORGAO_COMANDOS = (
    ('Comando-Geral', 'Comando-Geral'),
    ('Comando Provincial de Luanda', 'Comando Provincial de luanda'),
    ('Comando Provincial do Huambo', 'Comando Provincial do Huambo'),
    ('Comando Provincial do Bengo', 'Comando Provincial do Bengo'),
    ('Comando Provincial do Kuanza Sul', 'Comando Provincial do Kuanza Sul'),
    ('Comando Provincial do Kuanza Norte', 'Comando Provincial do Kuanza Norte'),
    ('Comando Provincial da Huila', 'Comando Provincial da Huila'),
    ('Comando Provincial da Lunda Norte', 'Comando Provincial da Lunda Norte'),
    ('Comando Provincial do Cunene', 'Comando Provincial do Cunene'),
    ('Comando Provincial do Uige', 'Comando Provincial do Uige'),
    ('Comando Provincial de Cabinda', 'Comando Provincial de Cabinda'),
    ('Comando Provincial do Namibe', 'Comando Provincial do Namibe'),
    ('Comando Provincial do Moxico', 'Comando Provincial do Moxico'),
    ('Comando Provincial do Bie', 'Comando Provincial do Bie'),
    ('Comando Provincial de Benguela', 'Comando Provincial de Benguela'),
    ('Comando Provincial do Malanje', 'Comando Provincial de Malanje'),
    ('Comando Provincial do Zaire', 'Comando Provincial do Zaire'),

)



PATENTE = (
    ('Agente-1ª-Classe', 'Agente 1ª Classe'),
    ('Agente-2ª-Classe', 'Agente 2ª Classe'),
    ('Agente-3ª-Classe', 'Agente 3ª Classe'),
    ('1ª-Subchefe', '1ª subchefe'),
    ('2ª-Subchefe', '2ª Subchefe'),
    ('3ª-Subchefe', '3ª Subchefe'),
    ('Inspector', 'Inspector'),
    ('Sub-inspetor', 'Sub-inspetor'),
    ('Inspector-chefe', 'Inspector-chefe'),
    ('Intendente', 'Intendente'),
    ('Superintendente', 'Superintendente'),
    ('Sub-comissário', 'Sub-comissário'),
    ('Comissário-geral', 'Comissário geral'),
    ('Comissário-chefe', 'Comissário chefe'),
)



DOCUMENTO_CATEGORIA = (
    ('Guia de Marcha', 'Guia de Marcha'),
    ('Mensagem', 'Mensagem'),
    ('Plano de Trabalho', 'Plano de Trabalho'),
    ('Officios', 'Officios'),
    ('Mapas', 'Mapas'),
    ('Declarações', 'Declarações'),
    ('Informações', 'Informações'),
    ('Propostas', 'Propostas'),
    ('Actas', 'Actas'),
    ('Relatórios', 'Relatórios'),
    ('Diversos', 'Diversos'),
)


PROVINCIA = (
    ('Luanda', 'Luanda'),
    ('Bengo', 'Bengo'),
    ('Benguela', 'Benguela'),
    ('Bié', 'Bié'),
    ('Cabinda', 'Cabinda'),
    ('Cunene', 'Cunene'),
    ('Huambo', 'Huambo'),
    ('Huila', 'Huila'),
    ('Cuando kubango', 'Cuando kubango'),
    ('Cuanza norte', 'Cuanza norte'),
    ('Cuanza sul', 'Cuanza sul'),
    ('Lunda Norte', 'Lunda Norte'),
    ('Lunda sul', 'Lunda sul'),
    ('Malange', 'Malange'),
    ('Moxico', 'Moxico'),
    ('Namibe', 'Namibe'),
    ('Uige', 'Uige'),
    ('Zaire', 'Zaire'),
)



MOTIVO_BAIXA = (
    ('Reforma', 'Reforma'),
    ('Demissão', 'Demissão'),
    ('Transferência', 'Transferência'),
    ('Falecimento', 'Falecimento'),
    ('Dificiência Contraída', 'Dificiência Contraída'),
    ('Invalidez', 'Invalidez'),
    ('Outro', 'Outro'),
)


INVALIDEZ = (
    ('', ''),
    ('Permanente', 'Permanente'),
    ('Parcial', 'Parcial'),
)

NOMIACAO_TIPO = (
    ('Indicação', 'Indicação'),
    ('Nomeação', 'Nomeação'),
)


MOTIVO_REFORMA = (
    ('Acidente', 'Acidente'),
    ('Dificiência Contraída', 'Dificiência Contraída'),
    ('Outro', 'Outro'),
)


NOMIACAO_CATEGORIA = (
    ('Graduação', 'Graduação'),
    ('Promoção', 'Promoção'),
)


MOTIVO_DESPROMOCAO = (
    ('Indisciplina', 'Indisciplina'),
    ('Homicído', 'Homicído'),
    ('Desvio de informação', 'Desvio de informação'),
    ('Calúnia e Difamação', 'Calúnia e Difamação'),
    ('Outras', 'Outras'),
)



IDADE_LIMITE = (
    ('50', 'Idade-> 50'),
    ('55', 'Idade-> 55'),
    ('60', 'Idade-> 60'),
    ('65', 'Idade-> 65'),
    ('69', 'Idade-> 69'),
)


IDADE_INTERVALOS = (
    (' ', ' '),
    ('18-20', 'Idade-> 18 a 20'),
    ('20-25', 'Idade-> 20 a 25'),
    ('25-30', 'Idade-> 25 a 30'),
    ('30-25', 'Idade-> 30 a 35'),
    ('35-40', 'Idade-> 35 a 40'),
    ('40-45', 'Idade-> 40 a 45'),
    ('45-50', 'Idade-> 45 a 50'),
    ('50-55', 'Idade-> 50 a 55'),
    ('55-60', 'Idade-> 55 a 60'),
    ('60-65', 'Idade-> 60 a 65'),
    ('65-70', 'Idade-> 65 a 70'),
    ('70-75', 'Idade-> 70 a 75'),
)

NIVEL_ACADEMICO = (
    ('9ªClasse', '9ª Classe'),
    ('12ªClasse', '12ª Classe'),
    ('13ªClasse', '13ª Classe'),
    ('Têcnico Medio', 'Têcnico Médio'),
    ('Licenciado', 'Licenciado'),
    ('Mestre', 'Mestre'),
    ('Doutor', 'Doutor'),
)


SITUACAO_TRANSFERENCIA = (
    ('Espera', 'Espera'),
    ('Autorizado', 'Autorizado'),
)


TIPO_LISTA_FORMACAO = (
    ('formacao', 'Selecionado para formação'),
    ('Desistente', 'Agentes desistentes'),
    ('Reprovado', 'Agentes reprovados'),
    ('Aprovado', 'Agentes aprovados'),
)


MENU_PESSOAL_QUADRO = {
    'pessoalQuadro': json.dumps(True),
    }

MENU_ESTATISTICA = {
    'estatistcas': json.dumps(True)
    }

MENU_FORMACAO = {
    'formacaoes': json.dumps(True)
    }

MENU_TRANSFERENCIA = {
    'transferencias': json.dumps(True)
    }

MENU_DOCUMENTO = {
    'documentos': json.dumps(True)
    }

MENU_UTILIZADOR = {
    'utilizadores': json.dumps(True)
    }


MENU_PERFIL = {
    'perfil': json.dumps(True)
    }
