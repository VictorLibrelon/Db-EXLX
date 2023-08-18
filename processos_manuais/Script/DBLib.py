import pyodbc 

dbServerPrivateVNETAddress="Endereço do server"
currentDbServerAddress=dbServerPrivateVNETAddress

class SqlServer:

    def GetConnection(self,database):
            try:
                con = pyodbc.connect(r"DRIVER={SQL Server};server="+currentDbServerAddress+";database=" + database + r";uid=wms;pwd=@avanade7411")
                con.autocommit = True
                return con
            except Exception as e:
                print(str(e))

    def billing_update_employee_id_and_alias(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_01_BillingUpdateEmployeeIDAndAlias")
        cur.close()
        con.close()

    def billing_get_aip_users(self):  
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_02_BillingGetAIPUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_atp_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_03_BillingGetATPUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_azure_ad_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_04_BillingGetAzureADUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_delv_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_05_BillingGetDelviUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_exchange_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_06_BillingGetExchangeUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_forms_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_07_BillingGetFormsUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_onde_drive_activity(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_08_BillingGetOneDriveActivity")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_planner_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_09_BillingGetPlannerUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_power_apps_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_10_BillingGetPowerAppsUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_power_automate_userss(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_11_BillingGetPowerAutomateUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_share_point_activity(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_13_BillingGetSharePointActivity")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_stream_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_14_BillingGetStreamUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_sway_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_15_BillingGetSwayUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_teams_activity(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_16_BillingGetTeamsActivity")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_to_do_users(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_17_BillingGetToDoUsers")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados
    
    def billing_get_yammer_activity(self):        
        con = self.GetConnection('Billing_')
        cur = con.cursor()
        cur.execute("exec sp_18_BillingGetYammerActivity")
        dados = cur.fetchall()
        cur.close()
        con.close()
        return dados

'''def runJob(self):
        con = self.GetConnection('Managed_Services')
        cur = con.cursor()
        cur.execute('EXEC msdb.dbo.sp_start_job @job_name = "OP_CONTROL_UPDATE"')
        cur.close()
        con.close()'''

'''sql = SqlServer()
sql.BillingUpdateEmployeeIDAndAlias()'''
