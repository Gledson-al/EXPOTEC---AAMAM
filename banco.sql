CREATE DATABASE expotec_aamam;
USE expotec_aamam;

CREATE TABLE usuarios (
id_usuario INT AUTO_INCREMENT PRIMARY KEY,
nome_usuario VARCHAR(100) NOT NULL,
dt_nasc_usuario DATE,
email_usuario VARCHAR(100) UNIQUE,
data_cadastro_usuario DATE,
usuario_ativo BOOL,
genero_usuario VARCHAR(50)
);

CREATE TABLE remedios (
id_remedio INT AUTO_INCREMENT PRIMARY KEY,
nome_remedio VARCHAR(100) NOT NULL,
descricao_remedio VARCHAR(250) NOT NULL,
dosagem_remedio VARCHAR(50),
horario_remedio DATETIME,
tipo_remedio VARCHAR(50)
);

CREATE TABLE tratamentos (
id_tratamento INT AUTO_INCREMENT PRIMARY KEY,
nome_tratamento VARCHAR(100) NOT NULL,
descricao_tratamento VARCHAR(250) NOT NULL,
tipo_tratamento VARCHAR(50),
duracao_tratamento DATETIME,
data_cadastro_tratamento DATE,
fk_tratamento_remedios INT,
fk_tratamento_usuarios INT
);

CREATE TABLE contato_emergencia (
id_contato INT AUTO_INCREMENT PRIMARY KEY,
nome_contato VARCHAR(100) NOT NULL,
telefone_contato VARCHAR(15),
parentesco VARCHAR(50),
fk_ce_usuario INT
);

ALTER TABLE contato_emergencia ADD CONSTRAINT FOREIGN KEY (fk_ce_usuario)
REFERENCES usuarios(id_usuario);

ALTER TABLE tratamentos ADD CONSTRAINT FOREIGN KEY (fk_tratamento_remedios)
REFERENCES remedios(id_remedio);

ALTER TABLE tratamentos ADD FOREIGN KEY (fk_tratamento_usuarios)
REFERENCES usuarios(id_usuario);

ALTER TABLE tratamentos ADD inicio_tratamento DATETIME AFTER tipo_tratamento;
ALTER TABLE remedios CHANGE horario_remedio horario_remedio VARCHAR(50);
ALTER TABLE remedios CHANGE horario_remedio horario_remedio VARCHAR(150);
ALTER TABLE remedios CHANGE tipo_remedio tipo_remedio VARCHAR(150);
ALTER TABLE remedios CHANGE dosagem_remedio dosagem_remedio VARCHAR(150);
ALTER TABLE tratamentos CHANGE descricao_tratamento descricao_tratamento VARCHAR(650);
ALTER TABLE tratamentos CHANGE duracao_tratamento duracao_tratamento VARCHAR(100);

INSERT INTO usuarios (nome_usuario, dt_nasc_usuario, email_usuario, data_cadastro_usuario, usuario_ativo, genero_usuario) VALUES
('João Silva', '2000-01-10', 'joao2000@gmail.com', '2025-01-11', 1 , 'Masculino'),
('Gabriel Toledo', '2000-01-11', 'gabriel2000@gmail.com', '2026-01-11',0, 'Masculino'),
('Hildeu Alves', '1964-01-12', 'hildeu1964@gmail.com', '2026-01-12', 1 , 'Masculino'),
('Armando Cruz', '1966-01-13', 'armando1966@gmail.com', '2026-01-13', 1 , 'Masculino'),
('Benedito Ferreira','1965-01-14', 'benedito1965@gmail.com', '2026-01-14', 1 , 'Masculino'),
('Gildete Santos', '1967-01-15', 'gildete1967@gmail.com', '2026-01-15', 1, 'Feminino'),
('Vera Sonia' , '1968-01-16', 'vera1968@gmail.com', '2026-01-16', 1 , 'Feminino'),
('Claudia Leite', '1969-01-17', 'claudia1969@gmail.com', '2026-01-16', 1 , 'Feminino'),
('Beatriz Santos', '2000-01-18', 'beatriz2000@gmail.com', '2026-01-17', 0 , 'Feminino'),
('Ana Carolina', '2000-01-19', 'anacarolina2000@gmail.com', '2026-01-18', 1 , 'Feminino');


INSERT INTO remedios (nome_remedio, descricao_remedio, dosagem_remedio, horario_remedio, tipo_remedio) VALUES
('Dipirona Monohidratada','analgésico e antitérmico comumente utilizado para aliviar dores de cabeça, dores em geral e reduzir a febre, agindo na redução da dor e da temperatura corporal. Consulte um médico para orientações.',
'500mg' ,  'De 8 em 8 Horas', 'medicamento analgésico e antitérmico ; não-opioides'),

('Fosfomicina', 'antibiótico em dose única indicado para tratar infecções urinárias baixas, como cistite aguda. Deve ser diluída em água conforme orientação médica ou da bula, preferencialmente à noite, após urinar.',
'50ml á 75ml dissolvido em água', 'Tomar uma vez ao dia, recomenda-se 2 á 3 horas antes de almoçar', 'antibiótico bactericida'),

