create database AgenciaTurismo;
use AgenciaTurismo;

create table rol(
	id int not null primary key,
    nombre varchar(20)
);

create table usuario(
	id int auto_increment not null primary key,
    username varchar(100) not null,
    correo varchar(150) not null,
    password varchar(200) not null,
    rol int not null,
    constraint rol_fk foreign key (rol) references rol(id)
);    


create table informacionPersonal(
    id_usuario int not null,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    fechaNacimiento date not null,
    genero varchar(1) not null,
    telefono varchar(15) not null,
    direccion varchar(200) not null,
    foreign key (id_usuario) references usuario(id)
);

create table destinos(
    id int auto_increment not null primary key,
    nombre varchar(100) not null,
    descripcion varchar(200) not null,
    costo float not null
);

create table paquete(
    id int auto_increment not null primary key,
    fecha date not null,
    costo float not null
);

create table paquete_destino(
    id_paquete int not null,
    id_destino int not null,
    foreign key (id_paquete) references paquete(id),
    foreign key (id_destino) references destinos(id)
);


create table reserva(
    id int auto_increment not null primary key,
    id_usuario int not null,
    id_paquete int not null,
    acompanantes int not null,
    foreign key (id_usuario) references usuario(id),
    foreign key (id_paquete) references paquete(id)
);

insert into rol values(1, "User");
insert into rol values(2, "Empleado");
insert into rol values(3, "Admin");

select * from destinos;

update usuario
set rol = 3
where id = 1;

delimiter //
create procedure verPaquetesP2()
begin
select p.id, d.id, d.nombre, d.descripcion, d.costo from paquete p join paquete_destino pd on p.id = pd.id_paquete join destinos d on pd.id_destino = d.id;
end

//