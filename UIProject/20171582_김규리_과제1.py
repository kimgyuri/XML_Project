import pymysql
import sys, datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import csv, json
import xml.etree.ElementTree as ET


####################################
class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='rbfl0309', db=db, charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
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

    def selectPlayerTeamId(self):
        sql = "SELECT DISTINCT team_id FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerNation(self):
        sql = "SELECT DISTINCT nation FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerHeight(self):
        sql = "SELECT DISTINCT height FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerWeight(self):
        sql = "SELECT DISTINCT weight FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    # def selectPlayerUsingbody(self,):
    def selectPlayerUsingAll(self, team_id, position, nation, height, weight, msg1, msg2):
        if team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함' and msg1 == '이하' and msg2 == '이히':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and height == '사용안함' and weight == '사용안함':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL"
            params = ()
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE height >= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE height >= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE height >= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE height <= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE height <= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation IS NULL and height >= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE nation IS NULL and height >= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation IS NULL and height <= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE nation IS NULL and height <= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL and height >= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL and height >= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL and height <= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL and height <= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and height >= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and height >= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and height <= %s and weight >= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and height <= %s and weight <= %s"
            params = (height, weight)
        elif team_id == '사용안함' and position == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation = %s and height >= %s and weight >= %s"
            params = (nation, height, weight)
        elif team_id == '사용안함' and position == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE nation = %s and height >= %s and weight >= %s"
            params = (nation, height, weight)
        elif team_id == '사용안함' and position == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation = %s and height >= %s and weight >= %s"
            params = (nation, height, weight)
        elif team_id == '사용안함' and position == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE nation = %s and height >= %s and weight >= %s"
            params = (nation, height, weight)
        elif team_id == '사용안함' and nation == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s and height >= %s and weight >= %s"
            params = (position, height, weight)
        elif team_id == '사용안함' and nation == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s and height >= %s and weight <= %s"
            params = (position, height, weight)
        elif team_id == '사용안함' and nation == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s and height <= %s and weight >= %s"
            params = (position, height, weight)
        elif team_id == '사용안함' and nation == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s and height <= %s and weight <= %s"
            params = (position, height, weight)
        elif position == '사용안함' and nation == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and height >= %s and weight >= %s"
            params = (team_id, height, weight)
        elif position == '사용안함' and nation == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and height >= %s and weight <= %s"
            params = (team_id, height, weight)
        elif position == '사용안함' and nation == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and height <= %s and weight >= %s"
            params = (team_id, height, weight)
        elif position == '사용안함' and nation == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and height <= %s and weight <= %s"
            params = (team_id, height, weight)
        elif position == '사용안함' and nation == '대한민국' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and height >= %s and weight >= %s"
            params = (team_id, height, weight)
        elif position == '사용안함' and nation == '대한민국' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and height >= %s and weight <= %s"
            params = (team_id, height, weight)
        elif position == '사용안함' and nation == '대한민국' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and height <= %s and weight >= %s"
            params = (team_id, height, weight)
        elif position == '사용안함' and nation == '대한민국' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and height <= %s and weight <= %s"
            params = (team_id, height, weight)
        elif team_id == '사용안함' and nation == '대한민국' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and height >= %s and weight >= %s"
            params = (position, height, weight)
        elif team_id == '사용안함' and nation == '대한민국' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and height >= %s and weight <= %s"
            params = (position, height, weight)
        elif team_id == '사용안함' and nation == '대한민국' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and height <= %s and weight >= %s"
            params = (position, height, weight)
        elif team_id == '사용안함' and nation == '대한민국' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and height <= %s and weight <= %s"
            params = (position, height, weight)
        elif position == '미정' and nation == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and height >= %s and weight >= %s"
            params = (team_id, height, weight)
        elif position == '미정' and nation == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and height >= %s and weight <= %s"
            params = (team_id, height, weight)
        elif position == '미정' and nation == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and height <= %s and weight >= %s"
            params = (team_id, height, weight)
        elif position == '미정' and nation == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and height <= %s and weight <= %s"
            params = (team_id, height, weight)
        elif team_id == '사용안함' and position == '미정' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height >= %s and weight >= %s"
            params = (nation, height, weight)
        elif team_id == '사용안함' and position == '미정' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height >= %s and weight <= %s"
            params = (nation, height, weight)
        elif team_id == '사용안함' and position == '미정' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height <= %s and weight >= %s"
            params = (nation, height, weight)
        elif team_id == '사용안함' and position == '미정' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height <= %s and weight <= %s"
            params = (nation, height, weight)
        elif position == '미정' and nation == '대한민국' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height >= %s AND weight >= %s"
            params = (team_id, height, weight)
        elif position == '미정' and nation == '대한민국' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height >= %s AND weight <= %s"
            params = (team_id, height, weight)
        elif position == '미정' and nation == '대한민국' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height <= %s AND weight >= %s"
            params = (team_id, height, weight)
        elif position == '미정' and nation == '대한민국' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height <= %s AND weight <= %s"
            params = (team_id, height, weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE height >= %s"
            params = (height)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE height <= %s"
            params = (height)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE nation IS NULL and height >= %s "
            params = (height)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE nation IS NULL and height <= %s"
            params = (height)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL and height >= %s"
            params = (height)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL and height <= %s"
            params = (height)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and height >= %s"
            params = (height)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and height <= %s"
            params = (height)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE weight >= %s"
            params = (weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '사용안함'and msg2 == '이하':
            sql = "SELECT * FROM player WHERE weight <= %s"
            params = (weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation IS NULL and weight >= %s"
            params = (weight)
        elif team_id == '사용안함' and position == '사용안함' and nation == '대한민국' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE nation IS NULL and weight <= %s"
            params = (weight)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL and weight >= %s"
            params = (weight)
        elif team_id == '사용안함' and position == '미정' and nation == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL and weight <= %s"
            params = (weight)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and weight >= %s"
            params = (weight)
        elif team_id == '사용안함' and position == '미정' and nation == '대한민국' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL and weight <= %s"
            params = (weight)
        elif team_id == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height >= %s AND weight >= %s"
            params = (position, nation, height, weight)
        elif team_id == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height >= %s AND weight <= %s"
            params = (position, nation, height, weight)
        elif team_id == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height <= %s AND weight >= %s"
            params = (position, nation, height, weight)
        elif team_id == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height <= %s AND weight <= %s"
            params = (position, nation, height, weight)
        elif position == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height >= %s AND weight >= %s"
            params = (team_id, nation, height, weight)
        elif position == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height >= %s AND weight <= %s"
            params = (team_id, nation, height, weight)
        elif position == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height <= %s AND weight >= %s"
            params = (team_id, nation, height, weight)
        elif position == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height <= %s AND weight <= %s"
            params = (team_id, nation, height, weight)
        elif nation == '사용안함' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height >= %s AND weight >= %s"
            params = (team_id, position, height, weight)
        elif nation == '사용안함' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height >= %s AND weight <= %s"
            params = (team_id, position, height, weight)
        elif nation == '사용안함' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height <= %s AND weight >= %s"
            params = (team_id, position, height, weight)
        elif nation == '사용안함' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height <= %s AND weight <= %s"
            params = (team_id, position, height, weight)
        elif position == '미정' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height >= %s AND weight >= %s"
            params = (team_id, nation, height, weight)
        elif position == '미정' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height >= %s AND weight <= %s"
            params = (team_id, nation, height, weight)
        elif position == '미정' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height <= %s AND weight >= %s"
            params = (team_id, nation, height, weight)
        elif position == '미정' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height <= %s AND weight <= %s"
            params = (team_id, nation, height, weight)
        elif nation == '대한민국' and msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND height >= %s AND weight >= %s"
            params = (team_id, position, height, weight)
        elif nation == '대한민국' and msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND height >= %s AND weight <= %s"
            params = (team_id, position, height, weight)
        elif nation == '대한민국' and msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND height <= %s AND weight >= %s"
            params = (team_id, position, height, weight)
        elif nation == '대한민국' and msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND height <= %s AND weight <= %s"
            params = (team_id, position, height, weight)
        elif team_id == '사용안함' and position == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE nation = %s and height >= %s"
            params = (nation, height)
        elif team_id == '사용안함' and position == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE nation = %s and height >= %s"
            params = (nation, height)
        elif team_id == '사용안함' and nation == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE position = %s and height >= %s"
            params = (position, height)
        elif team_id == '사용안함' and nation == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE position = %s and height <= %s"
            params = (position, height)
        elif position == '사용안함' and nation == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and height >= %s"
            params = (team_id, height)
        elif position == '사용안함' and nation == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and height <= %s"
            params = (team_id, height)
        elif position == '사용안함' and nation == '대한민국' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and height >= %s"
            params = (team_id, height)
        elif position == '사용안함' and nation == '대한민국' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and height <= %s"
            params = (team_id, height)
        elif team_id == '사용안함' and nation == '대한민국' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and height >= %s"
            params = (position, height)
        elif team_id == '사용안함' and nation == '대한민국' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and height <= %s"
            params = (position, height)
        elif position == '미정' and nation == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and height >= %s"
            params = (team_id, height)
        elif position == '미정' and nation == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and height <= %s "
            params = (team_id, height)
        elif team_id == '사용안함' and position == '미정' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height >= %s"
            params = (nation, height)
        elif team_id == '사용안함' and position == '미정' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height <= %s"
            params = (nation, height)
        elif position == '미정' and nation == '대한민국' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height >= %s"
            params = (team_id, height)
        elif position == '미정' and nation == '대한민국' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND height <= %s"
            params = (team_id, height)
        elif team_id == '사용안함' and position == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE nation = %s and weight >= %s"
            params = (nation, weight)
        elif team_id == '사용안함' and position == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE nation = %s and weight >= %s"
            params = (nation, weight)
        elif team_id == '사용안함' and nation == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s and weight >= %s"
            params = (position, weight)
        elif team_id == '사용안함' and nation == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s and weight <= %s"
            params = (position, weight)
        elif position == '사용안함' and nation == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and weight >= %s"
            params = (team_id, weight)
        elif position == '사용안함' and nation == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and weight <= %s"
            params = (team_id, weight)
        elif position == '사용안함' and nation == '대한민국' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and weight >= %s"
            params = (team_id, weight)
        elif position == '사용안함' and nation == '대한민국' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL and weight <= %s"
            params = (team_id, weight)
        elif team_id == '사용안함' and nation == '대한민국' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and weight >= %s"
            params = (position, weight)
        elif team_id == '사용안함' and nation == '대한민국' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL and weight <= %s"
            params = (position, weight)
        elif position == '미정' and nation == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and weight >= %s"
            params = (team_id, weight)
        elif position == '미정' and nation == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL and weight <= %s"
            params = (team_id, weight)
        elif team_id == '사용안함' and position == '미정' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s and weight >= %s"
            params = (nation, weight)
        elif team_id == '사용안함' and position == '미정' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s and weight <= %s"
            params = (nation, weight)
        elif position == '미정' and nation == '대한민국' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND weight >= %s"
            params = (team_id, weight)
        elif position == '미정' and nation == '대한민국' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL AND weight <= %s"
            params = (team_id, weight)
        elif team_id == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height >= %s"
            params = (position, nation, height)
        elif team_id == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND height <= %s"
            params = (position, nation, height)
        elif position == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height >= %s"
            params = (team_id, nation, height)
        elif position == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND height <= %s"
            params = (team_id, nation, height)
        elif nation == '사용안함' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height >= %s"
            params = (team_id, position, height)
        elif nation == '사용안함' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND height <= %s"
            params = (team_id, position, height)
        elif position == '미정' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height >= %s"
            params = (team_id, nation, height)
        elif position == '미정' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND height <= %s"
            params = (team_id, nation, height)
        elif nation == '대한민국' and msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND height >= %s "
            params = (team_id, position, height)
        elif nation == '대한민국' and msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND height <= %s"
            params = (team_id, position, height)
        elif team_id == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND weight >= %s"
            params = (position, nation, weight)
        elif team_id == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s AND weight <= %s"
            params = (position, nation, weight)
        elif position == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND weight >= %s"
            params = (team_id, nation, weight)
        elif position == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s AND weight <= %s"
            params = (team_id, nation, weight)
        elif nation == '사용안함' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND weight >= %s"
            params = (team_id, position, weight)
        elif nation == '사용안함' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND weight <= %s"
            params = (team_id, position, weight)
        elif position == '미정' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND weight >= %s"
            params = (team_id, nation, weight)
        elif position == '미정' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s AND weight <= %s"
            params = (team_id, nation, weight)
        elif nation == '대한민국' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND weight >= %s"
            params = (team_id, position, weight)
        elif nation == '대한민국' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL AND weight <= %s"
            params = (team_id, position, weight)
        elif msg1 == '이상' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and height >= %s and weight >= %s"
            params = (team_id, position, nation, height, weight)
        elif msg1 == '이상' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and height >= %s and weight <= %s"
            params = (team_id, position, nation, height, weight)
        elif msg1 == '이하' and msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and height <= %s AND weight >= %s"
            params = (team_id, position, nation, height, weight)
        elif msg1 == '이하' and msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and height <= %s and weight <= %s"
            params = (team_id, position, nation, height, weight)
        elif team_id == '사용안함' and position == '사용안함':
            sql = "SELECT * FROM player WHERE nation = %s"
            params = (nation)
        elif team_id == '사용안함' and nation == '사용안함':
            sql = "SELECT * FROM player WHERE position = %s"
            params = (position)
        elif position == '사용안함' and nation == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s"
            params = (team_id)
        elif position == '사용안함' and nation == '대한민국':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation IS NULL"
            params = (team_id)
        elif team_id == '사용안함' and nation == '대한민국':
            sql = "SELECT * FROM player WHERE position = %s AND nation IS NULL"
            params = (position)
        elif position == '미정' and nation == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL"
            params = (team_id)
        elif team_id == '사용안함' and position == '미정':
            sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s"
            params = (nation)
        elif position == '미정' and nation == '대한민국':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation IS NULL"
            params = (team_id)
        elif msg1 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and height >= %s"
            params = (team_id, position, nation, height)
        elif msg1 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and height <= %s"
            params = (team_id, position, nation, height)
        elif msg2 == '이상':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and weight >= %s"
            params = (team_id, position, nation, weight)
        elif msg2 == '이하':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation = %s and weight <= %s"
            params = (team_id, position, nation, weight)
        elif team_id == '사용안함':
            sql = "SELECT * FROM player WHERE position = %s AND nation = %s"
            params = (position, nation)
        elif position == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND nation = %s"
            params = (team_id, nation)
        elif nation == '사용안함':
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s"
            params = (team_id, position)
        elif position == '미정':
            sql = "SELECT * FROM player WHERE team_id = %s AND position IS NULL AND nation = %s"
            params = (team_id, nation)
        elif nation == '대한민국':
            sql = "SELECT * FROM player WHERE team_id = %s and position = %s and nation IS NULL"
            params = (team_id, position)
        else:
            sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s"
            params = (team_id, position, nation)

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        print(tuples)
        return tuples

# class DB_Update:
#     # 모든 갱신문은 여기에 각각 하나의 메소드로 정의
#     def insertPlayer(self, player_id, player_name, team_id, position):
#         sql = "INSERT INTO player (player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
#         params = (player_id, player_name, team_id, position)
#
#         util = DB_Utils()
#         util.updateExecutor(db="kleague", sql=sql, params=params)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.height = None # 키를 저장할 변수 정의
        self.weight = None # 몸무게를 저장할 변수 정의

    def setupUI(self):
        # 툴팁 설정
        QToolTip.setFont(QFont("SansSerif", 12))

        # 윈도우 설정
        self.setWindowTitle("Report UI")
        self.move(230, 50)
        self.resize(1000, 700)

        self.label0 = QLabel("선수 검색", self)
        self.label1 = QLabel("팀명: ", self)
        self.comboBox1 = QComboBox(self)
        self.label2 = QLabel("포지션: ", self)
        self.comboBox2 = QComboBox(self)
        self.label3 = QLabel("출신국: ", self)
        self.comboBox3 = QComboBox(self)
        self.resetButton = QPushButton("초기화", self)
        self.resetButton.clicked.connect(self.resetButton_Clicked)

        # 1행 라벨 및 버튼 위치 조정
        self.label0.move(150, 50)
        self.label1.move(150, 90)
        self.comboBox1.move(185, 90)
        self.comboBox1.resize(155, 20)
        query = DB_Queries()
        rows = query.selectPlayerTeamId()
        print(rows)
        print()
        columnName1 = list(rows[0].keys())[0]
        items = [row[columnName1] for row in rows]
        self.comboBox1.addItems({'사용안함': None})
        self.comboBox1.addItems(items)

        self.label2.move(350, 90)
        self.comboBox2.move(395, 90)
        self.comboBox2.resize(155, 20)
        query = DB_Queries()
        rows = query.selectPlayerPosition()
        print(rows)
        print()
        columnName2 = list(rows[0].keys())[0]
        items = ['미정' if row[columnName2] == None else row[columnName2] for row in rows]
        self.comboBox2.addItems({'사용안함': None})
        self.comboBox2.addItems(items)

        self.label3.move(560, 90)
        self.comboBox3.move(605, 90)
        self.comboBox3.resize(150, 20)
        self.resetButton.move(768, 83)
        query = DB_Queries()
        rows = query.selectPlayerNation()
        print(rows)
        print()
        columnName3 = list(rows[0].keys())[0]
        items = ['대한민국' if row[columnName3] == None else row[columnName3] for row in rows]
        self.comboBox3.addItems({'사용안함': None})
        self.comboBox3.addItems(items)

        self.label4 = QLabel("키: ", self)
        self.comboBox4 = QComboBox(self)
        query = DB_Queries()
        rows = query.selectPlayerHeight()
        print(rows)
        print()
        columnName4 = list(rows[0].keys())[0]
        items = ['없음' if row[columnName4] == None else str(row[columnName4]) for row in rows]
        items.sort()
        self.comboBox4.addItems({'사용안함': None})
        self.comboBox4.addItems(items)

        self.label5 = QLabel("몸무게: ", self)
        self.comboBox5 = QComboBox(self)
        query = DB_Queries()
        rows = query.selectPlayerWeight()
        print(rows)
        print()
        columnName5 = list(rows[0].keys())[0]
        items = ['없음' if row[columnName5] == None else str(row[columnName5]) for row in rows]
        items.sort()
        self.comboBox5.addItems({'사용안함': None})
        self.comboBox5.addItems(items)

        self.searchButton = QPushButton("검색", self)
        self.searchButton.clicked.connect(self.searchButton_Clicked)

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
        self.comboBox4.move(185, 135)
        self.comboBox4.resize(120, 20)
        self.groupbox1.move(315, 125)
        self.groupbox1.resize(130, 40)
        self.label5.move(458, 135)
        self.comboBox5.move(505, 135)
        self.comboBox5.resize(120, 20)
        self.groupbox2.move(635, 125)
        self.groupbox2.resize(130, 40)
        self.searchButton.move(768, 123)

        # 테이블 만들기
        # DB 검색문 실행
        query = DB_Queries()
        players = query.selectAll()  # 딕셔너리의 리스트
        print(players)

        #테이블 위젯 설정
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(150, 180)
        self.tableWidget.resize(690, 400)

        # 테이블에 데이터 베이스 삽입
        self.tableWidget.setRowCount(len(players))
        self.tableWidget.setColumnCount(len(players[0]))
        columnNames = list(players[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX in range(len(players)):
            player = players[rowIDX]

            for k, v in player.items():
                columnIDX = columnNames.index(k)

                if v == None:
                    continue
                elif isinstance(v, datetime.date):
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        # 파일 출력 부분
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
        self.saveButton.clicked.connect(self.FilesaveBtn)
        # 파일 출력 부분 위치 조정
        self.label6.move(150, 600)
        self.groupbox3.move(150, 630)
        self.saveButton.move(768, 630)

    def comboBox1_Activated(self):
        self.teamidValue = self.comboBox1.currentText()

    def comboBox2_Activated(self):
        self.positionValue = self.comboBox2.currentText()

    def comboBox3_Activated(self):
        self.nationValue = self.comboBox3.currentText()

    def comboBox4_Activated(self):
        self.heightValue = self.comboBox4.currentText()

    def comboBox5_Activated(self):
        self.weightValue = self.comboBox5.currentText()

    def radioBtn_Clicked1(self):
        if self.radioBtn1.isChecked() == True:
            self.msg1 = "이상"
        elif self.radioBtn2.isChecked() == True:
            self.msg1 = "이하"

    def radioBtn_Clicked2(self):
        if self.radioBtn3.isChecked() == True:
            self.msg2 = "이상"
        elif self.radioBtn4.isChecked() == True:
            self.msg2 = "이하"

    def resetButton_Clicked(self):
        self.tableWidget.clearContents()
        query = DB_Queries()
        players = query.selectAll()
        self.tableWidget.setRowCount(len(players))
        self.tableWidget.setColumnCount(len(players[0]))
        columnNames = list(players[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX in range(len(players)):
            player = players[rowIDX]

            for k, v in player.items():
                columnIDX = columnNames.index(k)

                if v == None:
                    continue
                elif isinstance(v, datetime.date):
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def searchButton_Clicked(self):
        query = DB_Queries()
        self.comboBox1_Activated()
        self.comboBox2_Activated()
        self.comboBox3_Activated()
        self.comboBox4_Activated()
        self.comboBox5_Activated()
        self.radioBtn_Clicked1()
        self.radioBtn_Clicked2()
        players = query.selectPlayerUsingAll(self.teamidValue, self.positionValue, self.nationValue, self.heightValue, self.weightValue, self.msg1, self.msg2)

        if players == ():
            self.tableWidget.clearContents()
        else:
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

                    if v == None:
                        continue
                    elif isinstance(v, datetime.date):
                        item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                    else:
                        item = QTableWidgetItem(str(v))

                    self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def FilesaveBtn(self):
        if self.radioBtn5.isChecked() == True:
            self.CSV()
        elif self.radioBtn6.isChecked() == True:
            self.JSON()
        elif self.radioBtn7.isChecked() == True:
            self.XML()

    def CSV(self):
        query = DB_Queries()
        self.comboBox1_Activated()
        self.comboBox2_Activated()
        self.comboBox3_Activated()
        self.comboBox4_Activated()
        self.comboBox5_Activated()
        self.radioBtn_Clicked1()
        self.radioBtn_Clicked2()
        players = query.selectPlayerUsingAll(self.teamidValue, self.positionValue, self.nationValue, self.heightValue, self.weightValue, self.msg1, self.msg2)
        print(players)
        print()

        with open('playerGK.csv', 'w', encoding='utf-8', newline='') as f:
            wr = csv.writer(f)

            # 테이블 헤더를 출력
            columnNames = list(players[0].keys())
            print(columnNames)
            print()

            wr.writerow(columnNames)

            # 테이블 내용을 출력
            for rowIDX in range(len(players)):
                row = list(players[rowIDX].values())
                print(row)

                wr.writerow(row)

    def JSON(self):

        query = DB_Queries()
        self.comboBox1_Activated()
        self.comboBox2_Activated()
        self.comboBox3_Activated()
        self.comboBox4_Activated()
        self.comboBox5_Activated()
        self.radioBtn_Clicked1()
        self.radioBtn_Clicked2()
        players = query.selectPlayerUsingAll(self.teamidValue, self.positionValue, self.nationValue, self.heightValue, self.weightValue, self.msg1, self.msg2)
        print(players)
        print()

        for player in players:
            for k, v in player.items():
                if isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')  # 키가 k인 item의 값 v를 수정
                    print(player[k])
        print()

        newDict = dict(playerGK=players)
        print(newDict)

        with open('player.json', 'w', encoding='utf-8') as f:
            json.dump(newDict, f, ensure_ascii=False)

        with open('playerGK_indent.json', 'w', encoding='utf-8') as f:
            json.dump(newDict, f, indent=4, ensure_ascii=False)

    def XML(self):

        query = DB_Queries()
        self.comboBox1_Activated()
        self.comboBox2_Activated()
        self.comboBox3_Activated()
        self.comboBox4_Activated()
        self.comboBox5_Activated()
        self.radioBtn_Clicked1()
        self.radioBtn_Clicked2()
        players = query.selectPlayerUsingAll(self.teamidValue, self.positionValue, self.nationValue, self.heightValue, self.weightValue, self.msg1, self.msg2)
        print(players)
        print()

        for player in players:
            for k, v in player.items():
                if isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')

        newDict = dict(playerGK=players)
        print(newDict)

        tableName = list(newDict.keys())[0]
        tableRows = list(newDict.values())[0]

        rootElement = ET.Element('Table')
        rootElement.attrib['name'] = tableName

        for row in tableRows:
            rowElement = ET.Element('Row')
            rootElement.append(rowElement)

            for columnName in list(row.keys()):
                if row[columnName] == None:
                    rowElement.attrib[columnName] = ''
                else:
                    rowElement.attrib[columnName] = row[columnName]

                if type(row[columnName]) == int:
                    rowElement.attrib[columnName] = str(row[columnName])

        # XDM 트리를 화일에 출력
        ET.ElementTree(rootElement).write('playerGK.xml', encoding='utf-8', xml_declaration=True)


#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

main()