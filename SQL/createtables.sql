CREATE TABLE employees (
    emp_nu  VARCHAR NOT NULL,
    emp_title_id VARCHAR NOT NULL,
    birth_date DATE NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    hire_date  DATE  NOT NULL,
    PRIMARY KEY (emp_nu)
);

CREATE TABLE departments (
    dept_nu VARCHAR(50) NOT NULL,
    dept_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (dept_nu),
    UNIQUE (dept_name)
);

CREATE TABLE dept_manager (
   dept_nu VARCHAR(50) NOT NULL,
   emp_nu VARCHAR NOT NULL,
   FOREIGN KEY (emp_nu)  REFERENCES employees (emp_nu),
   FOREIGN KEY (dept_nu) REFERENCES departments (dept_nu),
   PRIMARY KEY (emp_nu,dept_nu)
);

CREATE TABLE dept_emp (
    emp_nu  VARCHAR NOT NULL,
    dept_nu VARCHAR(50)  NOT NULL,
    FOREIGN KEY (emp_nu)  REFERENCES employees  (emp_nu),
    FOREIGN KEY (dept_nu) REFERENCES departments (dept_nu),
    PRIMARY KEY (emp_nu,dept_nu)
);

CREATE TABLE titles (
    emp_nu  VARCHAR NOT NULL,
    title VARCHAR(50) NOT NULL,
    FOREIGN KEY (emp_nu) REFERENCES employees (emp_nu),
    PRIMARY KEY (emp_nu,title)
);

CREATE TABLE salaries (
    emp_nu VARCHAR  NOT NULL,
    salary INT  NOT NULL,
    FOREIGN KEY (emp_nu) REFERENCES employees (emp_nu),
    PRIMARY KEY (emp_nu)
);