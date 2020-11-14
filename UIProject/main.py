import pymysql
import sys, datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


####################################
class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='rbfl0309', db=db, charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     # dictionary based cursor
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

    def updateExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='rbfl0309', db=db, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의
    def selectAll(self):
        sql = "SELECT * FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingTeamId(self, value):
        sql = "SELECT * FROM player WHERE team_id = %s"
        params = (value)

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerTeamId(self):
        sql = "SELECT DISTINCT team_id FROM player" #중복되는 것은 모두 없앰.
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingPosition(self, value):
        if value == '미정':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE position = %s"
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player" #중복되는 것은 모두 없앰.
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingNation(self, value):
        if value == '대한민국':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE nation = %s"
            params = (value)  # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerNation(self):
        sql = "SELECT DISTINCT nation FROM player" #중복되는 것은 모두 없앰.
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

class DB_Update:
    # 모든 갱신문은 여기에 각각 하나의 메소드로 정의
    def insertPlayer(self, player_id, player_name, team_id, position):
        sql = "INSERT INTO player (player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
        params = (player_id, player_name, team_id, position)

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)

class MainWindow(QWidget):          # QWidget 클래스의 서브클래스
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self): #윈도우에서 사용할 위젯
        # 툴팁 설정
        QToolTip.setFont(QFont("SansSerif", 12))

        # 윈도우 설정
        self.setWindowTitle("윈도우 생성 예제")
        self.move(230, 50)         # x, y
        self.resize(1000, 700)   # w, h

        self.label0 = QLabel("선수 검색", self)
        self.label1 = QLabel("팀명: ", self)
        self.comboBox1 = QComboBox(self)
        self.label2 = QLabel("포지션: ", self)
        self.comboBox2 = QComboBox(self)
        self.label3 = QLabel("출신국: ", self)
        self.comboBox3 = QComboBox(self)
        self.resetButton = QPushButton("초기화", self)

        #1행 라벨 및 버튼 위치 조정
        self.label0.move(150, 50)

        self.label1.move(150, 90)
        self.comboBox1.move(185, 90)
        self.comboBox1.resize(150, 20)
        # DB 검색문 실행
        query = DB_Queries()
        rows = query.selectPlayerTeamId()  # rows은 dictionary의 리스트
        print(rows)
        print()
        columnName1 = list(rows[0].keys())[0]
        items = [row[columnName1] for row in rows]
        self.comboBox1.addItems(items)

        self.label2.move(350, 90)
        self.comboBox2.move(395, 90)
        self.comboBox2.resize(150, 20)
        query = DB_Queries()
        rows = query.selectPlayerPosition()  # rows은 dictionary의 리스트
        print(rows)
        print()
        columnName2 = list(rows[0].keys())[0]
        items = ['미정' if row[columnName2] == None else row[columnName2] for row in rows]
        self.comboBox2.addItems(items)

        self.label3.move(560, 90)
        self.comboBox3.move(605, 90)
        self.comboBox3.resize(150, 20)
        self.resetButton.move(768, 83)
        query = DB_Queries()
        rows = query.selectPlayerNation()  # rows은 dictionary의 리스트
        print(rows)
        print()
        columnName3 = list(rows[0].keys())[0]
        items = ['대한민국' if row[columnName3] == None else row[columnName3] for row in rows]
        self.comboBox3.addItems(items)

        self.label4 = QLabel("키: ", self)
        self.lineEdit4 = QLineEdit(self)
        self.label5 = QLabel("몸무게: ", self)
        self.lineEdit5 = QLineEdit(self)
        self.searchButton = QPushButton("검색", self)

        self.groupbox1 = QGroupBox(self)
        self.radioBtn1 = QRadioButton("이상", self)
        self.radioBtn1.setChecked(True)
        self.radioBtn2 = QRadioButton("이하", self)
        hBox = QHBoxLayout()
        hBox.addWidget(self.radioBtn1)
        hBox.addWidget(self.radioBtn2)
        self.groupbox1.setLayout(hBox)

        self.groupbox2 = QGroupBox(self)
        self.radioBtn3 = QRadioButton("이상", self)
        self.radioBtn3.setChecked(True)
        self.radioBtn4 = QRadioButton("이하", self)
        hBox = QHBoxLayout()
        hBox.addWidget(self.radioBtn3)
        hBox.addWidget(self.radioBtn4)
        self.groupbox2.setLayout(hBox)

        # 2행 라벨 및 버튼 위치 조정
        self.label4.move(150, 135)
        self.lineEdit4.move(185, 135)
        self.lineEdit4.resize(120, 20)
        self.groupbox1.move(315, 125)
        self.groupbox1.resize(130, 40)
        self.label5.move(458, 135)
        self.lineEdit5.move(505, 135)
        self.lineEdit5.resize(120, 20)
        self.groupbox2.move(635, 125)
        self.groupbox2.resize(130, 40)
        self.searchButton.move(768, 123)
        # self.searchButton.clicked.connect(self.searchButton_Clicked)

        # 테이블 만들기
        # DB 검색문 실행
        query = DB_Queries()
        players = query.selectAll()  # 딕셔너리의 리스트
        print(players)

        #테이블 위젯 설정
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(150, 180)
        self.tableWidget.resize(690, 400)
        self.tableWidget.setRowCount(len(players))
        self.tableWidget.setColumnCount(len(players[0]))
        columnNames = list(players[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #테이블에 데이터 베이스 삽입
        for rowIDX in range(len(players)):
            player = players[rowIDX]

            for k, v in player.items():
                columnIDX = columnNames.index(k)

                if v == None:           # 파이썬이 DB의 널값을 None으로 변환함.(파이썬에서는 null이 없다.)
                    continue            # QTableWidgetItem 객체를 생성하지 않음
                elif isinstance(v, datetime.date):      # QTableWidgetItem 객체 생성
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        self.label6 = QLabel("파일 출력", self)
        self.groupbox3 = QGroupBox(self)
        self.radioBtn5 = QRadioButton("CSV", self)
        self.radioBtn5.setChecked(True)
        self.radioBtn6 = QRadioButton("JSON", self)
        self.radioBtn7 = QRadioButton("XML", self)
        hBox = QHBoxLayout()
        hBox.addWidget(self.radioBtn5)
        hBox.addWidget(self.radioBtn6)
        hBox.addWidget(self.radioBtn7)
        self.groupbox3.setLayout(hBox)
        self.saveButton = QPushButton("저장", self)

        # 파일 출력 부분 위치 조정
        self.label6.move(150, 600)
        self.groupbox3.move(150, 630)
        self.saveButton.move(768, 630)

        def comboBox1_Activated(self):
            self.teamidValue = self.comboBox.currentText()
        def comboBox2_Activated(self):
            self.positionValue = self.comboBox.currentText()
        def comboBox3_Activated(self):
            self.nationValue = self.comboBox.currentText()

        def resetButton_Clicked(self):
            self.tableWidget.clearContents()
            for rowIDX in range(len(players)):
                player = players[rowIDX]

                for k, v in player.items():
                    columnIDX = columnNames.index(k)

                    if v == None:  # 파이썬이 DB의 널값을 None으로 변환함.(파이썬에서는 null이 없다.)
                        continue  # QTableWidgetItem 객체를 생성하지 않음
                    elif isinstance(v, datetime.date):  # QTableWidgetItem 객체 생성
                        item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                    else:
                        item = QTableWidgetItem(str(v))

                    self.tableWidget.setItem(rowIDX, columnIDX, item)

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
        def searchButton_Clicked(self):
            query = DB_Queries()
            players = query.selectPlayerUsingPosition(self.positionValue)
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(players))
            self.tableWidget.setColumnCount(len(players[0]))
            columnNames = list(players[0].keys())
            self.tableWidget.setHorizontalHeaderLabels(columnNames)
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

            for rowIDX in range(len(players)):
                player = players[rowIDX]

                for k, v in player.items():
                    columnIDX = columnNames.index(k)

                    if v == None:  # 파이썬이 DB의 널값을 None으로 변환함.
                        continue  # QTableWidgetItem 객체를 생성하지 않음
                    elif isinstance(v, datetime.date):  # QTableWidgetItem 객체 생성
                        item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                    else:
                        item = QTableWidgetItem(str(v))

                    self.tableWidget.setItem(rowIDX, columnIDX, item)

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

        # def saveButton_Clicked(self):
        #     self.tableWidget.clearContents()
#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

main()