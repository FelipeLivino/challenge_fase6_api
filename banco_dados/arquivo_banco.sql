CREATE SCHEMA reply AUTHORIZATION ud9gsid03aiv8k;

CREATE TABLE reply.t_equipamento (
	id serial4 NOT NULL,
	marca varchar NOT NULL,
	modelo varchar NOT NULL,
	status varchar NOT NULL,
	CONSTRAINT t_equipamento_check CHECK (((status)::text = ANY ((ARRAY['DESLIGADO'::character varying, 'NORMAL'::character varying, 'ATENCAO'::character varying, 'FALHA'::character varying])::text[]))),
	CONSTRAINT t_equipamento_pk PRIMARY KEY (id)
);

CREATE TABLE reply.t_leitura_sensor (
	id serial4 NOT NULL,
	temperatura numeric NOT NULL,
	umidade numeric NULL,
	vibracao numeric NOT NULL,
	data_coleta timestamptz NOT NULL,
	t_equipamento_id serial4 NOT NULL,
	t_sensor_id serial4 NOT NULL,
	status varchar NOT NULL,
	CONSTRAINT t_leitura_sensor_check CHECK (((status)::text = ANY ((ARRAY['NORMAL'::character varying, 'ALERTA'::character varying, 'PERIGO'::character varying])::text[]))),
	CONSTRAINT t_leitura_sensor_pk PRIMARY KEY (id)
);

CREATE TABLE reply.t_sensor (
	id serial4 NOT NULL,
	nome varchar NOT NULL,
	status varchar NOT NULL,
	data_ativacao date NULL,
	CONSTRAINT t_sensor_check CHECK (((status)::text = ANY ((ARRAY['INATIVO'::character varying, 'ATIVO'::character varying])::text[]))),
	CONSTRAINT t_sensor_pk PRIMARY KEY (id)
);
