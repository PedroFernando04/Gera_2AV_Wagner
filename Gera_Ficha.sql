CREATE SCHEMA IF NOT EXISTS gera;
set search_path to gera;

drop table if exists gera.usuarios;
drop table if exists gera.personagens;
drop table if exists gera.racas;
drop table if exists gera.inventarios;
drop table if exists gera.atributos;
drop table if exists gera.armaduras;
drop table if exists gera.armas;
drop table if exists gera.itens;
drop table if exists gera.class_itens;


create table gera.class_itens(
	id_class_item serial primary key,
	categoria varchar (100) not null,
	tipo varchar(100),
	efeito varchar (100) not null
);

create table gera.itens(
	id_item serial primary key,
	nome varchar (100) not null,
	id_class_item integer references class_itens(id_class_item),
	quantidade integer not null default (0),
	valor money not null default (0),
	peso numeric not null default (0)
);

create table gera.armaduras (
	id_armadura serial primary key,
	nome varchar (200) not null,
	tipo varchar (200) not null,
	bonus varchar (200),
	defesa_base integer not null default (0),
	valor money default (0),
	peso numeric default (0)
);

create table gera.armas (
	id_arma serial primary key,
	nome varchar (200) not null,
	tipo varchar (200) not null,
	bonus varchar (200),
	ataque_base integer default (0),
	valor money default (0),
	peso numeric default (0)
);

create table gera.inventarios (
	id_inventario serial primary key,
	id_arma integer references armas (id_arma),
	id_item integer references itens (id_item),
	id_armadura integer references armaduras (id_armadura)
);

create table gera.racas (
	id_raca serial primary key,
	nome varchar (200) not null,
	passiva varchar (400) not null
);

create table gera.atributos (
	id_atributo serial primary key,
	forca integer not null,
	destreza integer not null,
	constituicao integer not null,
	inteligencia integer not null,
	sabedoria integer not null,
	carisma integer not null
);

create table gera.usuarios (
    id_usuario serial primary key,
    email varchar(100) not null,
    senha bytea not null,
    mod boolean default false
);

create table gera.personagens(
	id_personagem serial primary key,
	nome varchar (50),
	vida integer,
	dinheiro money,
	classe varchar (25),
	id_inventario integer references inventarios (id_inventario),
	id_raca integer references racas (id_raca),
	id_atributo integer references atributos (id_atributo),
	descricao varchar (1000),
    id_usuario integer references usuarios (id_usuario)
);

insert into gera.class_itens (categoria,tipo,efeito)
values ('consumível','Cura ','Cura 1d6'), --Poção de cura, ervas medicinais
('consumível','buff ','buff 1d6'), --Frasco de veneno, Frasco de fogo, Frasco de afinidade
('Arremeço','dano ','dano 1d10'), --machadinha, faca de arremeço, kunais, shikens, dardos
('arremeço','debuff ','Debilita inimigo por 1 rodada'), --pote de piche, dardo tranquilizante, bomba de choque
('magico','Cura ','Cura 1d10'), -- feitiço de benção, feitiço de cura, varinha de cura
('magico','dano ','dano 1d12'); -- Pergaminho de bola de fogo, pergaminho de estaca de gelo, varinha de mísseis arcanos


insert into itens (nome, id_class_item, quantidade, valor, peso)
values 
    -- Consumível: Cura (id_class_item = 1)
    ('Poção de Cura', 1, 5, 50.00, 0.5),
    ('Ervas Medicinais', 1, 15, 25.00, 0.3),
    -- Consumível: Buff (id_class_item = 2)
    ('Frasco de Veneno', 2, 2, 40.00, 0.2),
    ('Frasco de Fogo', 2, 2, 60.00, 0.3),
    ('Frasco de Afinidade', 2, 2, 75.00, 0.3),
    -- Arremesso: Dano (id_class_item = 3)
    ('Machadinha', 3, 6, 30.00, 0.8),
    ('Faca de Arremesso', 3, 8, 20.00, 0.4),
    ('Kunai', 3, 5, 15.00, 0.3),
    ('Shuriken', 3, 10, 10.00, 0.1),
    ('Dardo', 3, 2, 5.00, 0.2),
    -- Arremesso: Debuff (id_class_item = 4)
    ('Pote de Piche', 4, 1, 45.00, 1.0),
    ('Dardo Tranquilizante', 4, 5, 25.00, 0.2),
    ('Bomba de Choque', 4, 5, 60.00, 0.5),
    -- Mágico: Cura (id_class_item = 5)
    ('Feitiço de Benção', 5, 2, 150.00, 0.1),
    ('Feitiço de Cura', 5, 3, 100.00, 0.1),
    ('Varinha de Cura', 5, 1, 200.00, 0.5),
    -- Mágico: Dano (id_class_item = 6)
    ('Pergaminho de Bola de Fogo', 6, 1, 300.00, 0.2),
    ('Pergaminho de Estaca de Gelo', 6, 1, 250.00, 0.2),
    ('Varinha de Mísseis Arcanos', 6, 1, 400.00, 0.7);

