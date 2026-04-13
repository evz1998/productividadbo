
-- BASE DE DATOS: Sistema de Productividad Backoffice


CREATE DATABASE db_backoffice;


-- TABLA 1: areas
-- Áreas o departamentos de la empresa

CREATE TABLE db_backoffice.areas (
    idArea      INT          NOT NULL AUTO_INCREMENT,
    nomArea     VARCHAR(100) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    activa      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idArea)
);


-- TABLA 2: cargos
-- Cargos o roles que puede tener un asesor

CREATE TABLE db_backoffice.cargos (
    idCargo     INT          NOT NULL AUTO_INCREMENT,
    nomCargo    VARCHAR(100) NOT NULL,
    nivel       INT          NOT NULL DEFAULT 1,
    activo      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idCargo)
);


-- TABLA 3: asesores
-- Asesores del backoffice

CREATE TABLE db_backoffice.asesores (
    idAsesor    INT          NOT NULL AUTO_INCREMENT,
    cedula      VARCHAR(20)  NOT NULL UNIQUE,
    nombre      VARCHAR(200) NOT NULL,
    email       VARCHAR(200) NOT NULL UNIQUE,
    telefono    VARCHAR(20)  NOT NULL,
    idArea      INT          NOT NULL,
    idCargo     INT          NOT NULL,
    fechaIngreso DATETIME    NOT NULL,
    activo      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idAsesor),
    CONSTRAINT fk_asesores__areas
        FOREIGN KEY (idArea) REFERENCES db_backoffice.areas(idArea),
    CONSTRAINT fk_asesores__cargos
        FOREIGN KEY (idCargo) REFERENCES db_backoffice.cargos(idCargo)
);


-- TABLA 4: tiposCaso
-- Tipos de casos que pueden gestionar los asesores

CREATE TABLE db_backoffice.tiposCaso (
    idTipoCaso  INT          NOT NULL AUTO_INCREMENT,
    nomTipo     VARCHAR(100) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    tiempoMeta  INT          NOT NULL DEFAULT 60,
    activo      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idTipoCaso)
);


-- TABLA 5: prioridades
-- Niveles de prioridad de un caso

CREATE TABLE db_backoffice.prioridades (
    idPrioridad INT          NOT NULL AUTO_INCREMENT,
    nomPrioridad VARCHAR(50) NOT NULL,
    nivel        INT         NOT NULL DEFAULT 1,
    activa       BIT         NOT NULL DEFAULT 1,
    PRIMARY KEY(idPrioridad)
);


-- TABLA 6: estadosCaso
-- Estados por los que puede pasar un caso

CREATE TABLE db_backoffice.estadosCaso (
    idEstado    INT          NOT NULL AUTO_INCREMENT,
    nomEstado   VARCHAR(100) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    esFinal     BIT          NOT NULL DEFAULT 0,
    activo      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idEstado)
);


-- TABLA 7: canales
-- Canal por el que llega el caso (email, chat, telefono, etc.)

CREATE TABLE db_backoffice.canales (
    idCanal     INT          NOT NULL AUTO_INCREMENT,
    nomCanal    VARCHAR(100) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    activo      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idCanal)
);


-- TABLA 8: clientes
-- Clientes o usuarios que generan los casos

CREATE TABLE db_backoffice.clientes (
    idCliente   INT          NOT NULL AUTO_INCREMENT,
    documento   VARCHAR(20)  NOT NULL UNIQUE,
    nombre      VARCHAR(200) NOT NULL,
    email       VARCHAR(200) NOT NULL,
    telefono    VARCHAR(20)  NOT NULL,
    fechaRegistro DATETIME   NOT NULL,
    activo      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idCliente)
);


-- TABLA 9: casos
-- Casos gestionados por los asesores (tabla central)

