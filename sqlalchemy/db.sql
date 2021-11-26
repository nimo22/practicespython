create table cord(
    name varchar (50) not null primary key ,
    age int
);
create table user(
    ID int not null primary key ,
    name varchar (50) not null unique ,
 FOREIGN KEY(name) REFERENCES cord(name)
);

insert into user values
    (1,"ali"),
    (2,"john"),
    (3,"shaza"),
    (4,"elia")
;
insert into cord values
("ali",27),
("john",26),
("shaza",26);
