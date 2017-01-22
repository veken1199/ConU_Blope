from flask import Flask,render_template,request
import pypyodbc,json
app = Flask(__name__)


connection = pypyodbc.connect( "DRIVER={SQL Server};SERVER=tcp:blopes.database.windows.net,1433;uid=test;pwd=Concordia1;DATABASE=Blope")
connectLogin = connection.cursor()
UserId = " "
Name = " "
GPA = 0.0
School = " "
Year = 0
Program = " "
Picture = " "

@app.route("/", methods=['GET','POST'])
def welcome():
    if request.method=='POST':
        data = request.data
        userData = json.loads(data)
        for key,value in dict.items(userData["uid"]):
            UserId = value
        for key, value in dict.items(userData["School"]):
            School = value
        for key, value in dict.items(userData["Program"]):
            Program = value
        for key, value in dict.items(userData["Picture"]):
            Picture = value
        for key, value in dict.items(userData["Name"]):
            Name = value
        login(UserId,School,Program,Picture,Name)
    else:
        return render_template('login.html')



def login(Username, School, Program, Picture, Name):
    SQLcommand = "select UserId from dbo.users  where UserId = ?"
    connectLogin.execute(SQLcommand,(Username,))
    connectLogin.fetchall()
    if not connectLogin.rowcount:
        SQLCommand = ("INSERT INTO dbo.users "
                      "(UserId) "
                      "VALUES (?)")
        Values = [Username]
        connectLogin.execute(SQLCommand, Values)
        connection.commit()

        SQLCommand = ("INSERT INTO dbo.userInfo "
                      "(UserId) "
                      "VALUES (?, ? , ?, ? , ? )")
        Values = [Username, School, Program, Picture, Name]
        connectLogin.execute(SQLCommand, Values)
        connection.commit()

   #if user exist extract school and gpa from table
    else:
        SQLcommand = ("UPDATE School = ? ,Program = ? FROM dbo.userInfo where UserId = ? ")
        connectLogin.execute(SQLcommand, (School, Program, Username))

    return render_template('swipe.html')

@app.route("/swipe", methods=['GET','POST'])
def update():
    SQLcommand = "select Picture,Name from dbo.userInfo  where School = ?"
    connectLogin.execute(SQLcommand, (School,))
    row = connectLogin.fetchall();
    print(row)


if __name__ == "__main__":
    app.run()