CREATE TABLE db_backoffice.casos (
    idCaso      INT          NOT NULL AUTO_INCREMENT,
    idCliente   INT          NOT NULL,
    idTipoCaso  INT          NOT NULL,
    idPrioridad INT          NOT NULL,
    idCanal     INT          NOT NULL,
    idEstado    INT          NOT NULL,
    idAsesor    INT          NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
    fechaApertura DATETIME   NOT NULL,
    fechaCierre DATETIME,
    PRIMARY KEY(idCaso),
    CONSTRAINT fk_casos__clientes
        FOREIGN KEY (idCliente) REFERENCES db_backoffice.clientes(idCliente),
    CONSTRAINT fk_casos__tiposCaso
        FOREIGN KEY (idTipoCaso) REFERENCES db_backoffice.tiposCaso(idTipoCaso),
    CONSTRAINT fk_casos__prioridades
        FOREIGN KEY (idPrioridad) REFERENCES db_backoffice.prioridades(idPrioridad),
    CONSTRAINT fk_casos__canales
        FOREIGN KEY (idCanal) REFERENCES db_backoffice.canales(idCanal),
    CONSTRAINT fk_casos__estadosCaso
        FOREIGN KEY (idEstado) REFERENCES db_backoffice.estadosCaso(idEstado),
    CONSTRAINT fk_casos__asesores
        FOREIGN KEY (idAsesor) REFERENCES db_backoffice.asesores(idAsesor)
);


-- TABLA 10: seguimientosCaso
-- Historial de cambios de estado y notas en cada caso

CREATE TABLE db_backoffice.seguimientosCaso (
    idSeguimiento INT         NOT NULL AUTO_INCREMENT,
    idCaso        INT         NOT NULL,
    idAsesor      INT         NOT NULL,
    idEstado      INT         NOT NULL,
    nota          VARCHAR(500) NOT NULL,
    fechaRegistro DATETIME    NOT NULL,
    PRIMARY KEY(idSeguimiento),
    CONSTRAINT fk_seguimientos__casos
        FOREIGN KEY (idCaso) REFERENCES db_backoffice.casos(idCaso),
    CONSTRAINT fk_seguimientos__asesores
        FOREIGN KEY (idAsesor) REFERENCES db_backoffice.asesores(idAsesor),
    CONSTRAINT fk_seguimientos__estadosCaso
        FOREIGN KEY (idEstado) REFERENCES db_backoffice.estadosCaso(idEstado)
);


-- TABLA 11: turnos
-- Turnos de trabajo de los asesores

CREATE TABLE db_backoffice.turnos (
    idTurno     INT          NOT NULL AUTO_INCREMENT,
    nomTurno    VARCHAR(100) NOT NULL,
    horaInicio  TIME         NOT NULL,
    horaFin     TIME         NOT NULL,
    activo      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idTurno)
);


-- TABLA 12: asistencias
-- Registro de asistencia diaria de cada asesor

CREATE TABLE db_backoffice.asistencias (
    idAsistencia INT         NOT NULL AUTO_INCREMENT,
    idAsesor     INT         NOT NULL,
    idTurno      INT         NOT NULL,
    fecha        DATE        NOT NULL,
    horaEntrada  DATETIME    NOT NULL,
    horaSalida   DATETIME,
    minutosTrabajados INT    NOT NULL DEFAULT 0,
    PRIMARY KEY(idAsistencia),
    CONSTRAINT fk_asistencias__asesores
        FOREIGN KEY (idAsesor) REFERENCES db_backoffice.asesores(idAsesor),
    CONSTRAINT fk_asistencias__turnos
        FOREIGN KEY (idTurno) REFERENCES db_backoffice.turnos(idTurno)
);


-- TABLA 13: metasProductividad
-- Metas de productividad definidas por area o asesor

CREATE TABLE db_backoffice.metasProductividad (
    idMeta      INT          NOT NULL AUTO_INCREMENT,
    idArea      INT          NOT NULL,
    idTipoCaso  INT          NOT NULL,
    casosMetaDia INT         NOT NULL DEFAULT 10,
    vigenciaDesde DATE       NOT NULL,
    vigenciaHasta DATE,
    activa      BIT          NOT NULL DEFAULT 1,
    PRIMARY KEY(idMeta),
    CONSTRAINT fk_metas__areas
        FOREIGN KEY (idArea) REFERENCES db_backoffice.areas(idArea),
    CONSTRAINT fk_metas__tiposCaso
        FOREIGN KEY (idTipoCaso) REFERENCES db_backoffice.tiposCaso(idTipoCaso)
);


-- TABLA 14: evaluaciones
-- Evaluaciones de desempeño de los asesores