insert into gera.armaduras (nome, tipo, bonus, defesa_base, valor, peso)
values
	('Armadura de Couro', 'Leve', '+1 Destreza', 12, 150, 8),
	('Armadura de Placas', 'Pesada', '+2 Força', 18, 500, 15),
	('Armadura de Couro Reforçada', 'Média', '+1 Constituição', 14, 250, 10),
	('Cota de Malha', 'Média', '+1 Sabedoria', 16, 300, 12),
	('Armadura Mágica', 'Leve', '+3 Inteligência', 14, 400, 7),
	('Sunga de texugo', 'muito leve', '+2 Agilidade', 5, 10, 1);
	
insert into gera.armas (nome, tipo, bonus, ataque_base, valor, peso)
values
	('Espada Longa', 'Corpo a Corpo', '+2 Força', 15, 300, 3.5),
	('Arco Longo', 'À Distância', '+1 Destreza', 12, 250, 2.0),
	('Machado de Guerra', 'Corpo a Corpo', '+3 Força', 20, 400, 5.0),
	('Lança', 'Corpo a Corpo', '+1 Destreza', 10, 150, 3.0),
	('Báculo', 'Mágica', '+5 Inteligência', 12, 500, 2.5),
	('Cajado de Fogo', 'Mágica', '+4 Sabedoria', 15, 600, 2.0),
	('Adagas','Corpo a Corpo','+1 Destreza', 10, 100, 1.0);

insert into inventarios (id_arma, id_item, id_armadura)
values
    -- 1 Kit básico para o Guerreiro
    (1, 1, 2),  -- Espada Longa, Poção de Cura, Armadura de Placas
    -- 2 Kit básico para o Ladino
    (7, 3, 1),  -- Adagas, Frasco de Veneno, Armadura de Couro
    -- 3 Kit básico para o Curandeiro
    (5, 15, 6), -- Báculo, Feitiço de Benção, Cota de Malha
    -- 4 Kit básico para o Mago
    (6, 18, 5), -- Cajado de Fogo, Pergaminho de Bola de Fogo, Armadura Mágica
    -- 5 Kit básico para o Bardo
    (7, 5, 3),  -- Adagas, Frasco de Afinidade, Armadura de Couro Reforçada
    -- 6 Kit básico para o Druida
    (5, 14, 4); -- Báculo, Pote de Piche, Sunga de Texugo

insert into racas (nome,passiva)
values
	('Humano','Ganha mais 3 perícias básicas'),
	('Elfo', 'Visão noturna e +2 em Percepção'),
	('Anão', 'Resistência a venenos e +2 em Constituição'),
	('Orc', 'Força aumentada e +2 em Força'),
	('Halfling', 'Pequeno porte e +2 em Esquiva'),
	('Gnomo', 'Afinidade com magia e +2 em Inteligência'),
	('Tiefling', 'Resistência a fogo e +2 em Charme'),
	('Draconato', 'Sopro elemental e resistência ao tipo de dano do elemento'),
	('Meio-Elfo', '+1 em Carisma e escolha uma habilidade extra'),
	('Goblin', 'Movimento furtivo e +2 em Destreza');

insert into atributos (forca, destreza, constituicao,inteligencia,sabedoria,carisma)
values
	(20,20,20,20,20,20);
    
insert into gera.personagens (id_personagem, nome, vida, dinheiro, classe, id_inventario, id_raca, id_atributo, descricao, id_usuario) 
values
	(1, 'Theus', 999, 9999, 'Guerreiro',1,1,1,'GM',1 );
	
insert into gera.usuarios (email, senha, mod)
values ('mod@mod.com', 'mod', true, 1);