('Hidroclorotiazida','medicamento diurético da classe das tiazidas. Ele atua estimulando os rins a eliminarem o excesso de sódio e água, reduzindo o volume de sangue. É amplamente prescrito para o tratamento da pressão alta e de inchaços',
'50 á 100mg' , '1 100mg por dia ou 1 de 50mg de manhã e outra de noite' , 'Diuréticos'),

('Paracetamol' , 'é um medicamento analgésico e antitérmico amplamente utilizado para aliviar dores leves a moderadas e reduzir a febre. É seguro para a maioria das pessoas quando respeitada a dose diária máxima recomendada.',
'40 a 70 gotas' , 'De 6 em 6 horas' , 'medicamento analgésico (alivia a dor) e antipirético ou antitérmico (reduz a febre)'),

('Metformina' ,'medicamento antidiabético oral que reduz a glicose no sangue, diminuindo a produção hepática de açúcar e aumentando a sensibilidade à insulina',
'500mg' , '1 vez ao dia' , 'medicamento antidiabético oral da classe das biguanidas'), 

('Benzodiazepínicos', 'medicamentos depressores do sistema nervoso central, como clonazepam e diazepam. Eles agem acalmando o cérebro, sendo indicados para tratar ansiedade, insônia e convulsões.',
'5 á 10mg', '1 vez ao dia', 'classe de medicamentos depressores do sistema nervoso central.'),

('Corticoides Inalatórios' ,'medicamentos anti-inflamatórios de uso contínuo que atuam diretamente nas vias aéreas. Prescritos para asma e DPOC, reduzem a inflamação e evitam crises respiratórias graves. Como agem localmente, possuem mínimos efeitos colaterais.',
'40mg via oral', '1 vez ao dia', 'medicamentos anti-inflamatórios de uso diário e contínuo'),

('Estatinas', 'medicamentos que reduzem o colesterol ruim (LDL) no sangue ao bloquear a enzima que o produz no fígado. Elas previnem doenças como infarto e AVC, estabilizando placas de gordura nas artérias.',
'10mg á 40mg', '1 vez ao dia', 'são medicamentos prescritos para reduzir os níveis de colesterol LDL'), 

('Budesonida','corticoide de ação anti-inflamatória local. Disponível em spray nasal ou inaladores, trata doenças respiratórias como asma e rinite, reduzindo o inchaço e a irritação nas vias aéreas. Exige prescrição médica.',
'100 a 400mcg', '2 vezes ao dia', 'medicamento corticosteroide (ou glicocorticoide) com potente ação anti-inflamatória e antialérgica'),

('Pimecrolino','medicamento de uso tópico (creme) não corticoide, indicado para tratar eczema ou dermatite atópica. Inibidor da calcineurina, age reduzindo a inflamação, vermelhidão e coceira na pele',
'Aplicar 2 vezes ao dia', 'Aplicar uma fina camada de Pimecrolimo na pele afetada duas vezes ao dia e friccionar suave e completamente.', 'remédio de uso tópico (creme) indicado principalmente para o tratamento de eczema e dermatite atópica (leve a moderada)');



/*SELECT usuarios.id_usuario,
		usuarios.nome_usuario,
        contato_emergencia.id_contato,
        contato_emergencia.nome_contato,
        contato_emergencia.parentesco
FROM	usuarios INNER JOIN contato_emergencia
ON		contato_emergencia.fk_ce_usuario = usuarios.id_usuario
ORDER BY id_usuario;

SELECT tratamentos.nome_tratamento,
		tratamentos.descricao_tratamento,
        tratamentos.tipo_tratamento,
        tratamentos.inicio_tratamento,
        tratamentos.duracao_tratamento,
        tratamentos.data_cadastro_tratamento,
        remedios.nome_remedio,
        remedios.descricao_remedio,
        remedios.dosagem_remedio,
        remedios.horario_remedio,
        remedios.tipo_remedio
FROM	tratamentos INNER JOIN remedios
ON		tratamentos.fk_tratamento_remedios = remedios.id_remedio
ORDER BY id_remedio;*/