CREATE TABLE db_backoffice.evaluaciones (
    idEvaluacion  INT         NOT NULL AUTO_INCREMENT,
    idAsesor      INT         NOT NULL,
    periodo       VARCHAR(20) NOT NULL,
    calidad       DECIMAL(5,2) NOT NULL DEFAULT 0.0,
    puntualidad   DECIMAL(5,2) NOT NULL DEFAULT 0.0,
    casosGestionados INT      NOT NULL DEFAULT 0,
    nota          DECIMAL(5,2) NOT NULL DEFAULT 0.0,
    fechaEvaluacion DATETIME  NOT NULL,
    PRIMARY KEY(idEvaluacion),
    CONSTRAINT fk_evaluaciones__asesores
        FOREIGN KEY (idAsesor) REFERENCES db_backoffice.asesores(idAsesor)
);


-- TABLA 15: reportesDiarios
-- Resumen consolidado de productividad por asesor y dia

CREATE TABLE db_backoffice.reportesDiarios (
    idReporte     INT         NOT NULL AUTO_INCREMENT,
    idAsesor      INT         NOT NULL,
    fecha         DATE        NOT NULL,
    casosAbiertos  INT        NOT NULL DEFAULT 0,
    casosCerrados  INT        NOT NULL DEFAULT 0,
    casosEnProceso INT        NOT NULL DEFAULT 0,
    tiempoPromedio DECIMAL(10,2) NOT NULL DEFAULT 0.0,
    cumplioMeta   BIT         NOT NULL DEFAULT 0,
    PRIMARY KEY(idReporte),
    CONSTRAINT fk_reportes__asesores
        FOREIGN KEY (idAsesor) REFERENCES db_backoffice.asesores(idAsesor)
);


-- PROCEDIMIENTOS ALMACENADOS - Sistema Backoffice

-- Patrón: SELECT-all / SELECT-id / INSERT / UPDATE / DELETE


DELIMITER $$


-- TABLA 1: areas


