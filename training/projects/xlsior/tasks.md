1. Generate test .xlsx files:
    a. columns: Id, Name, Grade (Think of types and ranges)
    b. rows: 50
    c. files: studenys*.xls, *: 1 --> 10

2. Process test files:
    a. read (de-serialize) each row to Student class (think of the methods and attributes)
    b. validate id correctness (bonus: try and correct and update file)
    c. if average is below L, give a factor F (new column)
    d. create grades distribution chart