INSERT INTO tratamentos (nome_tratamento, descricao_tratamento, tipo_tratamento, inicio_tratamento, duracao_tratamento, data_cadastro_tratamento, fk_tratamento_remedios, fk_tratamento_usuarios) VALUES
('Dor de cabeça', 'Tratamento realizado com uso controlado de analgésicos prescritos, repouso adequado, hidratação constante e acompanhamento médico regular. O objetivo é reduzir crises frequentes de cefaleia tensional, aliviar dores intensas e melhorar significativamente a qualidade de vida do paciente.', 'Dor', '2026-05-23 00:00:00', '7 dias', '2026-05-23', 1, 1),
('Infecção urinária', 'Tratamento baseado na administração de antibióticos prescritos, aumento da ingestão de líquidos e acompanhamento médico para eliminação das bactérias causadoras da infecção e prevenção de novas complicações urinárias.', 'Infecção', '2026-05-23 00:00:00', '10 dias', '2026-05-23', 2 , 2),
('Hipertensão', 'Controle contínuo da pressão arterial com medicamentos anti-hipertensivos, prática regular de exercícios físicos, redução do consumo de sal e acompanhamento médico frequente para evitar complicações cardiovasculares.', 'Crônico', '2026-05-23 00:00:00', 'Uso contínuo', '2026-05-23', 3, 3),
('Gripe', 'Tratamento voltado para alívio dos sintomas gripais por meio de antitérmicos, repouso, hidratação constante e medicamentos para controle da febre, dores musculares e desconfortos respiratórios leves.', 'Viral', '2026-05-23 00:00:00', '5 dias', '2026-05-23', 4, 4),
('Diabetes Tipo 2', 'Tratamento focado no controle glicêmico através de medicamentos específicos, alimentação balanceada, prática de atividades físicas e monitoramento frequente dos níveis de glicose no sangue.', 'Crônico', '2026-05-23 00:00:00', 'Uso contínuo', '2026-05-23', 5, 5),
('Ansiedade', 'Tratamento realizado com acompanhamento psicológico regular, uso de ansiolíticos prescritos e desenvolvimento de hábitos saudáveis para redução de crises emocionais, estresse e dificuldades relacionadas ao sono.', 'Mental', '2026-05-23 00:00:00', '6 meses', '2026-05-23', 6, 6),
('Asma', 'Tratamento preventivo e contínuo utilizando broncodilatadores e controle ambiental para reduzir crises respiratórias, melhorar a capacidade pulmonar e proporcionar maior qualidade de vida ao paciente.', 'Respiratório', '2026-05-23 00:00:00', 'Uso contínuo', '2026-05-23', 7, 7),
('Colesterol Alto', 'Tratamento realizado com medicamentos para redução do colesterol, reeducação alimentar, diminuição do consumo de gorduras saturadas e prática regular de exercícios físicos para prevenção cardiovascular.', 'Crônico', '2026-05-23 00:00:00', '1 ano', '2026-05-23', 8, 8),
('Sinusite', 'Tratamento com antibióticos, lavagem nasal e medicamentos anti-inflamatórios para aliviar congestão nasal, dores faciais e inflamações nos seios da face causadas pela infecção.', 'Infecção', '2026-05-23 00:00:00', '14 dias', '2026-05-23', 9, 9),
('Dermatite Atópica', 'Tratamento dermatológico realizado com pomadas anti-inflamatórias, hidratantes específicos e medicamentos antialérgicos para reduzir coceiras, vermelhidão, irritações e controlar crises recorrentes na pele.', 'Dermatológico', '2026-05-23 00:00:00', '30 dias', '2026-05-23', 10, 10);


INSERT INTO contato_emergencia (nome_contato, telefone_contato, parentesco, fk_ce_usuario) VALUES
('Leticia', '(11)99876-1111', 'Esposa', 1),
('Junior', '(11)95678-2222', 'Irmão', 2),
('Matilde', '(11)91234-3333', 'Esposa', 3),
('Ana Maria', '(11)94321-4444', 'Mãe', 4),
('Aparecida', '(11)91111-5555', 'Esposa', 5),
('Lucas', '(11)91112-6666', 'Pai', 6),
('Juliana', '(11)91113-7777', 'Tia', 7),
('Rafael', '(11)91114-8888', 'Neto', 8),
('Beatriz', '(11)91115-9999', 'Prima', 9),
('Felipe', '(11)91116-0000', 'Irmão', 10);


SELECT * FROM usuarios;
SELECT * FROM remedios;
SELECT * FROM tratamentos;
SELECT * FROM contato_emergencia;

SELECT 
    usuarios.id_usuario,
    usuarios.nome_usuario,
    usuarios.email_usuario,
    usuarios.genero_usuario,

    contato_emergencia.id_contato,
    contato_emergencia.nome_contato,
    contato_emergencia.parentesco,
    contato_emergencia.telefone_contato,

    tratamentos.id_tratamento,
    tratamentos.nome_tratamento,
    tratamentos.tipo_tratamento,
    tratamentos.inicio_tratamento,
    tratamentos.duracao_tratamento,

    remedios.id_remedio,
    remedios.nome_remedio,
    remedios.tipo_remedio,
    remedios.dosagem_remedio,
    remedios.horario_remedio

FROM usuarios

INNER JOIN contato_emergencia
    ON contato_emergencia.fk_ce_usuario = usuarios.id_usuario

INNER JOIN tratamentos
    ON tratamentos.fk_tratamento_usuarios = usuarios.id_usuario

INNER JOIN remedios
    ON tratamentos.fk_tratamento_remedios = remedios.id_remedio

ORDER BY usuarios.id_usuario;