CREATE PROCEDURE `db_backoffice`.`proc_select_areas`()
BEGIN
    SELECT * FROM `db_backoffice`.`areas`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_area_id`(
    IN p_idArea INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`areas`
    WHERE idArea = p_idArea;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_area`(
    IN p_nomArea     VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_activa      BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`areas` (nomArea, descripcion, activa)
    VALUES (p_nomArea, p_descripcion, p_activa);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_area`(
    IN p_idArea      INT,
    IN p_nomArea     VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_activa      BIT
)
BEGIN
    UPDATE `db_backoffice`.`areas`
    SET nomArea     = p_nomArea,
        descripcion = p_descripcion,
        activa      = p_activa
    WHERE idArea = p_idArea;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_area`(
    IN p_idArea INT
)
BEGIN
    DELETE FROM `db_backoffice`.`areas`
    WHERE idArea = p_idArea;
END$$



-- TABLA 2: cargos


CREATE PROCEDURE `db_backoffice`.`proc_select_cargos`()
BEGIN
    SELECT * FROM `db_backoffice`.`cargos`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_cargo_id`(
    IN p_idCargo INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`cargos`
    WHERE idCargo = p_idCargo;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_cargo`(
    IN p_nomCargo VARCHAR(100),
    IN p_nivel    INT,
    IN p_activo   BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`cargos` (nomCargo, nivel, activo)
    VALUES (p_nomCargo, p_nivel, p_activo);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_cargo`(
    IN p_idCargo  INT,
    IN p_nomCargo VARCHAR(100),
    IN p_nivel    INT,
    IN p_activo   BIT
)
BEGIN
    UPDATE `db_backoffice`.`cargos`
    SET nomCargo = p_nomCargo,
        nivel    = p_nivel,
        activo   = p_activo
    WHERE idCargo = p_idCargo;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_cargo`(
    IN p_idCargo INT
)
BEGIN
    DELETE FROM `db_backoffice`.`cargos`
    WHERE idCargo = p_idCargo;
END$$



-- TABLA 3: asesores


CREATE PROCEDURE `db_backoffice`.`proc_select_asesores`()
BEGIN
    SELECT * FROM `db_backoffice`.`asesores`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_asesor_id`(
    IN p_idAsesor INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`asesores`
    WHERE idAsesor = p_idAsesor;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_asesor`(
    IN p_cedula       VARCHAR(20),
    IN p_nombre       VARCHAR(200),
    IN p_email        VARCHAR(200),
    IN p_telefono     VARCHAR(20),
    IN p_idArea       INT,
    IN p_idCargo      INT,
    IN p_fechaIngreso DATETIME,
    IN p_activo       BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`asesores`
        (cedula, nombre, email, telefono, idArea, idCargo, fechaIngreso, activo)
    VALUES
        (p_cedula, p_nombre, p_email, p_telefono, p_idArea, p_idCargo, p_fechaIngreso, p_activo);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_asesor`(
    IN p_idAsesor     INT,
    IN p_cedula       VARCHAR(20),
    IN p_nombre       VARCHAR(200),
    IN p_email        VARCHAR(200),
    IN p_telefono     VARCHAR(20),
    IN p_idArea       INT,
    IN p_idCargo      INT,
    IN p_fechaIngreso DATETIME,
    IN p_activo       BIT
)
BEGIN
    UPDATE `db_backoffice`.`asesores`
    SET cedula       = p_cedula,
        nombre       = p_nombre,
        email        = p_email,
        telefono     = p_telefono,
        idArea       = p_idArea,
        idCargo      = p_idCargo,
        fechaIngreso = p_fechaIngreso,
        activo       = p_activo
    WHERE idAsesor = p_idAsesor;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_asesor`(
    IN p_idAsesor INT
)
BEGIN
    DELETE FROM `db_backoffice`.`asesores`
    WHERE idAsesor = p_idAsesor;
END$$



-- TABLA 4: tiposCaso


CREATE PROCEDURE `db_backoffice`.`proc_select_tiposCaso`()
BEGIN
    SELECT * FROM `db_backoffice`.`tiposCaso`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_tipoCaso_id`(
    IN p_idTipoCaso INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`tiposCaso`
    WHERE idTipoCaso = p_idTipoCaso;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_tipoCaso`(
    IN p_nomTipo     VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_tiempoMeta  INT,
    IN p_activo      BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`tiposCaso` (nomTipo, descripcion, tiempoMeta, activo)
    VALUES (p_nomTipo, p_descripcion, p_tiempoMeta, p_activo);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_tipoCaso`(
    IN p_idTipoCaso  INT,
    IN p_nomTipo     VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_tiempoMeta  INT,
    IN p_activo      BIT
)
BEGIN
    UPDATE `db_backoffice`.`tiposCaso`
    SET nomTipo     = p_nomTipo,
        descripcion = p_descripcion,
        tiempoMeta  = p_tiempoMeta,
        activo      = p_activo
    WHERE idTipoCaso = p_idTipoCaso;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_tipoCaso`(
    IN p_idTipoCaso INT
)
BEGIN
    DELETE FROM `db_backoffice`.`tiposCaso`
    WHERE idTipoCaso = p_idTipoCaso;
END$$



-- TABLA 5: prioridades


CREATE PROCEDURE `db_backoffice`.`proc_select_prioridades`()
BEGIN
    SELECT * FROM `db_backoffice`.`prioridades`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_prioridad_id`(
    IN p_idPrioridad INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`prioridades`
    WHERE idPrioridad = p_idPrioridad;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_prioridad`(
    IN p_nomPrioridad VARCHAR(50),
    IN p_nivel        INT,
    IN p_activa       BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`prioridades` (nomPrioridad, nivel, activa)
    VALUES (p_nomPrioridad, p_nivel, p_activa);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_prioridad`(
    IN p_idPrioridad  INT,
    IN p_nomPrioridad VARCHAR(50),
    IN p_nivel        INT,
    IN p_activa       BIT
)
BEGIN
    UPDATE `db_backoffice`.`prioridades`
    SET nomPrioridad = p_nomPrioridad,
        nivel        = p_nivel,
        activa       = p_activa
    WHERE idPrioridad = p_idPrioridad;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_prioridad`(
    IN p_idPrioridad INT
)
BEGIN
    DELETE FROM `db_backoffice`.`prioridades`
    WHERE idPrioridad = p_idPrioridad;
END$$



-- TABLA 6: estadosCaso


CREATE PROCEDURE `db_backoffice`.`proc_select_estadosCaso`()
BEGIN
    SELECT * FROM `db_backoffice`.`estadosCaso`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_estadoCaso_id`(
    IN p_idEstado INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`estadosCaso`
    WHERE idEstado = p_idEstado;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_estadoCaso`(
    IN p_nomEstado   VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_esFinal     BIT,
    IN p_activo      BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`estadosCaso` (nomEstado, descripcion, esFinal, activo)
    VALUES (p_nomEstado, p_descripcion, p_esFinal, p_activo);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_estadoCaso`(
    IN p_idEstado    INT,
    IN p_nomEstado   VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_esFinal     BIT,
    IN p_activo      BIT
)
BEGIN
    UPDATE `db_backoffice`.`estadosCaso`
    SET nomEstado   = p_nomEstado,
        descripcion = p_descripcion,
        esFinal     = p_esFinal,
        activo      = p_activo
    WHERE idEstado = p_idEstado;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_estadoCaso`(
    IN p_idEstado INT
)
BEGIN
    DELETE FROM `db_backoffice`.`estadosCaso`
    WHERE idEstado = p_idEstado;
END$$



-- TABLA 7: canales


CREATE PROCEDURE `db_backoffice`.`proc_select_canales`()
BEGIN
    SELECT * FROM `db_backoffice`.`canales`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_canal_id`(
    IN p_idCanal INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`canales`
    WHERE idCanal = p_idCanal;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_canal`(
    IN p_nomCanal    VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_activo      BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`canales` (nomCanal, descripcion, activo)
    VALUES (p_nomCanal, p_descripcion, p_activo);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_canal`(
    IN p_idCanal     INT,
    IN p_nomCanal    VARCHAR(100),
    IN p_descripcion VARCHAR(300),
    IN p_activo      BIT
)
BEGIN
    UPDATE `db_backoffice`.`canales`
    SET nomCanal    = p_nomCanal,
        descripcion = p_descripcion,
        activo      = p_activo
    WHERE idCanal = p_idCanal;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_canal`(
    IN p_idCanal INT
)
BEGIN
    DELETE FROM `db_backoffice`.`canales`
    WHERE idCanal = p_idCanal;
END$$



-- TABLA 8: clientes


CREATE PROCEDURE `db_backoffice`.`proc_select_clientes`()
BEGIN
    SELECT * FROM `db_backoffice`.`clientes`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_cliente_id`(
    IN p_idCliente INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`clientes`
    WHERE idCliente = p_idCliente;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_cliente`(
    IN p_documento     VARCHAR(20),
    IN p_nombre        VARCHAR(200),
    IN p_email         VARCHAR(200),
    IN p_telefono      VARCHAR(20),
    IN p_fechaRegistro DATETIME,
    IN p_activo        BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`clientes`
        (documento, nombre, email, telefono, fechaRegistro, activo)
    VALUES
        (p_documento, p_nombre, p_email, p_telefono, p_fechaRegistro, p_activo);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_cliente`(
    IN p_idCliente     INT,
    IN p_documento     VARCHAR(20),
    IN p_nombre        VARCHAR(200),
    IN p_email         VARCHAR(200),
    IN p_telefono      VARCHAR(20),
    IN p_fechaRegistro DATETIME,
    IN p_activo        BIT
)
BEGIN
    UPDATE `db_backoffice`.`clientes`
    SET documento     = p_documento,
        nombre        = p_nombre,
        email         = p_email,
        telefono      = p_telefono,
        fechaRegistro = p_fechaRegistro,
        activo        = p_activo
    WHERE idCliente = p_idCliente;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_cliente`(
    IN p_idCliente INT
)
BEGIN
    DELETE FROM `db_backoffice`.`clientes`
    WHERE idCliente = p_idCliente;
END$$



-- TABLA 9: casos


CREATE PROCEDURE `db_backoffice`.`proc_select_casos`()
BEGIN
    SELECT * FROM `db_backoffice`.`casos`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_caso_id`(
    IN p_idCaso INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`casos`
    WHERE idCaso = p_idCaso;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_caso`(
    IN p_idCliente    INT,
    IN p_idTipoCaso   INT,
    IN p_idPrioridad  INT,
    IN p_idCanal      INT,
    IN p_idEstado     INT,
    IN p_idAsesor     INT,
    IN p_descripcion  VARCHAR(500),
    IN p_fechaApertura DATETIME,
    IN p_fechaCierre  DATETIME
)
BEGIN
    INSERT INTO `db_backoffice`.`casos`
        (idCliente, idTipoCaso, idPrioridad, idCanal, idEstado,
         idAsesor, descripcion, fechaApertura, fechaCierre)
    VALUES
        (p_idCliente, p_idTipoCaso, p_idPrioridad, p_idCanal, p_idEstado,
         p_idAsesor, p_descripcion, p_fechaApertura, p_fechaCierre);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_caso`(
    IN p_idCaso       INT,
    IN p_idCliente    INT,
    IN p_idTipoCaso   INT,
    IN p_idPrioridad  INT,
    IN p_idCanal      INT,
    IN p_idEstado     INT,
    IN p_idAsesor     INT,
    IN p_descripcion  VARCHAR(500),
    IN p_fechaApertura DATETIME,
    IN p_fechaCierre  DATETIME
)
BEGIN
    UPDATE `db_backoffice`.`casos`
    SET idCliente    = p_idCliente,
        idTipoCaso   = p_idTipoCaso,
        idPrioridad  = p_idPrioridad,
        idCanal      = p_idCanal,
        idEstado     = p_idEstado,
        idAsesor     = p_idAsesor,
        descripcion  = p_descripcion,
        fechaApertura = p_fechaApertura,
        fechaCierre  = p_fechaCierre
    WHERE idCaso = p_idCaso;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_caso`(
    IN p_idCaso INT
)
BEGIN
    DELETE FROM `db_backoffice`.`casos`
    WHERE idCaso = p_idCaso;
END$$



-- TABLA 10: seguimientosCaso


CREATE PROCEDURE `db_backoffice`.`proc_select_seguimientos`()
BEGIN
    SELECT * FROM `db_backoffice`.`seguimientosCaso`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_seguimiento_id`(
    IN p_idSeguimiento INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`seguimientosCaso`
    WHERE idSeguimiento = p_idSeguimiento;
END$$

-- Útil también: traer todos los seguimientos de un caso
CREATE PROCEDURE `db_backoffice`.`proc_select_seguimientos_caso`(
    IN p_idCaso INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`seguimientosCaso`
    WHERE idCaso = p_idCaso;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_seguimiento`(
    IN p_idCaso         INT,
    IN p_idAsesor       INT,
    IN p_idEstado       INT,
    IN p_nota           VARCHAR(500),
    IN p_fechaRegistro  DATETIME
)
BEGIN
    INSERT INTO `db_backoffice`.`seguimientosCaso`
        (idCaso, idAsesor, idEstado, nota, fechaRegistro)
    VALUES
        (p_idCaso, p_idAsesor, p_idEstado, p_nota, p_fechaRegistro);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_seguimiento`(
    IN p_idSeguimiento INT,
    IN p_idCaso        INT,
    IN p_idAsesor      INT,
    IN p_idEstado      INT,
    IN p_nota          VARCHAR(500),
    IN p_fechaRegistro DATETIME
)
BEGIN
    UPDATE `db_backoffice`.`seguimientosCaso`
    SET idCaso        = p_idCaso,
        idAsesor      = p_idAsesor,
        idEstado      = p_idEstado,
        nota          = p_nota,
        fechaRegistro = p_fechaRegistro
    WHERE idSeguimiento = p_idSeguimiento;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_seguimiento`(
    IN p_idSeguimiento INT
)
BEGIN
    DELETE FROM `db_backoffice`.`seguimientosCaso`
    WHERE idSeguimiento = p_idSeguimiento;
END$$



-- TABLA 11: turnos


CREATE PROCEDURE `db_backoffice`.`proc_select_turnos`()
BEGIN
    SELECT * FROM `db_backoffice`.`turnos`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_turno_id`(
    IN p_idTurno INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`turnos`
    WHERE idTurno = p_idTurno;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_turno`(
    IN p_nomTurno   VARCHAR(100),
    IN p_horaInicio TIME,
    IN p_horaFin    TIME,
    IN p_activo     BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`turnos` (nomTurno, horaInicio, horaFin, activo)
    VALUES (p_nomTurno, p_horaInicio, p_horaFin, p_activo);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_turno`(
    IN p_idTurno    INT,
    IN p_nomTurno   VARCHAR(100),
    IN p_horaInicio TIME,
    IN p_horaFin    TIME,
    IN p_activo     BIT
)
BEGIN
    UPDATE `db_backoffice`.`turnos`
    SET nomTurno   = p_nomTurno,
        horaInicio = p_horaInicio,
        horaFin    = p_horaFin,
        activo     = p_activo
    WHERE idTurno = p_idTurno;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_turno`(
    IN p_idTurno INT
)
BEGIN
    DELETE FROM `db_backoffice`.`turnos`
    WHERE idTurno = p_idTurno;
END$$



-- TABLA 12: asistencias


CREATE PROCEDURE `db_backoffice`.`proc_select_asistencias`()
BEGIN
    SELECT * FROM `db_backoffice`.`asistencias`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_asistencia_id`(
    IN p_idAsistencia INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`asistencias`
    WHERE idAsistencia = p_idAsistencia;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_asistencia`(
    IN p_idAsesor          INT,
    IN p_idTurno           INT,
    IN p_fecha             DATE,
    IN p_horaEntrada       DATETIME,
    IN p_horaSalida        DATETIME,
    IN p_minutosTrabajados INT
)
BEGIN
    INSERT INTO `db_backoffice`.`asistencias`
        (idAsesor, idTurno, fecha, horaEntrada, horaSalida, minutosTrabajados)
    VALUES
        (p_idAsesor, p_idTurno, p_fecha, p_horaEntrada, p_horaSalida, p_minutosTrabajados);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_asistencia`(
    IN p_idAsistencia      INT,
    IN p_idAsesor          INT,
    IN p_idTurno           INT,
    IN p_fecha             DATE,
    IN p_horaEntrada       DATETIME,
    IN p_horaSalida        DATETIME,
    IN p_minutosTrabajados INT
)
BEGIN
    UPDATE `db_backoffice`.`asistencias`
    SET idAsesor          = p_idAsesor,
        idTurno           = p_idTurno,
        fecha             = p_fecha,
        horaEntrada       = p_horaEntrada,
        horaSalida        = p_horaSalida,
        minutosTrabajados = p_minutosTrabajados
    WHERE idAsistencia = p_idAsistencia;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_asistencia`(
    IN p_idAsistencia INT
)
BEGIN
    DELETE FROM `db_backoffice`.`asistencias`
    WHERE idAsistencia = p_idAsistencia;
END$$



-- TABLA 13: metasProductividad


CREATE PROCEDURE `db_backoffice`.`proc_select_metas`()
BEGIN
    SELECT * FROM `db_backoffice`.`metasProductividad`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_meta_id`(
    IN p_idMeta INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`metasProductividad`
    WHERE idMeta = p_idMeta;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_meta`(
    IN p_idArea        INT,
    IN p_idTipoCaso    INT,
    IN p_casosMetaDia  INT,
    IN p_vigenciaDesde DATE,
    IN p_vigenciaHasta DATE,
    IN p_activa        BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`metasProductividad`
        (idArea, idTipoCaso, casosMetaDia, vigenciaDesde, vigenciaHasta, activa)
    VALUES
        (p_idArea, p_idTipoCaso, p_casosMetaDia, p_vigenciaDesde, p_vigenciaHasta, p_activa);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_meta`(
    IN p_idMeta        INT,
    IN p_idArea        INT,
    IN p_idTipoCaso    INT,
    IN p_casosMetaDia  INT,
    IN p_vigenciaDesde DATE,
    IN p_vigenciaHasta DATE,
    IN p_activa        BIT
)
BEGIN
    UPDATE `db_backoffice`.`metasProductividad`
    SET idArea        = p_idArea,
        idTipoCaso    = p_idTipoCaso,
        casosMetaDia  = p_casosMetaDia,
        vigenciaDesde = p_vigenciaDesde,
        vigenciaHasta = p_vigenciaHasta,
        activa        = p_activa
    WHERE idMeta = p_idMeta;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_meta`(
    IN p_idMeta INT
)
BEGIN
    DELETE FROM `db_backoffice`.`metasProductividad`
    WHERE idMeta = p_idMeta;
END$$



-- TABLA 14: evaluaciones


CREATE PROCEDURE `db_backoffice`.`proc_select_evaluaciones`()
BEGIN
    SELECT * FROM `db_backoffice`.`evaluaciones`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_evaluacion_id`(
    IN p_idEvaluacion INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`evaluaciones`
    WHERE idEvaluacion = p_idEvaluacion;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_evaluacion`(
    IN p_idAsesor         INT,
    IN p_periodo          VARCHAR(20),
    IN p_calidad          DECIMAL(5,2),
    IN p_puntualidad      DECIMAL(5,2),
    IN p_casosGestionados INT,
    IN p_nota             DECIMAL(5,2),
    IN p_fechaEvaluacion  DATETIME
)
BEGIN
    INSERT INTO `db_backoffice`.`evaluaciones`
        (idAsesor, periodo, calidad, puntualidad, casosGestionados, nota, fechaEvaluacion)
    VALUES
        (p_idAsesor, p_periodo, p_calidad, p_puntualidad, p_casosGestionados, p_nota, p_fechaEvaluacion);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_evaluacion`(
    IN p_idEvaluacion     INT,
    IN p_idAsesor         INT,
    IN p_periodo          VARCHAR(20),
    IN p_calidad          DECIMAL(5,2),
    IN p_puntualidad      DECIMAL(5,2),
    IN p_casosGestionados INT,
    IN p_nota             DECIMAL(5,2),
    IN p_fechaEvaluacion  DATETIME
)
BEGIN
    UPDATE `db_backoffice`.`evaluaciones`
    SET idAsesor         = p_idAsesor,
        periodo          = p_periodo,
        calidad          = p_calidad,
        puntualidad      = p_puntualidad,
        casosGestionados = p_casosGestionados,
        nota             = p_nota,
        fechaEvaluacion  = p_fechaEvaluacion
    WHERE idEvaluacion = p_idEvaluacion;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_evaluacion`(
    IN p_idEvaluacion INT
)
BEGIN
    DELETE FROM `db_backoffice`.`evaluaciones`
    WHERE idEvaluacion = p_idEvaluacion;
END$$



-- TABLA 15: reportesDiarios


CREATE PROCEDURE `db_backoffice`.`proc_select_reportes`()
BEGIN
    SELECT * FROM `db_backoffice`.`reportesDiarios`;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_select_reporte_id`(
    IN p_idReporte INT
)
BEGIN
    SELECT * FROM `db_backoffice`.`reportesDiarios`
    WHERE idReporte = p_idReporte;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_insert_reporte`(
    IN p_idAsesor       INT,
    IN p_fecha          DATE,
    IN p_casosAbiertos  INT,
    IN p_casosCerrados  INT,
    IN p_casosEnProceso INT,
    IN p_tiempoPromedio DECIMAL(10,2),
    IN p_cumplioMeta    BIT
)
BEGIN
    INSERT INTO `db_backoffice`.`reportesDiarios`
        (idAsesor, fecha, casosAbiertos, casosCerrados, casosEnProceso, tiempoPromedio, cumplioMeta)
    VALUES
        (p_idAsesor, p_fecha, p_casosAbiertos, p_casosCerrados, p_casosEnProceso, p_tiempoPromedio, p_cumplioMeta);
END$$

CREATE PROCEDURE `db_backoffice`.`proc_update_reporte`(
    IN p_idReporte      INT,
    IN p_idAsesor       INT,
    IN p_fecha          DATE,
    IN p_casosAbiertos  INT,
    IN p_casosCerrados  INT,
    IN p_casosEnProceso INT,
    IN p_tiempoPromedio DECIMAL(10,2),
    IN p_cumplioMeta    BIT
)
BEGIN
    UPDATE `db_backoffice`.`reportesDiarios`
    SET idAsesor       = p_idAsesor,
        fecha          = p_fecha,
        casosAbiertos  = p_casosAbiertos,
        casosCerrados  = p_casosCerrados,
        casosEnProceso = p_casosEnProceso,
        tiempoPromedio = p_tiempoPromedio,
        cumplioMeta    = p_cumplioMeta
    WHERE idReporte = p_idReporte;
END$$

CREATE PROCEDURE `db_backoffice`.`proc_delete_reporte`(
    IN p_idReporte INT
)BEGIN
    DELETE FROM `db_backoffice`.`reportesDiarios`
    WHERE idReporte = p_idReporte;
END$$

DELIMITER ;


-- VERIFICACION

SHOW PROCEDURE STATUS WHERE Db = 'db_backoffice';
