drop table if exists Users cascade; 
-*-
create table Users (
  id serial PRIMARY KEY,
  name varchar(50) not null,
  email varchar(50) not null,
  phone varchar(20),
  mobile varchar(20),
  status int
);
-*-
create or replace function get_users() 
returns setof users AS $$
BEGIN
    return query select * from Users;
END;
$$ LANGUAGE plpgsql;
-*-
create or replace function add_user(name char(50), email char(50)) 
returns void AS $$
BEGIN
    insert into Users (name, email) values (name, email);
END;
$$ LANGUAGE plpgsql;


