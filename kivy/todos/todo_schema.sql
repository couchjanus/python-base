-- Schema for to-do application examples.

-- Projects are high-level activities made up of tasks
create table project (
    index       integer primary key,
    title       text,
    description text,
    deadline    date
);

-- Tasks are steps that can be taken to complete a project
create table task (
    id           integer primary key autoincrement not null,
    priority     integer default 1,
    details      text,
    status       text,
    deadline     date,
    completed_on date,
    index        integer not null references project(index)
);

