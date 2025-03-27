CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_number VARCHAR(20)
);

INSERT INTO students (name, roll_number) VALUES
('Alice Johnson', '101'),
('Bob Smith', '105'),
('Charlie Brown', '103'),
('Harris', '104');
