# coding=gbk
'''
Created on 2016年1月23日

@author: 大雄
'''
import logging
import os
import subprocess

from utils import getHome


class AbstractCommand:
    cmd = None
    def execute(self):
        logging.info("execute:" + self.cmd)
        p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (stdoutdata, stderrdata) = p.communicate(timeout=60)
        if p.returncode != 0:
            raise ChildProcessError(stdoutdata.decode() + stderrdata.decode() )
        return stdoutdata
        
class SSHCommand(AbstractCommand):
    def __init__(self, host, command):
        cmd_template = """ssh {0} '{1}'"""
        self.cmd = cmd_template.format(host, command)
        
class RsyncCommand(AbstractCommand):
    def __init__(self, local_path, remote_host, remote_path):
        cmd_template = """rsync -azP --delete --exclude logs --exclude *.log --exclude */*.log --exclude .svn --exclude WEB-INF/wx-conf/zaofans.com {0}/  {1}:{2}/"""
        cmd_template2 = """rsync -azP --delete --exclude logs --exclude *.log --exclude */*.log --exclude .svn --exclude WEB-INF/wx-conf/zaofans.com {0}/  {1}/"""
        
        if remote_host:
            self.cmd = cmd_template.format(local_path, remote_host, remote_path)
        else:
            self.cmd = cmd_template2.format(local_path, remote_path)

class CopyCommand(AbstractCommand):
    def __init__(self, src, target):
        cmd_template = """cp -rp {0} {1}"""
        self.cmd = cmd_template.format(src, target) 

class SCPCommand(AbstractCommand):
    def __init__(self, src, remote, target):
        cmd_template = """scp -r {0} {1}:{2}"""
        self.cmd = cmd_template.format(src, remote, target) 
        
class SQLite3_Win32_Command(AbstractCommand):
    def __init__(self, db, sql):
        Home = getHome()
        if os.path.exists(sql):
            cmd_template = Home +  """/sqlite3.exe {0} < {1}"""
            self.cmd = cmd_template.format(db, sql)
        else:
            cmd_template = Home +  """/sqlite3.exe {0} {1}"""
            self.cmd = cmd_template.format(db, sql)
          
def createCommand(*args, **kargs):
    cmd_type = kargs.get("type")
    if not cmd_type:
        raise Exception("Command type not define")
    if cmd_type == 'SSH':
        return SSHCommand(*args)
    if cmd_type == "RSYNC":
        return RsyncCommand(*args)
    if cmd_type == "COPY":
        return CopyCommand(*args)
    if cmd_type == "SCP":
        return SCPCommand(*args)
    if cmd_type == "SQLite3_Win32":
        return SQLite3_Win32_Command(*args)

