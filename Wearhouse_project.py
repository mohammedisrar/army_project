# importing Flask and other modules
from flask import Flask, request, render_template
import pandas as pd
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def add_Remove():

    file_path_New="C:/Users/ASUS/OneDrive/Desktop/Python/Test Deploy/Wearhouse_new.xlsx"
    file_path_old="C:/Users/ASUS/OneDrive/Desktop/Python/Test Deploy/Wearhouse_old.xlsx"
    Wearhouse_new =pd.read_excel(file_path_New)
    Wearhouse_old = pd.read_excel(file_path_old)
    
    # getting input with name = fname in HTML form
    fname = request.form.get("fname")   
    
    # getting input with name = fcount in HTML form
    fcount = request.form.get("fcount", type=int)
    
    # getting input with name = operation in HTML form
    task = request.form.get("operation")
    
    # getting input with name = Wearhouse in HTML form
    NeworOld = request.form.get("Wearhouse")

    ##### Task 1 ADD ####
    if task == "add":
           
        ####################### Section 1 To add Furnitures in New Wearhouse #########################
        if NeworOld=="nw": 
            if fname not in list(Wearhouse_new.columns):
                Wearhouse_new[fname]=fcount #To add New Furniture that does not exist in the Wearhouse
                Wearhouse_new.to_excel(file_path_New,index=False)
            else:
                c=int(Wearhouse_new[fname].values)
                Wearhouse_new[fname]=c+fcount
                Wearhouse_new.to_excel(file_path_New,index=False)
            result=f"""
                    <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                    <center>
                    <h2 style="color:blue">Furniture Added Successfully!!!!!</h2>
                    <h3 style="color:green">{fname}:{fcount}</h3> 
                    <h4 style="color:green">New Wearhouse stock</b></h4>
                    {Wearhouse_new.to_html(index=False)}
                    </center>
                    </body>
                    """
            return result
        
        ####################### Section 2 To add Furnitures in Old Wearhouse   ######################### 
        elif NeworOld=="ow":         
            if fname not in list(Wearhouse_old.columns):
                Wearhouse_old[fname]=fcount #To add New Furniture that does not exist in the Wearhouse
                Wearhouse_old.to_excel(file_path_old,index=False)
            else:
                c=int(Wearhouse_old[fname].values)
                Wearhouse_old[fname]=c+fcount
                Wearhouse_old.to_excel(file_path_old,index=False)
            result=f"""
                    <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                    <center>
                    <h2 style="color:blue">Furniture Added Successfully!!!!!</h2>
                    <h3 style="color:green">{fname}:{fcount}</h3> 
                    <h4 style="color:green">Old Wearhouse stock</b></h4>
                    {Wearhouse_old.to_html(index=False)}
                    </center></body>
                    """         
            return result
   
    ##### Task 2 Remove ####
    elif task =="remove":
        
        ####################### Section 3 To remove Furnitures from New Wearhouse #########################  
        if NeworOld=="nw":     
            #Returns warning if item enter does not exists
            if fname not in list(Wearhouse_new.columns):
                result=f"""
                        <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                        <center>
                        <h2 style="color:red">Furniture does not exist in Wearhouse!!!!</h2>
                        <h3 style="color:blue">Furnitures Present In Wearhouse</b></h3> 
                        {Wearhouse_new.to_html(index=False)}
                        </center>
                        </body>
                        """
                return result         
                
            #If item enter does exists in file
            else:
                c=int(Wearhouse_new[fname].values)
                #If Furniture count entered exceed available furniture 
                if c<fcount:                          
                    result=f"""
                            <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                            <center>
                            <h2 style="color:red">Item number entered is out of limit!!!!!</h2>
                            <h3 style="color:blue">Furniture Limit</h3> 
                            <b>{Wearhouse_new.to_html(index=False)}</b>
                            </center>
                            </body>
                            """
                    return result 
            
                else:  
                    Wearhouse_new[fname]=c-fcount
                    Wearhouse_new.to_excel(file_path_New,index=False)
                    result=f"""
                            <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                            <center>
                            <h2 style="color:blue">Furniture Removed Successfully!!!!!</h2>
                            <h3 style="color:green">{fname}:{fcount}</h3> 
                            <h4 style="color:green">New Wearhouse stock</h4> 
                            {Wearhouse_new.to_html(index=False)}
                            </center>
                            </body
                            """
                    return result    
                        
        ####################### Section 4 To remove Furnitures from Old Wearhouse #########################        
        elif NeworOld=="ow":

            #Returns warning if item enter does not exists
            if fname not in list(Wearhouse_old.columns):
                result=f"""
                        <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                        <center>
                        <h2 style="color:red">Furniture does not exist in Wearhouse!!!!</h2>
                        <h3 style="color:blue">Furnitures Present In Wearhouse</b></h3> 
                        {Wearhouse_old.to_html(index=False)}
                        </center>
                        </body>
                        """
                return result  
            #If item enter does exists in file       
            else: 
                c=int(Wearhouse_old[fname].values)  
            #If Furniture count entered exceeds available furniture return warning
                if c<fcount:                          
                    result=f"""
                            <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                            <center>
                            <h2 style="color:red">Item number entered is out of limit!!!!!</h2>
                            <h3 style="color:blue">Furniture Limit</h3> 
                            <b>{Wearhouse_old.to_html(index=False)}</b>
                            </center>
                            </body>
                            """
                    return result 
                
                else:
                    Wearhouse_old[fname]=c-fcount
                    Wearhouse_old.to_excel(file_path_old,index=False)
                    result=f"""
                            <body style="background-image: linear-gradient(to bottom right, orange, white,green);">
                            <center>
                            <h2 style="color:blue">Furniture Removed Successfully!!!!!</h2>
                            <h3 style="color:green">{fname}:{fcount}</h3> 
                            <h4 style="color:green">Old Wearhouse stock</h4> 
                            {Wearhouse_old.to_html(index=False)}
                            </center>
                            </body>
                            """
                    return result                
    return render_template("home.html")

if __name__=='__main__':
    app.run(debug=True)